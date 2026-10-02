from django.shortcuts import render

from .forms import StudentForm


def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form})
