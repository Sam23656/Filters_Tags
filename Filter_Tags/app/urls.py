from django.urls import path

from app.views import show_index_page

urlpatterns = [
    path('', show_index_page),
]
