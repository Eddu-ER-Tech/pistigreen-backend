from django.http import JsonResponse


from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.object.all()

    serializer = PostSerializer(posts, many = True)

    return JsonResponse({'data': serializer.data})