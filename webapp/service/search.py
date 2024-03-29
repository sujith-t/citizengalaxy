from django.core.paginator import Paginator
from webapp.models import SdssMetadataModel


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class GalaxyLocatorServiceImpl:

    default_page_size = 25

    def search(self, param: dict):
        pass

    def get_page_result(self, page_no):
        query_sets = SdssMetadataModel.objects.select_related("catalog")
        paginator = Paginator(query_sets, self.default_page_size)
        page = paginator.page(page_no)

        return paginator.num_pages, page.object_list

    def get_details(self, obj_id):
        pass
