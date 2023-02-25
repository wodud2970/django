from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload

# Create your views here.

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['imgfile']

        #DB에 저장
        fileupload = FileUpload(title = title, content = content, imgfile = img)
        fileupload.save()

        post = FileUpload.objects.all()
        return render(request, 'detail.html',{'post' :post} )
    
    else:
        fileuploadForm = FileUploadForm
        context = {'fileuploadForm' : fileuploadForm}

        return render(request, 'fileupload.html', context)
    
#index에서 가져오고 제출

def index(request):
    pass