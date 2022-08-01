from dlt.common.configuration import BaseConfiguration


class NormalizeVolumeConfiguration(BaseConfiguration):
    NORMALIZE_VOLUME_PATH: str = "_storage/normalize"  # path to volume where normalized loader files will be stored


class ProductionNormalizeVolumeConfiguration(NormalizeVolumeConfiguration):
    NORMALIZE_VOLUME_PATH: str = None
