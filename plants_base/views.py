from rest_framework import generics
# TODO: Create your views here.

class Plants(generics.CreateAPIView):

    # def get_queryset(self):
    #     raise Exception(self)
    #     return user.accounts.all()

    def post(self, request, *args, **kwargs):
        # raise Exception(self.type)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
