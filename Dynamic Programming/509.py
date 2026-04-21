# %%
def fib(n: int) -> int:
    if n in [0, 1]:
        return n
    
    start = 1
    current_fn = 1
    prev_fn = 0
    while start < n:
        next_fn = current_fn + prev_fn
        prev_fn = current_fn
        current_fn = next_fn
        start += 1
    return next_fn

n = 14
fib(n)
# %%
