from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('current_projects/', views.current_projects, name='current_projects'),
    path('past_projects/', views.past_projects, name='past_projects')
]
