from django.db import models


# @author Sujith T
# Deus et scientia erit pactum meum
class IauNameDirectoryModel(models.Model):
    iauname = models.CharField(primary_key=True, max_length=20)
    ra = models.FloatField(blank=True, null=True)
    declination = models.FloatField(blank=True, null=True)
    petro_theta = models.FloatField(blank=True, null=True)
    petro_th50 = models.FloatField(blank=True, null=True)
    petro_th90 = models.FloatField(blank=True, null=True)
    elpetro_absmag_r = models.FloatField(blank=True, null=True)
    sersic_nmgy_r = models.FloatField(blank=True, null=True)
    redshift = models.FloatField(blank=True, null=True)
    mag_r = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_posterior_base'


# model to retrieve galaxy_catalog table
class GalaxyCatalogModel(models.Model):
    obj_id = models.CharField(primary_key=True, max_length=20)
    iauname = models.CharField(max_length=20, blank=True, null=True, )
    ra = models.FloatField(blank=True, null=True)
    declination = models.FloatField(blank=True, null=True)
    ra_string = models.CharField(max_length=15, blank=True, null=True)
    dec_string = models.CharField(max_length=15, blank=True, null=True)
    obj_class = models.CharField(max_length=10, blank=True, null=True)
    taxanomy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galaxy_catalog'


