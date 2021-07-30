from django.urls import path
from .views import AlertListView, AlertView

urlpatterns = [
    path('manage', AlertView.as_view()),
    path('details', AlertListView.as_view())
]