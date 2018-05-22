import decrement
import increment
number = int(input('Enter any number for increment '))
incClass = increment.Increment(number)
test = incClass.inc()
print(test)

decNumber = int(input('Enter any number for decrement '))
decClass = decrement.Decrement(decNumber)
testDec = decClass.dec()
print(testDec)


