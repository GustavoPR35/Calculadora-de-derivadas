def exibirPolinomio(coeficientes, expoentes):
  termos = []

  for coeficiente, expoente in zip(coeficientes, expoentes):

      cont = 0
      aux = 0
      for i in expoentes:
        if i != 0:
          cont += 1
      if cont == 0:
        for i in coeficientes:
          aux += i
        return aux

      if coeficiente == 0:
          continue

      if expoente == 0:
          termos.append(f"{coeficiente}")

      elif expoente == 1:
          if coeficiente == 1:
              termos.append("x")
          elif coeficiente == -1:
              termos.append("-x")
          else:
              termos.append(f"{coeficiente}x")

      else:
          if coeficiente == 1:
              termos.append(f"x^{expoente}")
          elif coeficiente == -1:
              termos.append(f"-x^{expoente}")
          else:
              termos.append(f"{coeficiente}x^{expoente}")

  polinomio = " + ".join(termos)
  polinomio = polinomio.replace("+ -", "- ")

  return polinomio

def calcularDerivada(coeficientes, expoentes):
  d_coeficientes = []
  d_expoentes = []
  for coeficiente, expoente in zip(coeficientes, expoentes):
      if expoente == 0:
          continue
      d_coeficientes.append(expoente * coeficiente)
      d_expoentes.append(expoente - 1)
  return d_coeficientes, d_expoentes

def exibirDerivada(coeficientes, expoentes):
  d_coeficientes, d_expoentes = calcularDerivada(coeficientes, expoentes)

  cont = 0
  for i in d_expoentes:
    if i != 0:
      cont += 1
  if cont == 0:
    return "0"

  derivada = exibirPolinomio(d_coeficientes, d_expoentes)
  return derivada

def calcularVF(coeficientes, expoentes, a):
  f_a = 0

  for coeficiente, expoente in zip(coeficientes, expoentes):
      f_a += coeficiente * (a ** expoente)

  return f_a

def calcularVFderivada(d_coeficientes, d_expoentes, a):
  f_da = 0

  for coeficiente, expoente in zip(d_coeficientes, d_expoentes):
      f_da += coeficiente * (a ** expoente)

  return f_da

#y - f(a) = f'(a) * (x - a)
#y = f'(a) * (x - a) + f(a)
def retaTangente(f_da, a, f_a):
  rtConta = (f"y = {f_da:.2f} * (x - {a:.2f}) + {f_a:.2f}")
  rtConta = rtConta.replace(" + -", " - ")
  rtConta = rtConta.replace(" - -", " + ")
  return rtConta

#y = f'(a) * x - f'(a) * a + f(a)
def calculoRT(f_da, a, f_a):
  if f_da == 0:
      resultado = (f"y = {f_a:.2f}")
      return resultado
  elif f_da == 1:
      termoX = ("x")
  elif f_da == -1:
      termoX = ("-x")
  else:
      termoX = (f"{f_da:.2f}x")

  termo2 = f_da * a
  termo3 = f_a

  constante = termo3 - termo2 # - (f'(a)*a) + f(a) ===> f(a) - (f'(a)*a)

  if constante == 0:
      resultado = (f"y = {termoX}")
  elif constante > 0:
      resultado = (f"y = {termoX} + {constante:.2f}")
  else:
      resultado = (f"y = {termoX} - {constante:.2f}")
      resultado = resultado.replace(" - -", " + ")

  return resultado

def Calculadora():

  print("\n-------------------------------------------------------")
  print("\nCalculadora de derivada primeira de funções polinomiais")
  print("\n-------------------------------------------------------")
  print("\nInforme o numero de monômios na função polinomial")

  n = int(input())
  if n < 0 or n == 0:
    print("\nNúmero de monômios deve ser maior que 0.")
    return
  coeficientes = []
  expoentes = []

  print("\n-------------------------------------------------------\n")

  for i in range(n):
      print(f"Digite o coeficiente e o expoente do monômio {i+1}:")
      coeficiente = int(input("Coeficiente: "))
      expoente = int(input("Expoente: "))
      coeficientes.append(coeficiente)
      expoentes.append(expoente)

  print("\n-------------------------------------------------------")

#função e derivada
  print("\nFunção polinomial:")
  print(f"f(x) = {exibirPolinomio(coeficientes, expoentes)}")

  print("\nDerivada:")
  print(f"f'(x) = {exibirDerivada(coeficientes, expoentes)}")
  d_coeficientes, d_expoentes = calcularDerivada(coeficientes, expoentes) #guardano
  print("\n-------------------------------------------------------")

#valor funcional aq
  print("\nDeseja calcular valor funcional?")
  escolha1 = input("S/N: ").lower()
  if escolha1 == "s" or escolha1 == "sim":
      print("\nQual será o valor de a?")
      a = float(input("a: "))
      f_a = calcularVF(coeficientes, expoentes, a)
      f_da = calcularVFderivada(d_coeficientes, d_expoentes, a)
      pontoP = (f"{a}, {f_a:.2f}")

      print("\n-------------------------------------------------------")
      print(f"\na = {a}   |   f({a}) = {f_a:.2f}    |   f'({a}) = {f_da:.2f}    |   P({pontoP})")
      print("\n-------------------------------------------------------")
#eq rt
      print(f"\nDeseja calcular a equação da reta tangente ao gráfico de f no ponto P({pontoP})?")
      escolha2 = input("S/N: ").lower()
      if escolha2 == "s" or escolha2 == "sim":
          print("\n-------------------------------------------------------")
          print(f"\nConta:  --| {retaTangente(f_da, a, f_a)} |--")
          print(f"\nA equação da reta tangente ao gráfico de f no ponto P({pontoP}) é:")
          print(f"\nResultado:  --| {calculoRT(f_da, a, f_a)} |--")
          print("\n-------------------------------------------------------")
      elif escolha2 == "n" or escolha2 == "nao":
          print("\nOk. Não calcular.")
      else:
          print("\nOpção inválida.")

  elif escolha1 == "n" or escolha1 == "nao":
      print("\nOk. Não calcular.")
  else:
      print("\nOpção inválida.")

def main():
  while True:
      Calculadora()
      while True:
          print("\nDeseja derivar outro polinômio?")
          continuar = input("S/N: ").lower()
          if continuar == "s" or continuar == "sim":
              break
          elif continuar == "n" or continuar == "nao":
              print("\nOk. Encerrando o programa.")
              return
          else:
              print("\nOpção inválida.")

if __name__ == "__main__":
  main()