from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HOME, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('check/', views.CHECKBOXES, name='checkboxes'),
    path('signin/', LoginView.as_view(template_name='sign_in.html'), name='sign_in'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)