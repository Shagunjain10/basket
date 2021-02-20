from django.urls import include, path
from . import views

urlpatterns = [
    path('items/', views.grocery),
]
