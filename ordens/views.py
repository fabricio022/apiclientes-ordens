from rest_framework import generics
from ordens.models import OrdemServicoModel
from ordens.serializers import OrdemServicoSerializer
from ordens.infrastructure.django_repository import DjangoOrdemServicoRepository
from ordens.usecases.criar_ordem import CriarOrdemServico

class OrdemServicoListCreateView(generics.ListCreateAPIView):
    queryset = OrdemServicoModel.objects.all()
    serializer_class = OrdemServicoSerializer

    def perform_create(self, serializer):
        repo = DjangoOrdemServicoRepository()
        usecase = CriarOrdemServico(repo)
        ordem = usecase.execute(
            cliente_id=serializer.validated_data['cliente_id'],
            descricao=serializer.validated_data['descricao']
        )
        serializer.instance = OrdemServicoModel.objects.get(pk=ordem.id)
