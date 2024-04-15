from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HOME, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('about/', views.ABOUT, name='about'),
    path('check/', views.CHECKBOXES, name='checkboxes'),
    path('skate-dice/', views.skate_dice, name='skate_dice'),
    path('signin/', LoginView.as_view(template_name='sign_in.html'), name='sign_in'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url=reverse_lazy('change_password_done')
    ), name='change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(
        template_name='change_password_done.html'
    ), name='change_password_done'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

# This appends the static URLs to the urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
