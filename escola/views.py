from typing import cast

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle

from escola.models import Curso, Estudante, Matricula
from escola.serializers import (
    CursoSerializer,
    EstudanteSerializer,
    EstudanteSerializerV2,
    ListaMatriculasCursoSerializer,
    ListaMatriculasEstudanteSerializer,
    MatriculaSerializer,
)
from escola.throttles import MatriculaAnonRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    # serializer_class = EstudanteSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]

    def get_serializer_class(self):
        request = cast(Request, self.request)

        if request.version == "v2":
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]


class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"]).order_by(
            "id"
        )
        return queryset

    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"]).order_by("id")
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
