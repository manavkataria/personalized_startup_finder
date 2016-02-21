from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CbObjects(models.Model):

    id = models.CharField(primary_key=True, max_length=64)
    entity_type = models.CharField(max_length=16)
    entity_id = models.BigIntegerField()
    parent_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255)
    normalized_name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    category_code = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    closed_at = models.DateField(blank=True, null=True)
    domain = models.CharField(max_length=64, blank=True, null=True)
    homepage_url = models.CharField(max_length=64, blank=True, null=True)
    twitter_username = models.CharField(max_length=64, blank=True, null=True)
    logo_url = models.CharField(max_length=255, blank=True, null=True)
    logo_width = models.IntegerField(blank=True, null=True)
    logo_height = models.IntegerField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    tag_list = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=64, blank=True, null=True)
    state_code = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    first_investment_at = models.DateField(blank=True, null=True)
    last_investment_at = models.DateField(blank=True, null=True)
    investment_rounds = models.IntegerField(blank=True, null=True)
    invested_companies = models.IntegerField(blank=True, null=True)
    first_funding_at = models.DateField(blank=True, null=True)
    last_funding_at = models.DateField(blank=True, null=True)
    funding_rounds = models.IntegerField(blank=True, null=True)
    funding_total_usd = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    first_milestone_at = models.DateField(blank=True, null=True)
    last_milestone_at = models.DateField(blank=True, null=True)
    milestones = models.IntegerField(blank=True, null=True)
    relationships = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cb_objects'
        unique_together = (('entity_type', 'entity_id'),)
