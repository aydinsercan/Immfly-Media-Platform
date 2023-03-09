from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from core.models import Channel, Content

html = "<h1> There is no channel for given id <h1>"

def channels_list(request):
    channels = Channel.objects.filter(parent_channel=None) 
    channel_name = 'Channel List'                        
    current_channel = False        
    return render(request,'channels.html',{'channels':channels,'channel_name':channel_name,'current': current_channel})

def channels(request, channel_id):
    try:
        current_channel = Channel.objects.get(id=channel_id)
    except:
        return HttpResponseNotFound(html)

    channels = Channel.objects.filter(parent_channel=current_channel)
    channel_name = current_channel.title
    current_channel = current_channel.parent_channel

    if not channels:
        return redirect('/channels/' + str(channel_id) + '/content')
    return render(request,'channels.html',{'channels':channels,'channel_name':channel_name,'current': current_channel})

def contents(request, channel_id):
    if not channel_id:
        return HttpResponseNotFound(html)
    try:
        channel = Channel.objects.get(id=channel_id)
    except:
        return HttpResponseNotFound(html)
    contents = Content.objects.filter(channel=channel)

    return render(request, 'content.html', {'contents': contents, 'channel': channel})

