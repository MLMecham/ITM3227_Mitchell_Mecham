# Cool docker commands

## Weather

This code manually makes the scheduler run a dag for a certain date. Just update it when needed and the processed_dates.txt ensures no duplicates.

docker exec -it itm3227_mitchell_mecham-airflow-scheduler-1 airflow backfill create --dag-id WEATHER_DAG_MECHAM_M --from-date 2026-05-03 --to-date 2026-05-09