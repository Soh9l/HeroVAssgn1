from flask import Flask
app = Flask("MyAssignment")


@app.route("/")
def index():
    return "Welcome to the App"


@app.route("/health")
def helathstat():
    return "App is running"


app.run(debug=True)
