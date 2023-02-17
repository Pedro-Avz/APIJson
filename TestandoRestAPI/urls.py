from django.urls import path, include

from .views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacao/', AvaliacaoAPIView.as_view(), name='avaliacao')

]
