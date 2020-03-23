from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name="password_change" ),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name="home/index.html"), name="password_change_done"),
    re_path('profile/edit/$', views.edit_profile, name='edit_profile'),
]
