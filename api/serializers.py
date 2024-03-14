from rest_framework import serializers


# @author Sujith T
# Deus et scientia erit pactum meum
# Serializer for the web-service
class ClassifySerializer(serializers.Serializer):
    petror50_r = serializers.FloatField(required=True, min_value=0.5, max_value=107.0)
    petror90_r = serializers.FloatField(required=True, min_value=0.8, max_value=219.0)
    petromag_u = serializers.FloatField(required=True, min_value=9.7, max_value=46.0)
    petromag_g = serializers.FloatField(required=True, min_value=9.0, max_value=42.4)
    petromag_r = serializers.FloatField(required=True, min_value=7.0, max_value=27.8)
    petromag_i = serializers.FloatField(required=True, min_value=8.0, max_value=46.1)
    petromag_z = serializers.FloatField(required=True, min_value=5.0, max_value=45.4)

    petromagerr_u = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_g = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_r = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_i = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_z = serializers.FloatField(required=True, min_value=0.0000001)

    psfmag_r = serializers.FloatField(required=True, min_value=0.0000001)
    fibermag_r = serializers.FloatField(required=True, min_value=0.0000001)

    devmag_r = serializers.FloatField(required=True, min_value=0.0000001)
    devmagerr_r = serializers.FloatField(required=True, min_value=0.0000001)
    expmag_r = serializers.FloatField(required=True, min_value=0.0000001)
    expmagerr_r = serializers.FloatField(required=True, min_value=0.0000001)

    fracdev_r = serializers.FloatField(required=True, min_value=0.0000001)
    mu50_r = serializers.FloatField(required=True, min_value=0.0000001)

    extinction_u = serializers.FloatField(required=True, min_value=0.0000001)
    extinction_g = serializers.FloatField(required=True, min_value=0.0000001)
    extinction_r = serializers.FloatField(required=True, min_value=0.0000001)
    extinction_i = serializers.FloatField(required=True, min_value=0.0000001)
    extinction_z = serializers.FloatField(required=True, min_value=0.0000001)

    rowc_u = serializers.FloatField(required=True, min_value=0.0000001)
    colc_u = serializers.FloatField(required=True, min_value=0.0000001)
    rowc_g = serializers.FloatField(required=True, min_value=0.0000001)
    colc_g = serializers.FloatField(required=True, min_value=0.0000001)
    rowc_r = serializers.FloatField(required=True, min_value=0.0000001)
    colc_r = serializers.FloatField(required=True, min_value=0.0000001)
    rowc_i = serializers.FloatField(required=True, min_value=0.0000001)
    colc_i = serializers.FloatField(required=True, min_value=0.0000001)
    rowc_z = serializers.FloatField(required=True, min_value=0.0000001)
    colc_z = serializers.FloatField(required=True, min_value=0.0000001)

    cmodelmag_r = serializers.FloatField(required=True, min_value=0.0000001)
    cmodelmagerr_r = serializers.FloatField(required=True, min_value=0.0000001)

    redshift = serializers.FloatField(required=True, min_value=0.0000001)
    redshifterr = serializers.FloatField(required=True, min_value=0.0000001)

    petromag_mu = serializers.FloatField(required=True)
    petromag_mg = serializers.FloatField(required=True)
    petromag_mr = serializers.FloatField(required=True)
    petromag_mi = serializers.FloatField(required=True)
    petromag_mz = serializers.FloatField(required=True)

    petromagerr_mu = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_mg = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_mr = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_mi = serializers.FloatField(required=True, min_value=0.0000001)
    petromagerr_mz = serializers.FloatField(required=True, min_value=0.0000001)

    petror50_r_kpc = serializers.FloatField(required=True, min_value=0.0000001)
    petror50_r_kpc_simple_bin = serializers.IntegerField(required=True, min_value=0)
    petromag_mr_simple_bin = serializers.IntegerField(required=True, min_value=0)
    redshift_simple_bin = serializers.IntegerField(required=True, min_value=0)
    wvt_bin = serializers.IntegerField(required=True, min_value=0)
