# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll
'''
def index(request):
#    return HttpResponse("Hello, world. You are at the poll index.")
#    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
'''
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

from django.http import Http404

def detail(request, poll_id):
#    return HttpResponse("You're looking at poll %s." % poll_id)
    '''    
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})
    '''
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
