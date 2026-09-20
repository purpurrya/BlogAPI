from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "content",
            "created_at",
        )
        model = Post
        read_only_fields = ("author",)
