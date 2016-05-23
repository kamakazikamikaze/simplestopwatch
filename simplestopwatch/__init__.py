# -*- coding: utf-8 -*-
# Originally named `stopwatch`
#
# Copyright (C) 2008 John Paulett (john -at- 7oars.com)
# Copyright (C) 2016 Kent Coble (coblekent@gmail.com)
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

"""simplestopwatch is a very simple Python module for measuring time.
Great for finding out how long code takes to execute.

>>> import simplestopwatch as sw
>>> t = sw.Timer()
>>> t.elapsed
3.8274309635162354
>>> print t
15.9507198334 sec
>>> t.stop()
30.153270959854126
>>> print t
30.1532709599 sec

Decorator exists for printing out execution times:
>>> from simplestopwatch import clockit
>>> @clockit
    def mult(a, b):
        return a * b
>>> print mult(2, 6)
mult in 1.38282775879e-05 sec
6

"""
from __future__ import print_function
import time

__version__ = '0.3.3'
__author__ = 'John Paulett <http://blog.7oars.com>, Kent Coble <https://github.com/kamakazikamikaze'


class Timer(object):

    def __init__(self):
        self.__stopped = None
        self.__start = self.__time()

    def stop(self):
        """Stops the clock permanently for the instance of the Timer.
        Returns the time at which the instance was stopped.
        """
        self.__stopped = self.__last_time()
        return self.elapsed

    def elapsed(self):
        """The number of seconds since the current time that the Timer
        object was created.  If stop() was called, it is the number
        of seconds from the instance creation until stop() was called.
        """
        return self.__last_time() - self.__start
    elapsed = property(elapsed)

    def elapsed_human(self):
        """Total elapsed time formatted into full time units,
        such as minutes, hours, days, and weeks. Merely
        for human-readable convenience.
        """
        intervals = (
            ('weeks', 604800),
            ('days', 86400),
            ('hours', 3600),
            ('mins', 60),
            ('secs', 1),
        )
        seconds = self.elapsed
        result = []
        for name, count in intervals:
            value = int(seconds // count)
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result)
    elapsed_human = property(elapsed_human)

    def start_time(self):
        """The time at which the Timer instance was created.
        """
        return self.__start
    start_time = property(start_time)

    def stop_time(self):
        """The time at which stop() was called, or None if stop was
        never called.
        """
        return self.__stopped
    stop_time = property(stop_time)

    def __last_time(self):
        """Return the current time or the time at which stop() was call,
        if called at all.
        """
        if self.__stopped is not None:
            return self.__stopped
        return self.__time()

    def __time(self):
        """Wrapper for time.time() to allow unit testing.
        """
        return time.time()

    def __str__(self):
        """Nicely format the elapsed time
        """
        return str(self.elapsed) + ' sec'


def clockit(func):
    """Function decorator that times the evaluation of *func* and prints the
    execution time.
    """
    def new(*args, **kw):
        t = Timer()
        retval = func(*args, **kw)
        t.stop()
        print("{} in {}".format(func.__name__, t))
        del t
        return retval
    return new
