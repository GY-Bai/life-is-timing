#!/usr/bin/env python3
from estimate_scar_half_life import empirical_half_life

# Exact crossing.
h, interp = empirical_half_life([(0.0, -10.0), (1.0, -7.0), (2.0, -5.0)])
assert abs(h - 2.0) < 1e-12 and interp is False

# Interpolated crossing: |beta| 7 at year 1 -> 3 at year 3, target=5 => year 2.
h, interp = empirical_half_life([(0.0, -10.0), (1.0, -7.0), (3.0, -3.0)])
assert abs(h - 2.0) < 1e-12 and interp is True

# Right censoring.
h, interp = empirical_half_life([(0.0, -10.0), (5.0, -8.0), (10.0, -6.0)])
assert h is None and interp is False

print("Scar half-life estimator self-test OK")
