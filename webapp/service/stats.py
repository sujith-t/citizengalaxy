from webapp.models import GalaxyCatalogModel, GalaxyTaxonomyModel
from django.db.models import Count
from django.db import connection


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class StatisticalServiceImpl:

    def class_counts(self):
        code_mapping = {}
        codes = GalaxyTaxonomyModel.objects.all()
        for c in codes:
            code_mapping[c.id] = c.code

        output = {}
        counts = GalaxyCatalogModel.objects.all().order_by('taxanomy_id').values('taxanomy_id').annotate(
            count=Count("taxanomy_id"));
        for c in counts:
            output[code_mapping[c["taxanomy_id"]]] = c["count"]

        return output

    def htf_sequence(self):
        return GalaxyTaxonomyModel.objects.exclude(parent_id=None)

    def feature_values(self, param: dict):
        output = {}
        if "class" not in param.keys() or "features" not in param.keys() or len(param['features']) == 0:
            return

        taxonomy = GalaxyTaxonomyModel.objects.filter(code=param["class"]).first()
        features = param["features"]
        columns = (",".join(features)).lower()
        with connection.cursor() as cursor:
            q = ("SELECT %s FROM galaxy_catalog AS gc JOIN sdss_meta AS sm "
                 + "ON gc.obj_id = sm.obj_id WHERE gc.taxanomy_id = %s") % (columns, taxonomy.id)
            cursor.execute(q)
            results = cursor.fetchall()
            output['total'] = len(results)

            for r in results:
                for i in range(0, len(features)):
                    if features[i] not in output.keys():
                        output[features[i]] = []

                    output[features[i]].append(r[i])

            cursor.close()

        return output

    def class_values(self, param: dict):
        output = {}
        if "classes" not in param.keys() or "feature" not in param.keys() or len(param['classes']) == 0:
            return

        taxonomies = GalaxyTaxonomyModel.objects.filter(code__in=param["classes"])
        classes = {str(t.id) : t.code for t in taxonomies}

        with (connection.cursor() as cursor):
            q = ("SELECT gc.taxanomy_id, %s FROM galaxy_catalog AS gc JOIN sdss_meta AS sm "
                 + "ON gc.obj_id = sm.obj_id WHERE gc.taxanomy_id IN (%s)") % (param['feature'], ",".join(classes))

            cursor.execute(q)
            results = cursor.fetchall()

            for r in results:
                clazz = classes[str(r[0])]
                if clazz not in output.keys():
                    output[clazz] = []

                output[clazz].append(r[1])

            cursor.close()

        counts_list = [len(output[x]) for x in output]
        max_limit = max(counts_list)

        output['label_count'] = max_limit

        return output
