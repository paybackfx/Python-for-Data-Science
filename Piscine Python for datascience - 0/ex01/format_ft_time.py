#!/usr/bin/env python3
# =============================================================================
# EXERCISE 01: FIRST USE OF PACKAGE
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Explicit Imports (import time): the subject forbids wildcard imports, so
#    every module is imported by name and every symbol stays traceable to the
#    library it came from.
# 2. The Unix Epoch (time.time()): returns the number of seconds elapsed since
#    January 1, 1970 as a float, which is how computers store an instant.
# 3. Format Specifiers ({value:,.4f} and {value:.2e}): the part after the colon
#    inside an f-string controls the rendering - a comma adds thousand
#    separators, .4f keeps four decimals, .2e switches to scientific notation.
# 4. strftime("%b %d %Y"): turns a datetime object into human readable text,
#    where %b is the abbreviated month, %d the zero-padded day and %Y the year.
# =============================================================================

import time
from datetime import datetime

seconds = time.time()

print(f"Seconds since January 1, 1970: {seconds:,.4f} "
      f"or {seconds:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
