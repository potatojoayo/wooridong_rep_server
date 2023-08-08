import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from user.types import UserType


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)
    token_test = graphene.String()

    @staticmethod
    @login_required
    def resolve_token_test(_, __):
        try:
            return 'pass'
        except:
            return 'fail'


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
