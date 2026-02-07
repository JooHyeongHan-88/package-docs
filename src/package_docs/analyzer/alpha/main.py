from package_docs.analyzer.alpha.facade.analysis import AnalysisFacade
from package_docs.analyzer.alpha.facade.query import QueryFacade


class Alapha:
    """Alpha 분석 객체.

    분석(`analysis`)과 조회(`query`) 기능을 하나의 인터페이스로 사용.
    """

    analysis: AnalysisFacade
    """분석 관련 기능을 제공."""

    query: QueryFacade
    """데이터 조회 기능 제공."""

    def __init__(self):
        self.analysis = AnalysisFacade()
        self.query = QueryFacade()
