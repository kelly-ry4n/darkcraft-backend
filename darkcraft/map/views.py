from django.shortcuts import render, redirect
import subprocess
from models import MapRender
# Create your views here.


def render_map(request):
    
    existing = subprocess.Popen(['ps','aux'])
    if 'map.sh' in existing:
        return redirect('/')

    subprocess.Popen(['sh','/home/minecraft/mapper/map.sh'])

    return redirect('/')

def get_render_progress():
    head = subprocess.call(['head', '/home/minecraft/mapper/mapper.log'])
    tail = subprocess.call(['tail', '/home/minecraft/mapper/mapper.log'])

    return head + '\n...\n' + tail