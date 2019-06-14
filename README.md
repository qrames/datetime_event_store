# datetime_event_store
Horodatage storage pakage


## Method store event
```python
class DatetimeEventStore :

    def store_event(*args, **kwargs):
        date = kwargs['at']
        data = kwargs['data']
        ...
```


## Method
```python
class DatetimeEventStore :

    def get_events(*args, **kwargs) :
        start = kwargs['start']
        end = kwargs['end']
        ...
        return enventsListe
```
