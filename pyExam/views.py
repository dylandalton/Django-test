from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-date_and_time')[:5]
    template = loader.get_template('pyExam/index.html')
    context = {
        'latest_article_list' : latest_article_list
    }
    return HttpResponse(template.render(context, request))

#def detail(request, article_id):
    #return HttpResponse("You're looking at article %s." % article_id)

#def results(response, article_id):
    #response = "You're looking at the results of article %s"
     #return HttpResponse(response % article_id)