from sympy import integrate , symbols , sqrt
x = symbols (" x ")
t = symbols (" t " , positive = True)
# We need to integrate (t/sqrt(x - t))
# According to the property of definite integral, for any function f(x)
# integral [f(x)] (limits from 0 to a) = integral [f(a - x)] (limits from 0 to a)
# a is any arbitary constant
# By the above property
# integral (t/sqrt(x - t) , (t,0,x)) = integral ((x - t)/sqrt(t) , (t,0,x)) 
print(integrate ((x-t)/sqrt(t) , (t,0,x)))
