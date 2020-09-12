#basic_app urls.py
from django.conf.urls import url###
from basic_app import views###


# TEMPLATE URLS!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url('register/', views.register, name ='register'),
    url('user_login/', views.user_login, name ='user_login'),
    #url('',views.index, name ='index'),
]
