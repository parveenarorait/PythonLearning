def main():
 print("Displaying even numbers between given start and end number")
 printEvenNumbers(1, 1000)
 print("================================================")

 print("Displaying prime numbers between given start and end number")
 printPrimeNumbers(1, 1000)
 print("================================================")

 print("Displaying strong numbers between given start and end number")
 printStrongNumbers(1, 1000)
 print("================================================")

 print("Displaying armstrong numbers between given start and end number")
 printArmstrongNumbers(1, 1000)
 print("================================================")

 print("Displaying palindrome numbers between given start and end number")
 printPalindromeNumbers(1, 1000)
 print("================================================")

 print("Displaying fibonacci series for given number of count")
 printFibonacciSeries(20)
 print("================================================")

 print("Displaying perfect numbers between given start and end number")
 printPerfectNumbers(1, 1000)
 print("================================================")

 input()

def printEvenNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i % 2 == 0:
			print(i)

def printPrimeNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i <= 0:
			continue
		if i == 1:
			continue
		if i == 2:
			print(2)
			continue
		isPrime = True;
		for j in range(2, i // 2 + 1):
			if i != j and i % j == 0:
				isPrime = False
				break
		if isPrime:
			print(i)

def printStrongNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		checkAndPrintIfStrongNumber(i)

def printArmstrongNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i < 0:
			continue
		if i == 0:
			print(0)
			continue
		if(i == 1):
			print(1)
			continue
		checkAndPrintIfArmstrongNumber(i)

def printPalindromeNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber + 1):
		if i <= 0:
			continue
		checkAndPrintIfPalindromeNumber(i)

def printFibonacciSeries(count):
	if count <= 0:
		print("Invalid count")
	elif count == 1:
	    print(0)
	elif count == 2:
		print(0)
		print(1)
	else:
		print(0)
		print(1)
		element1 = 0
		element2 = 1
		for i in range(2, count):
			element3 = element1 + element2
			print(element3)
			element1 = element2
			element2 = element3

def printPerfectNumbers(startNumber, endNumber):
	for i in range(startNumber, endNumber):
		if i < 6:
			continue
		checkAndPrintIfPerfectNumber(i)

def getFactorial(num):
	if num <= 1:
		return 1
	if num == 2:
	    return 2
	return num * getFactorial(num -1)

def getCube(num):
	return num * num * num

def checkAndPrintIfStrongNumber(number):
	originalNumber = number
	sumOfAllDigitFactorial = 0
	while number>0:
		lastDigit = number % 10
		sumOfAllDigitFactorial += getFactorial(lastDigit)
		number = number // 10
	if originalNumber == sumOfAllDigitFactorial:
		print(originalNumber)

def checkAndPrintIfArmstrongNumber(number):
	originalNumber = number
	sumOfAllDigitCube = 0
	while number>0:
		lastDigit = number % 10
		sumOfAllDigitCube += getCube(lastDigit);
		number = number // 10
	if originalNumber == sumOfAllDigitCube:
		print(originalNumber)

def checkAndPrintIfPalindromeNumber(number):
	originalNumber = number
	reversedNumber = 0;
	while number > 0:
		lastDigit = number % 10
		reversedNumber = reversedNumber * 10 + lastDigit;
		number = number // 10
	if originalNumber == reversedNumber:
		print(originalNumber)

def checkAndPrintIfPerfectNumber(number):
	sumOfProperDivisors = 0
	for i in range(1, number // 2 + 1):
		if number % i == 0:
			sumOfProperDivisors += i
	if number == sumOfProperDivisors:
		print(number)

if __name__  == "__main__":
	main()
