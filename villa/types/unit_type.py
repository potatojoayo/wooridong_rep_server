from graphene_django import DjangoObjectType

from ..models import Unit


class UnitType(DjangoObjectType):
    class Meta:
        model = Unit
