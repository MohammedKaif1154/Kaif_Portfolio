from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import messages  # Import Django's messaging framework
from .models import Contact

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects_show = [
        {
            "title": "Donation and Charities management system",
            "path": "images/Al-khair.png",
        },
        {
            "title": "CRUD",
            "path": "images/CRUD.PNG",
        },
        {
            "title": "Portfolio",
            "path": "images/profile.png",
        },
    ]
    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experience = [
        {
            "company": "Softools",
            "position": "DATA SCIENCE INTERN",
            "duration": "6 Months",
        },
    ]
    return render(request, "experience.html", {"experience": experience})


def certificate(request):
    return render(request, "certificate.html")


def contact(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        messsage = request.POST.get("messsage", "").strip()  # Correct form field to database field

        # Validate the form data
        if not name or not email or not phone or not messsage:
            messages.error(request, "All fields are required.")
            return redirect("/contact")

        # Create and save the Contact instance
        contact_entry = Contact(name=name, email=email, phone=phone, messsage=messsage)
        contact_entry.save()

        # Add a success message and redirect
        messages.success(request, "Your message has been submitted successfully!")
        return redirect("/contact")

    return render(request, "contact.html")


def resume(request):
    resume_path = "myapp/resume1.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(
                resume_file.read(), content_type="application/pdf"
            )
            response["Content-Disposition"] = 'attachment; filename="resume1.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
