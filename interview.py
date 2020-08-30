# Напишите функцию find_amount, которая возвращает наиболее часто встречающуюся букву во фразе.
# Считайте, что text может быть только строковый
# Если максимумов несколько, верните ту букву, которая располагается ближе к началу текста

def find_amount(text):
  pass



assert find_amount(‘abc’) == ‘a’, ‘Error’
assert find_amount(‘eqrq’) == ‘q’, ‘Error’
assert find_amount(‘abccdd’) ==‘c’, ‘Error’
assert find_amount(‘’) is None, ‘Error’
print(‘Success!’)