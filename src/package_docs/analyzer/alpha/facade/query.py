import pandas as pd

from package_docs.analyzer.alpha.query.params import (
    ChipQueryParams,
    MeasurementQueryParams,
)
from package_docs.analyzer.alpha.query.chip import ChipQuery
from package_docs.analyzer.alpha.query.measure import MeasurementQuery


class QueryFacade:
    """Alpha 객체 데이터 쿼리 파사드로 여러 테이블 읽기 API 제공."""

    def __init__(self):
        self._get_chip = ChipQuery()
        self._get_measure = MeasurementQuery()

    def get_chip(
        self,
        limit: int = 100,
        offset: int = 0,
        chip_type: str = "default_chip",
        include_metadata: bool = True,
    ) -> pd.DataFrame:
        """chip 데이터 쿼리 수행.

        Args:
            limit (int, optional): 쿼리 데이터 제한량. Defaults to 100.
            offset (int, optional): 쿼리 데이터 offset. Defaults to 0.
            chip_type (str, optional): chip 타입. Defaults to "default_chip".
            include_metadata (bool, optional): 메타 데이터 포함 여부. Defaults to True.

        Returns:
            pd.DataFrame: 쿼리된 chip 데이터 테이블.
        """

        params = ChipQueryParams(
            limit=limit,
            offset=offset,
            chip_type=chip_type,
            include_metadata=include_metadata,
        )
        return self._get_chip.execute(params)

    def get_measure(
        self,
        limit: int = 100,
        offset: int = 0,
        measurement_type: str = "default_measurement",
        normalize: bool = False,
    ) -> pd.DataFrame:
        """_summary_

        Args:
            limit (int, optional): 쿼리 데이터 제한량. Defaults to 100.
            offset (int, optional): 쿼리 데이터 offset. Defaults to 0.
            measurement_type (str, optional): 측정 방식 타입. Defaults to "default_measurement".
            normalize (bool, optional): 정규화 여부. Defaults to False.

        Returns:
            pd.DataFrame: 쿼리된 측정 데이터 테이블.
        """

        params = MeasurementQueryParams(
            limit=limit,
            offset=offset,
            measurement_type=measurement_type,
            normalize=normalize,
        )
        return self._get_measure.execute(params)
