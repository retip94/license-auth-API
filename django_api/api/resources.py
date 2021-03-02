# api/resources.py
from tastypie.resources import ModelResource
from .models import Token





class TokenResource(ModelResource):
    class Meta:
        queryset = Token.objects.all()
        excludes = ['created_at', 'id']
        include_resource_uri = False
        resource_name = 'token'
