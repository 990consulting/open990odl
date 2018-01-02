from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import datetime
from open990.util import arguments
from open990.xmlfiles.parse import flatten
import time
import io


description = """Transforms XML into a list of key-value pairs, with the keys
consisting of Xpaths and the values consisting of the text from each element.
Assumes that the XML has already been preprocessed by converting attributes to
elements, removing namespaces, and converting from Unicode to ASCII."""

parser = arguments.base_parser(description)
parser = arguments.input_arg(parser)
parser.add_argument("--xml-column", action="store",
        help="Column in source file(s) containing preprocessed XML.", default="xml")
parser.add_argument("--xpath-column", action="store",
        help="Column in which to store xpath.", default = "xpath")
parser.add_argument("--value-column", action="store",
        help="Column in which to store value.", default = "value")

parser = arguments.target_column(parser)
args = parser.parse_known_args()[0]

output_path = arguments.get_output_path(args)

spark = SparkSession.builder.getOrCreate()

schema = ArrayType(
        StructType([
            StructField("xpath", StringType(), False),
            StructField("value", StringType(), False)
        ]))

udf_parse = udf(flatten, schema)

spark.read.parquet(*args.input) \
    .repartition(args.partitions) \
    .withColumn("dummy", udf_parse(args.xml_column)) \
    .withColumn("dummy", explode(col("dummy"))) \
    .withColumn(args.xpath_column, col("dummy.xpath")) \
    .withColumn(args.value_column, col("dummy.value")) \
    .drop("dummy") \
    .write.parquet(output_path, mode="overwrite")
