from operator import ge
import graphene
from graphene_django import DjangoObjectType
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from rx import Observable

from graphene_timescale.models import GithubVaxData

class GithubVaxDataType(DjangoObjectType):
    
    class Meta:
        model = GithubVaxData
        fields = ('date', 'location', 'total_vaccinations')
        

class Query(graphene.ObjectType):
    all_data = graphene.List(GithubVaxDataType)
    data_by_location = graphene.List(GithubVaxDataType, location=graphene.String(required=True))
                                      
    def resolve_all_data(root, info):
        return GithubVaxData.objects.all()
    
    def resolve_data_by_location(root, info, location):
        try:
            return GithubVaxData.objects.filter(location=location)
        except GithubVaxData.DoesNotExist:
            return None
        
def get_latest_vaccinations():
    return GithubVaxData.objects\
                .distinct('location')\
                .order_by('location', '-date')\
        

class Subscription(graphene.ObjectType):
    total_vaccinations = graphene.List(GithubVaxDataType,
                                        up_to=graphene.Int())

    @staticmethod
    def resolve_total_vaccinations(root, info, up_to):
        return Observable.interval(3000) \
                         .map(lambda i: get_latest_vaccinations())
        
            
        

schema = graphene.Schema(query=Query, subscription=Subscription)