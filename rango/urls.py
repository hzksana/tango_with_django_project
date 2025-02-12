from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
path('add_category/', views.add_category, name='add_category'),
path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
]
#<a href="{% url 'rango:about' %}">About</a>
#colon in url separates namespace from actual URL name

#<a href="{% url 'about' %}">About</a>
#if appname not specified, reference a URL with just name of mapping you want to refer to

# URL mappings can employ reverse URL matching. That is we can reference the URL mapping by name rather than by the URL