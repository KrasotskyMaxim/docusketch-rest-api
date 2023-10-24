from flask import Flask, request, jsonify
from pymongo import MongoClient

import config


app = Flask(__name__)

client = MongoClient(config.DB_HOST, config.DB_PORT)
db = client.example_db
collection = db.example_collection


@app.route('/api/<key>', methods=['GET'])
def get_data(key):
    data = collection.find_one({'key': key})
    if not data:
        return jsonify({'message': 'Key not found'})
    return jsonify({'key': data['key'], 'value': data['value']})
    

@app.route('/api/<key>', methods=['POST'])
def add_data(key):
    value = request.json.get('value')
    if not value:
        return jsonify({'message': 'Value is required'}), 400
    new_data = {'key': key, 'value': value}
    collection.insert_one(new_data)
    return jsonify({'message': 'Data created successfully'})


@app.route('/api/<key>', methods=['PUT'])
def edit_data(key):
    value = request.json.get('value')
    if not value:
        return jsonify({'message': 'Value is required'}), 400
    update_result = collection.update_one({'key': key}, {'$set': {'value': value}})
    if not update_result.modified_count:
        return jsonify({'message': 'Key not found'})
    return jsonify({'message': 'Data updated successfully'})


if __name__ == '__main__':
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.DEBUG)
