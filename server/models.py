from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'

# PATCH route: update the plant's is_in_stock status (or other fields as needed)
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json() or {}

    # Update the is_in_stock attribute if it is provided in the request body
    if 'is_in_stock' in data:
        plant.is_in_stock = data['is_in_stock']

    # Add additional fields to update here if needed

    db.session.commit()
    return jsonify(plant.to_dict()), 200

# DELETE route: delete a plant
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    # Return an empty response with status code 204 (No Content)
    return '', 204

if __name__ == '__main__':
    app.run(port=5555)
