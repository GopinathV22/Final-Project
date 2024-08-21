from models.product import Product
 
# Task 2a: Test Case for READ Functionality
def test_read_product():
    product = Product(id=1, name="Test Product", category="Test Category", price=19.99)
    product_dict = product.to_dict()
    assert product_dict["name"] == "Test Product"
    assert product_dict["category"] == "Test Category"
    assert product_dict["price"] == 19.99
 
# Task 2b: Test Case for UPDATE Functionality
def test_update_product():
    product = Product(id=1, name="Old Name", category="Old Category", price=19.99)
    product.update(name="New Name", category="New Category", price=29.99)
    assert product.name == "New Name"
    assert product.category == "New Category"
    assert product.price == 29.99
 
# Task 2c: Test Case for DELETE Functionality
def test_delete_product():
    product = Product(id=1, name="Test Product", category="Test Category", price=19.99, available=True)
    product.update(available=False)
    assert product.available is False
 
# Task 2d: Test Case for LIST ALL Functionality
def test_list_all_products():
    products = [
        Product(id=1, name="Product 1", category="Category 1", price=10.00),
        Product(id=2, name="Product 2", category="Category 2", price=20.00),
    ]
    product_dicts = [product.to_dict() for product in products]
    assert len(product_dicts) == 2
    assert product_dicts[0]["name"] == "Product 1"
    assert product_dicts[1]["name"] == "Product 2"
 
# Task 2e: Test Case for FIND BY NAME Functionality
def test_find_by_name():
    products = [
        Product(id=1, name="Product 1", category="Category 1", price=10.00),
        Product(id=2, name="Product 2", category="Category 2", price=20.00),
        Product(id=3, name="Product 1", category="Category 3", price=15.00)
    ]
    found_products = [p for p in products if p.name == "Product 1"]
    assert len(found_products) == 2
    assert found_products[0].category == "Category 1"
    assert found_products[1].category == "Category 3"
 
# Task 2f: Test Case for FIND BY CATEGORY Functionality
def test_find_by_category():
    products = [
        Product(id=1, name="Product 1", category="Category 1", price=10.00),
        Product(id=2, name="Product 2", category="Category 2", price=20.00),
        Product(id=3, name="Product 3", category="Category 1", price=15.00)
    ]
    found_products = [p for p in products if p.category == "Category 1"]
    assert len(found_products) == 2
    assert found_products[0].name == "Product 1"
    assert found_products[1].name == "Product 3"
 
# Task 2g: Test Case for FIND BY AVAILABILITY Functionality
def test_find_by_availability():
    products = [
        Product(id=1, name="Product 1", category="Category 1", price=10.00, available=True),
        Product(id=2, name="Product 2", category="Category 2", price=20.00, available=False),
        Product(id=3, name="Product 3", category="Category 3", price=15.00, available=True)
    ]
    available_products = [p for p in products if p.available]
    assert len(available_products) == 2
    assert available_products[0].name == "Product 1"
    assert available_products[1].name == "Product 3"