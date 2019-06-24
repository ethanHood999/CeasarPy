import os
import smtplib, ssl

def main():
	os.system("clear")
	print("Welcome to the Ceasar Cipher!")
	repeat = 'Y'
	while(repeat =='Y' or repeat == 'y'):
		choice = 0
		while(choice < 1 or choice > 2):
			print("Choose what you would like to do: ")
			print("1. Encrypt")
			print("2. Decrypt")
			choice = input()
			choice = int(choice)

		if(choice == 1):
			print("Type your message below to encrypt it")
			msg = input()
			msg = str(msg)
			print("Now type the shift you want to encrypt your message by")
			sft = input()
			sft = int(sft)
			message = msgEncrypt(msg, sft)
			print("")
			print("Would you like to send this over email to a friend? (Y/N)")
			decide = input()
			if(decide == 'Y' or decide == 'y'):
				userName = input("Enter the email address to send from: ")
				password = input("Enter the email address password: ")
				reciever = input("Enter the email address that you will be sending to: ")
				emailSend(userName, password, reciever, message)

		elif(choice == 2):
			print("Type your message below to decrypt it")
			msg = input()
			msg = str(msg)
			print("Now type the shift that is needed to decrypt your message")
			sft = input()
			sft = int(sft)
			message = msgDecrypt(msg, sft)
			print("")
			print("Would you like to send this over email to a friend?")
			decide = input()
			if(decide == 'Y' or decide == 'y'):
				userName = input("Enter the email address to send from: ")
				password = input("Enter the email address password: ")
				reciever = input("Enter the email address that you will be sending to: ")
				emailSend(userName, password, reciever, message)

		print("Would you like to run this again? (Y/N): ")
		repeat = input()

def msgEncrypt(text, shift):
	multiText = []
	y = 0 #to access the array 
	for i in text:
		if((ord(i) >= 65 and ord(i) < 91) or (ord(i) > 96 and ord(i) <= 122)):
			if((ord(i) + shift > 90) and (ord(i) + shift < 97)):
				diff = 90 - ord(i)
				multiText.append(64 + (shift - diff))
			elif(ord(i) + shift > 122):
				diff = 122 - ord(i)
				multiText.append(96 + (shift - diff))
			else:
				multiText.append(ord(i) + shift)
		else:
			multiText.append(ord(i))

	for x in multiText:
		multiText[y] = chr(x)
		y += 1

	j = ""
	for k in multiText:
		print(k, end='')
		j = j + k

	return j


def msgDecrypt(text, shift):
	multiText = []
	y = 0
	for i in text:
		if((ord(i) >= 65 and ord(i) < 91) or (ord(i) > 96 and ord(i) <= 122)):
			if((ord(i) - shift < 65)):
				diff = ord(i) - 65
				multiText.append(91 - (shift-diff))
			elif((ord(i) - shift < 97) and (ord(i) - shift >= 90)):
				diff = ord(i) - 97
				multiText.append(123 - (shift-diff))
			else:
				multiText.append(ord(i) - shift)
		else:
			multiText.append(ord(i))

	for x in multiText:
		multiText[y] = chr(x)
		y += 1

	j = ""
	for k in multiText:
		print(k, end='')
		j = j + k

	return j

def emailSend(userName, password, reciever, message):
	port = 465
	smtp_server = "smtp.gmail.com"

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(userName, password)
		server.sendmail(userName, reciever, message)


if __name__ == '__main__': main()



