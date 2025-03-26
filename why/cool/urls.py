from django.urls import path
from cool.views import cool_views

app_name="cool"

urlpatterns = [
    path('cool/',cool_views,name="cool_name")
]