from dataclasses import dataclass
from typing import Literal

import pandas as pd


@dataclass(kw_only=False)
class BaseAnalysisParams:
    """Base parameters for analysis."""

    name: str
    interval: float
    threshold: int
    data: pd.DataFrame


@dataclass(kw_only=False)
class CorrelationAnalysisParams(BaseAnalysisParams):
    """Parameters for correlation analysis."""

    method: Literal["pearson", "spearman", "kendall"] = "pearson"
    normalize: bool = False


@dataclass(kw_only=False)
class DistributionAnalysisParams(BaseAnalysisParams):
    """Parameters for distribution analysis."""

    bins: int = 10
    range: tuple[float, float] | None = None
    cumulative: bool = False
    normalize: bool = False
