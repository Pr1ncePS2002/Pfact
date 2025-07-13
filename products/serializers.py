from rest_framework import serializers
from .models import Product
from reviews.models import Review

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at', 'average_rating']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews:
            return None
        return round(sum([r.rating for r in reviews]) / len(reviews), 2)