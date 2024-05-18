import math
from webapp.models import GalaxyCatalogModel, SdssMetadataModel, GalaxyTaxonomyModel


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class CatalogSearchResult:

    def __init__(self, meta: SdssMetadataModel, catalog: GalaxyCatalogModel):
        self.obj_id = catalog.obj_id
        self.iauname = catalog.iauname
        self.ra = catalog.ra
        self.declination = catalog.declination
        self.obj_class = catalog.obj_class
        self.redshift = None
        self.petror50_r = None

        if meta is not None:
            self.redshift = meta.redshift
            self.petror50_r = meta.petror50_r


class GalaxyDetail(CatalogSearchResult):
    def __init__(self, meta: SdssMetadataModel, catalog: GalaxyCatalogModel, taxonomy: GalaxyTaxonomyModel):
        super().__init__(meta, catalog)

        ra_tmp = catalog.ra / 15
        self.ra_string = str(math.floor(ra_tmp)) + "h "
        ra_tmp = (ra_tmp - math.floor(ra_tmp)) * 60
        self.ra_string += str(math.floor(ra_tmp)) + "m "
        ra_tmp = (ra_tmp - math.floor(ra_tmp)) * 60
        self.ra_string += str(math.floor(ra_tmp)) + "s "
        ra_tmp = round((ra_tmp - math.floor(ra_tmp)) * 1000, 4)
        self.ra_string += str(ra_tmp) + "ms"

        factor = -1
        dec_tmp = catalog.declination
        if dec_tmp > 0:
            factor = 1
        dec_tmp = abs(dec_tmp)
        self.dec_string = str(math.floor(dec_tmp) * factor) + "° "
        dec_tmp = (dec_tmp - math.floor(dec_tmp)) * 60
        self.dec_string += str(math.floor(dec_tmp)) + "' "
        dec_tmp = (dec_tmp - math.floor(dec_tmp)) * 60
        self.dec_string += str(math.floor(dec_tmp)) + '" '
        dec_tmp = round((dec_tmp - math.floor(dec_tmp)) * 1000, 4)
        self.dec_string += str(dec_tmp) + "ms"

        self.petror50_r = meta.petror50_r
        self.petror90_r = meta.petror90_r

        self.wvt_bin = meta.wvt_bin
        self.redshift_simple_bin = meta.redshift_simple_bin
        self.petror50_r_kpc_simple_bin = meta.petror50_r_kpc_simple_bin
        self.petromag_mr_simple_bin = meta.petromag_mr_simple_bin
        self.redshifterr = meta.redshifterr
        self.mu50_r = meta.mu50_r
        self.cmodelmag_r = meta.cmodelmag_r
        self.cmodelmagerr_r = meta.cmodelmagerr_r

        self.taxonomy_code = taxonomy.code
