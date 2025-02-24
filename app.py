from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"message": "Item not found"}, 404

    def post(self):
        data = request.get_json()
        new_item = {"name": data["name"], "price": data["price"]}
        items.append(new_item)
        return new_item, 201

    def delete(self, name):
        for item in items:
            if item["name"] == name:
                items.remove(item)
                return {"message": "Item deleted"}


api.add_resource(Item, "/item/<string:name>", "/item")


if __name__ == "__main__":
    app.run(debug=True)
