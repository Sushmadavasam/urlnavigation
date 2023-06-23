from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'sushma','number':9701436038}
    return render(request,'jinjaprint.html',d)