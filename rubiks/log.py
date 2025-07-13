"""Append-only Parquet writers for run-level and (optional) trace-level logs."""
from pathlib import Path
import pyarrow as pa, pyarrow.parquet as pq
from .schema import *
BASE_SCHEMA=pa.schema([(n, pa.type_for_alias(t)) for n,t in FIELDS])
# Fix: Combine BASE_SCHEMA fields with TRACE_EXTRA using field names and types
trace_fields = [(f.name, f.type) for f in BASE_SCHEMA] + [(n, pa.type_for_alias(t)) for n,t in TRACE_EXTRA]
TRACE_SCHEMA = pa.schema(trace_fields)

_run_writer = None
_trace_writer = None

def _get_writer(path, schema):
    global _run_writer, _trace_writer
    if path == PARQUET_PATH:
        if _run_writer is None:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            _run_writer = pq.ParquetWriter(path, schema, compression='zstd')
        return _run_writer
    else:
        if _trace_writer is None:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            _trace_writer = pq.ParquetWriter(path, schema, compression='zstd')
        return _trace_writer

def write_record(rec:dict):
    rec['schema_version']=SCHEMA_VERSION
    table=pa.Table.from_pydict({k:[rec.get(k)] for k,_ in FIELDS},schema=BASE_SCHEMA)
    _get_writer(PARQUET_PATH, BASE_SCHEMA).write_table(table)

def write_trace(t):
    t['schema_version']=SCHEMA_VERSION
    table=pa.Table.from_pydict({k:[t.get(k)] for k,_ in FIELDS+TRACE_EXTRA},schema=TRACE_SCHEMA)
    _get_writer(TRACE_PATH, TRACE_SCHEMA).write_table(table)