from django.urls import path
from . import views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordSetForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('notification/', views.notification, name='notification'),
    path('booknow/', views.booknow, name='booknow'),
    path('cookie/', views.cookie, name='cookie'),
    path('search_location/', views.search, name='search_location'),
    path('accounts/profile/', views.superadmin.as_view(), name='profile'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('price/', views.price, name='price'),
    path('charts/', views.charts, name='charts'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='adminpanel/login.html',authentication_form=LoginForm), name="login"),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='adminpanel/changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='adminpanel/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerlogout/', views.customerlogout,name='customerlogout'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
    path('utilities_animation/', views.utilities_animation, name='utilities_animation'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='adminpanel/password_reset.html'), name='passwordreset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='adminpanel/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='adminpanel/password_reset_confirm.html',form_class=MyPasswordSetForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='adminpanel/password_reset_complete.html'),name='password_reset_complete'),
    path('utilities_border/', views.utilities_border, name='utilities_border'),
    path('utilities_color/', views.utilities_color, name='utilities_color'),
    path('utilities_other/', views.utilities_other, name='utilities_other'),
    path('signup/', views.customer, name='customer'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerdashboard/', views.customerdashboard, name='customerdashboard'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('how_it_works/', views.how_it_works, name='how-it-works'),
    path('features/', views.features, name='features'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout1/', views.checkout1, name='checkout1'),   
    path('calculator/', views.calculator, name='calculator'),
    path('booknow1/', views.booknow1, name='booknow1'),
    path('contactus/', views.contactus, name='contactus'),
    path('table1/', views.table1, name='table1'),
    path('adminetable/', views.adminetable, name='adminetable'),


    
]