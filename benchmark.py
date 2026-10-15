import time
from math import isqrt
from statistics import median

from collisions import E_half, E_fast


def benchmark(func, *args, repeats=5):
    times = []
    result = None

    for _ in range(repeats):
        start = time.perf_counter()
        result = func(*args)
        times.append(time.perf_counter() - start)

    return result, median(times)


print(
    f"{'N':>12} {'sqrt(N)':>14} {'groups':>12} "
    f"{'E_half (s)':>12} {'E_fast (s)':>12} {'speedup':>10}"
)
print("-" * 78)

for exp in (6, 8, 10, 12, 14, 16, 18, 21):
    N = 10**exp + 12345

    (fast_result, groups), fast_time = benchmark(E_fast, N, True)

    if exp <= 16:
        half_result, half_time = benchmark(E_half, N)

        if half_result != fast_result:
            raise AssertionError(f"Results differ for N={N}")

        speedup = f"{half_time / fast_time:.2f}x"
        half_text = f"{half_time:.6f}"
    else:
        speedup = "-"
        half_text = "-"

    print(
        f"{N:12,d} {isqrt(N):14,d} {groups:12,d} "
        f"{half_text:>12} {fast_time:12.6f} {speedup:>10}"
    )
