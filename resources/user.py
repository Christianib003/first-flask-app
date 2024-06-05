from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UserModel
from schemas import UserSchema


user_blp = Blueprint("Users", __name__, description="Operations on users")

@user_blp.route("/register")
class UserRegister(MethodView):
    @user_blp.arguments(UserSchema)
    @user_blp.response(200, UserSchema)
    def post(self, user_data):
        # Check if user already exists
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="User already exists")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return {"message": "User created successfully"}

@user_blp.route("/users/<int:user_id>")
class UserDetail(MethodView):
    @user_blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user