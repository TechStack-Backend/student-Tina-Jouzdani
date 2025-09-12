from django.urls import path
from . import views

urlpatterns = [
    path("developer/", views.developers_list_views,name="developers_list"),
    path("developer/<str:username>", views.developers_cv_views,name="developers_cv"),
]
