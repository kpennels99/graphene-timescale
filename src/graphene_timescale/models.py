from django.db import models


class Region(models.Model):
    
    name = models.CharField(max_length=100)
    alpha_2 = models.CharField(max_length=2)
    alpha_3 = models.CharField(max_length=3)
    country_code = models.IntegerField()
    iso_3166_2 = models.CharField(max_length=50)
    region = models.CharField(max_length=50, null=True)
    sub_region = models.CharField(max_length=50, null=True)
    intermediate_region = models.CharField(max_length=50, null=True)
    region_code = models.IntegerField(null=True)
    sub_region_code = models.IntegerField(null=True)
    intermediate_region_code = models.IntegerField(null=True)


class GithubVaxData(models.Model):
    
    date = models.DateField(primary_key=True)
    location = models.CharField(max_length=50)
    iso_code =  models.CharField(max_length=10)
    total_vaccinations = models.FloatField(null=True)
    people_vaccinated = models.FloatField(null=True)
    people_fully_vaccinated = models.FloatField(null=True)
    total_boosters = models.FloatField(null=True)
    daily_vaccinations_raw = models.FloatField(null=True)
    daily_vaccinations = models.FloatField(null=True)
    total_vaccinations_per_hundred = models.FloatField(null=True)
    people_vaccinated_per_hundred = models.FloatField(null=True)
    people_fully_vaccinated_per_hundred = models.FloatField(null=True)
    total_boosters_per_hundred = models.FloatField(null=True)
    daily_vaccinations_per_million = models.FloatField(null=True)
    daily_people_vaccinated = models.FloatField(null=True)
    daily_people_vaccinated_per_hundred = models.FloatField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f"{self.location} on {self.date}"
