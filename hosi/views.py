from django.shortcuts import render, redirect, get_object_or_404

from hosi.forms import AppointmentForm, QueryForm, NewsletterForm
from hosi.models import Appointment, Query,Newsletter
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm()

    return render(request, "index.html", {"form": form})

def Querys(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = QueryForm()

    return render(request, "contact.html", {"form": form})

def Newsletters(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsletterForm()

    return render(request, 'contact.html', {'form': form})

#appointments editing
def Appointmentslist(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointmentslist.html',{'appointments': appointments})

def editappointment(request,id):
    appointments = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointments)
        if form.is_valid():
            form.save()
            return redirect('appointmentslist')
    else:
            form = AppointmentForm(instance=appointments)
    return render(request, 'editappointment.html', {'form': form, 'appointments': appointments})

def deleteappointment(request,id):
    appointments = get_object_or_404(Appointment, id=id)
    try:
        appointments.delete()
        return redirect('appointmentslist')
    except Exception as e:
        messages .error(request, 'Appointment not deleted')
    return redirect('appointmentslist')
#query editing
def Querylist(request):
    querys = Query.objects.all()
    return render(request, 'querylist.html',{'querys': querys})

def editquery(request,id):
    querys = get_object_or_404(Query, id=id)
    if request.method == "POST":
        form = QueryForm(request.POST, instance=querys)
        if form.is_valid():
            form.save()
            return redirect('querylist')
    else:
            form = QueryForm(instance=querys)
    return render(request, 'editquery.html', {'form': form, 'querys': querys})

def deletequery(request,id):
    querys = get_object_or_404(Query, id=id)
    try:
        querys.delete()
        return redirect('querylist')
    except Exception as e:
        messages .error(request, 'Query not deleted')
    return redirect('querylist')

#Newsletter edit
def Newsletterlist(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletterlist.html',{'newsletters': newsletters})

def editnewsletter(request,id):
    newsletters = get_object_or_404(Newsletter, id=id)
    if request.method == "POST":
        form = NewsletterForm(request.POST, instance=newsletters)
        if form.is_valid():
            form.save()
            return redirect('newsletterlist')
    else:
            form = NewsletterForm(instance=newsletters)
    return render(request, 'editnewsletter.html', {'form': form, 'newsletters': newsletters})

def deletenewsletter(request,id):
    newsletters = get_object_or_404(Newsletter, id=id)
    try:
        newsletters.delete()
        return redirect('newsletterlist')
    except Exception as e:
        messages .error(request, 'Email not deleted')
    return redirect('newsletterlist')
