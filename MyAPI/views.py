from django.shortcuts import render
# from . forms import ApprovalForm
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


# def myform(request):
#     if request.method == 'POST':
#         form = ApprovalForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit=False)
#     else:
#         form = ApprovalForm()
#     return render(request, 'myform/cxform.html', {'form': form})


# @api_view(["POST"])
def approvereject(request):
    try:
        mdl = joblib.load(
            "/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
        # mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1, -1)
        scalers = joblib.load(
            "/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl .predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            # firstname = form.cleaned_data['firstname']
            # dependants = form.cleaned_data['dependants']
            # lastname = form.cleaned_data['lastname']
            # applicantincome = form.cleaned_data['applicantincome']
            # coapplicatincome = form.cleaned_data['coapplicatincome']
            # loanamt = form.cleaned_data['loanamt']
            # loanterm = form.cleaned_data['loanterm']
            # credithistory = form.cleaned_data['credithistory']
            # gender = form.cleaned_data['gender']
            # married = form.cleaned_data['married']
            # graduatededucation = form.cleaned_data['graduatededucation']
            # selfemployed = form.cleaned_data['selfemployed']
            # area = form.cleaned_data['area']

            Firstname = form.cleaned_data['Firstname']
            Lastname = form.cleaned_data['Lastname']
            Dependants = form.cleaned_data['Dependants']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicatIncome = form.cleaned_data['CoapplicatIncome']
            Loan_Amount = form.cleaned_data['Loan_Amount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']

            # print(firstname, lastname, dependants, married, area)

    else:
        form = MyForm()

    return render(request, 'myform/cxform.html', {'form': form})
