# Django
from django.urls import include, path
# Django REST Framework
from rest_framework.routers import DefaultRouter
#Views
from .views import DnaView, StatsView

urlpatterns = [
    path('mutation',DnaView.as_view(),name='dna_mutation'),
    path('stats',StatsView.as_view(),name='stats')
]