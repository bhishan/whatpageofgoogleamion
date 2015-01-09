from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

import mechanize
pos_in_search = 0


def mypositioningoogle(keyw, domain):
    global pos_in_search
    br = mechanize.Browser() #initiating a browser

    br.set_handle_robots(False) #we're acting like we're not a bot/robot

#user aget 
    br.addheaders = [("User-agent","Mozilla/5.0")]
    keyw = str(keyw)
    domain = str(domain)
    print type(keyw)
    domain = "http://" + domain

    qe="" 

    alert = ""
    for i in range(0,len(keyw)):
        if keyw[i] ==" ":
            qe+="+"
        else:
            qe+=keyw[i]



    counter = 0

    for i in range(0,10):
        google_url = br.open("https://www.google.com/search?q=" + qe + "&start=" + str(counter))
        search_keyword = google_url.read()
        if domain in search_keyword:
            alert = "found"
            print "it's working"
            break
        counter+=10

    if alert == "found":
        pos_in_search = i+1
        if pos_in_search <= 4:
            return "Congratulations!! Your site is seen in page " + str(pos_in_search) + " of google search result for the keyword"
        else:
            return "Your site is seen in page " + str(pos_in_search) + " of google search result for the keyword"
    else:
        return "Your site is not within first 10 pages of google search result for the keyword"

# Create your views here.
keyword = ""
domain_name = ""

def create_search(request):
    global keyword
    global domain_name
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        domain_name = request.POST.get('domain_name')
        print keyword
    return HttpResponseRedirect('/whatpageofsearchamion/')
def archive(request):
    global keyword
    global domain_name
    print domain_name
    return render_to_response('archive.html', {'keyword': keyword , 'position_in_search': mypositioningoogle(keyword, domain_name)}, RequestContext(request))
