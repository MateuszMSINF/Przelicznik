from time import sleep

def naC(temp):
	return (5/9) * (temp-32)

def naF(temp):
	return (9/5) * temp + 32


while(True):
	opcja = input("1.Zamiana [°C] na [°F]\n2.Zamiana [°F] na [°C]\nWpisz cokolwiek innego by zakończyć program:\n")
	if opcja == '1':
		temp = int(input("Podaj temp w [°C]: "))
		print(temp, "[°C] = ", round(naF(temp),2), "[°F]\n")
		sleep(.400)
	elif opcja == '2':
		temp = int(input("Podaj temp w [°F]: "))
		print(temp, "[°F] = ", round(naC(temp),2), "[°C]\n")
		sleep(.400)
	else:
		print("Koniec")
		break