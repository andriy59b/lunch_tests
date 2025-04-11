import pytest
from rest_framework.test import APIClient
from api.models import Employee, Restaurant
from datetime import date

@pytest.mark.django_db
def test_create_menu():
    user = Employee.objects.create_user(username="chef", password="12345678", build_version="1.0")
    restaurant = Restaurant.objects.create(name="Kebab King")
    client = APIClient()
    client.force_authenticate(user=user)

    payload = {
        "restaurant": restaurant.id,
        "day": date.today().isoformat(),
        "items": "Kebab, Fries"
    }

    response = client.post("/api/menus/", payload)
    assert response.status_code == 201
    assert "Kebab" in response.data["items"]
