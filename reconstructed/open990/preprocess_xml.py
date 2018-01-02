from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from datetime import datetime
from open990.util import arguments
from open990.xmlfiles.util import clean_xml
from open990.xmlfiles.normalize import normalize
import time
import io

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

udf_clean = udf(clean_xml, StringType())
udf_normalize = udf(normalize, StringType())

description = ""
parser = arguments.base_parser(description)
parser = arguments.input_arg(parser)
parser = arguments.target_column(parser)
args = parser.parse_known_args()[0]

tgt = args.target_column
output_path = arguments.get_output_path(args)

spark.read.parquet(*args.input) \
    .repartition(args.partitions) \
    .withColumn(tgt, udf_clean(tgt)) \
    .withColumn(tgt, udf_normalize(tgt)) \
    .write.parquet(output_path, mode="overwrite")
