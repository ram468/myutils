from django.shortcuts import render
from django.http import HttpResponse
import string
import datetime

# Create your views here.
def home(request):
    return render(request , 'base.html')

def analyzetext(request):
    text=request.GET.get('textbox','default')
    charcount = len(text) 
    ctext=request.GET.get('removepunc','Off')
    caps=request.GET.get('firstcaps','Off')
    spaceremove=request.GET.get('spaceremover','Off')
    newlineremover=request.GET.get('newlineremover','Off')
    
    #print(ctext)
    if ctext=='on':
           
        a=string.punctuation
        analyzetext = ''
        for text in text:
            if text not in a:
                analyzetext += text
        params = {
            'purpose' : "Analysed Text : ",
            "b": analyzetext,
            'count' : charcount
        }
        return render(request , 'analyze.html', params)
        
    elif(caps=='on'):
        analyzetext=''
        for char in text:
            analyzetext = analyzetext + char.upper()
        params = {
            'purpose' : 'Analysed Text :',
            'b' : analyzetext,
            'count' : charcount
        }
        return render(request,'analyze.html',params)

    elif(spaceremove=='on'):
        analyzetext = ""
        for i in range(len(text)):
            if text[i] == " ":
                if text[i+1] == " ":
                    analyzetext += text[i]
            
            elif(text[i]!=" "):
                analyzetext += text[i]
        
        params = {
            'purpose' : 'Analysed Text :',
            'b' : analyzetext,
            'count' : charcount
        }
              
        return render(request,'analyze.html',params)

    elif(newlineremover=='on'):
        analyzetext=''
        for char in text:
            if char != "\n":
                analyzetext += char
        params = {
            'purpose' : 'Newlines Removed',
            'b' : analyzetext,
            'count' : charcount
        }
        return render(request,'analyze.html', params)



    else:
        return HttpResponse("Please Select Any Option")