# Model to retrieve HTF taxonomy
class GalaxyTaxonomyModel(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    h_path = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'galaxy_taxanomy'


# Model to retrieve sdss_meta table
class SdssMetadataModel(models.Model):
    obj_id = models.CharField(db_column='OBJ_ID', max_length=20, blank=True,
                              primary_key=True)  # Field name made lowercase.
    ra = models.FloatField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    declination = models.FloatField(db_column='DECLINATION', blank=True, null=True)  # Field name made lowercase.
    petror50_r = models.FloatField(db_column='PETROR50_R', blank=True, null=True)  # Field name made lowercase.
    petror90_r = models.FloatField(db_column='PETROR90_R', blank=True, null=True)  # Field name made lowercase.
    petromag_u = models.FloatField(db_column='PETROMAG_U', blank=True, null=True)  # Field name made lowercase.
    petromag_g = models.FloatField(db_column='PETROMAG_G', blank=True, null=True)  # Field name made lowercase.
    petromag_r = models.FloatField(db_column='PETROMAG_R', blank=True, null=True)  # Field name made lowercase.
    petromag_i = models.FloatField(db_column='PETROMAG_I', blank=True, null=True)  # Field name made lowercase.
    petromag_z = models.FloatField(db_column='PETROMAG_Z', blank=True, null=True)  # Field name made lowercase.
    petromagerr_u = models.FloatField(db_column='PETROMAGERR_U', blank=True, null=True)  # Field name made lowercase.
    petromagerr_g = models.FloatField(db_column='PETROMAGERR_G', blank=True, null=True)  # Field name made lowercase.
    petromagerr_r = models.FloatField(db_column='PETROMAGERR_R', blank=True, null=True)  # Field name made lowercase.
    petromagerr_i = models.FloatField(db_column='PETROMAGERR_I', blank=True, null=True)  # Field name made lowercase.
    petromagerr_z = models.FloatField(db_column='PETROMAGERR_Z', blank=True, null=True)  # Field name made lowercase.
    psfmag_r = models.FloatField(db_column='PSFMAG_R', blank=True, null=True)  # Field name made lowercase.
    fibermag_r = models.FloatField(db_column='FIBERMAG_R', blank=True, null=True)  # Field name made lowercase.
    devmag_r = models.FloatField(db_column='DEVMAG_R', blank=True, null=True)  # Field name made lowercase.
    devmagerr_r = models.FloatField(db_column='DEVMAGERR_R', blank=True, null=True)  # Field name made lowercase.
    expmag_r = models.FloatField(db_column='EXPMAG_R', blank=True, null=True)  # Field name made lowercase.
    expmagerr_r = models.FloatField(db_column='EXPMAGERR_R', blank=True, null=True)  # Field name made lowercase.
    fracdev_r = models.FloatField(db_column='FRACDEV_R', blank=True, null=True)  # Field name made lowercase.
    mu50_r = models.FloatField(db_column='MU50_R', blank=True, null=True)  # Field name made lowercase.
    extinction_u = models.FloatField(db_column='EXTINCTION_U', blank=True, null=True)  # Field name made lowercase.
    extinction_g = models.FloatField(db_column='EXTINCTION_G', blank=True, null=True)  # Field name made lowercase.
    extinction_r = models.FloatField(db_column='EXTINCTION_R', blank=True, null=True)  # Field name made lowercase.
    extinction_i = models.FloatField(db_column='EXTINCTION_I', blank=True, null=True)  # Field name made lowercase.
    extinction_z = models.FloatField(db_column='EXTINCTION_Z', blank=True, null=True)  # Field name made lowercase.
    rowc_u = models.FloatField(db_column='ROWC_U', blank=True, null=True)  # Field name made lowercase.
    colc_u = models.FloatField(db_column='COLC_U', blank=True, null=True)  # Field name made lowercase.
    rowc_g = models.FloatField(db_column='ROWC_G', blank=True, null=True)  # Field name made lowercase.
    colc_g = models.FloatField(db_column='COLC_G', blank=True, null=True)  # Field name made lowercase.
    rowc_r = models.FloatField(db_column='ROWC_R', blank=True, null=True)  # Field name made lowercase.
    colc_r = models.FloatField(db_column='COLC_R', blank=True, null=True)  # Field name made lowercase.
    rowc_i = models.FloatField(db_column='ROWC_I', blank=True, null=True)  # Field name made lowercase.
    colc_i = models.FloatField(db_column='COLC_I', blank=True, null=True)  # Field name made lowercase.
    rowc_z = models.FloatField(db_column='ROWC_Z', blank=True, null=True)  # Field name made lowercase.
    colc_z = models.FloatField(db_column='COLC_Z', blank=True, null=True)  # Field name made lowercase.
    cmodelmag_r = models.FloatField(db_column='CMODELMAG_R', blank=True, null=True)  # Field name made lowercase.
    cmodelmagerr_r = models.FloatField(db_column='CMODELMAGERR_R', blank=True, null=True)  # Field name made lowercase.
    redshift = models.FloatField(db_column='REDSHIFT', blank=True, null=True)  # Field name made lowercase.
    redshifterr = models.FloatField(db_column='REDSHIFTERR', blank=True, null=True)  # Field name made lowercase.
    petromag_mu = models.FloatField(db_column='PETROMAG_MU', blank=True, null=True)  # Field name made lowercase.
    petromag_mg = models.FloatField(db_column='PETROMAG_MG', blank=True, null=True)  # Field name made lowercase.
    petromag_mr = models.FloatField(db_column='PETROMAG_MR', blank=True, null=True)  # Field name made lowercase.
    petromag_mi = models.FloatField(db_column='PETROMAG_MI', blank=True, null=True)  # Field name made lowercase.
    petromag_mz = models.FloatField(db_column='PETROMAG_MZ', blank=True, null=True)  # Field name made lowercase.
    petromagerr_mu = models.FloatField(db_column='PETROMAGERR_MU', blank=True, null=True)  # Field name made lowercase.
    petromagerr_mg = models.FloatField(db_column='PETROMAGERR_MG', blank=True, null=True)  # Field name made lowercase.
    petromagerr_mr = models.FloatField(db_column='PETROMAGERR_MR', blank=True, null=True)  # Field name made lowercase.
    petromagerr_mi = models.FloatField(db_column='PETROMAGERR_MI', blank=True, null=True)  # Field name made lowercase.
    petromagerr_mz = models.FloatField(db_column='PETROMAGERR_MZ', blank=True, null=True)  # Field name made lowercase.
    petror50_r_kpc = models.FloatField(db_column='PETROR50_R_KPC', blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='REGION', blank=True, null=True)  # Field name made lowercase.
    petror50_r_kpc_simple_bin = models.IntegerField(db_column='PETROR50_R_KPC_SIMPLE_BIN', blank=True,
                                                    null=True)  # Field name made lowercase.
    petromag_mr_simple_bin = models.IntegerField(db_column='PETROMAG_MR_SIMPLE_BIN', blank=True,
                                                 null=True)  # Field name made lowercase.
    redshift_simple_bin = models.IntegerField(db_column='REDSHIFT_SIMPLE_BIN', blank=True,
                                              null=True)  # Field name made lowercase.
    wvt_bin = models.IntegerField(db_column='WVT_BIN', blank=True, null=True)  # Field name made lowercase.
    catalog = models.ForeignKey(GalaxyCatalogModel, on_delete=models.CASCADE, db_column='obj_id')

    class Meta:
        managed = False
        db_table = 'sdss_meta'
