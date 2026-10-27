from rest_framework import generics, viewsets

from escola.models import Curso, Estudante, Matricula
from escola.serializers import CursoSerializer, EstudanteSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, MatriculaSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasCursoSerializer