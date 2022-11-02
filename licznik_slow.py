from cgitb import text


text = input("Wpisz co chcesz: ")

print("ilość słów: ", len(text.split(" ")))
print("liczba znaków: ", len(text.replace(" ", "")))

c = 0
for char in text:
    if char.isalnum():
        c += 1

print("Znaki alfanumeryczne: ", c)
