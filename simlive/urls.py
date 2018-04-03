from django.urls import path

from . import views

app_name = 'simlive'
urlpatterns = [
    path('', views.index),
    path('<int:account_id>/', views.account_detail, name='account_detail'),
    path('accounts', views.bcaccount_list),
    path('videos', views.video_list),
    path('videos/<int:video_id>/', views.video_detail)
]
