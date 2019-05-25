from django.conf.urls import url
from . import views

# appname宣言
app_name="myapp"
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^reg_title/$',views.reg_title,name='reg_title'),
	url(r'^reg_book/$',views.reg_book,name='reg_book'),
	url(r'^ls_title/$',views.ls_title,name='ls_title'),
	url(r'^ls_book/$',views.ls_book,name='ls_book'),
	url(r'^ls_lend/$',views.ls_lend,name='ls_lend'),
#funo
	url(r'^list_user/$',views.list_user,name='list_user'),
	url(r'^return_book/$',views.return_book,name='return_book'),
	url(r'^sub_return_book/$',views.sub_return_book,name='sub_return_book'),
	url(r'^lend_book/$',views.lend_book,name='lend_book'),
	url(r'^return_book/$',views.return_book,name='return_book'),
]