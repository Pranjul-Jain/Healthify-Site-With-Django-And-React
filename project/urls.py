from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import LoginView, views, HealthifyView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),

    # authentication
    path("csrf/", LoginView.csrftoken, name="csrftoken"),
    path("login", LoginView.LoginPage),
    path("register", LoginView.RegisterPage),
    path("logout/", LoginView.logoutPage),
    path("authenticate/", LoginView.isAuthenticateApi),

    # Get data
    path("doctortips/", HealthifyView.HealthtipData),
    path("predict", HealthifyView.predictDisorder),

    # admin use
    path("adminlogin/", views.admin_login.as_view()),
    path("healthtips/", views.HealthtipsView.as_view(), name="healthtips"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
