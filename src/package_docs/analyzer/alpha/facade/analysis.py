from typing import Literal

import pandas as pd

from package_docs.analyzer.alpha.analysis.params import CorrelationAnalysisParams, DistributionAnalysisParams
from package_docs.analyzer.alpha.analysis.correlation import CorrelationAnalysis
from package_docs.analyzer.alpha.analysis.distribution import DistributionAnalysis


class AnalysisFacade:
    """Facade for accessing different analysis types."""

    def __init__(self):
        self._correlation_analysis = CorrelationAnalysis()
        self._distribution_analysis = DistributionAnalysis()


    def analyze_correlation(
            self,
            data: pd.DataFrame,
            method: Literal["pearson", "spearman", "kendall"] = "pearson",
            threshold: float = 0.5,
        ) -> pd.DataFrame:
        """_summary_

        Args:
            data (pd.DataFrame): _description_.
            method (Literal["pearson", "spearman", "kendall"], optional): _description_. Defaults to "pearson".
            threshold (float, optional): _description_. Defaults to 0.5.

        Returns:
            pd.DataFrame: _description_
        """

        params = CorrelationAnalysisParams(
            name="correlation_analysis",
            interval=1.0,
            data=data,
            method=method,
            threshold=threshold,
        )
        return self._correlation_analysis.run(params)


    def analyze_distribution(
            self,
            data: pd.DataFrame,
            bins: int = 10,
            normalize: bool = False,
        ) -> pd.DataFrame:
        """_summary_

        Args:
            data (pd.DataFrame): _description_.
            bins (int, optional): _description_. Defaults to 10.
            normalize (bool, optional): _description_. Defaults to False.

        Returns:
            pd.DataFrame: _description_
        """

        params = DistributionAnalysisParams(
            name="distribution_analysis",
            interval=2.0,
            data=data,
            bins=bins,
            cumulative=False,
            normalize=normalize,
            threshold=0,
        )
        return self._distribution_analysis.run(params)