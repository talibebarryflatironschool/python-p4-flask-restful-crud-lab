from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


# Initialize SQLAlchemy without the app then bind it
db = SQLAlchemy()


class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'

# PATCH route: update a plant
# @app.route('/plants/<int:id>', methods=['PATCH'])
# def update_plant(id):
    # plant = Plant.query.get_or_404(id)
    # data = request.get_json() or {}

    # if 'is_in_stock' in data:
    #     plant.is_in_stock = data['is_in_stock']

    # # Commit the update to the database
    # db.session.commit()
    # return jsonify(plant.to_dict()), 200

# DELETE route: delete a plant
# @app.route('/plants/<int:id>', methods=['DELETE'])
# def delete_plant(id):
#     plant = db.session.get(Plant,id)
#     db.session.delete(plant)
#     db.session.commit()
#     return '', 204

