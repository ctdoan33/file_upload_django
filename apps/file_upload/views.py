
from django.shortcuts import render, redirect, HttpResponse
from .forms import UploadFileForm

def handle_uploaded_file(file):
    with open("apps/file_upload/uploads/"+file.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
def success(request):
    return render(request, "file_upload/success.html")