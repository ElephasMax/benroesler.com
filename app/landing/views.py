from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {        
        'title' : 'Benny Roesler',
        'subtitle' : 'Security Researcher, Hack The Box Enthusiast, Adventurer',
        'email' : 'bennytroesler@gmail.com',
        'pgpURL' : "https://benroesler.com/pgp",
        'phone' : '(847) 571-2749',
        'name'  : 'Benny Roesler',

        'core' : [
            { 'https://benroesler.com/dropbox/career/Resume.pdf' : 'Resume' },
            { 'https://benroesler.com/dropbox/career/certificates/' : 'Certifications'},
            { 'https://www.linkedin.com/in/bennyroesler/' : 'Linkedin' },
        ],}
    return render(request,'landing/landing.html', context) 

def pgp(request):    
    return HttpResponse(open("landing/static/files/Ben_bennytroesler@gmail.com-0x90E8D08375659A63-pub.asc", 'r'),content_type="text/plain")