# factorie-boy uma biblioteca para construir modelos fakes
# importante para não perder tempo construindo modelos
import factory

from product.models import Product
from product.models import Category

# factory.django.DjangoModelFactory permite criar objetos correspondentes a modelos do Django.
# preenchendo automaticamente os campos definidos.


class CategoryFactory(factory.django.DjangoModelFactory):
    # O argumento 'pystr' cria uma sequência de caracteres alfanuméricos aleatórios.
    title = factory.Faker('pystr')
    slug = factory.Faker('slug')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        # importante! colocar o modelo para que o factory identifice os campos
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.SubFactory(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for categories in extracted:
                # adicionando categoria por categoria (list)
                self.category.add(categories)

    class Meta:
        # importante! colocar o modelo para que o factory identifice os campos
        model = Product
