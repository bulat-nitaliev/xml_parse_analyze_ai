
import factory
from factory.django import DjangoModelFactory
from core.models import Product, User, AnswerLLm

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    is_staff = True

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    prod_id = factory.Faker('random_int')
    name = factory.Faker('word')
    quantity = factory.Faker('random_int')
    price = factory.Faker('random_int')
    category = factory.Faker('company')
    date_product = factory.Faker('date')
    

class LlmFactory(DjangoModelFactory):
    class Meta:
        model = AnswerLLm

    user = factory.SubFactory(UserFactory)
    prompt = factory.Faker('text')
    answer = factory.Faker('text')
    dt_create = factory.Faker('date')

