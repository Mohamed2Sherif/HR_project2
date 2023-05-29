from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

urlpatterns = [
    # path("", home_view, name="welcome"),
    path("home/", home_view, name="home"),  # home_HR.html
    # admin
    path("", welcome_view, name="welcome"),
    path("login/", login_view, name="login"),  # login.html
    path("register/", registration_view, name="register"),  # add.html
    path("logout/", logoutview, name="logout"),  # logout
    path("about/", about_view, name="about"),  # about.html
    path("services/", services_view, name="services"),  # services.html
    path("contact/", contact_view.as_view(), name="contact"),  # contact.html
    path("add/", Add_View, name="add"),  # add.html
    path("delete/", delete_employee, name="delete_employee"),
    path("delete/<int:accId>/", emp_delete_table, name="emp_delete"),
    path("employee_detail/", employee_detail, name="employee_detail"),
    path("updating/<int:pk>/edit", employee_update.as_view(), name="updating"),
    path("profile/<int:pk>/", profile_view.as_view(), name="profile"),
    path("EmpTable", employee_List, name="EmpTable"),
    path("EmpTableredirect",list_after_delete,name="ladelete"),
    path("vacation/", request_vacation, name="vacation"),
    path("requests/", view_vacations.as_view(), name="requested"),
    path("acceptance",accept_view,name="accept"),
    path("Listemployee",EmpTable.as_view(),name="ListEmp")
]
