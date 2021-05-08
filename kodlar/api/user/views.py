from rest_framework import generics
from .serializer import UsersSerializer
from user.models import Users

class UserViews(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        tg_id=self.request.query_params.get('id')
        queryset=queryset.filter(tg_id=tg_id)

        return queryset
