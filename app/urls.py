
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path("run-database-script/", views.run_database_script, name="run_database_script"),
]

