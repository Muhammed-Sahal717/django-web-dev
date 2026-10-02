from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "profile_image"]

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age <= 18:
            raise forms.ValidationError("Age must be greater than 18.")

        return age
