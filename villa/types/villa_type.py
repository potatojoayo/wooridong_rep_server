import graphene
from graphene_django import DjangoObjectType

from villa.models import Villa
from .unit_type import UnitType
from .building_type import BuildingType


class VillaType(DjangoObjectType):
    class Meta:
        model = Villa

    buildings = graphene.List(BuildingType)

    @staticmethod
    def resolve_buildings(root, _):
        return root.buildings.all()

    my_unit = graphene.Field(UnitType, phone_number=graphene.String())

    @staticmethod
    def resolve_my_unit(root, info, **kwargs):
        if "phone_number" in kwargs:
            phone_number = kwargs.get('phone_number')
            return root.units.get(phone_number=phone_number)
        return info.context.user.my_unit.get()
