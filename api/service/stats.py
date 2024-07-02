from webapp.models import GalaxyCatalogModel, GalaxyTaxonomyModel
from django.db.models import Count


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class StatisticsServiceImpl:

    def class_counts(self):
        code_mapping = {}
        codes = GalaxyTaxonomyModel.objects.all()
        for c in codes:
            code_mapping[c.id] = c.code

        output = {}
        counts = GalaxyCatalogModel.objects.all().order_by('taxanomy_id').values('taxanomy_id').annotate(count=Count("taxanomy_id"));
        for c in counts:
            output[code_mapping[c["taxanomy_id"]]] = c["count"]

        return output
