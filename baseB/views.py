from rest_framework import viewsets, permissions
from .models import Cliente
from .serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf']
    
    def list(self, request, *args, **kwargs):
        cpf = request.query_params.get('cpf')
        if cpf:
            cliente = Cliente.objects.filter(cpf=cpf).first()
            if cliente:
                cliente.ultima_consulta = timezone.now()
                cliente.save()
        return super().list(request, *args, **kwargs)