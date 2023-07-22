from django.shortcuts import render
from .models import Data 
from countryinfo import CountryInfo
import pandas as pd


def getCountry():
    data=pd.read_csv("archive/countries.csv")
    countries=[i for i in data['Country']]
    return countries

global oldcap
oldcap=dict()

def getCaptial():
    countries=getCountry()
    
    for i in countries:
        try:
            oldcap[i]=CountryInfo(i.strip()).capital()
        except:
            oldcap[i]="Not found"
            pass
    return oldcap

def Main(request):
    captial=getCaptial()
    return render(request,'home.html',{"captial":captial})



