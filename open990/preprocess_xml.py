from open990.util import arguments
from open990.xmlfiles import preprocess

description = """Starting with one or more parquet files containing filings, 
validate each filing and reformat it for downstream analysis. Returns a 
parquet file with the contents of the target column from the original parquet 
file(s) replaced. All input parquet files must be in the same format."""

if __name__ == "__main__":
    parser = arguments.base_parser(description)
    parser = arguments.input_arg(parser)
    parser = arguments.target_column(parser)
    args = parser.parse_known_args()[0]

    preprocess.do_preprocess(args)
