from django.urls import path
from . import views

urlpatterns = [
    path("developers/", views.developers_list_view,name="developers_list"),
    path("developers/<str:username>", views.developer_cv_view,name="developers_cv"),
]
