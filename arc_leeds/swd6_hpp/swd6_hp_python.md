
---
Date: 02/06/2021
Speakers: Martin Callaghan, Alex Coleman
---

# SWD6: High Performance Python:

## Session 1

### Docs and Links

Slides: https://docs.google.com/presentation/d/17uiPJtg3vOuM3GZhnNuLOuqCqXScnzR-MKNjWAA1Wy8/edit#slide=id.g20f968a4d4_0_42
GitHub: https://github.com/ARCTraining/swd6_hpp


### What slows down code?

* Hitting memory limits
* Accidentally looping through arrays you're already looping through - for example calling a procedure inside a loop to find something, and then having that procedure loop through the array to find it.
* Putting low-probability if-statements early in an if-else ladder
* Using if-else ladders where a switch/case statement might be better
* Calling procedures or using complex if-statements inside very large data loops
* Using inefficient objects when an array might be better
* The ‘wrong’ algorithm
* Inefficient program structure, out-of-date libraries
* Time taken transferring data between (eg.) CPU and GPU


### Profiling

Notes: https://github.com/ARCTraining/swd6_hpp/blob/master/1_python_profiling.md

Profilers show which part of code is taking the longest ie slowing it down, so where you need to focus mostly on. Also means you dont have to optimise everything and make the code really hard to run

Go for lowest hanging fruit first.


#### cProfile

(run from directory: `/home/bs14e3m/Documents/learning/arc_leeds/swd6_high_performance_python/swd6_hpp`)

Python's built-in. Run with;

```{python}
python -m cProfile -s cumulative codes/primes.py
```

```{python}
python -m cProfile -o profile.stats codes/primes.py
```


#### line_profiler

Needs to be downloaded from conda. To use it add `@profile` to the top of the `.py` script. The `@` refers to it being a decorator. Want to put this before any function you want to profile.


#### Visualisation

`snakeviz` is a visualisation tool for the output files created by `cProfile`. Install with conda or pip. Alternative is `PyHeat` which overlays a 'time heatmap' on the code. PyHeat is gorgeous.

snakeviz: https://jiffyclub.github.io/snakeviz/
```
python -m cProfile -o primes.stats codes/primes.py
```

pyheat: https://github.com/csurfer/pyheat. There's also a way of using it in Python.
```
pyheat codes/primes.py --out primes.pyheat.png
```





### Compiling Python

Althoug Python is an interpreted language, tools exist to compile some parts of the code.


#### Cython

An "Ahead-of-Time" AOT method

Need to define C data types.

Need a `setup.py` file which instructs Python to create the C version of the `helloworld.pyx` file.

```{python}

from distutils.core import setup
from Cython.Build import cythonize

setup(
      ext_modules = cythonize("helloworld.pyx")
  )

```

Build Cython version:
```
python setup.py build_ext --inplace
```

Creates a file called `helloworld.so` (`so` means shared object file) on Linux & Mac (`.pyd` on Windows).

To use it, import it like a python module
```
import helloworld
```

If the module you want to create doesnt include any complex C, you can use `pyximport` module to build and load `.pyx` files automatically on import without writing `setup.py`.

Cython version should run faster. Can check runtimes with;
```
time python fib.py
time python fib.pyx
```

Variables are defined in a `.pyx` file, for instance:
```
cdef int n, k, i
cdef int p[1000]
```
Defines them as integers. Also for function def inputs, as in:
```
def primes(int kmax)
```


#### Numba

Numba does the compiling on-the-fly for you, so you don't need to do the compiling yourself like with Cython. Uses a process called **Just in Time** compilation or **jit**.

Need to install and import some functions.

NOTE! The compilation takes time itself, so probably best to run it only for functions that are repeatd multiple times. As if ran just once, the overhead of compiling might mean as a whole it takes longer.

Need to import at top and put `@jit` above functions.

```{python}
import numpy as np
from numba import double
from numba.decorators import jit
```

For parallelisable code, is the `@njit` operator, where we can add `parallel = True` to the function to get it to run in parallel
