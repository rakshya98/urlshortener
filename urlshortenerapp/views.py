from django.shortcuts import render
import pyshorteners

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')  
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return render(request, 'index.html', {'shortened_url': shortened_url ,'longer_url':url})
    else:
        return render(request, 'index.html')