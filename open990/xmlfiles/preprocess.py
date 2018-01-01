from open990.xmlfiles import util
from open990.xmlfiles import normalize
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from argparse import Namespace
from pyspark.sql import SparkSession
from open990.util import arguments
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext


def preprocess_xml(original: str) -> str:
    """
    Validate and reformat an XML-based IRS Form 990x e-filing for downstream
    processing.

    :param original: string containing XML, in the original IRS format
    :return: string containing reformatted XML
    """
    cleaned = util.clean_xml(original)
    util.raise_on_empty(cleaned)
    normalized = normalize.normalize(cleaned)
    return normalized

udf_preprocess = udf(preprocess_xml, StringType())

def do_preprocess(args: Namespace) -> None:
    tgt = args.target_column
    output_path = arguments.get_output_path(args)
    spark.read.parquet(*args.input) \
        .repartition(args.partitions) \
        .withColumn(tgt, udf_preprocess(tgt)) \
        .write.parquet(output_path)
