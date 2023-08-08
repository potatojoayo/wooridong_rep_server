import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from villa.models import Unit, Villa
from .types import VillaType, UnitType


class Query(graphene.ObjectType):
    villa_list = graphene.List(VillaType, unit_phone_number=graphene.String())

    @staticmethod
    def resolve_villa_list(_, __, **kwargs):
        if 'unit_phone_number' in kwargs:
            unit_phone_number = kwargs.get('unit_phone_number')
            units = Unit.objects.filter(phone_number=unit_phone_number)
            return [unit.villa for unit in units]
        return Villa.objects.all()

    my_unit = graphene.Field(UnitType, phone_number=graphene.String())

    @staticmethod
    def resolve_my_unit(_, __, **kwargs):
        if 'phone_number' in kwargs:
            phone_number = kwargs.get('phone_number')
            return Unit.objects.get(phone_number=phone_number)
        raise GraphQLError('휴대폰번호와 일치하는 Unit이 없습니다.')

    my_villa = graphene.Field(VillaType)

    @staticmethod
    @login_required
    def resolve_my_villa(_, info):
        return info.context.user.my_unit.get().villa


schema = graphene.Schema(query=Query)
