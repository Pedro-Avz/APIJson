from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class CursoAPIView(APIView):

    parser_classes = [JSONParser]
    def get(self, resquest, *args, **kwargs):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, resquest, *args, **kwargs):

        serializer = CursoSerializer(data=resquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

