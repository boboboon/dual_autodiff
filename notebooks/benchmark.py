"""Benchmarking script between python and cython."""

# %%
import timeit

import matplotlib.pyplot as plt
from dual_autodiffx import Dual as DualCython  # Import the Cythonized Dual class

from dual_autodiff import Dual  # Import your pure Python Dual class


# Benchmarking function
def benchmark_operations(dual_class, num_trials=100000):
    """Benchmark various operations on Dual numbers for a given class (Python or Cython)."""
    setup_code = f"{dual_class.__name__}(1.0, 1.0)"
    operations = {
        "Addition": f"{dual_class.__name__}(1.0, 1.0) + {dual_class.__name__}(2.0, 1.0)",
        "Multiplication": f"{dual_class.__name__}(1.0, 1.0) * {dual_class.__name__}(2.0, 1.0)",
        "Sine": f"{dual_class.__name__}(1.0, 1.0).sin()",
        "Cosine": f"{dual_class.__name__}(1.0, 1.0).cos()",
        "Exponential": f"{dual_class.__name__}(1.0, 1.0).exp()",
        "Logarithm": f"{dual_class.__name__}(1.0, 1.0).log()",
    }
    timings = {}
    for op_name, op_code in operations.items():
        time = timeit.timeit(
            op_code, setup=f"from __main__ import {dual_class.__name__}", number=num_trials
        )
        timings[op_name] = time
    return timings


# Running benchmarks for both versions
pure_python_timings = benchmark_operations(Dual)
cython_timings = benchmark_operations(DualCython)

# %%
# Plotting results
labels = list(pure_python_timings.keys())
python_times = list(pure_python_timings.values())
cython_times = list(cython_timings.values())

x = range(len(labels))
width = 0.4

plt.figure(figsize=(10, 6))
plt.bar(x, python_times, width=width, label="Pure Python", align="center")
plt.bar([i + width for i in x], cython_times, width=width, label="Cython", align="center")
plt.xlabel("Operation")
plt.ylabel("Time (s)")
plt.title("Performance Comparison: Pure Python vs. Cythonized Dual Class")
plt.xticks([i + width / 2 for i in x], labels, rotation=45)
plt.legend()
plt.show()

# %%
