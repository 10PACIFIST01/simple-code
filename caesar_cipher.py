def shifting(char, step, lang):
	if lang == "en":
		first_char = ord("a") if char.islower() else ord("A")
		last_char = ord("z") if char.islower() else ord("Z")
	elif lang == "ru":
		first_char = ord("а") if char.islower() else ord("А")
		last_char = ord("я") if char.islower() else ord("Я")

	char_num = (ord(char) + step) % [first_char, last_char + 1][ord(char) + step > last_char]
	new_char = chr(first_char + char_num)

	return new_char

def deshifting(char, step, lang):
	if lang == "en":
		first_char = ord("a") if char.islower() else ord("A")
		last_char = ord("z") if char.islower() else ord("Z")
		alphabet = 26
	elif lang == "ru":
		first_char = ord("а") if char.islower() else ord("А")
		last_char = ord("я") if char.islower() else ord("Я")
		alphabet = 32

	new_char = chr(ord(char) - step + alphabet * (ord(char) - step < first_char))

	return new_char

def sipher(text, step, lang):
	encrypt = ''
	for ch in text:
		if ch.isalpha():
			encrypt += shifting(ch, step, lang)
		else:
			encrypt += ch

	return encrypt

def desipher(text, step, lang):
	decrypt = ''
	for ch in text:
		if ch.isalpha():
			decrypt += deshifting(ch, step, lang)
		else:
			decrypt += ch

	return decrypt

direction = input("Шифруем(>) или дешифруем(<): ")
print("|")
lang = input("На каком языке будем шифровать(ru, en): ")
print("|")
step = int(input("Укажи шаг сдвига в числовом формате: "))
print()

text = input("Введи текст для расшифровки(дешифровки): ")

print()
print("*" * 10)
print()

if direction == ">":
	encoded = sipher(text, step, lang)
	print(encoded)
elif direction == "<":
	decoded = desipher(text, step, lang)
	print(decoded)
input()