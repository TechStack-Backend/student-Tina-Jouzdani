from django.urls import path
from . import views

urlpatterns = [
    path("developer/", views.developers_list_view,name="developers_list"),
    path("developer/<str:username>", views.developer_cv_view,name="developers_cv"),
]
