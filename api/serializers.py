from rest_framework import serializers


# @author Sujith T
# Deus et scientia erit pactum meum
# Serializer for the web-service
class ClassifySerializer(serializers.Serializer):
    #petror50_r = serializers.FloatField(required=True, min_value=0.5, max_value=107.0)
    petror90_r = serializers.FloatField(required=True, min_value=0.8, max_value=219.0)
    petromag_u = serializers.FloatField(required=True, min_value=9.7, max_value=46.0)
    #petromag_g = serializers.FloatField(required=True, min_value=9.0, max_value=42.4)
    petromag_r = serializers.FloatField(required=True, min_value=7.0, max_value=27.8)
    #petromag_i = serializers.FloatField(required=True, min_value=8.0, max_value=46.1)
    #petromag_z = serializers.FloatField(required=True, min_value=8.0, max_value=45.4)

    petromagerr_u = serializers.FloatField(required=True, min_value=7.3E-4, max_value=501375.0)
    #petromagerr_g = serializers.FloatField(required=True, min_value=3.5E-4, max_value=12593.0)
    petromagerr_r = serializers.FloatField(required=True, min_value=1.7E-4, max_value=784.0)
    #petromagerr_i = serializers.FloatField(required=True, min_value=3.7E-4, max_value=16350.0)
    petromagerr_z = serializers.FloatField(required=True, min_value=1.8E-4, max_value=7352259.0)

    psfmag_r = serializers.FloatField(required=True, min_value=13.3, max_value=27.8)
    #fibermag_r = serializers.FloatField(required=True, min_value=12.8, max_value=24.6)

    #devmag_r = serializers.FloatField(required=True, min_value=9.7, max_value=27.8)
    devmagerr_r = serializers.FloatField(required=True, min_value=0.001, max_value=4.4)
    #expmag_r = serializers.FloatField(required=True, min_value=7.5, max_value=28.0)
    #expmagerr_r = serializers.FloatField(required=True, min_value=0.001, max_value=4.3)

    fracdev_r = serializers.FloatField(required=True, min_value=0, max_value=1)
    #mu50_r = serializers.FloatField(required=True, min_value=15, max_value=49.8)

    #extinction_u = serializers.FloatField(required=True, min_value=0.01, max_value=3.0)
    #extinction_g = serializers.FloatField(required=True, min_value=0.01, max_value=2.2)
    extinction_r = serializers.FloatField(required=True, min_value=0.008, max_value=1.7)
    #extinction_i = serializers.FloatField(required=True, min_value=0.005, max_value=1.2)
    #extinction_z = serializers.FloatField(required=True, min_value=0.004, max_value=0.9)

    #rowc_u = serializers.FloatField(required=True, min_value=58, max_value=1463)
    #colc_u = serializers.FloatField(required=True, min_value=27, max_value=2026)
    #rowc_g = serializers.FloatField(required=True, min_value=59, max_value=1460)
    #colc_g = serializers.FloatField(required=True, min_value=31, max_value=2024)
    rowc_r = serializers.FloatField(required=True, min_value=62, max_value=1425)
    colc_r = serializers.FloatField(required=True, min_value=35, max_value=2021.5)
    #rowc_i = serializers.FloatField(required=True, min_value=41, max_value=1465)
    #colc_i = serializers.FloatField(required=True, min_value=34, max_value=2021)
    #rowc_z = serializers.FloatField(required=True, min_value=46, max_value=1471)
    #colc_z = serializers.FloatField(required=True, min_value=31, max_value=2027)

    #cmodelmag_r = serializers.FloatField(required=True, min_value=7.5, max_value=28)
    cmodelmagerr_r = serializers.FloatField(required=True, min_value=0.001, max_value=4.4)

    redshift = serializers.FloatField(required=True, min_value=-7.5E-5, max_value=0.3)
    redshifterr = serializers.FloatField(required=True, min_value=0, max_value=0.03)

    #petromag_mu = serializers.FloatField(required=True, min_value=-25, max_value=8)
    #petromag_mg = serializers.FloatField(required=True, min_value=-25.5, max_value=-0.3)
    petromag_mr = serializers.FloatField(required=True, min_value=-26.5, max_value=-1)
    #petromag_mi = serializers.FloatField(required=True, min_value=-26.1, max_value=5.5)
    #petromag_mz = serializers.FloatField(required=True, min_value=-26.6, max_value=3.4)

    petromagerr_mu = serializers.FloatField(required=True, min_value=0.01, max_value=32)
    #petromagerr_mg = serializers.FloatField(required=True, min_value=0.009, max_value=30)
    petromagerr_mr = serializers.FloatField(required=True, min_value=0.009, max_value=12)
    #petromagerr_mi = serializers.FloatField(required=True, min_value=0.009, max_value=29)
    petromagerr_mz = serializers.FloatField(required=True, min_value=0.009, max_value=31)

    #petror50_r_kpc = serializers.FloatField(required=True, min_value=-19500, max_value=105)
    petror50_r_kpc_simple_bin = serializers.IntegerField(required=True, min_value=0, max_value=150)
    #petromag_mr_simple_bin = serializers.IntegerField(required=True, min_value=0, max_value=180)
    redshift_simple_bin = serializers.IntegerField(required=True, min_value=0, max_value=15)
    wvt_bin = serializers.IntegerField(required=True, min_value=0, max_value=122)
