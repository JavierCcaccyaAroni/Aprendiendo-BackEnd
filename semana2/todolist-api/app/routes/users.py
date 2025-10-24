# Blueprint permite crear modulos de la aplicación
from flask import Blueprint, request
from utils import response_success, response_error
from app.models.users import User
from app.models.tasks import Task
from sqlalchemy.exc import IntegrityError
from app.crypt import bcrypt
from app.db import db

# crear la instancia de Blueprint

user_route = Blueprint('user_route', __name__)

@user_route.route("/users")
def get_users():
    try:
        users = User.query.all()
        serialized_users = [user.to_json() for user in users]
        return response_success(serialized_users)
    except Exception as e:
        return response_error(str(e))

@user_route.route("/users/<int:user_id>")
def get_user(user_id):
    try:
        user = User.query.get(user_id)

        if user is None:
            return response_error("User not found")

        return response_success(user.to_json())
    except Exception as e:
        return response_error(str(e))

@user_route.route("/users", methods=["POST"])
def add_user():
    try:
        user = User(**request.get_json())
        user.password = bcrypt.generate_password_hash(user.password)
        db.session.add(user)
        db.session.commit()

        return response_success("Usuario creado correctamente", 201)
    except IntegrityError:
        return response_error("El username o email ya existen")
    except Exception as e:
        return response_error(str(e))

@user_route.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return response_error("User not found")

        new_user = request.json
        user.name = new_user.get("name", user.name)
        user.lastname = new_user.get("lastname", user.lastname)
        user.phone = new_user.get("phone", user.phone)
        user.address = new_user.get("address", user.address)
        user.username = new_user.get("username", user.username)
        user.email = new_user.get("email", user.email)

        db.session.commit()

        return response_success("Usuario actualizado correctamente")
    except Exception as e:
        return response_error(str(e))
    
@user_route.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    try:
        # antes de eliminar el usuario, se deben eliminar sus tareas asociadas
        tasks_by_user = Task.query.filter_by(user_id=user_id).all()

        if len(tasks_by_user) is 0:
            user = User.query.get(user_id)

            if not user:
                return response_error("User not found")

            db.session.delete(user)
            db.session.commit()

            return response_success("User deleted")
        return response_success("User has no tasks to delete")
    except Exception as e:
        return response_error(str(e))
