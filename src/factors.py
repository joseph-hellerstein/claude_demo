def findFactors(n: int) -> dict[int, int]:
    """findFactors(n: int) -> dict[int, int]

    Factors a positive integer into its prime components.
    Divides n by each candidate prime starting from 2, counting how many
    times each prime divides evenly, until n is fully reduced.

    Usage example:
        >>> findFactors(12)
        {2: 2, 3: 1}
        >>> findFactors(360)
        {2: 3, 3: 2, 5: 1}
    """
    if n < 2:
        return {}

    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

