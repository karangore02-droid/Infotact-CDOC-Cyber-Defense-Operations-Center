import jwt
import os
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "super-secret-session-key"

# Load environment variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REALM = os.environ.get("REALM")
AUTH_SERVER_URL = os.environ.get("AUTH_SERVER_URL")

oauth = OAuth(app)

keycloak = oauth.register(
    name="keycloak",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    server_metadata_url=f"{AUTH_SERVER_URL}/realms/{REALM}/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid profile email"
    }
)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return '<a href="/login">Login with Keycloak</a>'


# ---------------- LOGIN ----------------
@app.route("/login")
def login():
    return keycloak.authorize_redirect(
        redirect_uri=url_for("auth", _external=True)
    )


# ---------------- AUTH CALLBACK ----------------
@app.route("/auth")
def auth():
    token = keycloak.authorize_access_token()

    # Store full token response
    session["user"] = token

    # ID token claims are already validated internally
    session["userinfo"] = token.get("userinfo", {})

    return redirect("/protected")


# ---------------- PROTECTED (RBAC READY) ----------------
@app.route("/protected")
def protected():
    if "user" not in session:
        return redirect("/")

    access_token = session["user"].get("access_token")

    # Decode WITHOUT signature verification (lab use only)
    decoded = jwt.decode(access_token, options={"verify_signature": False})

    roles = decoded.get("realm_access", {}).get("roles", [])

    if "admin" not in roles:
        return "Access Denied – Admin Role Required", 403

    return f"""
        <h1>Protected Page</h1>
        <p>Welcome {decoded.get('preferred_username')}</p>
        <p>Role: admin</p>
        <a href="/token">View Token</a><br><br>
        <a href="/logout">Logout</a>
    """


# ---------------- TOKEN VIEW ----------------
import jwt

@app.route("/token")
def token():
    if "user" not in session:
        return redirect("/")

    access_token = session["user"]["access_token"]

    decoded = jwt.decode(
        access_token,
        options={"verify_signature": False}
    )

    return f"<pre>{decoded}</pre>"


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        f"{AUTH_SERVER_URL}/realms/{REALM}/protocol/openid-connect/logout"
        f"?post_logout_redirect_uri=http://localhost:5000"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
