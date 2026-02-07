import pandas as pd

from package_docs.analyzer.alpha.query.base import BaseQuery
from package_docs.analyzer.alpha.query.params import MeasurementQueryParams


class MeasurementQuery(BaseQuery):
    """Concrete implementation of a measurement query."""

    def __init__(self):
        super().__init__(name="MeasurementQuery")

    def execute(self, params: MeasurementQueryParams) -> pd.DataFrame:
        """Execute the measurement query with the given parameters."""
        # Placeholder implementation for demonstration purposes
        data = {
            "measurement_type": [params.measurement_type] * params.limit,
            "value": range(params.offset, params.offset + params.limit),
            "normalized": [params.normalize] * params.limit,
        }
        return pd.DataFrame(data)
