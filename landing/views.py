from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {        
        'title' : 'Ben Roesler',
        'email' : 'bennytroesler@gmail.com',
        'pgpURL' : "https://benroesler.com/pgp",
        'phone' : '(847) 571-2749',
        'name'  : 'Ben Roesler',

        'core' : [
            { 'https://drive.google.com/file/d/10ft-feIjkUkVU63L45lR-2oS0qATKSke/view?usp=sharing' : 'Resume' },
            { 'https://drive.google.com/drive/folders/146NSwf5Le2YLQEpSQfj7ZnaJ8irOrgW-?usp=sharing' : 'Certifications'},
            { 'https://www.linkedin.com/in/bennyroesler/' : 'Linkedin' },
        ],}
    return render(request,'landing/landing.html', context) 

def pgp(request):    
    return HttpResponse(open("landing/static/files/Ben_bennytroesler@gmail.com-0x90E8D08375659A63-pub.asc", 'r'),content_type="text/plain")