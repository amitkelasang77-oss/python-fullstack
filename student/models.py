from django.db import models
class student_table(models.Model):
    reg_no=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.EmailField(default='example@gmail.com')
    marks=models.DecimalField(decimal_places=3,max_digits=6)
    date=models.DateField()

    def __str__(selfd) : 
        return super().__str__()

    
       