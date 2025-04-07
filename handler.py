from flask import Flask, request, render_template_string

app = Flask(__name__)

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login Page</h2>
    <form method="post">
        Username: <input name="username"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
    {% if error %}
        <p style="color:red">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Static check
        if username == "admin" and password == "pass123":
            return f"<h3>Welcome, {username}!</h3>"
        else:
            error = "Invalid credentials!"
    return render_template_string(LOGIN_HTML, error=error)

# Lambda handler
def handler(event, context):
    from serverless_wsgi import handle
    return handle(event, context, app)