from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("student_form")

    else:
        form = StudentForm()

    students = Student.objects.all()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "students": students,
        },
    )
