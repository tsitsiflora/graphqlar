import graphene
import testapi.schema


class Query(testapi.schema.Query, graphene.ObjectType):
    pass

class Mutation(testapi.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
