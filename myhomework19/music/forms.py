from django import forms
from music.models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ["title", "artist", "album", "album_cover_file", "description", "tag_set", ]