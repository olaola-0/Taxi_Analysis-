from pathlib import Path
import os

# Get the parent directory of the current file (__file__)
PARENT_DIR = Path(__file__).parent.resolve().parent

# Define paths for data directories relative to the parent.
DATA_DIR = PARENT_DIR / 'data'
TRIP_DATA = PARENT_DIR / 'data' / 'trip_data'
SQL_DB_DIR = PARENT_DIR / 'data' / 'sqllite_db'
TAXI_ZONES_DIR = PARENT_DIR /'data' / 'taxi_zones'

if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path (TRIP_DATA).exists():
    os.mkdir(TRIP_DATA)

if not Path (SQL_DB_DIR).exists():
    os.mkdir(SQL_DB_DIR)

if not Path (TAXI_ZONES_DIR).exists():
    os.mkdir(TAXI_ZONES_DIR)