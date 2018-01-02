from open990.xmlfiles import util
from open990.xmlfiles import normalize
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from argparse import Namespace
from pyspark.sql import SparkSession
from open990.util import arguments
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext


def _do_clean(original: str) -> str:
    """
    Validate and reformat an XML-based IRS Form 990x e-filing for downstream
    processing.

    :param original: string containing XML, in the original IRS format
    :return: string containing reformatted XML
    """
    cleaned = util.clean_xml(original)
    util.raise_on_empty(cleaned)
    return cleaned

udf_clean = udf(_do_clean, StringType())
udf_normalize = udf(normalize.normalize, StringType())

def do_preprocess(args: Namespace) -> None:
    tgt = args.target_column
    output_path = arguments.get_output_path(args)
    spark.read.parquet(*args.input) \
        .repartition(args.partitions) \
        .withColumn(tgt, udf_clean(tgt)) \
        .withColumn(tgt, udf_normalize(tgt)) \
        .write.parquet(output_path)
