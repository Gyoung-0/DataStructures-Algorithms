from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("UpdateParquetWithBrief") \
    .getOrCreate()

BASE_PARQUET_DIR = "s3a://gyoung0-test/ssg-parquet-output"
RAW_DATA_DIR = "s3a://gyoung0-test/ssg-raw-data"
jobs_to_process = [
    {
        'source_name': 'ssg_all_full',
        'brief_name': 'ssg_brief_full'
    },
    {
        'source_name': 'e_all_full',
        'brief_name': 'e_brief_full'
    }
]
KEY_COLUMN = "id"

for job_info in jobs_to_process:
    source_name = job_info['source_name']
    brief_name = job_info['brief_name']