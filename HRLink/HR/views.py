from django.shortcuts import render, redirect
from .models import Account, Employee
from .forms import RegistrationForm, AddForm, AccountAuthenticationForm
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, FormView , UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# gets all Account from The DataBase


def accountsview(request):
    context = {}
    accounts = Account.objects.all()

    context["accounts"] = accounts
    return render(request, "", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("home")
        else:
            context["registration_form"] = form
    else:
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "templates/add.html", context)


def home_view(request):
    User = request.user
    if User.is_authenticated:
        return render(request, "home_HR.html", {})
    else:
        return render(request, "registration/login.html", {})


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context["login_form"] = form
    return render(request, "registration/login.html", context)


def logoutview(request):
    logout(request)
    return redirect("login")


def about_view(request):
    return render(request, "about.html", {})


def services_view(request):
    return render(request, "services.html", {})


class contact_view(TemplateView):
    template_name = "contact.html"


def emptable_view(request):
    return render(request, "EmpTable.html", {})


def welcome_view(request):
    return render(request, "welcome.html", {})


def Add_View(request):
    form = AddForm()
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = AddForm
    context = {'form': form}
    return render(request, "add.html", context)


class HomePage(TemplateView):
    template_name = "home_HR.html"


def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')  # Assuming the input field has name 'employee_id'
        try:
            employee = Employee.objects.get(accId=employee_id)
            employee.delete()
            # Redirect to a success page or any other desired location
            return redirect('home')
        except Employee.DoesNotExist:
            # Handle the case when an employee with the provided ID does not exist
            error_message = "Employee with ID {} does not exist.".format(employee_id)
            return render(request, 'home_HR.html', {'error_message': error_message})
    else:
        return redirect('home')


# def employee_detail(request,employee_id):
#     employee = get_object_or_404(Employee, accId=employee_id)
#
#     if request.method == 'POST':
#         employee.salary = request.POST['salary']
#         employee.phone_number = request.POST['phone_number']
#         employee.availableVac = request.POST['availableVac']
#         employee.approvedVac = request.POST['approvedVac']
#         employee.save()
#
#     context = {'employee': employee}
#     return render(request, 'update.html', context)

def employee_detail(request):
    if request.method == 'POST':
        employeeid = request.POST.get('employeeid')  # Assuming the input field has name 'employee_id'
        try:
            employee = Employee.objects.get(accId=employeeid)
            context = {'employee': employee}
            return render(request, 'update.html', context)
        except Employee.DoesNotExist:
            # Handle the case when an employee with the provided ID does not exist

            return HttpResponse("employee doesn't exist", content_type="text/plain")
    else:
        return redirect('home')


# def employee_update(request):
#     if request.method == 'POST':
#         UpdateView
#         employeeid = request.POST.get('employeeid')
#
#         employee = Employee.objects.get(Q(accId__iexact = employeeid))
#         employee.salary = request.POST['salary']
#         employee.phone_number = request.POST['phone_number']
#         employee.availableVac = request.POST['availableVac']
#         employee.approvedVac = request.POST['approvedVac']
#         employee.save()
#         return redirect("home")
class employee_update(UpdateView):
    template_name = "update.html"
    model = Employee
    fields = ['salary','phone','availableVac','approvedVac']

    def get_success_url(self):
        return reverse_lazy('home')
