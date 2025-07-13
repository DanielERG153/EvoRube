"""Parquet schema and version tag.  Trace rows reuse base fields + extras."""
SCHEMA_VERSION=1
PARQUET_PATH='data/runs.parquet'
TRACE_PATH='data/trace.parquet'
FIELDS=[
 ('schema_version','uint8'),('trial_id','string'),('timestamp','int64'),
 ('track','string'),('scramble_n','int16'),('agent','string'),
 ('fitness','string'),('agent_params','string'),('budget','int32'),
 ('steps_used','int32'),('solved','bool'),('best_score','int32'),
 ('best_state','binary')]
TRACE_EXTRA=[('step_idx','int32'),('score','int32'),('state','binary')]