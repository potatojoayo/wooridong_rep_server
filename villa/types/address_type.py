from graphene_django import DjangoObjectType

from ..models import Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
       