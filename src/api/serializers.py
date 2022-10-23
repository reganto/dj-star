from rest_framework import serializers

from common.helpers import get_client_ip

from .models import Post, Rating


class PostSerializer(serializers.ModelSerializer):
    rating_count = serializers.ReadOnlyField(source="get_rating_counts")
    rating_average = serializers.ReadOnlyField(source="get_rating_average")

    class Meta:
        model = Post
        fields = ("title", "body", "rating_count", "rating_average")


class RatingSerializer(serializers.ModelSerializer):
    ip = serializers.ReadOnlyField()

    class Meta:
        model = Rating
        fields = ("ip", "post", "score")

    def create(self, validated_data):
        request = self.context["request"]
        ip = get_client_ip(request)
        post = validated_data.get("post")
        score = validated_data.get("score")

        rating, created = Rating.objects.update_or_create(
            ip=ip,
            defaults={
                "post": post,
                "score": score,
            },
        )
        return rating
