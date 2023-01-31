from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class addAttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"


class addMarksForm(ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"


class addNoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
