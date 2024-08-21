from app import create_app, db
from app.models import Item
 
def load_background_data():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Load background data
        items = [
            Item(name="Item 1", category="Category 1", available=True),
            Item(name="Item 2", category="Category 1", available=False),
            Item(name="Item 3", category="Category 2", available=True),
            Item(name="Item 4", category="Category 2", available=False),
        ]
        
        # Add items to the database
        db.session.bulk_save_objects(items)
        db.session.commit()
 
if __name__ == '__main__':
    load_background_data()