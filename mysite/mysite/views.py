from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext, Template, Context
from django.shortcuts import render_to_response

from blog.models import Post

import datetime

def hello(request):
	latest_post_list = Post.objects.all()
	t = Template('{{ latest_post_list }} was posted on {{ latest_post_title.publication_date }}.')
	c = Context({'latest_post_list':latest_post_list})
	return HttpResponse(t.render(c));
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def basicPage(request):
	return render_to_response('index.html');

def blogPage(request):
	return render_to_response('blog.html');

def mbb342Page(request):
	return render_to_response('mbb342.html');

def latestEntries(request):
    latest_post_list = Post.objects.order_by('-publication_date')
    template = get_template('blog.html')
    context = RequestContext(request, {'latest_post_list': latest_post_list})
    return HttpResponse(template.render(context))

