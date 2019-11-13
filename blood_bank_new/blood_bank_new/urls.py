"""blood_bank_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.indexPage, name="main"),
    path('login/', views.loginPage, name="login"),
    path('checkuser/', views.checkUser, name="checkuser"),

    path('inbox/', views.inboxPage, name="inbox"),

    path('addorg/', views.organizationPage, name="addorg"),
    path('saveOrg/', views.saveOrganization, name="saveOrg"),
    path('vieworg/', views.viewOrg, name="vieworg"),
    path('delete/', views.deleteEmployee, name="delete"),
    path('logout/', views.logOut, name="logout"),


    path('donor/', views.donorPage, name="donor"),
    path('checkdonor/', views.checkDonor, name="checkdonor"),
    path('donorreg/', views.donorReg, name="donorreg"),
    path('savedonor/', views.saveDonor, name="savedonor"),
    path('viewdonor/', views.viewDonor, name="viewdonor"),
    path('updatedonor/', views.updateDonor, name="updatedonor"),
    path('logoutDonor/', views.logoutDonor, name="logoutDonor"),

    path('orglogin/', views.orgLogin, name="orglogin"),
    path('checkorg/', views.checkOrg, name="checkorg"),
    path('logoutOrg/', views.logoutOrg, name="logoutOrg"),
]
