from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from open990.util import arguments
from open990.xmlfiles.parse import flatten


description = """General purpose left-join merge. Specify left and right 
source files and join column. Writes result to specified output location. """

parser = arguments.base_parser(description)
parser.add_argument("--left", action="append",
                    help="Path to left table input parquet file(s). Can "
                         "supply multiple.", required=True)
parser.add_argument("--right", action="append",
                    help="Path to right table input parquet file(s). Can "
                         "supply multiple.", required=True)
parser.add_argument("--by", action="store", help="Column on which to join.",
                    required = True)


args = parser.parse_known_args()[0]

output_path = arguments.get_output_path(args)

spark = SparkSession.builder.getOrCreate()

left = spark.read.parquet(*args.left)
right = spark.read.parquet(*args.right)

left.join(right, args.by) \
    .write.parquet(output_path, mode="overwrite")
