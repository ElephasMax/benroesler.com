from django.shortcuts import render

# Create your views here.
def home(request):
    context = {        
        'title' : 'Ben Roesler',
        'email' : 'bennytroesler@gmail.com',
        'phone' : '(847) 571-2749',
        'name'  : 'Ben Roesler',

        'core' : [
            { 'https://drive.google.com/file/d/1FdoueBrdZfk7RPF5BhOaMXXhZbCQpRCe/view?usp=sharing' : 'Resume' },
            { 'https://drive.google.com/drive/folders/146NSwf5Le2YLQEpSQfj7ZnaJ8irOrgW-?usp=sharing' : 'Certifications'},
            { 'https://www.linkedin.com/in/bennyroesler/' : 'Linkedin' },
        ],}
    return render(request,'landing/landing.html', context) 