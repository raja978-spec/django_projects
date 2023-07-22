from django.shortcuts import render
from .models import Data 
from countryinfo import CountryInfo
import pandas as pd
import wikipedia
import csv
import pycountry
from time import sleep
# Create your views here.

# OLD CODE

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

def oldCountry():
    capital=getCaptial()
    return capital


############################################################
#              NEW CODE

def get_all_countries():
    all_countries = list(pycountry.countries)
    country_names = [country.name for country in all_countries]
    return country_names

def get_country_info(country_name):
    country_info = CountryInfo(country_name).capital()
    return country_info

all_countries = get_all_countries()
newcaptial={}
def Country():
    
    for country_name in all_countries:
        try:newcaptial[country_name]=get_country_info(country_name)
        except:newcaptial[country_name]="Data not found"
    return newcaptial   
 
def Main(request):
    r=Country().values()=="Data not found"
    s=getCaptial().values()=="Not found"
    return render(request,"home.html",{"new":r,"old":s})


