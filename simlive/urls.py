from django.urls import path

from . import views

urlpatterns = [
    path('accounts', views.bcaccount_list),
    path('videos', views.video_list),
    path('videos/<int:video_id>/', views.video_detail)
]
