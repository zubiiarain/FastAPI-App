from flask import Flask, jsonify

app = Flask(__name__)

# ✅ Reusable response function
def make_response(status, message, data=None):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), status

# ✅ Dummy data
users = {
    1: {"name": "Alice", "email": "alice@example.com", "address": {"city": "Lahore", "country": "Pakistan"}},
    2: {"name": "Bob", "email": "bob@example.com", "address": {"city": "Karachi", "country": "Pakistan"}},
}

# ✅ Hello route (Task 1)
@app.route("/hello")
def hello():
    return make_response(200, "Hello World!", {"note": "This is a reusable response"})

# ✅ Profile route
@app.route("/profile")
def profile():
    user_profile = {
        "name": "John Doe",
        "email": "john@example.com",
        "skills": ["Python", "Flask", "APIs"],
        "location": {"city": "Islamabad", "country": "Pakistan"}
    }
    return make_response(200, "Mock profile loaded", user_profile)

# ✅ User route
@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return make_response(200, f"User {user_id} found", user)
    else:
        return make_response(404, f"User {user_id} not found", None)

# ✅ Start the server
if __name__ == "__main__":
    app.run(debug=True)
