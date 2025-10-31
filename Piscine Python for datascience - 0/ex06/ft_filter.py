def ft_filter(function_to_apply, iterable):
    """Return the elements of iterable for which function_to_apply(item) is True."""
    result = []
    for item in iterable:
        if function_to_apply(item):
            result.append(item)
    return result
