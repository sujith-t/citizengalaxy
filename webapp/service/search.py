import cmath as cm
from django.core.paginator import Paginator

from webapp.model.dto import CatalogSearchResult
from webapp.models import SdssMetadataModel, GalaxyCatalogModel, IauNameDirectoryModel


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class GalaxyLocatorServiceImpl:
    default_page_size = 25

    def get_page_result(self, page_no):
        query_sets = SdssMetadataModel.objects.select_related("catalog")
        paginator = Paginator(query_sets, self.default_page_size)

        if page_no < 1 or page_no > paginator.num_pages:
            return 1, []

        page = paginator.page(page_no)

        return paginator.num_pages, page.object_list

    def search(self, param: dict):
        result = []

        if param['search_option'] == "obj_id":
            galaxy_catalog = GalaxyCatalogModel.objects.filter(obj_id=param["search_value"]).first()
            sdss_meta = SdssMetadataModel.objects.filter(obj_id=param["search_value"]).first()

            if galaxy_catalog is not None:
                search_result = CatalogSearchResult(sdss_meta, galaxy_catalog)
                result.append(search_result)

        if param['search_option'] == "iauname":
            galaxy_catalogs = GalaxyCatalogModel.objects.filter(iauname=param["search_value"])
            iau_dir = IauNameDirectoryModel.objects.filter(iauname=param["search_value"]).first()

            if iau_dir is None or galaxy_catalogs.count() == 0:
                return []

            angular_distances = {}
            for item in galaxy_catalogs:
                cos_distance = ((cm.sin(iau_dir.declination) * cm.sin(item.declination))
                                + (cm.cos(iau_dir.declination) * cm.cos(item.declination) * cm.cos(
                            iau_dir.ra - item.ra)))
                angular_distances[cos_distance.real] = item

            # we get the max cosine to identify the closest object
            angular_closer_key = max(angular_distances)
            catalog = angular_distances[angular_closer_key]
            sdss_meta = SdssMetadataModel.objects.filter(obj_id=catalog.obj_id).first()
            search_result = CatalogSearchResult(sdss_meta, catalog)
            result.append(search_result)

        return result

    def get_details(self, obj_id):
        pass
