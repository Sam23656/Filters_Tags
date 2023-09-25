from app.views import show_index_page, show_block_page
from django.urls import path

urlpatterns = [
    path('', show_index_page),
    path('block/', show_block_page, name='block'),
]
