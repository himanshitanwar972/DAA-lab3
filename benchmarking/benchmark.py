import time
import tracemalloc


def measure_performance(function, *args, repeats=5):
    """
    Measure execution time and peak traced Python memory.

    Returns:
        average execution time in seconds
        peak traced memory in KB
    """

    execution_times = []
    peak_memory_kb = []

    for _ in range(repeats):
        tracemalloc.start()

        start_time = time.perf_counter()

        function(*args)

        elapsed = time.perf_counter() - start_time

        current_memory, peak_memory = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        execution_times.append(elapsed)
        peak_memory_kb.append(peak_memory / 1024)

    average_time = sum(execution_times) / repeats
    average_memory = sum(peak_memory_kb) / repeats

    return average_time, average_memory