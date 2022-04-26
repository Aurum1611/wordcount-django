import operator
from django.http import HttpResponse
from django.shortcuts import render
import re


def homepage(request):
    # data = {
    #     'q1': "What's there for dinner?",
    #     'q2': "Should we swiggy?",
    # }
    return render(request, 'index.html')#, data)


def lemons(request):
    response_str = "When life gives you lemon, make lemonade. - Boring Quote"
    return HttpResponse(response_str)


def count(req):
    alltext = req.GET['alltext']
    pure_text = re.sub(r'[^\w\s]', ' ', alltext)
    words = pure_text.split()
    wordcount = dict()
    
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    # sort the list in reverse of the natural order of the values
    countedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    
    data = {
        'totcount': len(words),
        'alltext': alltext,
        'wordcount': countedwords,
    }
    return render(req, 'count.html', data)


def about(req):
    return render(req, 'about.html')
