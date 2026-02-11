import pytest
from fastapi.testclient import TestClient
from app import app, activities

client = TestClient(app)


def test_get_activities_returns_all_activities():
    """Test that get_activities returns all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    assert response.json() == activities


def test_get_activities_contains_chess_club():
    """Test that Chess Club is in the returned activities"""
    response = client.get("/activities")
    assert "Chess Club" in response.json()


def test_get_activities_contains_programming_class():
    """Test that Programming Class is in the returned activities"""
    response = client.get("/activities")
    assert "Programming Class" in response.json()


def test_get_activities_contains_gym_class():
    """Test that Gym Class is in the returned activities"""
    response = client.get("/activities")
    assert "Gym Class" in response.json()


def test_get_activities_response_structure():
    """Test that each activity has the required fields"""
    response = client.get("/activities")
    activities_data = response.json()
    
    required_fields = ["description", "schedule", "max_participants", "participants"]
    
    for activity_name, activity_data in activities_data.items():
        for field in required_fields:
            assert field in activity_data, f"Missing field '{field}' in activity '{activity_name}'"