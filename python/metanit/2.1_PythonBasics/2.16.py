def multiply(n): return lambda m: n * m
 
 
fn = multiply(5)
print(fn(5))        # 
print(fn(6))        # 
print(fn(7))        # 