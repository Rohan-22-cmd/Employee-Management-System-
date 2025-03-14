# employee/forms.py
from django import forms
from .models import User, Department, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'Email', 'Mobile_Number','select_dept', 'select_role','Allcate_Reporting_Manager', 'Date_of_joining', 'username', 'Set_password']

    # Password field is hidden
    Set_password = forms.CharField(widget=forms.PasswordInput)  

    # Adding custom widgets for the dropdowns
    select_dept = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="✓ Select Department")
    select_role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="✓ Select Role")
    
    # Reporting Manager dropdown will show all users except the current one
    Allcate_Reporting_Manager = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Fetching all users as potential reporting managers
        empty_label="✓ Select Reporting Manager", 
        required=False  # Reporting manager can be optional
    )
    
    # Date of Joining field with calendar widget (Date picker)
    Date_of_joining = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # This creates an HTML5 date picker
        required=True
    )
