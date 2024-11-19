import factory

# pega o modelo pronto
from django.contrib.auth.models import User

from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        # importante! colocar o modelo para que o factory-boy identifique os campos
        model = User


# Quando você cria um objeto com OrderFactory, o factory.SubFactory cria automaticamente um usuário associado, caso nenhum seja especificado.
class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        # importante! colocar o modelo para que o factory-boy identifique os campos
        model = Order
