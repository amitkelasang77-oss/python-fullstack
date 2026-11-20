
from django import forms
from .models import Student_table


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student_table

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
