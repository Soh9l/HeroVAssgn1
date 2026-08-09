from flask import Flask, jsonify, request
app = Flask("MyAssignment")

voters_list = []


@app.route("/")
def index():
    return f"""Welcome to the App
            Use the url to register your vote by entering the url as /vote/'type in your name'"""


@app.route("/health")
def helathstat():
    return "App is running"


@app.get("/vote/<Name>")
def voter_get(Name):
    n = Name
    for i in voters_list:
        if i["person"] == n:
            i["Vote"] += 1
            return "Your vote is incremented"
    new_voter = {"person": n, "Vote": 1}
    voters_list.append(new_voter)
    return "Vote registered"


@app.get("/results")
def results():
    return jsonify(voters_list)


profiles = []


@app.post("/add")
def userpass():
    new_profile = {
        "Username": request.json["Username"],
        "Password": request.json["Password"]
    }
    profiles.append(new_profile)
    return jsonify({"msg": "Profile Added"}), 201


@app.get("/get/<username>")
def checkprofile(username):
    for i in profiles:
        if i["Username"] == username:
            return i["Password"]
    return {"error": "Username not found"}, 404


@app.delete("/add/reset")
def restvotes():
    voters_list.clear()
    return "Votes are all cleared"


@app.delete("/add/delete/<username>")
def removeusers(username):
    for n,i in enumerate(profiles):
        if i["Username"] == username:
            f = i["Username"]
            profiles.pop(n)
        return "User Deleted"
    return "No Username was found"


app.run(debug=True)
