import graphene

import advertisement.schema
import user.schema
import villa.schema
import pay.schema
import bank.schema


class Query(user.schema.Query, villa.schema.Query, pay.schema.Query, bank.schema.Query, advertisement.schema.Query):
    pass


class Mutation(user.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
