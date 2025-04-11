import pytest
from rest_framework.test import APIClient
from api.models import Employee

@pytest.mark.django_db
def test_create_restaurant():
    user = Employee.objects.create_user(username="admin", password="12345678", build_version="1.0")
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post("/api/restaurants/", {"name": "Sushi Place"})
    assert response.status_code == 201
    assert response.data["name"] == "Sushi Place"
