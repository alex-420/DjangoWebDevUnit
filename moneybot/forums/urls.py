from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ListForums.as_view(), name="all"),
    path("new/", views.CreateForum.as_view(), name="create"),
    path("posts/in/<slug>/",views.SingleForum.as_view(),name="single"),
    path("join/<slug>/",views.JoinForum.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveForum.as_view(),name="leave"),
]
