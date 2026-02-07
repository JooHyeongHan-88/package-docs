from abc import ABC, abstractmethod

import pandas as pd

from package_docs.analyzer.alpha.query.params import BaseQueryParams


class BaseQuery(ABC):
    """Abstract base class for queries."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, params: BaseQueryParams) -> pd.DataFrame:
        """Execute the query with the given parameters and return results as a DataFrame."""
        raise NotImplementedError
