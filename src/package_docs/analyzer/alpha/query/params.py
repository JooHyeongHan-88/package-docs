from dataclasses import dataclass


@dataclass(kw_only=False)
class BaseQueryParams:
    """Base class for query parameters."""

    limit: int = 100
    offset: int = 0


@dataclass(kw_only=False)
class ChipQueryParams(BaseQueryParams):
    """Query parameters for chip analysis."""

    chip_type: str = "default_chip"
    include_metadata: bool = True


@dataclass(kw_only=False)
class MeasurementQueryParams(BaseQueryParams):
    """Query parameters for measurement analysis."""

    measurement_type: str = "default_measurement"
    normalize: bool = False
