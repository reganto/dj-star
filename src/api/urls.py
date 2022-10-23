from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path(
        "posts/<int:post_fk>/rating/",
        views.PostRatingView.as_view(),
        name="post_rating",
    ),
]
