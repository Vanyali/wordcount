from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere': 'Passing Some aditional information in my view function!','form':'Now we gonna make form exactly below this, we could write html but let\'s do this way!'})
#Consegues imaginar construir toda pagina em html dentro de funcões? É aí que entre os templates.

def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #print(fulltext) Se quiseremos enviar para consola, só para testes.
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})

def aboutme(request):
    return render(request, 'aboutme.html')

