from django.contrib import admin
from django.contrib.sessions.backends import file
from django.urls import path,include

from .views import *

app_name = 'app'

urlpatterns = [
    path('all/',index,name='all'),
    path('python/',index2,name='index2'),
    path('html/', index_html, name='index_html'),
    path('html/python/', index2, name='index_htm'),
    path('rubric/<int:pk>/', detail, name='detail'),
    path('bb/<int:pk>/', detail_bb, name='detail_bb'),
    path('add-bb/', add_bb, name='add_bb'),
    path('stream/',stream,name='stream'),
    path('file/',file_response,name='file'),
    path('json/',json_response,name='json'),
    path('update/<int:pk>/bb/',update_bb,name='update_bb'),
    path('delete/<int:pk>/bb/',delete_bb,name='delete_bb'),

]
