from graphene_django import DjangoObjectType

from bank.models import Bank


class BankType(DjangoObjectType):
    class Meta:
        model = Bank
       