
def fibo_sum( index ):
    if index <= 2:
        return 1
    return fibo_sum(index - 1) + fibo_sum(index - 2)
