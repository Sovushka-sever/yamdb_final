from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre', 'category', 'description')


class TitleReadSerializer(TitleSerializer):
    category = CategorySerializer(read_only=True, required=False)
    genre = GenreSerializer(read_only=True, required=False, many=True)
    rating = serializers.FloatField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'genre', 'rating', 'category', 'description')
        read_only_fields = ('id', 'rating')
