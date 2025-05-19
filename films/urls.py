from django.urls import *
from .views import *

app_name = 'films'

urlpatterns = [
    re_path(r'^A.{1}!/$', FilmListView.as_view(), name='regular_films'),
    path('allfilms/', FilmListView.as_view(), name='all'),
    path('slug/<slug:slug>/', FilmDetailBySlugView.as_view(), name='film-by-slug'),
    path('pk/<int:pk>/', FilmDetailByIdView.as_view(), name='film-by-id'),
    path('addfilm/', FilmCreateView.as_view(), name='add_and_save_film'),
    path('index/', IndexView.as_view(), name='index'),
]
