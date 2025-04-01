import requests
import json
from datetime import datetime

# API Configuration
BASE_URL = "http://localhost:8000"
TOKEN = None

def test_register():
    """Test user registration"""
    url = f"{BASE_URL}/auth/register"
    data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    response = requests.post(url, json=data)
    print("Register Response:", response.json())
    return response.status_code == 201

def test_login():
    """Test user login and get token"""
    global TOKEN
    url = f"{BASE_URL}/auth/login"
    data = {
        "username": "test@example.com",
        "password": "testpassword123"
    }
    response = requests.post(url, data=data)
    print("Login Response:", response.json())
    if response.status_code == 200:
        TOKEN = response.json()["access_token"]
        return True
    return False

def test_create_blog():
    """Test creating a blog post"""
    if not TOKEN:
        print("No token available. Please login first.")
        return False
    
    url = f"{BASE_URL}/blog/"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = {
        "title": "Test Blog Post",
        "body": "This is a test blog post created via API"
    }
    response = requests.post(url, json=data, headers=headers)
    print("Create Blog Response:", response.json())
    return response.status_code == 201

def test_get_blogs():
    """Test getting all blogs"""
    if not TOKEN:
        print("No token available. Please login first.")
        return False
    
    url = f"{BASE_URL}/blog/"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    print("Get Blogs Response:", response.json())
    return response.status_code == 200

def test_get_users():
    """Test getting all users"""
    if not TOKEN:
        print("No token available. Please login first.")
        return False
    
    url = f"{BASE_URL}/user/"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    print("Get Users Response:", response.json())
    return response.status_code == 200

def run_all_tests():
    """Run all tests in sequence"""
    print("\n=== Starting API Tests ===\n")
    
    # Test registration
    print("Testing registration...")
    if test_register():
        print("✓ Registration successful")
    else:
        print("✗ Registration failed")
    
    # Test login
    print("\nTesting login...")
    if test_login():
        print("✓ Login successful")
    else:
        print("✗ Login failed")
    
    # Test blog creation
    print("\nTesting blog creation...")
    if test_create_blog():
        print("✓ Blog creation successful")
    else:
        print("✗ Blog creation failed")
    
    # Test getting blogs
    print("\nTesting get blogs...")
    if test_get_blogs():
        print("✓ Get blogs successful")
    else:
        print("✗ Get blogs failed")
    
    # Test getting users
    print("\nTesting get users...")
    if test_get_users():
        print("✓ Get users successful")
    else:
        print("✗ Get users failed")
    
    print("\n=== Tests Completed ===\n")

if __name__ == "__main__":
    run_all_tests() 