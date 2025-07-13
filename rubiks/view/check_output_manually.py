# EvoRube/rubiks/view/check_output_manually.py
import duckdb
import os

con = duckdb.connect()
parquet_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'runs.parquet')
con.sql(f"SELECT * FROM '{parquet_path}'").show()