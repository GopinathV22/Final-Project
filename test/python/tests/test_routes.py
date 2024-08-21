import pytest
from app import create_app, db
from app.models import Item 
 
# Task 3a: READ Test Case
def test_read_item(client, db):
    item = Item(name="Test Item", category="Test Category", available=True)
    db.session.add(item)
    db.session.commit()
    
    response = client.get(f'/items/{item.id}')
    
    assert response.status_code == 200
    assert response.json['name'] == 'Test Item'
    assert response.json['category'] == 'Test Category'
    assert response.json['available'] is True
 
# Task 3b: UPDATE Test Case
def test_update_item(client, db):
    item = Item(name="Old Name", category="Old Category", available=True)
    db.session.add(item)
    db.session.commit()
    
    response = client.put(f'/items/{item.id}', json={
        'name': 'New Name',
        'category': 'New Category',
        'available': False
    })
    
    assert response.status_code == 200
    updated_item = Item.query.get(item.id)
    assert updated_item.name == 'New Name'
    assert updated_item.category == 'New Category'
    assert updated_item.available is False
 
# Task 3c: DELETE Test Case
def test_delete_item(client, db):
    item = Item(name="Test Item", category="Test Category", available=True)
    db.session.add(item)
    db.session.commit()
    
    response = client.delete(f'/items/{item.id}')
    
    assert response.status_code == 204
    assert Item.query.get(item.id) is None
 
# Task 3d: LIST ALL Test Case
def test_list_all_items(client, db):
    items = [
        Item(name="Item 1", category="Category 1", available=True),
        Item(name="Item 2", category="Category 2", available=False)
    ]
    db.session.bulk_save_objects(items)
    db.session.commit()
    
    response = client.get('/items')
    
    assert response.status_code == 200
    assert len(response.json) == 2
    assert any(item['name'] == 'Item 1' for item in response.json)
    assert any(item['name'] == 'Item 2' for item in response.json)
 
# Task 3e: LIST BY NAME Test Case
def test_list_items_by_name(client, db):
    items = [
        Item(name="Unique Name", category="Category", available=True),
        Item(name="Another Name", category="Category", available=True)
    ]
    db.session.bulk_save_objects(items)
    db.session.commit()
    
    response = client.get('/items', query_string={'name': 'Unique Name'})
    
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Unique Name'
 
# Task 3f: LIST BY CATEGORY Test Case
def test_list_items_by_category(client, db):
    items = [
        Item(name="Item 1", category="Category 1", available=True),
        Item(name="Item 2", category="Category 2", available=True)
    ]
    db.session.bulk_save_objects(items)
    db.session.commit()
    
    response = client.get('/items', query_string={'category': 'Category 1'})
    
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['category'] == 'Category 1'
 
# Task 3g: LIST BY AVAILABILITY Test Case
def test_list_items_by_availability(client, db):
    items = [
        Item(name="Available Item", category="Category", available=True),
        Item(name="Unavailable Item", category="Category", available=False)
    ]
    db.session.bulk_save_objects(items)
    db.session.commit()
    
    response = client.get('/items', query_string={'available': 'true'})
    
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['available'] is True