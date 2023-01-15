from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request,'photo/gallery.html')

def add(request):
    return render(request,'photo/add.html')
def photo(request,pk):
    return render(request,'photo/photo.html')