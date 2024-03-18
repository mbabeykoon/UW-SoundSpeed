from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from typing import List, Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PreprocessingConfig:
    numerical_features: List[str]
    numerical_transformer: Dict[str, any]
    categorical_features: List[str]
    categorical_transformer: Dict[str, any]


@dataclass(frozen=True)
class PrepareDataConfig:
    root_dir: Path
    data_file_path: Path
    preprocessing: PreprocessingConfig

@dataclass(frozen=True)
class PCAConfig:
    n_components: float

@dataclass(frozen=True)
class ModelConfig:
    KNeighborsRegressor: Dict[str, List[int]]

@dataclass(frozen=True)
class GridSearchConfig:
    cv: int
    scoring: str

@dataclass(frozen=True)
class TrainTestSplitConfig:
    test_size: float
    random_state: int


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    data_file_path: Path
    preprocessing: PreprocessingConfig
    pca: PCAConfig
    model: ModelConfig
    grid_search: GridSearchConfig
    train_test_split: TrainTestSplitConfig
    knn_model_path: Path