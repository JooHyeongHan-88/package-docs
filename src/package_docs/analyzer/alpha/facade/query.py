import pandas as pd

from package_docs.analyzer.alpha.query.params import ChipQueryParams, MeasurementQueryParams
from package_docs.analyzer.alpha.query.chip import ChipQuery
from package_docs.analyzer.alpha.query.measure import MeasurementQuery


class QueryFacade:
    """Facade for accessing different query types."""

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
        """_summary_

        Args:
            limit (int, optional): _description_. Defaults to 100.
            offset (int, optional): _description_. Defaults to 0.
            chip_type (str, optional): _description_. Defaults to "default_chip".
            include_metadata (bool, optional): _description_. Defaults to True.

        Returns:
            pd.DataFrame: _description_
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
            limit (int, optional): _description_. Defaults to 100.
            offset (int, optional): _description_. Defaults to 0.
            measurement_type (str, optional): _description_. Defaults to "default_measurement".
            normalize (bool, optional): _description_. Defaults to False.

        Returns:
            pd.DataFrame: _description_
        """

        params = MeasurementQueryParams(
            limit=limit,
            offset=offset,
            measurement_type=measurement_type,
            normalize=normalize,
        )
        return self._get_measure.execute(params)    