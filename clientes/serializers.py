from rest_framework import serializers

class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()
    email = serializers.EmailField()
    telefone = serializers.CharField()
