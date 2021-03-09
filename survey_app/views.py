from django.shortcuts import render, redirect

Locations = (
    'Dallas',
    'Seattle',
    'Chicago'
)
Languages = (
    'Python',
    'Java',
    'Ruby'
)

def index(request):
    context = {
        'locations': Locations,
        'languages': Languages
    }
    return render(request,'index.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'your_name': request.POST['your_name'],
        'locations': request.POST['locations'],
        'languages': request.POST['languages']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request,'result.html', context)

