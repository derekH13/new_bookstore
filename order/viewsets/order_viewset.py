from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

# função ModelViewSet traz funcionalidades prontas para ser usada


class OrderViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # definindo o serializer que esta viewset esta relacionada
    serializer_class = OrderSerializer
    # a query de listagem vai ser ordenado pelo id
    queryset = Order.objects.all().order_by("id")

    class Meta:
        ordering = ['-id']
