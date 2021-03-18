from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class ApiCoachListView(ListAPIView):
    queryset = Coach.object.all()
    serializer_class = CoachSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination