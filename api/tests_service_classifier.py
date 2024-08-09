import unittest

from api.serializers import ClassifySerializer
from api.service.classifier import ClassifierFactory, RandomForestClassifierImpl, ClassifierModel
from webapp.service.search import GalaxyLocatorServiceImpl


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class ClassifierFactoryTestCase(unittest.TestCase):

    # fetching default classifier based on settings (RandomForest is default)
    def test_fetch_classifier_with_no_param(self):
        classifier = ClassifierFactory.fetch_classifier()
        self.assertTrue(isinstance(classifier, RandomForestClassifierImpl))

    # fetching Random Forest classifier by parameter
    def test_fetch_classifier_random_forest_param(self):
        classifier = ClassifierFactory.fetch_classifier("random_forest")
        self.assertTrue(isinstance(classifier, RandomForestClassifierImpl))

    # check whether nothing returned when invalid parameter is passed
    def test_fetch_classifier_invalid_param(self):
        classifier = ClassifierFactory.fetch_classifier("something_else")
        self.assertFalse(isinstance(classifier, ClassifierModel))


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class RandomForestClassifierTestCase(unittest.TestCase):

    # test on the instance whether it's getting created properly
    def test_instance(self):
        classifier = RandomForestClassifierImpl()
        self.assertTrue(isinstance(classifier, ClassifierModel))

    # private function to retrieve objects for classification
    def _get_object(self, id):
        locator = GalaxyLocatorServiceImpl()
        search_param = {"search_value": id, "search_option": "obj_id"}
        galaxy_json = locator.get_details(search_param, True)
        del galaxy_json["declination"]
        del galaxy_json["dec_string"]
        del galaxy_json["iauname"]
        del galaxy_json["obj_class"]
        del galaxy_json["obj_id"]
        del galaxy_json["ra"]
        del galaxy_json["ra_string"]
        del galaxy_json["taxonomy_code"]

        return galaxy_json

    # test whether the input auto adjusts outliers
    def test_border_value_adjust(self):
        galaxy_json = self._get_object("587722982834504179")
        classifier = RandomForestClassifierImpl()
        adjusted_data = classifier._detect_adjust_border_values(galaxy_json)

        self.assertNotEquals(galaxy_json["rowc_u"], adjusted_data["ROWC_U"])
        self.assertEquals(1426.758, adjusted_data["ROWC_U"])

    # test whether the ML model can detects ecliptic types
    def test_classification_for_ecliptic(self):
        galaxy_json = self._get_object("587722982834504179")

        classifier = RandomForestClassifierImpl()
        serializer = ClassifySerializer(data=galaxy_json)
        clazz = "some"
        if serializer.is_valid():
            clazz = classifier.predict_galaxy_class(serializer.data)

        self.assertEquals("Ei", clazz)

    # check whether the ML model can detect spiral types
    def test_classification_for_spiral(self):
        galaxy_json = self._get_object("587722981741363323")

        classifier = RandomForestClassifierImpl()
        serializer = ClassifySerializer(data=galaxy_json)
        clazz = "some"
        if serializer.is_valid():
            clazz = classifier.predict_galaxy_class(serializer.data)

        self.assertEquals("Sc", clazz)

    # test whether the model can predict barred-spiral types
    def test_classification_for_barred_spiral(self):
        galaxy_json = self._get_object("587722981744509013")

        classifier = RandomForestClassifierImpl()
        serializer = ClassifySerializer(data=galaxy_json)
        clazz = "some"
        if serializer.is_valid():
            clazz = classifier.predict_galaxy_class(serializer.data)

        self.assertEquals("SBc", clazz)
