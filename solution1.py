# Write code for algorithm 1 below

def one_function(num):
    if num == 0:
        return 0

    else:
        print(num)
        return (num * one_function(num-1))


n=5
one_function(n)