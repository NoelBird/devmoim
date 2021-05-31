from django.shortcuts import render, redirect
from .models import Writing
from django.contrib.auth import get_user

# Create your views here.
def index(request):
    page = 1
    if request.GET.get("page"):
        page = int(request.GET.get("page"))
    total_count = Writing.objects.count()
    page_size = 10
    num_of_pages = 1 + (total_count-1)//page_size
    writings = Writing.objects.all().order_by("-pk")[page_size*(page-1):page_size*page]
    context = {}
    context["writings"] = writings
    context["num_of_pages"] = list(range(1, num_of_pages+1))
    context["page"] = page
    return render(request, "freeboard/index.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = get_user(request)
        if user.is_authenticated:
            Writing.objects.create(title=title, content=content, user=user)
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