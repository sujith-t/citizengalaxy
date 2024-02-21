from citizengalaxy.settings import STATICFILES_DIRS
#from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
from sklearn.impute import KNNImputer

# @author Sujith T
class GalaxyClassClassifier:

    def __init__(self):
        dir_path = "/galaxy_classification/dataset"
        model_path = dir_path + "/rf_model.joblib"
        self._classifier = joblib.load(model_path)
        self._df = pd.read_csv(dir_path + "/categorized.csv")
        print("Model and csv data loaded")

        self._replace_missing_values()
        print("Missing values are imputed for csv data")

        self._adjust_outliers_by_groups()
        print("Outliers are adjusted for csv data")

    def _replace_missing_values(self):
        imputer = KNNImputer(n_neighbors=5)
        columns_for_knn_impute = ["PETROMAG_MU"]
        imputed_data = imputer.fit_transform(self._df[columns_for_knn_impute])
        tmp_df = pd.DataFrame(imputed_data, columns=columns_for_knn_impute)

        self._df["PETROMAG_MU"] = tmp_df["PETROMAG_MU"]

    def _adjust_outliers_by_groups(self):
        omit_columns = ["OBJ_ID", "REGION", "code"]
        distinct = set(self._df["code"].unique())

        for v in distinct:
            tmp_df = self._df[self._df["code"] == v]
            tmp_df = tmp_df.drop(columns=omit_columns)
            q1 = tmp_df.quantile(0.25)
            q3 = tmp_df.quantile(0.75)
            irq = q3 - q1
            lower_limit = q1 - (1.5 * irq)
            upper_limit = q3 + (1.5 * irq)

            # adjust the outlier value for each column
            for col in tmp_df.columns:
                tmp_df.loc[tmp_df[col] < lower_limit[col], col] = lower_limit[col]
                tmp_df.loc[tmp_df[col] > upper_limit[col], col] = upper_limit[col]
                self._df.loc[tmp_df.index, col] = tmp_df[col]
    def predict_galaxy_class(self, features = []):
        return self._classifier.predict(features)