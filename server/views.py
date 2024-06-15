from django.http import HttpRequest, HttpResponse
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload_file(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.files.get("file").name)
            return HttpResponse()

    return HttpResponse(status=400)
