from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import RegisterSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserView(generics.GenericAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        authenticated = authenticate(username=request.POST['username'], password=request.POST['password'])
        if authenticated:
            refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully",
        })
