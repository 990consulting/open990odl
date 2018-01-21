#!/bin/sh
echo "*** Current directory ***"
pwd
echo "*** Contents of directory ***"
ls -l
echo "*** Changing to open990 ***"
cd open990
echo "*** Contents of directory ***"
ls -l
echo "*** Creating zip file ***"
find . -name "*.py" -print | zip dependencies.zip -@ || exit 1
echo "*** Contents of directory ***"
ls -l
echo "*** Running spark ***"
PYSPARK_PYTHON=/usr/bin/python3 spark-submit --py-files dependencies.zip ./open990/merge.py $@
