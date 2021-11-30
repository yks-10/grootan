from django.forms import ModelForm
from .models import Devi
class Devisha(ModelForm):
    class Meta:
        model=Devi
        fields=['name','age','dob','first_name','last_name','address','phone_no','mail_id']
