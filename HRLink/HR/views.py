from random import randint, choice
from datetime import date, timedelta,datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Account, Employee, vacation
from .forms import RegistrationForm, AddForm, AccountAuthenticationForm
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    DeleteView,
    CreateView,
    FormView,
    UpdateView,
    DetailView,
    ListView,
)

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse


# Create your views here.
# gets all Account from The DataBase

query_name = ""
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
    context = {"form": form}
    return render(request, "add.html", context)


class HomePage(TemplateView):
    template_name = "home_HR.html"


def delete_employee(request):
    if request.method == "POST":
        employee_id = request.POST.get(
            "employee_id"
        )  # Assuming the input field has name 'employee_id'
        try:
            employee = Employee.objects.get(accId=employee_id)
            employee.delete()
            # Redirect to a success page or any other desired location
            return redirect("home")
        except Employee.DoesNotExist:
            # Handle the case when an employee with the provided ID does not exist
            error_message = "Employee with ID {} does not exist.".format(employee_id)
            return render(request, "home_HR.html", {"error_message": error_message})
    else:
        return redirect("home")


def employee_List(request):
    # generate_objects(30)
    if request.GET.get('que') == "" or request.GET.get('Name') == "":
            employeelist = Employee.objects.all()
            context = {"employees": employeelist}
            return render(request, "EmpTable.html", context)
    if request.method == "GET":
       
        if ("que" in request.GET) and request.GET["que"].strip():
            query_string = request.GET['que']
            employeelist = Employee.objects.filter(
                Name__icontains=query_string,
                email__icontains=query_string,
            )
            context = {"employees": employeelist}
            return render(request, "EmpTable.html", context)
        else:
            Name = request.GET.get("Name")
            try:
                employeelist = Employee.objects.filter(Q(Name__icontains=Name))
                context = {"employees": employeelist}

                return render(request, "EmpTable.html", context)
            except:
                pass
    context = {}            
    return render(request, "EmpTable.html", context)


# delete from table
def emp_delete_table(request, accId):
    try:
        emp = Employee.objects.get(accId=accId)
        context = {"object": emp}
        query_name=request.GET["empname"]
        if request.method == "POST":
            if('delete' in request.POST) :
                emp.delete()
            return redirect("ladelete")

    except Employee.DoesNotExist:
        error_message = "Employee with ID {} does not exist.".format(accId)
        return HttpResponse(error_message)
    return render(request, "delete.html", context)


def list_after_delete(request):
    if request.method == "GET":
        Name = query_name
        employeelist = Employee.objects.filter(Q(Name__icontains=Name))
        context = {"employees": employeelist}

    if request.GET.get('que') == "" or request.GET.get('Name') == "":
        employeelist = Employee.objects.all()
        context = {"employees": employeelist}
        return render(request, "EmpTable.html", context)
    if request.method == "GET":

        if ("que" in request.GET) and request.GET["que"].strip():
            query_string = request.GET['que']
            employeelist = Employee.objects.filter(
                Name__icontains=query_string,
                email__icontains=query_string,
            )
            context = {"employees": employeelist}
            return render(request, "EmpTable.html", context)
        else:
            Name = request.GET.get("Name")
            try:
                employeelist = Employee.objects.filter(Q(Name__icontains=Name))
                context = {"employees": employeelist}

                return render(request, "EmpTable.html", context)
            except:
                pass
        return render(request, "EmpTable.html", context)

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
    if request.method == "POST":
        employeeid = request.POST.get(
            "employeeid"
        )  # Assuming the input field has name 'employeeid'
        try:
            employee = Employee.objects.get(accId=employeeid)
            context = {"employee": employee}
            return render(request, "update.html", context)
        except Employee.DoesNotExist:
            # Handle the case when an employee with the provided ID does not exist

            return HttpResponse("employee doesn't exist", content_type="text/plain")
    else:
        return redirect("home")


# def employee_update(request):
#     if request.method == 'POST':
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
    fields = ["salary", "phone", "availableVac", "approvedVac"]

    def get_success_url(self):
        return reverse_lazy("home")


class profile_view(DetailView):
    template_name = "profile.html"
    model = Employee
    context_object_name = "employee"


def generate_objects(num_objects):
    for i in range(num_objects):
        email = f"user{i}@example.com"
        accId = randint(100000, 999999)
        name = f"User {i}"
        address = f"Address {i}"
        gender = choice(["M", "F"])
        salary = randint(5000, 10000)
        phone = f"0123456789{i}"
        birth_date = date.today() - timedelta(days=randint(10000, 20000))
        available_vac = randint(0, 10)
        approved_vac = randint(0, available_vac)

        obj = Employee(
            email=email,
            accId=accId,
            Name=name,
            address=address,
            gender=gender,
            salary=salary,
            phone=phone,
            Birth_date=birth_date,
            availableVac=available_vac,
            approvedVac=approved_vac,
        )
        obj.save()

def date_from_string(date_str):
    """Convert a date string in the format 'YYYY-MM-DD' to a date object"""
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def request_vacation(request):
    if request.method == 'POST' :
        employee_id = request.POST.get("employee_id")
        employee = Employee.objects.get(accId=employee_id)
        employee_pk = employee.pk

        firstdate = request.POST.get("from-date")
        frstdate = date_from_string(firstdate)
        secondate = request.POST.get("to-date")
        reason = request.POST.get("reason")
        secdate = date_from_string(secondate)
        finaldate= secdate - frstdate

        vacation.objects.create(start_date=firstdate,end_date=secondate,employee=employee_id,reason=reason)

    return redirect('home')


def welcome_view(request):
    return render(request,"welcome.html",{})
#
# def view_vacation(request):
#     return render(request,"manager.html",{})

class view_vacations(ListView):
    template_name = "manager.html"
    model = vacation
    context_object_name = "vacations"


def accept_view(request):
    id = request.GET.get('id')
    employee = Employee.objects.get(accId=id)
    if request.method == 'GET':
        if 'Accept' in request.GET:
            firstdate = request.GET.get("start")
            frstdate = date_from_string(firstdate)
            secondate = request.GET.get("end")
            secdate = date_from_string(secondate)
            finaldate = secdate - frstdate
            vac = vacation.objects.get(employee=id)
            if employee.availableVac > finaldate.days:
                employee.availableVac = employee.availableVac - finaldate.days
                employee.approvedVac = employee.approvedVac + finaldate.days
                employee.save()
                vac.delete()
                return redirect("requested")
        if 'Decline' in request.GET:
            vac = vacation.objects.get(employee=id)
            vac.delete()
            return redirect("requested")
