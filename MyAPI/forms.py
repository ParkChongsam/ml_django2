from django.forms import ModelForm
from . models import approvals


class MyForm(ModelForm):
    class Meta:
        model = approvals
        fields = '__all__'


# exclude = 'firstname'

# from django import forms


# class ApprovalForm(forms.Form):

#     Firstname = forms.CharField(max_length=15)
#     Lastname = forms.CharField(max_length=15)
#     Dependants = forms.IntegerField()
#     ApplicantIncome = forms.IntegerField()
#     CoapplicatIncome = forms.IntegerField()
#     Loan_Amount = forms.IntegerField()
#     Loan_Amount_Term = forms.IntegerField()
#     Credit_History = forms.IntegerField()
#     Gender = forms.ChoiceField(
#         choices=[('Male', 'Male'), ('Female', 'Female')])
#     Married = forms.ChoiceField(choices=[(('Yes', 'Yes'), ('No', 'No'))])
#     Education = forms.ChoiceField(choices=[(
#         ('Graduated', 'Graduated'),
#         ('Not_Graduate', 'Not_Graduate')
#     )])
#     Self_Employed = forms.ChoiceField(choices=[(
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )])
#     Property_Area = forms.ChoiceField(choices=[(
#         ('Rural', 'Rural'),
#         ('Semiurban', 'Semiurban'),
#         ('Urban', 'Urban')
#     )])
