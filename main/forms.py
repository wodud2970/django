from django.forms import ModelForm
#DB가져오기
from .models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile','content']