# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin

# db = SQLAlchemy()

# class Plant(db.Model, SerializerMixin):
#     __tablename__ = 'plants'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     image = db.Column(db.String)
#     price = db.Column(db.Float)
#     is_in_stock = db.Column(db.Boolean)

#     def __repr__(self):
#         return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'



from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Example Plant model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(200))
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "is_in_stock": self.is_in_stock
        }

# Update Route: PATCH /plants/:id
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    # Update the plant's stock status if provided
    if 'is_in_stock' in data:
        plant.is_in_stock = data['is_in_stock']
    
    # Add additional fields to update as needed

    db.session.commit()
    return jsonify(plant.to_dict()), 200

# Destroy Route: DELETE /plants/:id
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    # Return an empty response with 204 status code
    return '', 204

if __name__ == '__main__':
    app.run(port=5555)
