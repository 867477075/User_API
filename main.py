import requests
import json
from pprint import pprint
from flask import Flask, render_template, request, Response
from dal.dml import insert_data ,delete_record ,upsert,patch_record
from models.datamodels.user_model import User_data
from pymysql.err import IntegrityError
app = Flask(__name__)

URL = "https://reqres.in/api/users?page=2"


@app.route("/")
def hello():
    return "Welcome to our API"


@app.route("/user")
def get_data():
    response = requests.get(URL)
    page_data = response.json()
    user_details = page_data.get("data")

    return render_template("user_data.html", User_Data=user_details)


@app.route("/user", methods=["post"])
def post_data():
    request_data = request.json
    data = User_data(**request_data)

    all_column = [x for x in request_data]
    all_value = [y for y in request_data.values()]
    try:
        result = insert_data(
            "userdb.user_entry", all_column, all_value
        )
    except IntegrityError as err:
        response_obj = {
            "Message": f"{err} - Record already exist "
        }
        return Response(json.dumps(response_obj))

    response_obj = {
        "Message": f"{result} Record inserted "
    }

    return Response(json.dumps(response_obj))


@app.route("/user/<int:id_>", methods=["DELETE"])
def delete(id_):
    user_id = id_
    result = delete_record("userdb.user_entry",user_id)
    if result == 0:
        response_obj = {
            "Message": f"No records found to delete "
        }

        return Response(json.dumps(response_obj))

    response_obj = {
        "Message": f" {user_id} Record deleted "
    }

    return Response(json.dumps(response_obj))


@app.route("/user",methods=["PUT"])
def put_data():
    request_data = request.json

    data = User_data(**request_data)

    result, status = upsert("userdb.user_entry",request_data)
    breakpoint()
    if status == 0:
        response_obj = {
            "Message":f"{result} New Record  added successfully"
        }
        return Response(json.dumps(response_obj))
    response_obj = {
        "Message": f"{result} Existing record Updated"
    }
    return Response(json.dumps(response_obj))


@app.route("/user",methods=["PATCH"])
def patch_data():
    request_data = request.json

    # data = User_data(**request_data)
    result = patch_record("userdb.user_entry",request_data)

    response_obj = {
        "Message": f"{result} requested data patched "
    }
    return Response(json.dumps(response_obj))




if __name__ == "__main__":
    app.run(debug=True,port=8080)
