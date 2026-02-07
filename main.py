import package_docs as pack


def main():
    # ====================================
    # core
    # ====================================
    # logger
    logger = pack.get_logger("test_logger")
    logger.info("Logger is working!")

    # bucket
    bucket = pack.Bucket(
        name="my-bucket",
        region="Korea",
        creation_date="2024-01-01",
    )
    logger.info(bucket.get_info())

    # ====================================
    # dataio
    # ====================================
    # load
    num = pack.dataio.load()
    logger.info(f"load function returned: {num}")

    # bigdataquery
    bdq = pack.dataio.bigdataquery(val=num)
    logger.info(f"BigDataQuery function returned DataFrame with shape: {bdq.shape}")

    # ====================================
    # analyzer
    # ====================================
    alpha = pack.analyzer.alpha.Alapha()

    # query
    chip = alpha.query.get_chip(
        limit=100,
        offset=10,
        chip_type="satellite",
        include_metadata=True,
    )

    measure = alpha.query.get_measure(
        limit=50,
        offset=5,
        measurement_type="default_measurement",
        normalize=True,
    )

    logger.info(f"Chip DataFrame shape: {chip.shape}")
    logger.info(f"Measurement DataFrame shape: {measure.shape}")

    # analysis
    correlation = alpha.analysis.analyze_correlation(
        data=chip,
        method="pearson",
        threshold=0.5,
    )

    distribution = alpha.analysis.analyze_distribution(
        data=measure,
        bins=10,
        normalize=False,
    )

    logger.info(f"Correlation Analysis result shape: {correlation.shape}")
    logger.info(f"Distribution Analysis result shape: {distribution.shape}")


if __name__ == "__main__":
    main()
