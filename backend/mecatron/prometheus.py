from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway

registry = CollectorRegistry()

peso_da_garrafa = Gauge(
    'peso_da_garrafa_de_agua',
    'peso da garrafa de água',
    registry=registry
)

umidade_da_terra = Gauge(
    'umidade_da_terra',
    'umidade da terra',
    registry=registry
)

def send_metrics():
    pushadd_to_gateway("pushgateway:9091", job='mecatron-app', registry=registry)