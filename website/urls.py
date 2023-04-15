from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]

# process
# 1. create the template (html page)
# 2. create an url
# 3. create a view
