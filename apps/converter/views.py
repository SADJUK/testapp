from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
from models import FileForm
from django.core.servers.basehttp import FileWrapper
import xmltodict, json
import os
# Create your views here.


def return_file(request, filename):
    name = 'media/' + filename
    wrapper = FileWrapper(file(name))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(name)
    return response


def save_file(f):
    filename = f._get_name()
    splitted_name = filename.split('.')
    extension = splitted_name[len(splitted_name)-1]
    name = splitted_name[0]
    with open('media/' + str(filename), 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return (filename, name, extension)


def converter(filename, name, extension, output_format):
    if extension == 'xml' and output_format == 'json':
        with open('media/' + filename, "r") as _in:
            xml_text = _in.read()
        parser = xmltodict.parse(xml_text)
        result = json.dumps(parser)
        output_name = name + '.json'
        with open('media/' + output_name, 'w') as out:
            out.write(result)
        return output_name
    else:
        return filename


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            filename, name, extension = save_file(request.FILES['file'])
            result = converter(filename, name, extension, form['select'].value())
            return render(request, 'show_result.html', {'url': result})
    else:
        form = FileForm()
    return render(request, 'upload_page.html', {'form': form})
