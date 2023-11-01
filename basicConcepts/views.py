from django.shortcuts import render,HttpResponse

def Welcome(request):
  return render(request,'index.html')

from django.shortcuts import render

def user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        return render(request, 'user.html', {'name': username})
    else:
        return render(request, 'user.html', {'name': 'Anonymous'})
