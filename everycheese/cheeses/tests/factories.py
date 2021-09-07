from django.template.defaultfilters import slugify
import factory.fuzzy
from ..models import Cheese
import factory


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.fuzzy.FuzzyText()

    class Meta:
        model = Cheese