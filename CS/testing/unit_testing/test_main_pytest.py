from main_pytest import add, ShoppingCart, ItemDatabase, divide, UserManager, Database, is_prime, get_weather, save_user, APIClient, UserService, webapp
import pytest
from unittest.mock import Mock

#  ------------ Simple testing ------------

def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, "(-1) + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"
    assert add(-1, -2) == -3, "(-1) + (-2) should be -3"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    assert divide(9, 3) == 3, "9 / 3 should be 3"
    assert divide(5, 2) == 2.5, "5 / 2 should be 2.5"

# ------------ Testing using fixtures (=Context managers) ------------

@pytest.fixture
def cart():
    return ShoppingCart(max_size=5)

def test_can_add_item_to_cart(cart):
    cart.add('apple')
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')
    assert 'apple' in cart.get_items()

def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add('apple')
    with pytest.raises(OverflowError, match="Cart is full!"):
        cart.add('apple')

def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')
    """ 
    price_map = {
        'apple': 1.0,
        'orange': 2.0
    }
    assert cart.get_total_price(price_map=price_map) == 3.0
     """
    item_db = ItemDatabase()
    #item_db.get = Mock(return_value=1.0)
    def mock_get_item(item: str):
        return 1 if item == 'apple' else 2
    item_db.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(price_map=item_db) == 3.0

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before test."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("john_doe", "another@example.com")

@pytest.fixture
def db():
    """Provides a fresh instance of the Database class for each separate test and cleans up after the test."""
    database = Database()
    yield database
    database.data.clear()

def test_add_user(db):
    db.add_user(1, 'Alice')
    assert db.get_user(1) == 'Alice'

def test_add_duplicate_user(db):
    db.add_user(1, 'ALice')
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, 'Bob')

def test_delete_user(db):
    db.add_user(2, 'Bob')
    db.delete_user(2)
    assert db.get_user(2) is None

# ------------ Testing using parametrization ------------

@pytest.mark.parametrize("number, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
    (30, False),
])

def test_is_prime(number, expected):
    assert is_prime(number) == expected

# ------------ Testing using mock data ------------

def test_get_weather(mocker):
    mock_get_request = mocker.patch('main_pytest.requests.get')
    mock_get_request.return_value.status_code = 200
    mock_get_request.return_value.json.return_value = {'temperature': 25, 'condition': 'sunny'}
    result = get_weather('Dubai')
    assert result == {'temperature': 25, 'condition': 'sunny'}
    mock_get_request.assert_called_once_with("https://api.weather.com/v1/Dubai")

def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    
    save_user("Alice", 30)
    
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30)
    )

def test_get_username(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)
    mock_api_client.get_user_data.return_value = {'id': 1, 'name': 'Alice'}
    service = UserService(mock_api_client)
    result = service.get_username(1)
    assert result == 'ALICE'
    mock_api_client.get_user_data.assert_called_once_with(1)

# ------------ API testing ------------

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    webapp.config['TESTING'] = True # Enabling testing mode for the app
    with webapp.test_client() as client:
        yield client

def test_add_user(client):
    """Test adding a new user."""
    response = client.post("/users", json={'id': 1, 'name': 'Alice'})
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'Alice'}

def test_get_user(client):
    """Test retrieving a user."""
    client.post("/users", json={'id': 2, 'name': 'Bob'})
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json == {'id': 2, 'name': 'Bob'}

def get_user_not_found(client):
    """Test retrieving a non-existent user."""
    response = client.get("/users/3")
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}

def test_add_duplicate_user(client):
    """Test adding a duplicate user."""
    client.post("/users", json={'id': 3, 'name': 'Charlie'})
    response = client.post("/users", json={'id': 3, 'name': 'Charlie'})
    assert response.status_code == 400
    assert response.json == {'error': "User already exists"}