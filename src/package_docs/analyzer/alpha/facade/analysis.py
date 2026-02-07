from typing import Literal

import pandas as pd

from package_docs.analyzer.alpha.analysis.params import (
    CorrelationAnalysisParams,
    DistributionAnalysisParams,
)
from package_docs.analyzer.alpha.analysis.correlation import CorrelationAnalysis
from package_docs.analyzer.alpha.analysis.distribution import DistributionAnalysis


class AnalysisFacade:
    """Alpha 객체 분석 파사드로 여러 분석 메소드 제공."""

    def __init__(self):
        self._correlation_analysis = CorrelationAnalysis()
        self._distribution_analysis = DistributionAnalysis()

    def analyze_correlation(
        self,
        data: pd.DataFrame,
        method: Literal["pearson", "spearman", "kendall"] = "pearson",
        threshold: float = 0.5,
    ) -> pd.DataFrame:
        """상관 분석 수행.

        Args:
            data (pd.DataFrame): 분석 대상 데이터 테이블.
            method (Literal["pearson", "spearman", "kendall"], optional): 상관 분석 메소드. Defaults to "pearson".
            threshold (float, optional): 통계적 유의수준. Defaults to 0.5.

        Returns:
            pd.DataFrame: 상관 분석 결과 테이블.
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
        """분포 분석 수행.

        Args:
            data (pd.DataFrame): 분석 대상 데이터 테이블.
            bins (int, optional): 데이터 분할 단위. Defaults to 10.
            normalize (bool, optional): 정규화 수행 여부. Defaults to False.

        Returns:
            pd.DataFrame: 분포 분석 결과 테이블.
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
