from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
urlpatterns = [
    # path("", home_view, name="welcome"),
    path("home/", home_view, name="home"),  # home_HR.html
      # admin
     path("", login_view, name='login'),  # login.html
    path("register/", registration_view, name="register"),  # add.html
    path("logout/", logoutview, name='logout'),  # logout
    path("about/", about_view, name="about"),  # about.html
    path("services/", services_view, name="services"),  # services.html
    path("contact/", contact_view.as_view(), name="contact"),  # contact.html
    path("EmpTable/", emptable_view, name="EmpTable"),
    path("add/", Add_View, name="add"), # add.html
    path('delete/', delete_employee, name='delete_employee'),
    path('employee_detail/', employee_detail, name='employee_detail'),
    path('updating/<int:pk>/edit', employee_update.as_view(), name='updating'),
]
