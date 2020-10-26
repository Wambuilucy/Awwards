from .models import Post,Profile
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title','image','description','link')
        
class ProfileSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (' First_Name','Last_Name',' Email',' bio',' profile_pic')