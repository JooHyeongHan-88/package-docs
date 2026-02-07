class Bucket:
    """
    S3 Bucket 모사 클래스.

    Attributes:
        name (str): bucket 이름.
        region (str): AWS 지역.
        creation_date (str): bucket 생성 날짜.
    """

    def __init__(self, name: str, region: str, creation_date: str):
        self.name = name
        self.region = region
        self.creation_date = creation_date

    def get_info(self) -> str:
        """
        bucket에 대한 정보 리턴.

        Returns:
            str: bucket에 대한 정보 string.
        """
        return f"Bucket Name: {self.name}, Region: {self.region}, Created On: {self.creation_date}"