from django.urls import path

from estoque.views import index


urlpatterns = [
    path('', index, name='index'),
]
