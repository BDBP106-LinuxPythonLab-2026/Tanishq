L=[1,5,6,2,3,2,4,5,6,7,8]
K=2
for x in L:
      if L.count(x) > K:
        print(x)
        break