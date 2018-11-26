from django.http import HttpResponse
from django.shortcuts import render
from frequency import most_frequent
from valuesort import sortValue

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext']
    name = request.GET['Username']
    text = fulltext.replace('\n', ' ')
    text = text.split()
    number = len(text)
    most_frq = most_frequent(text)
    sortedDict = sortValue(most_frq[2])
    wrd = ['','']
    if len(most_frq[0]) > 1: wrd[0], wrd[1] = 'words', 'are'
    else: wrd[0], wrd[1] = 'word', 'is'

    return render(request, 'count.html', {'wordcount': number, 'name': name, 'text': fulltext,
                                          'max_value':most_frq[1], 'words':most_frq[0], 'sortd': sortedDict,
                                          'wrd0': wrd[0], 'wrd1': wrd[1]})

def about(request):
    return render(request, 'about.html')