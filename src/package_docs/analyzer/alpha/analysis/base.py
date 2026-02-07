from abc import ABC, abstractmethod

import pandas as pd

from package_docs.analyzer.alpha.analysis.params import BaseAnalysisParams


class BaseAnalysis(ABC):
    """Abstract base class for analyses."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, params: BaseAnalysisParams) -> pd.DataFrame:
        """Run the analysis with the given parameters and return results as a DataFrame."""
        raise NotImplementedError
