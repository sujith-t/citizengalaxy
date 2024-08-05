import cmath as cm
from django.core.paginator import Paginator
import json

from webapp.model.dto import CatalogSearchResult, GalaxyDetail
from webapp.models import SdssMetadataModel, GalaxyCatalogModel, IauNameDirectoryModel, GalaxyTaxonomyModel


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

    def search(self, param: dict, is_json=False):
        result = []

        def _compute_cosine(source_dec: float, source_ra: float, catalogs: list):
            ang_dist = {}
            for item in catalogs:
                cos_distance = ((cm.sin(source_dec) * cm.sin(item.declination))
                                + (cm.cos(source_dec) * cm.cos(item.declination)
                                   * cm.cos(source_ra - item.ra)))
                ang_dist[cos_distance.real] = item
            return ang_dist

        if param['search_option'] == "obj_id":
            galaxy_catalog = GalaxyCatalogModel.objects.filter(obj_id=param["search_value"]).first()
            sdss_meta = SdssMetadataModel.objects.filter(obj_id=param["search_value"]).first()

            if galaxy_catalog is not None:
                search_result = CatalogSearchResult(sdss_meta, galaxy_catalog)
                if is_json:
                    search_result = json.loads(json.dumps(search_result.__dict__))
                result.append(search_result)

        if param['search_option'] == "iauname":
            galaxy_catalogs = GalaxyCatalogModel.objects.filter(iauname=param["search_value"])
            iau_dir = IauNameDirectoryModel.objects.filter(iauname=param["search_value"]).first()

            if iau_dir is None or galaxy_catalogs.count() == 0:
                return []

            angular_distances = _compute_cosine(iau_dir.declination, iau_dir.ra, galaxy_catalogs)

            # we get the max cosine to identify the closest object acos > 0.99 nearing 1 = 0deg
            angular_closer_key = max(angular_distances)
            search_result = None
            if angular_closer_key > 0.99:
                catalog = angular_distances[angular_closer_key]
                sdss_meta = SdssMetadataModel.objects.filter(obj_id=catalog.obj_id).first()
                search_result = CatalogSearchResult(sdss_meta, catalog)

            if is_json:
                search_result = json.loads(json.dumps(search_result.__dict__))

            if search_result is not None:
                result.append(search_result)

        if param['search_option'] == "ra_dec":

            input_ra, input_dec = float(param["ra"]), float(param["dec"])
            galaxy_catalogs = GalaxyCatalogModel.objects.filter(ra__gt=(input_ra - 0.25), ra__lt=(input_ra + 0.25),
                                                                declination__gt=(input_dec - 0.25),
                                                                declination__lt=(input_dec + 0.25))

            angular_distances = _compute_cosine(input_dec, input_ra, galaxy_catalogs)
            keys = sorted(angular_distances, reverse=True)

            if len(keys) > 10:
                keys = keys[0:10]

            for k in keys:
                catalog = angular_distances[k]
                sdss_meta = SdssMetadataModel.objects.filter(obj_id=catalog.obj_id).first()
                search_result = CatalogSearchResult(sdss_meta, catalog)
                if is_json:
                    search_result = json.loads(json.dumps(search_result.__dict__))

                result.append(search_result)

        return result

    def get_details(self, param: dict, is_json=False) -> GalaxyDetail:

        search_result = self.search(param)
        if len(search_result) == 0:
            return

        galaxy_catalog = GalaxyCatalogModel.objects.filter(obj_id=search_result[0].obj_id).first()
        if galaxy_catalog is None:
            return

        sdss_meta = SdssMetadataModel.objects.filter(obj_id=search_result[0].obj_id).first()
        taxonomy = GalaxyTaxonomyModel.objects.filter(id=galaxy_catalog.taxanomy_id).first()

        result = GalaxyDetail(sdss_meta, galaxy_catalog, taxonomy)
        if is_json:
            result = json.loads(json.dumps(result.__dict__))

        return result
