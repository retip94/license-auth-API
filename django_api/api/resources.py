# api/resources.py
from tastypie.resources import ModelResource
from .models import Note, Token

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'

class TokenResource(ModelResource):
    class Meta:
        queryset = Token.objects.all()
        excludes = ['created_at', 'id']
        include_resource_uri = False
        resource_name = 'token'
