alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
letters = [c for c in alphabet]
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
letter_morse = {key:value for key, value in zip(letters, morse)}

def to_morse(text):
	result = ""
	for ch in text:
    	if ch in alphabet:
        	result += letter_morse[ch] + " "
    return result[:-1]

if __name__ == "__main__":
	text = input().upper()
	print(to_morse(text))
	input()