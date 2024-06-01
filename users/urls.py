from django.urls import path

from users import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "profile/<int:pk>/",
        views.UserDetailView.as_view(),
        name="profile"
    ),
    path(
        "profile/<int:pk>/update/",
        views.UserUpdateView.as_view(),
        name="profile-update"
    ),
    path(
        "profile/<int:pk>/delete/",
        views.UserDeleteView.as_view(),
        name="profile-delete"
    ),
]

app_name = "users"
