from open990.util import arguments

description = """Transform all XML files from target column in target parquet 
file(s) into key-value pairs. Emits a new parquet file containing these 
simplified key-value pairs."""

parser = arguments.base_parser(description, use_input=True)
args = parser.parse_known_args()[0]


