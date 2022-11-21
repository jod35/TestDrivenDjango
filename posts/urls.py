from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="homepage"),
    path("post/<int:id>/",views.post_detail,name='post_detail')
]
