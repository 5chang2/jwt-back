from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article


@api_view(['GET', 'POST'])
def list_and_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
    return Response(serializer.data)