import joblib
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import KBinsDiscretizer
from citizengalaxy.settings import STATICFILES_DIRS
from abc import ABC, abstractmethod


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class ClassifierModel(ABC):

    # default constructor
    def __init__(self):
        # initialize all data transformers
        # StandardScaler, KBinsDiscretizer
        def _initialize():
            # initializing data transformers
            trans_values = self._std_scaler.fit_transform(df[self._features])
            trans_df = pd.DataFrame(trans_values, columns=self._features)
            self._kbins.fit_transform(trans_df)

        # load models and CSV files
        data_path = str(STATICFILES_DIRS.__getitem__(0)) + "/data"
        # self._classifier = joblib.load(data_path + "/rf_model.joblib")
        self._min_max_df = pd.read_csv(data_path + "/feature_min_max.csv")
        df = pd.read_csv(data_path + "/categorized_preprocess.csv")

        # initialize data transformers
        self._std_scaler = preprocessing.StandardScaler()
        self._kbins = KBinsDiscretizer(n_bins=1000, encode='ordinal', strategy='uniform', subsample=None)

        self._features = []
        for i in range(self._min_max_df.shape[0]):
            self._features.append(self._min_max_df["feature"][i])

        _initialize()
        print("Feature min/max are loaded")

    # transforms user inputs to approximate ranges
    # each feature value is detected on the class ranges and they are approximated
    # if value is closer to either min/max value of a class (10% default) it's approximated to that value
    def _detect_adjust_border_values(self, data={}, border_cutoff_percent=10):
        # converting the keys to uppercase
        data = {k.upper(): data[k] for k in data}

        inx = 0
        # locate the row relavant for a give feature
        for col in self._features:
            # first detect the direction for the feature min = -1, max = 1
            adjusted_feature_value = data[col]

            tmp_df = self._min_max_df[self._min_max_df["feature"] == col]
            max_lookup = (tmp_df['max_order'][inx]).split()
            min_lookup = (tmp_df['min_order'][inx]).split()

            # collect first 2 applicable classes and check whether any outlier handling required
            applicable_class = []

            # detect the applicable range starting with smallest max value per class
            for class_max_col in max_lookup:
                cls = class_max_col.split("_")[0]
                if tmp_df[class_max_col][inx] > data[col] > tmp_df[(cls + "_min")][inx]:
                    applicable_class.append(cls)

                    if len(applicable_class) >= 2:
                        break

            # detecting whether the feature specific data point is moving towards the max|min direction from it's
            # range midpoint
            if len(applicable_class) > 0:
                cls_half_range_distance = (tmp_df[applicable_class[0] + "_max"][inx] -
                                           tmp_df[applicable_class[0] + "_min"][inx]) / 2
                cls_range_mid_point = tmp_df[applicable_class[0] + "_max"][inx] - cls_half_range_distance
                distance_from_middle = data[col] - cls_range_mid_point
                cutoff_distance = (100 - border_cutoff_percent) / 100 * cls_half_range_distance

                # towards max
                if distance_from_middle > 0:
                    cut_off_point = cls_range_mid_point + cutoff_distance
                    # is it nearing the max value
                    if data[col] > cut_off_point:
                        print(col, "more than max cutoff")
                        adjusted_feature_value = tmp_df[applicable_class[0] + "_max"][inx]

                else:  # towards min
                    cut_off_point = cls_range_mid_point - cutoff_distance
                    # is it nearing the min value
                    if data[col] < cut_off_point:
                        print(col, "less than min cutoff")
                        adjusted_feature_value = tmp_df[applicable_class[0] + "_min"][inx]

            # detecting whether the datapoint of a feature is beyond the highest max class of a feature
            if len(applicable_class) == 0 and data[col] > tmp_df[max_lookup[-1]][inx]:
                adjusted_feature_value = tmp_df[max_lookup[-1]][inx]
                print(col, "max outlier")

            # detecting whether the datapoint of a feature is beyond the lowest min class of a feature
            if len(applicable_class) == 0 and data[col] < tmp_df[min_lookup[-1]][inx]:
                adjusted_feature_value = tmp_df[min_lookup[-1]][inx]
                print(col, "min outlier")

            data[col] = adjusted_feature_value
            inx += 1

        return data

    # abstract method to be implemented in the child classes
    @abstractmethod
    def predict_galaxy_class(self, data={}):
        pass


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class RandomForestClassifierImpl(ClassifierModel):

    # default constructor
    def __init__(self):
        super().__init__()

        data_path = str(STATICFILES_DIRS.__getitem__(0)) + "/data"
        self._classifier = joblib.load(data_path + "/rf_model.joblib")

    # does the class prediction for a galaxy based on user inputs
    def predict_galaxy_class(self, data={}):
        data_to_predict = [self._detect_adjust_border_values(data)]
        data_to_predict = self._std_scaler.transform(pd.DataFrame(data_to_predict))
        data_to_predict = pd.DataFrame(data=data_to_predict, columns=self._features)

        data_to_predict = pd.DataFrame(data=self._kbins.transform(data_to_predict), columns=self._features)
        predictions = self._classifier.predict(data_to_predict)

        print("Predicted with Random Forest")
        return predictions[0]


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
# A sample alternate classifier for Neural Network
class NeuralNetworkClassifierImpl(ClassifierModel):

    # default constructor
    def __init__(self):
        super().__init__()

        data_path = str(STATICFILES_DIRS.__getitem__(0)) + "/data"
        self._classifier = joblib.load(data_path + "/rf_model.joblib")

    # does the class prediction for a galaxy based on user inputs
    def predict_galaxy_class(self, data={}):
        data_to_predict = [self._detect_adjust_border_values(data)]
        data_to_predict = self._std_scaler.transform(pd.DataFrame(data_to_predict))
        data_to_predict = pd.DataFrame(data=data_to_predict, columns=self._features)

        data_to_predict = pd.DataFrame(data=self._kbins.transform(data_to_predict), columns=self._features)
        predictions = self._classifier.predict(data_to_predict)

        print("Predicted with Neural Network")
        return predictions[0]


# @author Sujith T
# Factory to maintain models singleton
# Deus et Scientia Erit Pactum Meum 2024
class ClassifierFactory:
    # class variable only accessible within the class
    _clazz_dict = {}

    @classmethod
    def fetch_classifier(cls, model_name='random_forest'):

        if model_name not in cls._clazz_dict.keys():
            classifier = None

            if model_name == "random_forest":
                classifier = RandomForestClassifierImpl()

            if model_name == "neural_network":
                classifier = NeuralNetworkClassifierImpl()

            cls._clazz_dict[model_name] = classifier

        return cls._clazz_dict[model_name]
