from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/',
views.show_category, name='show_category'),
path('add_category/', views.add_category, name='add_category'),
]

# URL mappings can employ reverse URL matching. That is we can reference the URL mapping by name rather than by the URL