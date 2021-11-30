from django.db import models
# Create your models here.
class Devi(models.Model):
    name=models.CharField( max_length=30)
    age=models.CharField( max_length=4)
    dob=models.DateField()
    first_name=models.CharField( max_length=30)
    last_name=models.CharField( max_length=30)
    address=models.CharField( max_length=30)
    phone_no=models.CharField( max_length=12)
    mail_id=models.EmailField(primary_key=True)

    def __str__(self):
        return self.mail_id


