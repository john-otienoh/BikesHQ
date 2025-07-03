from django.contrib.auth import views as auth_views
from django.urls import include, path
from account.views import RegisterView, profile, CustomLoginView
from account.forms import LoginForm
from .views import home, products, product_detail

# app_name = "account"

urlpatterns = [
    path("home/", home, name="home"),
    path("products/", products, name="products"),
    path("product/<slug:product>/", product_detail, name="product_detail"),
    path("category/<slug:category_slug>/", products, name='product_by_category'),
    path(
        "login/",
        CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="registration/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
    path("", include("django.contrib.auth.urls")),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile, name="profile"),
]
