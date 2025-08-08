from rest_framework import serializers

class OrdemServicoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cliente_id = serializers.IntegerField()
    descricao = serializers.CharField()
    status = serializers.CharField(read_only=True)
    data_abertura = serializers.DateTimeField(read_only=True)
