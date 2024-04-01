from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import joblib
import os
from uwsoundspeed.entity.config_entity import DataPreprocessingConfig

class DataPreprocessor:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config
        self.column_transformer = self._create_column_transformer()
        self.pca = PCA(n_components=config.pca_n_components)

    def _create_column_transformer(self):
        # Setup the numerical transformer pipeline
        numerical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        categorical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])

        # Combine into a ColumnTransformer
        return ColumnTransformer(transformers=[
            ('num', numerical_pipeline, self.config.numerical_features),
            ('cat', categorical_pipeline, self.config.categorical_features),
        ])

    def preprocess_and_apply_pca(self):
        # Read data
        df = pd.read_pickle(self.config.data_path)

        # Fit and transform the data with the pre-defined column transformer
        X_transformed = self.column_transformer.fit_transform(df)

        # Apply PCA with the pre-initialized PCA instance
        X_pca = self.pca.fit_transform(X_transformed)

        return X_pca

    def save(self, subdir_name="preprocessor"):
        """Saves the preprocessor and PCA components to the specified directory."""
        save_dir = os.path.join(self.config.root_dir, subdir_name)
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, "preprocessor_and_pca.joblib")
        joblib.dump({'column_transformer': self.column_transformer, 'pca': self.pca}, save_path)
