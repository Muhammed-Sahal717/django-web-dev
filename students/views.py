from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.shortcuts import redirect, render

from .forms import StudentForm, UserRegisterForm
from .models import Course, Student


@login_required
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


def student_queries(request):
    django_course = Course.objects.filter(name="Django").first()

    students_by_course = (
        Student.objects.filter(courses=django_course)
        if django_course
        else Student.objects.none()
    )

    students_over_20 = Student.objects.filter(age__gt=20)

    students_ordered = Student.objects.order_by("name")

    students_excluding_20 = Student.objects.exclude(age=20)

    courses_with_count = Course.objects.annotate(student_count=Count("student"))

    total_students = Student.objects.aggregate(total=Count("id"))

    return render(
        request,
        "students/student_queries.html",
        {
            "students_by_course": students_by_course,
            "students_over_20": students_over_20,
            "students_ordered": students_ordered,
            "students_excluding_20": students_excluding_20,
            "courses_with_count": courses_with_count,
            "total_students": total_students,
        },
    )


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("student_form")
    else:
        form = UserRegisterForm()

    return render(request, "students/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("student_form")
    else:
        form = AuthenticationForm()

    return render(request, "students/login.html", {"form": form})
