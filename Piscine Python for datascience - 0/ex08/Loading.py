import time
import sys

def ft_tqdm(lst: range) -> None:
    """
    Mimics tqdm function with yield operator.
    """
    total = len(lst)
    start_time = time.time()
    
    # Initial print
    # 0%|                                                 | 0/333 [00:00<?, ?it/s]
    # But the example shows:
    # 100%|[===============================================================>]| 333/333
    # Let's try to match the standard tqdm output format first as requested "close as possible to the original version"
    # The example output in the prompt is a bit specific:
    # 100%|[===============================================================>]| 333/333
    # 100%|
    # | 333/333 [00:01<00:00, 191.61it/s]
    
    # Standard tqdm format often looks like:
    # 100%|██████████| 333/333 [00:01<00:00, 191.61it/s]
    # The prompt example uses [=>] style for the bar.
    
    # Terminal width detection (optional, but good for "copying" tqdm)
    # For now, let's stick to a fixed width or dynamic.
    # The example seems to have a specific width.
    
    def format_time(seconds):
        m, s = divmod(seconds, 60)
        return f"{int(m):02}:{int(s):02}"

    for i, elem in enumerate(lst):
        yield elem
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        iteration = i + 1
        
        percent = int(iteration / total * 100)
        
        # Calculate speed (it/s)
        if elapsed_time > 0:
            speed = iteration / elapsed_time
        else:
            speed = 0
            
        # Calculate remaining time (ETA)
        if speed > 0:
            remaining_items = total - iteration
            eta_seconds = remaining_items / speed
            eta_str = format_time(eta_seconds)
        else:
            eta_str = "?"

        elapsed_str = format_time(elapsed_time)
        
        # Bar construction
        # The prompt example: [=================>]
        # It seems to always have > at the end of the filled part?
        # And the bar is enclosed in []
        
        # Let's assume a fixed length for the bar to match the visual
        bar_length = 64
        filled_length = int(bar_length * iteration // total)
        
        if filled_length == 0:
            bar = ""
        else:
            # Always put > at the end of the filled part
            # But if it's full (100%), does it still have >?
            # The example shows 100% ... [====>]
            # So yes.
            bar = "=" * (filled_length - 1) + ">"
        
        # Pad with spaces
        bar = bar.ljust(bar_length, ' ')
        
        # Output format
        # 100%|[===============================================================>]| 333/333
        # I will include the stats as well because tqdm has them.
        
        output = f"{percent}%|[{bar}]| {iteration}/{total} [{elapsed_str}<{eta_str}, {speed:.2f}it/s]"
        
        # Print with carriage return
        # Use simple print with end='\r' or sys.stdout
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()
        
    print() # Newline at the end