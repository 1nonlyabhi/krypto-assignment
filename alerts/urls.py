from django.urls import path
from .views import AlertListView, AlertView, TriggerView

urlpatterns = [
    path('manage', AlertView.as_view()),
    path('alertlist', AlertListView.as_view()),
    path('currentprice', TriggerView.as_view())
]