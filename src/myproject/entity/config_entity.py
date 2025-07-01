from dataclasses import dataclass
from pathlib import Path

dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str
    unzip_dir: str