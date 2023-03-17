from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import movie
from .forms import movieform
from .forms import newform

# Create your views here.
def index(request):
     obj=movie.objects.all()
     context={
        'movie_list':obj
     }
     return render(request,"index.html",context)

def detail(request,movie_id):
    obj=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':obj})

def add_movie(request):
    if request.method=="POST":
        name  = request.POST.get('name')
        des   = request.POST.get('des')
        year  = request.POST.get('year')
        img   = request.FILES['img']
        Movie = movie(name=name,des=des,year=year,img=img)
        Movie.save()
    return render(request,"add.html")

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,"delete.html")

def new(request):
    if request.method=="POST":
        name  = request.POST.get('name')
        des   = request.POST.get('des')
        year  = request.POST.get('year')
        img   = request.FILES['img']
        Movie = movie(name=name,des=des,year=year,img=img)
        Movie.save()
    return render(request,"new.html")
