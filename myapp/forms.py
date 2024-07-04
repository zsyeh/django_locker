from django import forms
from .models import UserDevice

class UserDeviceForm(forms.ModelForm):
    class Meta:
        model = UserDevice
        fields = ['userid', 'name', 'age', 'gender']

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userid', 'name', 'age', 'gender']