from django.contrib.gis.db import models

class EparxiakoOdikoDiktio(models.Model):
    gid = models.AutoField(primary_key=True)
    aa = models.SmallIntegerField(blank=True, null=True)
    yparith = models.CharField(max_length=254, blank=True, null=True)
    onomasia = models.CharField(max_length=100, blank=True, null=True)
    katataksi = models.CharField(max_length=100, blank=True, null=True)
    tmima = models.CharField(max_length=50, blank=True, null=True)
    apallotr = models.CharField(max_length=100, blank=True, null=True)
    fekapall = models.CharField(max_length=50, blank=True, null=True)
    arfakellou = models.CharField(max_length=50, blank=True, null=True)
    sxolia = models.CharField(max_length=250, blank=True, null=True)
    parakatath = models.CharField(max_length=250, blank=True, null=True)
    yp = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiLineStringField(srid=2100, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'eparxiako_odiko_diktio'

    def __str__(self):
        return self.onomasia
  
    def __unicode__(self):
        return self.onomasia or u''

class OdikoDiktyoKritis(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    namegrk = models.CharField(max_length=66, blank=True, null=True)
    nameeng = models.CharField(max_length=69, blank=True, null=True)
    length = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    armodiot = models.CharField(max_length=49, blank=True, null=True)
    arth_num = models.CharField(max_length=33, blank=True, null=True)
    other_name = models.CharField(max_length=123, blank=True, null=True)
    fek = models.CharField(max_length=25, blank=True, null=True)
    geom = models.MultiLineStringField(srid=2100, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'odiko_diktyo_kritis'

    def __str__(self):
        return self.namegrk

    def __unicode__(self):
        return self.namegrk or u''


'''class Trans_network(models.Model):
    objectid = models.IntegerField()
    typeid = models.FloatField()
    namegrk = models.CharField(max_length=200)
    nameeng = models.CharField(max_length=200)
    length = models.FloatField()
    armodiot = models.CharField(max_length=200)
    arth_num = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)

    lstring = models.MultiLineStringField()
    objects = models.GeoManager()

    def __str__(self):
        return self.nameeng
    
    def __unicode__(self):
        return self.nameeng
'''                            
class Loc(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()

    def __str__(self):
        return self.name


