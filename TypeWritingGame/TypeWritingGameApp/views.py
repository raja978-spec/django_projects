import random
from django.shortcuts import render
import datetime
import time

# Create your views here.
def App(request):
     if request.method=="POST":
        resultString_getter=str(request.POST.get('result'))
        given_String=str(request.POST.get('result2'))
        resultString_setter=''.join(resultString_getter)
        given_String_setter=''.join(given_String)
        Converted_Givenstring_to_list=given_String_setter.split(' ')
        Converted_Resultstring_to_list=resultString_setter.split(' ')
        count=0
        for i in range(0,len(Converted_Givenstring_to_list)):
            try:
                if Converted_Resultstring_to_list[i]==Converted_Givenstring_to_list[i]:
                    count=count+1
                else:
                    continue
            except Exception:
                pass
        #Score=len(count)
        output={
            'lenofConverted_Resultstring_to_list':len(Converted_Resultstring_to_list),
            'lenofConverted_Givenstring_to_list':len(Converted_Givenstring_to_list),
            'lenofCount':count
        }
        return render(request,'index.html',context=output)
     else:
       text=startgame()
       Given_string=''.join(text)
       return render(request,'index.html',{'text':Given_string})

def startgame():
    r=random.randrange(1,10)
    with open(f'TypeWritingGameApp/Text/Note_{r}.txt','r') as f:
        s=f.readlines()
    return s    

def Welcomepage(request):
    return render(request,'Welcome.html')