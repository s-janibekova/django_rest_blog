from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment



class UserSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'comments')



class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner', 'post')

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at','comments')
        model = Post

