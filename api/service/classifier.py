from citizengalaxy.settings import STATICFILES_DIRS

import joblib
import pandas as pd


# @author Sujith T
class GalaxyClassClassifier:

    def __init__(self):
        dir_path = "/galaxy_classification/dataset"
        model_path = dir_path + "/rf_model.joblib"
        self._classifier = joblib.load(model_path)
        self._min_max_df = pd.read_csv(dir_path + "/feature_min_max.csv")
        self._features = []
        for i in range(self._min_max_df.shape[0]):
            self._features.append(self._min_max_df["feature"][i])

        print("Model and feature min/max are loaded")

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

    def predict_galaxy_class(self, data={}):
        data = self._detect_adjust_border_values(data)
        # return self._classifier.predict(features)
