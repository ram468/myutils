from django.shortcuts import render
from django.http import HttpResponse
import string

# Create your views here.
def home(request):
    return render(request , 'index.html')

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

def capitalise(request):
    return HttpResponse("capitalise")

def newlineremover(request):
    return HttpResponse("newlineremover")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")