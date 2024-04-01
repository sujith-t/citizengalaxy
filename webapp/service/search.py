from django.core.paginator import Paginator

from webapp.model.dto import CatalogSearchResult
from webapp.models import SdssMetadataModel, GalaxyCatalogModel, AutoPosteriorBaseModel


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
            galaxy_catalogs = GalaxyCatalogModel.objects.filter(obj_id=param["search_value"]).values()
            iau_dir = AutoPosteriorBaseModel.objects.filter(iauname=param["search_value"]).first()

            return galaxy_catalogs

        return result

    def get_details(self, obj_id):
        pass
