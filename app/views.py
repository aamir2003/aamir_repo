from django.shortcuts import render

# Create your views here.
def my_fun(request):
    print("**************************************************************************")
    return render(request,'app/my.html')