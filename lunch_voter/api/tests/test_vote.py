import pytest
from rest_framework.test import APIClient
from django.utils import timezone
from api.models import Employee, Restaurant, Menu

@pytest.mark.django_db
def test_vote_success():
    user = Employee.objects.create_user(username="testuser", password="12345678", build_version="1.0")
    restaurant = Restaurant.objects.create(name="Test Resto")
    menu = Menu.objects.create(restaurant=restaurant, day=timezone.now().date(), items="Pizza")

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post(f"/api/vote/{menu.id}/")
    assert response.status_code == 200
    assert response.data["message"] == "Vote saved"
