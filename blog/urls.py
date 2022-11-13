from django.urls import path
from .views import homepage,detail_page


urlpatterns = [
    path('',homepage,name='home_page'),
    path('<int:id>/',detail_page,name='detail')
]