from rest_framework import serializers
from .models import Artist, Language, Album, Music, Playlist , AddedTrack

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'  

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True, read_only=True)
    album = AlbumSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Music
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    songs = MusicSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = '__all__'
        

class AddedTrackSerializer(serializers.ModelSerializer):
    music = MusicSerializer()
    playlist = PlaylistSerializer()
    class Meta:
        model=AddedTrack
        fields='__all__'