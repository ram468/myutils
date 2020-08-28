from django.shortcuts import render
from django.http import HttpResponse
import string

# Create your views here.
def home(request):
    return render(request , 'base.html')

def analyzetext(request):
    text=request.GET.get('textbox','default')
    ctext=request.GET.get('removepunc','Off')
    caps=request.GET.get('firstcaps','Off')
    
    #print(ctext)
    if ctext=='on':
            
        a=string.punctuation
        analyzetext = ''
        for text in text:
            if text not in a:
                analyzetext += text
        params = {
            'purpose' : "Analysed Text : ",
            "b": analyzetext
        }
        return render(request , 'analyze.html', params)
    elif(caps=='on'):
        analyzetext=''
        for char in text:
            analyzetext = analyzetext + char.upper()
        params = {
            'purpose' : 'Analysed Text :',
            'b' : analyzetext
        }
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")



def newlineremover(request):
    return HttpResponse("newlineremover")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")