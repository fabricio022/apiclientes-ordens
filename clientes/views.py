from rest_framework import generics
from clientes.models import ClienteModel
from clientes.serializers import ClienteSerializer
from clientes.infrastructure.django_repository import DjangoClienteRepository
from clientes.usecases.criar_cliente import CriarCliente

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer

    def perform_create(self, serializer):
        # Aqui garantimos que ainda usamos o Use Case
        repo = DjangoClienteRepository()
        usecase = CriarCliente(repo)
        cliente = usecase.execute(
            nome=serializer.validated_data['nome'],
            email=serializer.validated_data['email'],
            telefone=serializer.validated_data['telefone']
        )
        # O GenericAPIView precisa salvar no banco via serializer
        serializer.instance = ClienteModel.objects.get(pk=cliente.id)
