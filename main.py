import requests
import json
from pprint import pprint
from flask import Flask,render_template

app = Flask(__name__)

URL = "https://reqres.in/api/users?page=2"


@app.route('/')
def hello():

    return "Welcome to our API"


@app.route("/user")
def get_data():
    response = requests.get(URL)

    page_data = response.json()
    user_details = page_data.get("data")

    return render_template("user_data.html",User_Data=user_details)


if __name__ == "__main__":
    app.run(debug=True)








