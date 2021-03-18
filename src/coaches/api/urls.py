from django.urls import path

# from coaches.api.views import api_detail_coach_view

from coaches.api.views import (
    api_detail_coach_view,
    ApiCoachListView
)

app_name = 'coaches'

urlpatterns = [
    path('list', ApiCoachListView.as_view(), name="list"),
    path('<slug>', api_detail_coach_view, name='detail'),
    # path('list', ApiCoachListView.as_view(), name="list"),
]