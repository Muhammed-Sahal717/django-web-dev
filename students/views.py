from django.shortcuts import redirect, render

from .forms import StudentForm


def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_form")

    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form})
