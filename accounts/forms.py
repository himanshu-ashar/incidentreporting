from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class SignUpForm(UserCreationForm):

    class Meta:
        fields=("username","first_name","last_name","email","password1","password2")
        model = get_user_model()

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
