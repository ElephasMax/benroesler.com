from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {        
        'title' : 'Benny Roesler',
        'subtitle' : 'Security Researcher, Hack The Box Enthusiast, Adventurer',
        'email' : 'bennytroesler@gmail.com',
        'pgpURL' : "https://files.benroesler.com/c/Ben_bennytroesler@gmail.com-0x90E8D08375659A63-pub.asc",
        'phone' : '(847) 571-2749',
        'name'  : 'Benny Roesler',

        'core' : [
            { 'https://files.benroesler.com/c/resume.pdf' : 'Resume' },
            { 'https://files.benroesler.com/c/certs/' : 'Certifications'},
        ],}
    return render(request,'landing/landing.html', context) 
