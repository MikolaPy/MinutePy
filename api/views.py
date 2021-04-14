from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import *
from .serializers import *

@api_view(['GET'])
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()[:10]
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSetializer


@api_view(['GET','POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request,pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    else:
        comments = Comment.objects.get(post=pk)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)


