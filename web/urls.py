from django.urls import path

from . import views


app_name = 'web'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

    path('web/', views.CreateWebView.as_view(), name='web'),

    path('web_done/', views.WebSuccessView.as_view(),name = 'web_done'),

    path('webs/<int:product>',
        views.NameView.as_view(),
        name='webs_cat'
        ),


    path('user-list/<int:user>',
        views.UserView.as_view(),
        name='user_list'
        ),

    path('web-detail/<int:pk>',
        views.DetailView.as_view(),
        name = 'web_detail'
        ),

     path('web/<int:pk>/delete/',
        views.WebDeleteView.as_view(),
        name = 'web_delete'
        ),

    path('mypage/', views.IndexView.as_view(), name= 'mypage')

]

