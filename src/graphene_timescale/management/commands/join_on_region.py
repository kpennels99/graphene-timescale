from django.core.management.base import BaseCommand, CommandError

from django.db import connection

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    UPDATE graphene_timescale_githubvaxdata 
                    SET region_id = (
                        SELECT id 
                        FROM graphene_timescale_region 
                        WHERE graphene_timescale_region.alpha_3 = graphene_timescale_githubvaxdata.iso_code)
                """
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully joined graphene_timescale_githubvaxdata and graphene_timescale_region'
            )    
        )