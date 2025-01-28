from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.
def create(request):
    frm = MovieForm()

    if request.POST:
        # title = request.POST.get("title")
        # year = request.POST.get("year")
        # desc = request.POST.get("description")
        # movie_obj = MovieInfo(title=title,year=year,description=desc)
        # movie_obj.save()
        if request.POST:
            frm=MovieForm(request.POST)
            if frm.is_valid():
                frm.save()
        else:
            frm=MovieForm()



    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    return render(request,'list.html',{'movies':movie_data})

def edit(request,pk):
    instance_to = MovieInfo.objects.get(pk=pk)
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')
        instance_to.title = title
        instance_to.year = year
        instance_to.description = description
        instance_to.save()

    
    frm = MovieForm(instance=instance_to)

    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_data = MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_data})