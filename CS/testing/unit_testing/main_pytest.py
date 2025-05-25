from typing import List

#  ------------ Simple testing ------------

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size
    
    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("Cart is full!")
        self.items.append(item)
    
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price

class ItemDatabase:
    def __init__(self) -> None:
        ...
    
    def get(self, item: str) -> float:
        ...

# ------------ Testing using fixtures (=Context managers) ------------

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True
    
    def get_user(self, username):
        return self.users.get(username)

import sqlite3
class Database:
    """Simulates a basic user database."""
    def __init__(self):
        self.data = {}
    
    def add_user(self, user_id, name):
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = name
    
    def get_user(self, user_id):
        return self.data.get(user_id, None)
    
    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]

# ------------ Testing using parametrization ------------

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

# ------------ Testing using mock data ------------
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")

def save_user(name, age):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

class APIClient:
    """Simulates an external API Client."""
    def get_user_data(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("API request failed")

class UserService:
    """Uses APIClient to fetch user data and process it."""
    def __init__(self, api_client: APIClient):
        self.api_client: APIClient = api_client
    
    def get_username(self, user_id):
        """Fetches a user and returns their username in uppercase."""
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper()

# ------------ API testing ------------

from flask import Flask, jsonify, request

webapp = Flask(__name__)

users = {} # Simulated in-memory db

@webapp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns user info by ID."""
    user = users.get(user_id)
    if user:
        return jsonify({'id': user_id, "name": user}), 200
    return jsonify({"error": "User not found"}), 404

@webapp.route("/users", methods=['POST'])
def add_user():
    """Adds a new user."""
    data = request.json
    user_id = data.get('id')
    name = data.get('name')
    if not user_id or not name:
        return jsonify({'error': "Invalid data"}), 400
    if user_id in users:
        return jsonify({'error': "User already exists"}), 400
    users[user_id] = name
    return jsonify({'id': user_id, 'name': name}), 201