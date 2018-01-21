from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from open990.util import arguments
from open990.xmlfiles.parse import flatten


description = """Convert one or more CSV files to parquet."""

parser = arguments.base_parser(description)
parser = arguments.input_arg(parser)

args = parser.parse_known_args()[0]

output_path = arguments.get_output_path(args)

spark = SparkSession.builder.getOrCreate()

spark.read.parquet(*args.input) \
    .write.parquet(output_path, mode="overwrite")
