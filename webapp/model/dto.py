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

        self.petromag_u = meta.petromag_u
        self.petromag_g = meta.petromag_g
        self.petromag_r = meta.petromag_r
        self.petromag_i = meta.petromag_i
        self.petromag_z = meta.petromag_z

        self.petromagerr_u = meta.petromagerr_u
        self.petromagerr_g = meta.petromagerr_g
        self.petromagerr_r = meta.petromagerr_r
        self.petromagerr_i = meta.petromagerr_i
        self.petromagerr_z = meta.petromagerr_z

        self.petromag_mu = meta.petromag_mu
        self.petromag_mg = meta.petromag_mg
        self.petromag_mr = meta.petromag_mr
        self.petromag_mi = meta.petromag_mi
        self.petromag_mz = meta.petromag_mz

        self.petromagerr_mu = meta.petromagerr_mu
        self.petromagerr_mg = meta.petromagerr_mg
        self.petromagerr_mr = meta.petromagerr_mr
        self.petromagerr_mi = meta.petromagerr_mi
        self.petromagerr_mz = meta.petromagerr_mz

        self.extinction_u = meta.extinction_u
        self.extinction_g = meta.extinction_g
        self.extinction_r = meta.extinction_r
        self.extinction_i = meta.extinction_i
        self.extinction_z = meta.extinction_z

        self.rowc_u = meta.rowc_u
        self.rowc_g = meta.rowc_g
        self.rowc_r = meta.rowc_r
        self.rowc_i = meta.rowc_i
        self.rowc_z = meta.rowc_z

        self.colc_u = meta.colc_u
        self.colc_g = meta.colc_g
        self.colc_r = meta.colc_r
        self.colc_i = meta.colc_i
        self.colc_z = meta.colc_z
