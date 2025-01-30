from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),

]
# URL mappings can employ reverse URL matching. That is we can reference the URL mapping by name rather than by the URL