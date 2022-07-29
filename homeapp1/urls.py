from django.urls import path
from .views import HomeAppViews

urlpatterns=[
    path('',HomeAppViews.as_view(),name='home'),
]