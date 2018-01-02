find . -name "*.py" -print | zip dependencies.zip -@
PYSPARK_PYTHON=/usr/bin/python3 spark-submit --py-files dependencies.zip ./open990/preprocess_xml.py --input "s3://odl-990-long/2018-01-01/sample10/xml" --output "s3://odl-990-long/2018-01-01/reconstituted" --target-column "xml" --partitions 10
