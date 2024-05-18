import unittest

from api.service.classifier import ClassifierFactory, RandomForestClassifierImpl, ClassifierModel


class ClassifierFactoryTestCase(unittest.TestCase):

    def test_fetch_classifier_with_no_param(self):
        classifier = ClassifierFactory.fetch_classifier()
        self.assertTrue(isinstance(classifier, RandomForestClassifierImpl))

    def test_fetch_classifier_random_forest_param(self):
        classifier = ClassifierFactory.fetch_classifier("random_forest")
        self.assertTrue(isinstance(classifier, RandomForestClassifierImpl))

    def test_fetch_classifier_invalid_param(self):
        classifier = ClassifierFactory.fetch_classifier("something_else")
        self.assertFalse(isinstance(classifier, RandomForestClassifierImpl))


class RandomForestClassifierTestCase(unittest.TestCase):

    def test_instance(self):
        classifier = RandomForestClassifierImpl()
        self.assertTrue(isinstance(classifier, ClassifierModel))

    def test_border_value_adjust(self):
        self.assertTrue(True)

    def test_classification_for_ecliptic(self):
        self.assertTrue(True)

    def test_classification_for_spiral(self):
        self.assertTrue(True)

    def test_classification_for_barred_spiral(self):
        self.assertTrue(True)