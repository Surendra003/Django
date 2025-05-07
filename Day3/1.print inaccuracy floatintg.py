print(0.1+0.2==0.3) #result false due to floating point precision errors in python
import math
print(math.isclose(0.1+0.2,0.3)) #math.isclose() forfloat comparision, this checks two numbers are close