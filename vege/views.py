from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def receipes(request):
    if request.method == "POST":
     
     data = request.POST

     receipe_img = request.FILES.get('receipe_img')
     receipe_name = data.get('receipe_name')
     receipe_desc = data.get('receipe_desc')
    #  print(receipe_name)
    #  print(receipe_desc)
    #  print(receipe_img)
     Receipe.objects.create(
        receipe_img = receipe_img,
        receipe_name=receipe_name,
        receipe_desc=receipe_desc,
        )

   # return redirect('')
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}


    return render(request, 'receipes.html', context)