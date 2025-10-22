"""
URL configuration for crm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
import crm_data
from django.conf.urls.static import static
from . import views
from django.conf import settings
from crm_data.views import *
app_name='crm_data'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummy/',dummy,name='dummy'),
    path('home/',home,name='home'),
    path('registration/',registration,name='registration'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('contact_us/',contact_us,name='contact_us'),
    path('about_us/',about_us,name='about_us'),
    path('profile/',profile,name='profile'),
    path('callingsheet/', views.callingsheet, name='callingsheet'),
    path('intrested/',intrested,name='intrested'),
    path('escalation/',escalation,name='escalation'),
    path('paymentconfirmation/',paymentconfirmation,name='paymentconfirmation'),
    path('paymentdone/',paymentdone,name='paymentdone'),
    path('move_to_interested/<int:id>/', views.move_to_interested, name='move_to_interested'),
    path('move_to_escalation/<int:id>/', views.move_to_escalation, name='move_to_escalation'),
    path('move_to_payment_confirmation/<int:id>/', views.move_to_payment_confirmation, name='move_to_payment_confirmation'),
    path('move_to_payment_done/<int:id>/', views.move_to_payment_done, name='move_to_payment_done'),
    path('interested_to_callingsheet/<int:id>/', views.interested_to_callingsheet, name='interested_to_callingsheet'),
    path('interested_to_escalation/<int:id>/', views.interested_to_escalation, name='interested_to_escalation'),
    path('interested_to_payment_confirmation/<int:id>/', views.interested_to_payment_confirmation, name='interested_to_payment_confirmation'),
    path('interested_to_payment_done/<int:id>/', views.interested_to_payment_done, name='interested_to_payment_done'),
    path('escalation/to_interested/<int:pk>/', views.move_escalation_to_interested, name='move_escalation_to_interested'),
    path('escalation/to_callingsheet/<int:pk>/', views.move_escalation_to_callingsheet, name='move_escalation_to_callingsheet'),
    path('escalation/to_payment_confirmation/<int:pk>/', views.move_escalation_to_payment_confirmation, name='move_escalation_to_payment_confirmation'),
    path('escalation/to_payment_done/<int:pk>/', views.move_escalation_to_payment_done, name='move_escalation_to_payment_done'),
    path('paymentconfirmation/to_callingsheet/<int:pk>/', views.paymentconfirmation_to_callingsheet, name='paymentconfirmation_to_callingsheet'),
    path('paymentconfirmation/to_interested/<int:pk>/', views.paymentconfirmation_to_interested, name='paymentconfirmation_to_interested'),
    path('paymentconfirmation/to_escalation/<int:pk>/', views.paymentconfirmation_to_escalation, name='paymentconfirmation_to_escalation'),
    path('paymentconfirmation/to_payment_done/<int:pk>/', views.paymentconfirmation_to_payment_done, name='paymentconfirmation_to_payment_done'),
    path('paymentdone/to_callingsheet/<int:pk>/', views.paymentdone_to_callingsheet, name='paymentdone_to_callingsheet'),
    path('paymentdone/to_interested/<int:pk>/', views.paymentdone_to_interested, name='paymentdone_to_interested'),
    path('paymentdone/to_escalation/<int:pk>/', views.paymentdone_to_escalation, name='paymentdone_to_escalation'),
    path('paymentdone/to_paymentconfirmation/<int:pk>/', views.paymentdone_to_paymentconfirmation, name='paymentdone_to_paymentconfirmation'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
