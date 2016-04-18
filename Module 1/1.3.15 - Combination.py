n, k = map(int, input().split())
from math import factorial as f
print(int(f(n)/f(k)/f(n-k)))