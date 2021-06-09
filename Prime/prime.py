def prime_checker(number):
  prime = True
  for i in range(2, number):
    if number % i == 0:
      prime = False
  if prime == False:
    print(f"No {number} is not a Prime Number")
  else: print(f"Yes {number} is a Prime Number!!")

n = int(input("Check this number: "))
prime_checker(number=n)