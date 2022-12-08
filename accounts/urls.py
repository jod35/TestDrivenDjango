from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.register_user,name='signup_page'),
    path('login/',views.login_page,name='login_page')
]