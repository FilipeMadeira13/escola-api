from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from escola.views import CursoViewSet, EstudanteViewSet, ListaMatriculasCurso, ListaMatriculasEstudante, MatriculaViewSet

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
]
