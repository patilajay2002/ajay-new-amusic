from django.shortcuts import render
from django.db.models import Count

from .models import Artist, Language, Album, Music, Playlist,AddedTrack
from .serializers import ArtistSerializer, LanguageSerializer, AlbumSerializer, MusicSerializer, PlaylistSerializer,AddedTrackSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here. 

@api_view(['GET'])
def get_music(request):
    musics=Music.objects.all().order_by('-release_date')
    serializer=MusicSerializer(musics,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_playlist(request):
    playlist=Playlist.objects.annotate(song_count=Count('songs')).filter(song_count__gt=3).order_by('-song_count')
    serializer=PlaylistSerializer(playlist,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def add_track(request):
    addTrack=AddedTrack.objects.all().order_by('-added_at')
    serializer=AddedTrackSerializer(addTrack,many=True)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)


# search
@api_view(['GET'])
def all_music_search(request):
    query = request.GET.get('q', '') 
    music_serializer=None
    if query:
        query=query[:len(query)-1]
        music_results = Music.objects.filter(title__icontains=query.upper())
        print("lsit",music_results)
        # Serialize results
        music_serializer = MusicSerializer(music_results, many=True)
    return Response(music_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def all_playlist_search(request):
    query = request.GET.get('q', '') 
    playlist_serializer=None
    if query:
        query=query[:len(query)-1]
        playlist__results =Playlist.objects.filter(name__icontains=query.upper())
        # Serialize results
        playlist_serializer = PlaylistSerializer(playlist__results, many=True)
    return Response(playlist_serializer.data,status=status.HTTP_200_OK)