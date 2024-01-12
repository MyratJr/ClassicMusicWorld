from django.db.models import Q
from django.shortcuts import render
from .models import *

def home(request):
    context = {
        'compositor' : Compositor.objects.all().order_by('-song_count'),
    }
    if request.method == "POST":
        got = request.POST.get('song')
        gozleg = Music.objects.filter(Q(title__icontains=got) | Q(property__fullname__icontains=got)).select_related("property")
        context['gozleg'] = gozleg
        context['salam'] = "salam"
    else:
        context['musics'] = Music.objects.all().order_by("-id").select_related("property")[:12]
    return render(request, "index.html", context)


def single_channell(request, id, part):
    one_compositor = Compositor.objects.get(id=id)
    context = {
        'compositor' : Compositor.objects.all().order_by('-song_count'),
        'single' : one_compositor,
    }
    if request.method == "POST" and part == 'musics':
        got = request.POST.get('wert')
        context['musics'] = Music.objects.filter(property=Compositor.objects.get(id=id), title__icontains=got).select_related("property")
    elif part == 'musics':
        context['musics'] = Music.objects.filter(property=Compositor.objects.get(id=id)).select_related("property")
    elif part == 'about':
        context['about'] = 'about'
    elif part == 'AtoZ':
        context['musics'] = Music.objects.filter(property=Compositor.objects.get(id=id)).order_by('title').select_related("property")
    elif part == 'ZtoA':
        context['musics'] = Music.objects.filter(property=Compositor.objects.get(id=id)).order_by('-title').select_related("property")
    return render(request, "single_channel.html", context)


def listen_music(request, user_id, music_id):
    one_music = Music.objects.get(property=Compositor.objects.get(id=user_id), id=music_id)
    context = {
        'compositor' : Compositor.objects.all().order_by('-song_count'),
        'single' : Compositor.objects.get(id=user_id),
        'music1' : one_music,
        "music2" : Music.objects.filter(Q(property=Compositor.objects.get(id=user_id)), ~Q(id=music_id))
    }
    return render(request, "listen_music.html", context)