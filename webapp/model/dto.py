# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
from webapp.models import GalaxyCatalogModel, SdssMetadataModel


# @author Sujith T
# Deus et scientia erit pactum meum
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
