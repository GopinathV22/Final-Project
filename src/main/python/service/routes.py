from flask import Flask, request, jsonify, abort
from app.models import db, Item
 
# Task 4a: READ Test Case
def test_read_item(client, db):
    item = Item(name="Test Item", category="Test Category", available=True)
    db.session.add(item)
    db.session.commit()
    
    response = client.get(f'/items/{item.id}')
    
    assert response.status_code == 200
    assert response.json['name'] == 'Test Item'
    assert response.json['category'] == 'Test Category'
    assert response.json['available'] is True
    app = Flask(__name__)
 
# Task 4b: UPDATE Function
    @app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        abort(404)
    
    data = request.get_json()
    item.name = data.get('name', item.name)
    item.category = data.get('category', item.category)
    item.available = data.get('available', item.available)
    db.session.commit()
    
    return jsonify({
    'name': item.name,
        'category': item.category,
        'available': item.available
    }), 200
 
# Task 4c: DELETE Function
    @app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        abort(404)
    
    db.session.delete(item)
    db.session.commit()
    
    return '', 204
 
# Task 4d: LIST ALL / LIST BY NAME / LIST BY CATEGORY / LIST BY AVAILABILITY
    @app.route('/items', methods=['GET'])
def list_items():
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')
 
    query = Item.query
 
    if name:
    query = query.filter(Item.name == name)
    if category:
        query = query.filter(Item.category == category)
    if available:
        query = query.filter(Item.available == (available.lower() == 'true'))
 
    items = query.all()
    result = [{
'id': item.id,
'name': item.name,
        'category': item.category,
        'available': item.available
    } for item in items]
 
    return jsonify(result), 200