#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
from pyparsing import unicode

from code_files.service_helper import ServiceHelper

app = Flask(__name__)
helper = ServiceHelper("app.json")
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/flowers', methods=['GET'])
def get_flowers():
    return jsonify({'flowers': helper.get()})


@app.route('/flowers/<int:flower_id>', methods=['GET'])
def get_flower(flower_id):
    flowers = helper.get()
    for flower in flowers:
        if flower['id']==str(flower_id):
            return jsonify({'flower':flower})
    abort(404)


@app.route('/flowers/<int:flower_id>', methods=['DELETE'])
def delete_flower(flower_id):
    flowers = helper.get()
    for flower in flowers:
        if flower['id']==str(flower_id):
            flowers.remove(flower)
            helper.set(flowers)
            return jsonify({'status':True})
    abort(404)


@app.route('/flowers', methods=['POST'])
def add_flower():
    if not request.json or not 'name' in request.json:
        abort(400)
    flowers = helper.get()
    flower = {
        'id': request.json['id'],
        'name': request.json['name'],
        'color': request.json['color'],
        'category': request.json['category']
        }
    flowers.append(flower)
    helper.set(flowers)
    return jsonify({'flower': flower}), 201


@app.route('/flowers/<int:flower_id>', methods=['PUT'])
def update_flower(flower_id):
    flowers = helper.get()
    flower = [flower for flower in flowers if flower['id'] == str(flower_id)]
    if len(flower) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'id' in request.json and type(request.json['id']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not unicode:
        abort(400)
    new_flower={}
    new_flower['name'] = request.json.get('name', flower[0]['name'])
    new_flower['color'] = request.json.get('color', flower[0]['color'])
    new_flower['category'] = request.json.get('category', flower[0]['category'])
    flowers = update_state(flower_id,new_flower,flowers)
    helper.set(flowers)
    return jsonify({'task': flower[0]})


def update_state(id,new_flower,flowers):
    for flower in flowers:
        if flower['id']==str(id):
            flower['name'] = new_flower['name']
            flower['color'] = new_flower['color']
            flower['category'] = new_flower['category']
    return flowers


if __name__ == '__main__':
    app.run(debug=True,port=333)