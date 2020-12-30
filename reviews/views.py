from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

from artworks.models import Title

from .models import Comment, Review
from .permissions import IsOwnerOrSuperuserOrReadOnly
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrSuperuserOrReadOnly,)

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        author = self.request.user
        review = Review.objects.filter(author=author, title_id=title)
        if len(review) == 0:
            serializer.save(author=self.request.user, title_id=title)
        else:
            raise ValidationError()

    def get_queryset(self):
        queryset = Review.objects.filter(title_id=self.kwargs.get('title_id'))
        return queryset


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrSuperuserOrReadOnly,)

    def perform_create(self, serializer):
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review_id)

    def get_queryset(self):
        queryset = Comment.objects.filter(
            review_id=self.kwargs.get('review_id'))
        return queryset
