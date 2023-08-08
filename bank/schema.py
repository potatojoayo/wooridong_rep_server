import graphene

from bank.types import BankType


class Query(graphene.ObjectType):
    bank = graphene.Field(BankType)


schema = graphene.Schema(query=Query)
