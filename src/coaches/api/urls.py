from django.urls import path

from coaches.api.views import (
    ApiCoachListView
)

app_name = 'coaches'

urlpatterns = [
    path('list', ApiCoachListView.as_view(), name='list'),
]