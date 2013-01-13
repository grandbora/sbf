from flat.models import Poll,Flat
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)

def detail(request, someid):
	# get the flat expose id, get from db and render...
	a_flat = Flat(title="A nice and warm flat")
	return render_to_response("flat.html", {'flat': a_flat})

def intro(request):
	a_flat = Flat(title="A nice and warm flat")
	return render_to_response("flat/flat.html", {'flat': a_flat})