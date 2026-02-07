def _load() -> None:
    """load 보조 함수"""
    pass


def load() -> int:
    """local 함수

    load 함수는 임의로 숫자 42를 반환합니다.

    Returns:
        int: 임의로 출력되는 숫자 42.

    Example:
        별칭으로 부르기:
        ```python
        import package_docs as pack

        num = pack.dataio.load()
        ```

        함수 직접 부르기:
        ```python
        from package_docs.dataio.local import load
        
        num = load()
        ```
    """
    _load()
    return 42