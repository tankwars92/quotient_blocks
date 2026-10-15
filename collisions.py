from math import isqrt

def E_brute(N):
    return sum(1 for i in range(1, N + 1) for j in range(i + 1, N + 1) if N // i == N // j)

def E_blocks(N):
    total = 0
    i = 1

    while i <= N:
        r = N // (N // i)
        c = r - i + 1
        total += c * (c - 1) // 2
        i = r + 1

    return total

def E_half(N):
    s = isqrt(N)
    total = 0

    for w in range(1, s + 1):
        c = N // w - N // (w + 1)
        total += c * (c - 1) // 2

    return total

def _groups(N):
    s = isqrt(N)
    v = 1

    while v <= s:
        m = N // (v * (v + 1))

        if m == 0:
            return

        vmax = (isqrt(4 * (N // m) + 1) - 1) // 2

        if vmax > s:
            vmax = s

        ln = vmax - v + 1
        n1 = (N // v - N // (vmax + 1)) - ln * m

        yield m, ln, n1
        v = vmax + 1

def E_fast(N, count_groups=False):
    total = 0
    g = 0

    for m, ln, n1 in _groups(N):
        total += (ln - n1) * (m * (m - 1) // 2) + n1 * (m * (m + 1) // 2)
        g += 1

    return (total, g) if count_groups else total

def block_histogram(N):
    h = {}

    for m, ln, n1 in _groups(N):
        if ln - n1:
            h[m] = h.get(m, 0) + (ln - n1)

        if n1:
            h[m + 1] = h.get(m + 1, 0) + n1

    h.pop(0, None)
    big = sum(j * c for j, c in h.items() if j >= 2)
    h1 = N - big

    if h1:
        h[1] = h1

    return dict(sorted(h.items()))

def block_histogram_brute(N):
    h = {}
    i = 1

    while i <= N:
        r = N // (N // i)
        c = r - i + 1
        h[c] = h.get(c, 0) + 1
        i = r + 1

    return dict(sorted(h.items()))