from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
]

# process
# 1. create the template (html page)
# 2. create an url
# 3. create a view
