from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'register/', user_views.register, name='register'),
    url(r'profile/', user_views.profile, name='profile'),
    url(r'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    url(r'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    url(r'password-reset-confirm/(?P<uidb64>[0-9a-zA-Z_\-]+)/(?P<token>[0-9a-zA-Z]{1,13}-[0-9a-zA-Z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
