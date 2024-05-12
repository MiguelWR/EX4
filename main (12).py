#Exercício 4

def M(n):
  if n == 2 or n == 3:
      return True
  elif n < 2:
      return False
  elif n % 2 == 0:
      return M(n // 2)
  else:
      return M(n - 3)


print(M(6))
print(M(9))
print(M(16))
print(M(21))
print(M(26))
print(M(54))
print(M(72))
print(M(218))