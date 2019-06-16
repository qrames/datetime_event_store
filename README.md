# datetime_event_store
Horodatage storage pakage

## install :

clone datetime_event_store in your project :
```bash
git clone http://github.com/qrames/datetime_event_store
```
On your Postgres database install and configure TimescaleDB
```bash
Your_db=# CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
ATTENTION:  
WELCOME TO
 _____ _                               _     ____________  
|_   _(_)                             | |    |  _  \ ___ \
  | |  _ _ __ ___   ___  ___  ___ __ _| | ___| | | | |_/ /
  | | | |  _ ` _ \ / _ \/ __|/ __/ _` | |/ _ \ | | | ___ \
  | | | | | | | | |  __/\__ \ (_| (_| | |  __/ |/ /| |_/ /
  |_| |_|_| |_| |_|\___||___/\___\__,_|_|\___|___/ \____/
               Running version 1.3.1
For more information on TimescaleDB, please visit the following links:

 1. Getting started: https://docs.timescale.com/getting-started
 2. API reference documentation: https://docs.timescale.com/api
 3. How TimescaleDB is designed: https://docs.timescale.com/introduction/architecture

Note: TimescaleDB collects anonymous reports to better understand and assist our users.
For more information and how to disable, please see our docs https://docs.timescaledb.com/using-timescaledb/telemetry.

CREATE EXTENSION
```

configure your database in db_config.json
```json
{
    "host":"localhost",
    "database": "your_database",
    "user": "your_username",
    "password": "your_password",
}

```


in your database create the table
```sql
CREATE TABLE events (
  time        TIMESTAMPTZ       NOT NULL,
  event        TEXT              NOT NULL
);
```
```sql
SELECT create_hypertable('events', 'time');
```
## Method store event
```python
class DatetimeEventStore :

    def store_event(*args, **kwargs):
        date = kwargs['at']
        data = kwargs['data']
        ...
```


## Method
```python get events
class DatetimeEventStore :

    def get_events(*args, **kwargs) :
        start = kwargs['start']
        end = kwargs['end']
        ...
        return enventsListe
```
