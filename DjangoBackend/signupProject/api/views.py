from django.shortcuts import render
from .models import signup
from .MySerializer import SignupSerializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SignupDetails(APIView):

    def get_object(self, id):
        try:
            prd = signup.objects.get(id=id)
            return prd
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):

        prd = self.get_object(id)
        if(prd is not None):

            serializer = SignupSerializers(prd)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        prd = self.get_object(id)
        serializer = SignupSerializers(prd, data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        prd = self.get_object(id)
        prd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SignupList(APIView):

    def get(self, request):
        prds = signup.objects.all()
        serializer = SignupSerializers(prds, many=True)
        return Response(serializer.data)

    # Insert record
    def post(self, request):
        serializer = SignupSerializers(data=request.data)

        if(serializer.is_valid()):

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
