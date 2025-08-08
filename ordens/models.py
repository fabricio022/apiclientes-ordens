from django.db import models
from clientes.models import ClienteModel

class OrdemServicoModel(models.Model):
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="ordens")
    descricao = models.TextField()
    status = models.CharField(max_length=20, default="aberta")
    data_abertura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OS {self.id} - {self.status}"