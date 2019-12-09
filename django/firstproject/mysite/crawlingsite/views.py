from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'crawlingsite/index.html', {})

#def post_list(request):
#        return render(request, 'crawlingsite/post_list.html', {})

#def delivery_food(request):
#        return render(request, "crawlingsite/delivery_food.html", {})

#def delivery_time(request):
#        return render(request, "crawlingsite/delivery_time.html", {})
