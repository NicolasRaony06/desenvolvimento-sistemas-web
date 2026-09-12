from django.shortcuts import render

# Create your views here.
def portifolio(request):
    if request.method == 'GET':
        return render(request, 'portifolio/portifolio.html')