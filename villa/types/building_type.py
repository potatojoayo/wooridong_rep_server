import graphene
from graphene_django import DjangoObjectType

from ..models import Building
from .unit_type import UnitType


class BuildingType(DjangoObjectType):
    class Meta:
        model = Building

    units = graphene.List(UnitType)

    @staticmethod
    def resolve_units(root, _):
        return root.units.all()
