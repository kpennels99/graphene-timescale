# Generated by Django 3.2.13 on 2022-04-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alpha_2', models.CharField(max_length=2)),
                ('alpha_3', models.CharField(max_length=3)),
                ('country_code', models.IntegerField()),
                ('iso_3166_2', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50, null=True)),
                ('sub_region', models.CharField(max_length=50, null=True)),
                ('intermediate_region', models.CharField(max_length=50, null=True)),
                ('region_code', models.IntegerField(null=True)),
                ('sub_region_code', models.IntegerField(null=True)),
                ('intermediate_region_code', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GithubVaxData',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('iso_code', models.CharField(max_length=10)),
                ('total_vaccinations', models.FloatField(null=True)),
                ('people_vaccinated', models.FloatField(null=True)),
                ('people_fully_vaccinated', models.FloatField(null=True)),
                ('total_boosters', models.FloatField(null=True)),
                ('daily_vaccinations_raw', models.FloatField(null=True)),
                ('daily_vaccinations', models.FloatField(null=True)),
                ('total_vaccinations_per_hundred', models.FloatField(null=True)),
                ('people_vaccinated_per_hundred', models.FloatField(null=True)),
                ('people_fully_vaccinated_per_hundred', models.FloatField(null=True)),
                ('total_boosters_per_hundred', models.FloatField(null=True)),
                ('daily_vaccinations_per_million', models.FloatField(null=True)),
                ('daily_people_vaccinated', models.FloatField(null=True)),
                ('daily_people_vaccinated_per_hundred', models.FloatField(null=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='graphene_timescale.region')),
            ],
        ),
        migrations.RunSQL(
            "ALTER TABLE graphene_timescale_githubvaxdata DROP CONSTRAINT graphene_timescale_githubvaxdata_pkey;"
        ),
        migrations.RunSQL(
            "SELECT create_hypertable('graphene_timescale_githubvaxdata', 'date', chunk_time_interval => INTERVAL '30 days');"
        )
    ]
