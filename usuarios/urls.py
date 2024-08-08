from django.urls import path
from .views import LoginUser, LogOutUser, RegisterUser

urlpatterns = [
    path('/registrar', RegisterUser.as_view()),
    path('/login', LoginUser.as_view()),
    path('/logout', LogOutUser.as_view()),
    # To-Do: Otro endpoint (usuario, por ejemplo)
]
