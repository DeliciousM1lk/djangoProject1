from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import *

from .models import *
from .form import *

def index(request):
    s="Список объявлений\n\n\n\n\n"
    for b in Bb.objects.all():
        s += b.title + "\n"+ b.content+"\n\n\n"
    return HttpResponse(s,content_type="text/plain; charset=utf-8")


def index_html(request):
    bbs=Bb.objects.all()
    rubrics=Rubric.objects.all()
    context={"bbs":bbs,"rubrics":rubrics}
    return render(request,'index.html',context)

def index2(request):
    return HttpResponse("Python Django")

def detail(request,pk):
    rubric=Rubric.objects.get(pk=pk)
    all_bb=Bb.objects.filter(rubric=rubric)
    context={"rubric":rubric,"all_bb":all_bb}
    return render(request,'detail.html',context)


def detail_bb(request,pk):
    bb=Bb.objects.get(pk=pk)
    context={"bb":bb}
    return render(request,'detail_bb.html',context)



def add_bb(request):
    if request.method=="POST":
        bbform=BbForm(request.POST)
        if bbform.is_valid():
            bbform.save()
            return HttpResponseRedirect(
                reverse
                ("app:detail",
                 kwargs={"pk":bbform.cleaned_data["rubric"].pk}
                 ))
        else:
            context={"form":bbform}
            return render(request,'add_bb.html',context)
    else:
        bbform=BbForm()
        context={"form":bbform}
        return render(request,'add_bb.html',context)

def stream(request):
    resp_content=('Здесь ','будет ','отправляться ','текст')
    return StreamingHttpResponse(
        resp_content,
        content_type="text/plain; charset=utf-8")

@require_GET
def file_response(request):
    file_path=r"C:\Users\winge\PycharmProjects\djangoProject1\project\static\picture.jpg"
    return FileResponse(open(file_path, 'rb'), content_type='image/jpg',as_attachment=True)

def our_decorator(func):
    def wrapper(request):
        print("hello")
        return func(request)
    return wrapper

@our_decorator
@require_http_methods(['GET','POST'])
def json_response(request):
    bb=Bb.objects.get(title="Машина")
    dictionary={
        "title":bb.title,
        "content":bb.content,
        "price":bb.price,
        "published":bb.published,
    }
    return JsonResponse(dictionary)


def update_bb(request,pk):
    bb=Bb.objects.get(pk=pk)
    if request.method=="POST":
        form=BbForm(request.POST,instance=bb)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse
                ("app:detail",
                 kwargs={"pk": form.cleaned_data["rubric"].pk}
                 ))
        else:
            context = {"form": form}
            return render(request, 'add_bb.html', context)
    else:
        form = BbForm(instance=bb)
        context = {"form": form}
        return render(request, 'add_bb.html', context)

def delete_bb(request,pk):
    bb=get_object_or_404(Bb,pk=pk)
    if request.method=="POST":
        bb.delete()
        return redirect(reverse("app:index_html"))
    return Http404()

