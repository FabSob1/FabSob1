'''Napisz program który policzy ilość występowania liter w danym tekście i zwróci w postaci słownika:
{‘a’: 12, ‘b’: 12, ‘c’: 34, …, ‘z’: 34}
Tekst do analizy znajduje się w pliku text.txt
Zawartość z pliku tekstowego można wczytać do programu za pomocą funkcji input. Program uruchamiamy w taki sposób:
python main.py < text.txt wtedy cała zawartość tekstu zostanie zapisana w zmiennej do której odwołuje się funkcja input, np.:
text = input(),
pod zmienną text będziemy mieli całą zawartość tekstu.'''

text = input()

text = text.lower().strip()#Usuwa kropki

slownik = {}

for i in text:
    
    if i != " " and i !="." and i !=',':

        slownik[i] = slownik.get(i, 0) +1 #Dodaje wartość jeden do klucza 
        
print(sorted(slownik.items()))