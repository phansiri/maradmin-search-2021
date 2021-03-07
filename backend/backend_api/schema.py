import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Maradmin

class MaradminNode(DjangoObjectType):
    class Meta:
        model = Maradmin
        filter_fields = {
            'number': ['exact','icontains'],
            'title': ['exact','icontains'],
            'date': ['exact','icontains'],
            'status': ['exact'],
            'body': ['exact','icontains']
            }
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    maradmin = graphene.relay.Node.Field(MaradminNode)
    all_maradmins = DjangoFilterConnectionField(MaradminNode)