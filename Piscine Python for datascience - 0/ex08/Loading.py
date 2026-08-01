# =============================================================================
# EXERCISE 08: LOADING ...
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Generators (yield): a function containing yield returns a generator. Each
#    yield hands one item back to the for loop and freezes the function until
#    the next iteration, which is what lets the bar be redrawn between items.
# 2. Carriage Return (end="\r"): "\r" moves the cursor back to column 0 without
#    starting a new line, so every redraw overwrites the previous bar in place
#    instead of flooding the terminal with 333 lines.
# 3. os.get_terminal_size(): the subject suggests adapting to the terminal
#    width. It raises OSError when stdout is redirected to a pipe or a file,
#    so the call is guarded and falls back to the classic 80 columns.
#
# NOTE: the prototype is kept exactly as the subject writes it, "-> None",
#    even though a generator function really returns a generator object. The
#    subject wins over the annotation.
# =============================================================================

import os

FALLBACK_WIDTH = 80


def ft_tqdm(lst: range) -> None:
    """Yield every item of lst while drawing a tqdm-like progress bar."""
    total = len(lst)
    if total == 0:
        return
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = FALLBACK_WIDTH
    suffix = f"100%|[]| {total}/{total}"
    width = max(columns - len(suffix), 10)

    for index, item in enumerate(lst, start=1):
        filled = width * index // total
        bar = "=" * (filled - 1) + ">" if filled else ""
        percent = 100 * index // total
        print(f"\r{percent}%|[{bar:<{width}}]| {index}/{total}",
              end="", flush=True)
        yield item
