from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path("", views.channels_list, name='chanlist'),
    path("<str:channel_id>/", views.channels, name='chan'),
    path("<str:channel_id>/content/", views.contents, name='cont')
]