from django.shortcuts import render, redirect
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.
def create(request):
    if request.method == "POST":
        print("hi")
        print(request.FILES)  # Debugging file uploads

        frm = MovieForm(request.POST, request.FILES)

        if frm.is_valid():
            frm.save()
            return redirect('create')  # Ensure this matches your URL name

    else:
        frm = MovieForm()

    return render(request, 'create.html', {'frm': frm})
  


  
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