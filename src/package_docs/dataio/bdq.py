import pandas as pd


def bigdataquery(val: int) -> pd.DataFrame:
    """Bigdataquery API 모사 함수.

    Args:
        val (int): 아무 integer.

    Returns:
        pd.DataFrame: `val` 값을 넣은 테이블 데이터.

    Example:
        ```python
        import package_docs as pack

        df = bigdataquery(10)
        ```
    """
    return pd.DataFrame({'value': [val]})
