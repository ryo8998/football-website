from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="home"),
    path('rules/', views.rule, name='rule'),
    path('stars-players/', views.star_players, name='star_players'),
    path('stars-players/<int:id>', views.player_detail, name='player-detail'),
    path('links/', views.links, name='links'),
]