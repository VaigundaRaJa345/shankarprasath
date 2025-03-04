from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint  # Assuming you have a model named Complaint

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')

def track(request):
    return render(request, 'track.html')

def register(request):
    return render(request, 'register.html')

def help_page(request):
    return render(request, 'help.html')

def admin_page(request):
    complaints = Complaint.objects.all()  # Fetch all complaints from the database
    return render(request, 'admin.html', {'complaints': complaints})

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import Complaint

from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint
import uuid

def register_complaint(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address", "")
        crime_location = request.POST.get("crime_location", "")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        crime_type = request.POST.get("crime_type")
        other_crime_type = request.POST.get("other_crime_type", "")
        crime_description = request.POST.get("crime_description", "")
        eviurl = request.POST.get("eviurl", "")

        # Use 'other_crime_type' if 'Other' is selected
        if crime_type == "Other":
            crime_type = other_crime_type

        # Generate unique Complaint ID
        complaint_id = "CR" + str(uuid.uuid4().hex[:8]).upper()

        # Save to database
        complaint = Complaint.objects.create(
            complaint_id=complaint_id,
            name=name,
            address=address,
            crime_location=crime_location,
            email=email,
            phone=phone,
            crime_type=crime_type,
            description=crime_description,
            evidence_url=eviurl,
            status="Pending",
        )

        # Show an alert pop-up with the Complaint ID
        return HttpResponse(
            f"<script>alert('Complaint Registered! Your Complaint ID is: {complaint_id}'); window.location.href='/';</script>"
        )

    return render(request, "register.html")

def track_complaint(request):
    if request.method == "POST":
        complaint_id = request.POST.get("complaint_id")

        try:
            complaint = Complaint.objects.get(complaint_id=complaint_id)
            return render(request, "track.html", {"complaint": complaint})

        except Complaint.DoesNotExist:
            return HttpResponse(
                "<script>alert('Complaint ID not found! Please check and try again.'); window.location.href='/track';</script>"
            )

    return render(request, "track.html")
