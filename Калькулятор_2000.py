#Калькулятор 3.1
launglich = input("Выберете язык/Choose a language: ")
if launglich == "Русский":
	print("Калькулятор 2000")
	a = float( input( "Первое число:" ) )
	what = input( "Действие (+, -, *, /):" )
	b = float( input( "Второе число:" ) )
	if what == "+":
		c = a + b
		print ("Итого: " + str(c))
	elif what == "-":
		c = a - b
		print ("Итого: " + str(c))
	elif what == "*":
		c = a * b
		print ("Итого: " + str(c))
	elif what == "/":
		c = a / b
		print ("Итого: " + str(c))
	else:
		print ("Неверный синтаксис!")
elif launglich == "English":
#Yandex Translator was used for the translation
	print("Calculator 2000")
	a = float( input( "The first number:" ) )
	what = input( "Action (+, -, *, /):" )
	b = float( input( "The second number:" ) )
	if what == "+":
		c = a + b
		print ("Total: " + str(c))
	elif what == "-":
		c = a - b
		print ("Total: " + str(c))
	elif what == "*":
		c = a * b
		print ("Total: " + str(c))
	elif what == "/":
		c = a / b
		print ("Total: " + str(c))
	else:
		print ("Incorrect syntax!")
else:
	print("Неизвестный язык/Unknown language")
input()
