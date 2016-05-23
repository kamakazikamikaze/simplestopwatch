# simplestopwatch
A very simple python module for measuring elapsed time

Originally named `stopwatch`, the `simplestopwatch` module is designed for uncomplicated use and simple reporting.

## Usage Example

```python

>>>import simplestopwatch as ssw
>>>s = ssw.Timer()
>>>s.elapsed
2.27779998
>>>s.stop()
25.864999

>>>s = ssw.Timer()
>>>s.stop()
181.0035
>>s.elapsed_human
3 mins, 1 sec
```

The module is able to report human-readable format in seconds, minutes, hours, days, and weeks. If you need anything higher than that, you may want to have your cranium checked.


### Acknowledgements

Many thanks to John Paulett (john@7oars.com) as the original author of this package. This was cloned from his collection at https://code.google.com/archive/p/7oars/
