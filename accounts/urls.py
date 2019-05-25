from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

app_name='accounts'
urlpatterns=[
	path('signup/',views.SignUpView.as_view(),name='signup'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^logout_view/$',views.logout_view,name='logout_view'),
]