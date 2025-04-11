from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuViewSet, vote, results

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('menus', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vote/<int:menu_id>/', vote),
    path('results/', results),
]
