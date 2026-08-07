from flask import Flask, jsonify, request
app = Flask("MyAssignment")

voters_list = [{"person":"No One","Vote":0}]


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
           i["Vote"]+=1
           return "Your vote is incremented"
    new_voter={"person":n,"Vote":1}
    voters_list.append(new_voter)
    return "Vote registered"


@app.get("/results")
def results():
    return jsonify(voters_list)

app.run(debug=True)
