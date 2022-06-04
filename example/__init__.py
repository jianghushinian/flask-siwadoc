from flask import Flask

from example.dto import LoginModel, UserModel, QueryModel
from flask_siwadoc import SiwaDoc

app = Flask(__name__)

siwa = SiwaDoc(app)


# or
# siwa.init_app(app)

@app.route("/hello", methods=["GET"])
@siwa.doc()
def hello():
    return "hello siwadoc"


@app.route("/login", methods=["POST"])
@siwa.doc(body=LoginModel, resp=UserModel)
def login(body: LoginModel):
    return {"username": body.username, "id": 1}


@app.route("/users/<int(min=1):user_id>", methods=["GET"])
@siwa.doc(resp=UserModel, tags=["user"])
def users(user_id):
    """
    user detail
    """
    return {"username": "siwa", "id": user_id}


#
@app.route("/users", methods=["GET"])
@siwa.doc(query=QueryModel)
def users_list():
    """
    user list
    """
    return [{"username": "siwa", "id": 1}]


if __name__ == '__main__':
    app.run()