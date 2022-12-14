from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="homepage"),
    path("post/<int:id>/",views.post_detail,name='post_detail'),
    path("create_post/",views.create_post,name='create_post')
]
