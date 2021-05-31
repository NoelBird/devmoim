from django.shortcuts import render, redirect
from .models import Writing

# Create your views here.
def index(request):
    writings = Writing.objects.all().order_by("-pk")
    context = {}
    context["writings"] = writings
    return render(request, "freeboard/index.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Writing.objects.create(title=title, content=content)
        return redirect("freeboard:index")
    else:
        return render(request, "freeboard/create.html")

def detail(request, pk: int):
    writing = Writing.objects.get(pk=pk)
    context = {}
    context["writing"] = writing
    return render(request, "freeboard/detail.html", context=context)

def delete(request, pk: int):
    writing = Writing.objects.get(pk=pk)
    writing.delete()
    return redirect("freeboard:index")

def update(request, pk: int):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        writing = Writing.objects.get(pk=pk)
        writing.title = title
        writing.content = content
        writing.save()
        return redirect("freeboard:index")
    else:
        context = {}
        context["writing"] = Writing.objects.get(pk=pk)
        return render(request, "freeboard/update.html", context=context)