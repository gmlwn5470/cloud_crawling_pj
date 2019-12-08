from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    template=loader.get_template('crawlingsite/index.html')
    context={
            'latest_question_list':"test",
    }
    return HttpResponse(template.render(context,request))

#def post_list(request):
#        return render(request, 'crawlingsite/post_list.html', {})

#def delivery_food(request):
#        return render(request, "crawlingsite/delivery_food.html", {})

#def delivery_time(request):
#        return render(request, "crawlingsite/delivery_time.html", {})
