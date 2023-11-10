from rest_framework import viewsets
from rest_framework.response import Response
from .prometheus import peso_da_garrafa, umidade_da_terra, send_metrics

# Create your views here.
class PesoAguaView(viewsets.ViewSet):
    def create(self, request):
        peso = request.data['peso']
        peso_da_garrafa.set(peso)
        send_metrics()
        return Response(f"peso = {peso}")
    
class UmidadePlantaview(viewsets.ViewSet):
    def create(self, request):
        umidade = request.data['umidade']
        umidade_da_terra.set(umidade)
        send_metrics()
        return Response(f"umidade = {umidade}")