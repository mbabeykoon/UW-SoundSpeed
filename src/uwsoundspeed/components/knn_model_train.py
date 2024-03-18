import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
import os
import shutil
import zipfile
from uwsoundspeed import logger
from uwsoundspeed.utils.common import get_size, load_from_pkl
from uwsoundspeed.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PreprocessingConfig)

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib


class KnnModelTrain:

    def __init__(self, config_manager):
        self.config_manager = config_manager  # Correct initialization
        self.config = self.config_manager.get_prepare_base_model_config()
        self.data = None
        self.preprocessor = None
        self.best_model = None   
        
    def load_data(self):
        base_model_config = self.config_manager.get_prepare_base_model_config()
        self.data = pd.read_pickle(base_model_config.data_file_path)
        logger.info(f"Data loaded successfully from {base_model_config.data_file_path}.")

    def prepare_pipeline(self):
        prep_config = self.config_manager.get_preprocessing_config()
        pca_config = self.config_manager.get_pca_config()
        model_config = self.config_manager.get_model_config().KNeighborsRegressor  


        # Numerical features pipeline
        numerical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy=prep_config.numerical_transformer['imputer_strategy'])),
            ('scaler', StandardScaler())
        ])

        # Categorical features pipeline
        categorical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy=prep_config.categorical_transformer['imputer_strategy'])),
            ('onehot', OneHotEncoder(handle_unknown=prep_config.categorical_transformer['handle_unknown']))
        ])

        # Combined preprocessing pipeline
        preprocessor = ColumnTransformer(transformers=[
            ('num', numerical_pipeline, prep_config.numerical_features),
            ('cat', categorical_pipeline, prep_config.categorical_features)
        ])

        # Full pipeline with PCA and KNeighborsRegressor placeholder
        self.pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('pca', PCA(n_components=pca_config.n_components)),
        ('knn', KNeighborsRegressor(n_neighbors=model_config['n_neighbors'][0]))  
        ])


        
    def train_test_split(self):
    # Retrieve train-test split configuration using the config_manager
        split_config = self.config_manager.get_train_test_split_config()
        X = self.data.drop('c', axis=1)  # Make sure 'target_column' matches your actual target column name
        y = self.data['c']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=split_config.test_size, random_state=split_config.random_state
        )
        logger.info("Train-test split completed.")


    def train_and_evaluate(self):

        model_config = self.config_manager.get_model_config().KNeighborsRegressor
        grid_search_config = self.config_manager.get_grid_search_config()

  
        
        grid_search = GridSearchCV(
            self.pipeline,
            param_grid={'knn__n_neighbors': model_config['n_neighbors']},
            cv=grid_search_config.cv,
            scoring=grid_search_config.scoring,
            verbose=1
        )

        grid_search.fit(self.X_train, self.y_train)
        self.best_model = grid_search.best_estimator_

        y_pred = self.best_model.predict(self.X_test)
        logger.info(f"R^2: {r2_score(self.y_test, y_pred)}")
        logger.info(f"RMSE: {mean_squared_error(self.y_test, y_pred, squared=False)}")

    def save_model(self):
        knn_model_path = self.config_manager.get_prepare_base_model_config().knn_model_path
        joblib.dump(self.best_model, knn_model_path)
        logger.info(f"Best KNN model saved to {knn_model_path}")



