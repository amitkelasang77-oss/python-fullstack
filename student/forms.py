
from django import forms
from .models import student_table


class StudentForm(forms.ModelForm):

    class Meta:
        model = student_table

        fields = [
            'reg_no',
            'name',
            'email',
            'marks',
            'date'
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
