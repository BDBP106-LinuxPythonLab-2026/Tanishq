import math
angles=[24,56,34]
result=list(map(lambda i:(math.sin(math.radians(i)), math.cos(math.radians(i))) ,angles))
print(result)