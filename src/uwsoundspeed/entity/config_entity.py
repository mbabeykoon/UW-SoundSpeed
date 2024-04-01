from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict,Any

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    data_path: Path
    numerical_features: List[str]
    # numerical_transformer: Dict[str, Any]
    categorical_features: List[str]
    # categorical_transformer: Dict[str, Any]
    pca_n_components: float