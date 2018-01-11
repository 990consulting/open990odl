from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from open990.util import arguments
from open990.xmlfiles.parse import flatten


description = """Rename a column in one or more parquet sources and emit to
specified output location."""

parser = arguments.base_parser(description)
parser = arguments.input_arg(parser)
parser.add_argument("--existing", action="store", help="Name of column to "
                    "change.", required=True)
parser.add_argument("--to", action="store", help="New name for column.",
                    required=True)

args = parser.parse_known_args()[0]

output_path = arguments.get_output_path(args)

spark = SparkSession.builder.getOrCreate()

left = spark.read.parquet(*args.left)
right = spark.read.parquet(*args.right)

spark.read.parquet(*args.input) \
    .withColumnRenamed(args.existing, args.to) \
    .write.parquet(output_path, mode="overwrite")
