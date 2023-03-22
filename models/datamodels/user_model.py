from pydantic import BaseModel


class User_data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avtar: str


if __name__ == "__main__":
    data = {
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
        "last_name": "Lawson",
        "avatar": "https://reqres.in/img/faces/7-image.jpg",
    }
    result = User_data(**data)
    print(result)
