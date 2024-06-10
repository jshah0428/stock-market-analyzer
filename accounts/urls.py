from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_form, name = "signup"),
    path('login/', views.login_form, name = "login"), #repath could work here as well, similar to above.
    path('logout/', views.logout_form, name = "logout")



]
