from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/action", methods=["POST"])
def handle_action():
    action = request.form["action"]
    # Process the player action here
    return "Action received: " + action

if __name__ == "__main__":
    app.run(debug=True)
