from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
# establish connection to mongodb
client = MongoClient("mongodb://localhost:27017")
db = client.store
collection = db.fakestore


# create operation
@app.route('/stores', methods=['POST'])
def create_stores():
    data = request.get_json()
    insert_result = collection.insert_one(data)
    return jsonify({"message": "Store created successfully", "id": str(insert_result.inserted_id)}), 201


# read operation
@app.route('/stores', methods=['GET'])
def get_stores():
    fakestore = list(collection.find())
    for store in fakestore:
        store['_id'] = str(store['_id'])  # Convert objectId to string
    return jsonify(fakestore), 200


# update operation
@app.route('/stores/<store_id>', methods=['PUT'])
def update_stores(store_id):
    data = request.get_json()
    update_result = collection.update_one({'_id': ObjectId(store_id)}, {'$set': data})
    if update_result.modified_count > 0:
        return jsonify({"message": "product updated successfully"}), 200
    else:
        return jsonify({"message": "product not found"}), 404


# Delete operation
@app.route('/stores/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    delete_result = collection.delete_one({'_id': ObjectId(store_id)})
    if delete_result.deleted_count > 0:
        return jsonify({"message": "product deleted successfully"}), 200
    else:
        return jsonify({"message": "product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
