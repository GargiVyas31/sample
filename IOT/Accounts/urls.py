from django.urls import path
from .import views
app_name='Accounts'

urlpatterns=[
	path('register/',views.register,name="register"),
	path('login/',views.login,name="login"),
	path('',views.homepage,name="homepage")
	]