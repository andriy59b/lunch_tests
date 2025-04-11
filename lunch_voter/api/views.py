from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import date
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer




class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = self.request.GET.get('today')
        if today:
            return self.queryset.filter(day=date.today())
        return super().get_queryset()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    Vote.objects.update_or_create(employee=request.user, menu=menu)
    return Response({'message': 'Vote saved'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def results(request):
    today = date.today()
    menus = Menu.objects.filter(day=today)
    output = []
    for menu in menus:
        count = Vote.objects.filter(menu=menu).count()
        output.append({
            'restaurant': menu.restaurant.name,
            'votes': count
        })
    return Response(sorted(output, key=lambda x: -x['votes']))


