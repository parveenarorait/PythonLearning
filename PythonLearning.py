def main():
 print("Displaying even numbers between given start and end number")
 printEvenNumbers(1, 1000)
 print("================================================")

 print("Displaying prime numbers between given start and end number")
 printPrimeNumbers(1, 1000)
 print("================================================")

 printStrongNumber(1, 1000)

def printEvenNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i % 2 == 0:
			print(i)

def printPrimeNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i == 1:
			continue
		if i == 2:
			print(2)
			continue
		isPrime = True;
		for j in range(2, i):
			if i != j and i % j == 0:
				isPrime = False
				break
		if isPrime:
			print(i)

def printStrongNumber(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		checkAndPrintIfStrongNumber(i)

def getFactorial(num):
	if num <= 1:
		return 1
	if num == 2:
	    return 2
	return num * getFactorial(num -1)

def checkAndPrintIfStrongNumber(number):
	originalNumber = number
	sumOfAllDigitFactorial = 0
	while number>0:
		lastDigit = number % 10
		sumOfAllDigitFactorial += getFactorial(lastDigit)
		number = number // 10
	if originalNumber == sumOfAllDigitFactorial:
		print(originalNumber)

if __name__  == "__main__":
	main()
