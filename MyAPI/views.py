from django.shortcuts import render
from . forms import ApprovalForm
# from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib import messages
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
def ohevalue(df):
    ohe_col = joblib.load("C:/project/ml_django2/MyAPI/allcol.pkl")
    cat_columns = ['Gender', 'Married', 'Education',
                   'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


# @api_view(["POST"])
def approvereject(unit):
    try:
        mdl = joblib.load("C:\\project\\ml_django2\\MyAPI\\loan_model.pkl")
        # mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
        # mydata = request.data
        # unit = np.array(list(mydata.values()))
        # unit = unit.reshape(1, -1)
        scalers = joblib.load("C:\\project\\ml_django2\\MyAPI\scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl .predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})

        return newdf.values[0][0]
    except ValueError as e:
        return (e.args[0])

    #     return ('Your Status is {}'.format(newdf))
    # except ValueError as e:
    #     return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        # form = MyForm(request.POST)
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
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            # print(approvereject(ohevalue(df)))
            # print(ohevalue(df))
            answer = approvereject(ohevalue(df))
            messages.success(request, 'Application Status: {}'.format(answer))

    else:
        form = ApprovalForm()
        # form = MyForm()

    return render(request, 'myform/cxform.html', {'form': form})


# def approvereject(unit):
#     try:
#         mdl = joblib.load("C:\\project\\ml_django2\\MyAPI\\loan_model.pkl")
#         scalers = joblib.load("C:\\project\\ml_django2\\MyAPI\scalers.pkl")
#         X = scalers.transform(unit)
#         y_pred = mdl.predict(X)
#         y_pred = (y_pred > 0.58)
#         newdf = pd.DataFrame(y_pred, columns=['Status'])
#         newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
#         K.clear_session()
#         return (newdf.values[0][0], X[0])
#     except ValueError as e:
#         return (e.args[0])


# def cxcontact(request):
#     if request.method == 'POST':
#         form = ApprovalForm(request.POST)
#         if form.is_valid():
#             Firstname = form.cleaned_data['firstname']
#             Lastname = form.cleaned_data['lastname']
#             Dependents = form.cleaned_data['Dependents']
#             ApplicantIncome = form.cleaned_data['ApplicantIncome']
#             CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
#             LoanAmount = form.cleaned_data['LoanAmount']
#             Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
#             Credit_History = form.cleaned_data['Credit_History']
#             Gender = form.cleaned_data['Gender']
#             Married = form.cleaned_data['Married']
#             Education = form.cleaned_data['Education']
#             Self_Employed = form.cleaned_data['Self_Employed']
#             Property_Area = form.cleaned_data['Property_Area']
#             myDict = (request.POST).dict()
#             df = pd.DataFrame(myDict, index=[0])
#             answer = approvereject(ohevalue(df))[0]
#             Xscalers = approvereject(ohevalue(df))[1]
#             if int(df['LoanAmount']) < 25000:
#                 messages.success(
#                     request, 'Application Status: {}'.format(answer))
#             else:
#                 messages.success(
#                     request, 'Invalid: Your Loan Request Exceeds $25,000 Limit')

#     form = ApprovalForm()

#     return render(request, 'myform/cxform.html', {'form': form})
