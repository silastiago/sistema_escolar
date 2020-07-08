from rest_framework.viewsets import ModelViewSet
from estudantes.models import Estudante
from .serializers import EstudanteSerializer

class EstudanteViewSet(ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filterset_fields = ['nome']