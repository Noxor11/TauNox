from django.urls import path
from . import views


urlpatterns = [

    path("create-game/", views.create_game),
    path("join-game/<str:id>", views.join_game)

]
    
