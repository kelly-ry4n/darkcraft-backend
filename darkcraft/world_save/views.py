from django.shortcuts import render, redirect
from models import WorldSave
from forms import RequestWorldSaveForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.core.files import File
import os
# Create your views here.
import subprocess

def save_form(request):

    form = RequestWorldSaveForm(request.POST or None)

    if form.is_valid():

        

        w = WorldSave(signature=form.cleaned_data['signature'])
        w.save()

        archive_filename = '/home/minecraft/world_backups/darkcraft_{}.zip'.format(w.date).replace(' ','_')
        print subprocess.call([
            'zip',
            '-r',
            archive_filename,
            '/home/minecraft/minecraft/world'
            ])

        w.compressed_file.save(archive_filename,File(open(archive_filename)))
        w.save()

        return HttpResponseRedirect('/')

    return render(request, 'form.html', {'form':form, 'submit_url':'/save/'})

def list_map_saves(request):

    return render(request,
        'save_list.html',
        {
        'saves':WorldSave.objects.all().exclude(compressed_file='').order_by('-date')
        })


def download_world(request,id):
    try:
        w = WorldSave.objects.filter(id=id)[0]
    except IndexError:
        return HttpResponse('Invalid ID')

    file_path = w.compressed_file.path
    file_wrapper = FileWrapper(file(file_path,'rb'))
    response = HttpResponse(file_wrapper, content_type='application/zip')
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(w.compressed_file.path))
    return response