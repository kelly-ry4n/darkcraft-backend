from django.shortcuts import render, redirect
import subprocess
from models import MapRender
# Create your views here.


def render_map(request):
    
    existing = subprocess.check_output(['ps','aux']).replace('\n','\n\n<p><br>')
    if 'map.sh' in existing:
        return redirect('/')

    subprocess.Popen(['sh','/home/minecraft/mapper/map.sh'])

    return redirect('/')

def get_render_progress():
    head = subprocess.check_output(['head', '/home/minecraft/mapper/mapper.log'])
    tail = subprocess.check_output(['tail', '/home/minecraft/mapper/mapper.log'])

    return head + '\n...\n' + tail