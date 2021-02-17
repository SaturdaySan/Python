'''
THIS EXERCISES are given by the site programmareinpython
'''

'''
ESERCIZIO 1
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), 
sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
'''
'''
n1 = int(input("digita il primo numero "))
print(id(n1))
n2 = int(input("digita il secondo numero"))
print(id(n2))

def massimoNumeri(n1 ,n2) :
    print(n1 , n2)
    if n1 > n2 :
        print("n1 è il numero maggiore")
    elif n2 > n1 :
        print("n2 è il numero maggiore")
    elif n1 == n2 :
        print("i numeri sono uguali")
    print(id(n1))
    print(id(n2))

massimoNumeri(n1,n2)
'''
'''
ESERCIZIO 2
Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!
'''
'''
trio = []
def massimoTreNumeri(trio:[]):
    while len(trio) <= 2:
        trio.append(int(input("digita il numero da confrontare")))
        print(trio)

    if trio[0] > trio[1] and trio[0]> trio[2]:
        print(trio[0])
    elif trio[1] > trio[0] and trio[1]> trio[2]:
        print(trio[1])
    elif trio[2] > trio[1] and trio[2]> trio[0]:
        print(trio[2])

massimoTreNumeri(trio)
'''
'''
ESERCIZIO 3
Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.
'''
'''
def isVocale(char : str ):
    if len(char ) > 1:
        print("this ain't a char ")
        return False
    else :
        voc = ["a","e","i","o","u","A","E","I","O","U"] 
        i = 0
        for chars in voc :
            print(chars)
            if char == voc[i] :
                print(char+" è una vocale")
                break
            else :
                i+=1
        else :
            print("non è una vocale")
        
isVocale("y")
'''
'''
ESERCIZIO 4
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
'''
'''
num = [1,2,3]

def calcolaTutto(numbers : []):
    somma = 0
    for x in numbers:
        somma += x
    print(somma)
        

calcolaTutto(num)
'''
'''
ESERCIZIO 5
Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.
'''
'''
def moltiplicaTutto(numbers : []) :
    moltiplica = 1
    for x in numbers : 
        moltiplica *= x
    print(moltiplica)
    

nums = [4 , 2 , 1]

moltiplicaTutto(nums)
'''
'''
ESERCIZIA 6
Scrivi una funzione a cui passerai come parametro una stringa
e ti restituirà una versione della stessa stringa al contrario (ad esempio "abcd" diventa "dcba".
'''
'''
def inverso(word : str):
    reverseString = []
    for leng in word:
        reverseString.append(leng)
    i = len(reverseString)-1
    reverso = ""
    for rev in reverseString:
        reverso += reverseString[i]
        i = i -1
    return reverso
      
print(inverso("annanatan"))
'''
'''
ESERCIZIO 7
Scrivi una funzione a cui viene passata una parola 
e riconosce se si tratta di un palindromo(parole che si leggono uguali anche al contrario) oppure meno.
'''
'''
#FAILED
def testa_parole(parola):
    indice = (len(parola) -1)
    nuova_parola = ""
    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1
    if nuova_parola == parola:
        print('La parola passata è un palindromo! ' + nuova_parola)
    else:
        print('Mi dispiace, la parola inserita non è un palindromo...')

testa_parole("ono")
'''
'''
ESERCIZIO 8
Scrivi una funzione che manda in print la lunghezza 
di una stringa o lista passata come parametro.
In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()
'''
'''
def myLenVersion(lista : list):
    i = 0
    for x in lista:
        i+=1
    print(i)

ciao = [1,2,3,4,5]
myLenVersion(ciao)
'''
'''
ESERCIZIO 9
Scrivi una funzione che, data una lista di numeri, 
fornisce in output un istogramma basato su questi numeri, 
usando asterischi per disegnarlo.
Ad esempio, data la lista [3,7,9,5] deve produrre questo grafico:
***
*******
*********
*****
'''
'''
#FAILED
def istogramma(lista : list):
    for num in lista:
        if num == 0:
            print("*" * num)


lista = [0,1,2,3,4,5,6]
istogramma(lista)
'''     
'''
ESERCIZIO 10
Scrivi una funzione che, data in ingresso una lista A contenente parole, restituisce in 
output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
'''
'''
def giveBack(lista : list):
    listBack = []
    for thing in lista:
        listBack.append(len(thing))
    return listBack

lista = ["cio","cion","ciong","ciongi"]
print(giveBack(lista))
'''
'''
ESERCIZIO 11
Scrivi un programma che, passata come parametro una lista di interi, 
fornisce in output il maggiore tra i numeri contenuti nella lista.
'''
'''
def countList(lista :list):
    maj = 0
    for x in lista:
        if x > maj:
            maj = x
    return maj

lista = [1,2,3,20,20]
print(countList(lista))
'''
'''
ESERCIZIO 12
Scrivi una funzione a cui passare una stringa come parametro, 
e che restituisca un dizionario rappresentante la frequenza di ciscun carattere componente 
la stringa. Ad esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}.
'''
'''
def componente (frase : str):
    dictionary = {}
    chars = "abcdefghijklmnopqrstuvwxyz"
    for char in frase:
        count = frase.count(char)
        if count > 0:
            dictionary.update({char : count})
            #print (char,count)
    print(dictionary)
        

componente("ababcc")
'''
'''
ESERCIZIO 13
Scrivi una funzione a cui vengono passati un valore e una lista di valori, 
e che ti dica in output se il valore passato è presente o meno nella lista.
'''
'''
def isPresent(valore : object , listaValori : list):
    for x in listaValori:
        if valore == x:
            print(x , "è presente")
            return True
        
valore = 2
listaValori = ["ciao", 2, 5]
isPresent(valore , listaValori)
'''
'''
ESERCIZIO 14
In Svezia, i bambini giocano spesso 
utilizzando un linguaggio un pó particolare, detto "rövarspråket", 
che significa "linguaggio dei furfanti": 
consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo.
Ad esempio la parola "mangiare" diventa "momanongogiarore".
Scrivi una funzione in grado di tradurre una parola 
o frase passata tramite input() in "rövarspråket".

mangiare -> (m1)(o)(m 2)anongogiarore

'''
'''
def traduttore():
    print("
    Ciao! questo programma traduce un testo passato in "rövarspråket".
    Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
    ")
'''
'''
FAILED
    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]
    
    while True:
        testo = input('\nInserisci il testo che desideri tradurre -> ')
        tradotta = ""
        for x in testo:
            if x in vocali or x in specials:
                tradotta += x #tradotta = tradotta + x
            else:
                tradotta = tradotta + x + "o" + x

        print(f"Ecco a te la traduzione! '{tradotta}'")

        if input("\nDesidere tradurre un'altra frase? ") == "no":
            break

traduttore()
'''
'''
ESERCIZIO 15
Scrivi una funzione che, 
a scelta dell'utente, calcoli l'area di:
    un cerchio
    un quadrato
    un rettangolo
    un triangolo
Sentiti libero/a di estendere le potenzialità 
della funzione quanto meglio credi...
'''
'''
def geometria():
    print("digita: \n [1] - per calcoalre l'aera del cerchio \n [2] - per calcolare l'aera di un quadrato \n [3] - per calcolare l'aera di un rettangolo \n [4] - per calcolare l'area di un  triangolo ")
    scelta = int(input("inserisci il numero per scegliere quale aerea calcolare: "))

    def cerchio():
        raggio = int(input("inserisci il raggio del cerchio:"))
        print(str(2 * 3.14 * raggio))

    def quadrato():
        lato = int(input("inserisci il lato del quadrato"))
        print(str(lato * lato))

    def rettangolo():
        base = int(input("inserisci la base del rettangolo"))
        altezza = int(input("inserisci l'altezza del rettangolo"))
        print(str(base * altezza))

    def triangolo():
        base = int(input("inserisci la base del triangolo"))
        altezza = int(input("inserisci la base del triangolo"))
        somma = base * altezza 
        print(str(somma / 2))
    
    dictionary = {
        1 : cerchio,
        2 : quadrato,
        3 : rettangolo,
        4 : triangolo,
    }

    def exit():
        print("bye bye")
    dictionary.get(scelta,exit)()


geometria()
'''

'''
ESERCIZIO 16

Scrivi una funzione che, dato in ingresso un valore espresso in metri, 
mandi in print l'equivalente in :
miglia terrestri,
iarde,
piedi
pollici.
'''
'''
def american(metri : float):
    # 1,0936 -> miglia terrestri
    # 39,370 -> pollici
    # 3.2808 -> piedi 
    
    def miglia():
        print(str(str(metri)+"in piedi sono: "+str(metri * 1.0936)))

    def pollici():
        print(str(metri)+"in pollici sono: "+str(metri * 39.370))

    def piedi():
        print(str(metri)+"in piedi sono: "+str(metri * 3.2808))
    
    def exit():
        print("bye bye")
    
    dictionary = {
        1 : miglia,
        2 : pollici,
        3 : piedi,
    }

    scelta = int(input("imponi la tua scelta"))

        
    dictionary.get(scelta,exit)()

american(float(input("digita i metri:")))
'''
'''
ESERCIZIO 17
Scrivi una semplice funzione che converta un dato numero di giorni,
ore e minuti,
passati dall'utente tramite funzione input,
in secondi.
'''
'''
def timeCalc():
    days = int(input("digita i giorni da convertire"))
    
    hours = int(input("digita le ore da convertire"))
    
    minutes = int(input("digita i minuti da convertire"))

    daysInSecond = days * 86400
    hoursInSecond = hours * 3600
    minutesInSecond = minutes * 60

    calc = daysInSecond + hoursInSecond + minutesInSecond

    print( str(days) , str(hours) , str(minutes) + " in secondi equivalgono a " + str(calc))

timeCalc()
'''
'''
ESERCIZIO 18

Scrivi una funzione generatrice di password.

La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice,
o di 20 caratteri ascii qualora desideri una password più complicata.
'''
'''
import random

def passwordGen():
    alphaBM = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFHJKLZXCVBNM1234567890_-?$£&()=^*èé[]+§°ç@#òàù:;,"
    optional = int(input("digita di quanto lunga vuoi la password"))
    cont = 0
    password = ""
    if optional == 8 or optional == 20:
        while cont < optional:
            num = random.randint(0,len(alphaBM)-1)
            print(alphaBM[num])
            password += str(alphaBM[num])
            cont += 1
    else:
        print("non fattibile")
        return 


passwordGen()
'''
'''
ESERCIZIO 19

Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore,
a un chipset per comunicazioni wireless (es WiFi o Bluetooth),
composto da 6 coppie di cifre esadecimali separate da due punti.

Un esempio di MAC è 02:FF:A5:F2:55:12.

Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.
'''
'''
import random
def macGenerator():
    exNum = "0123456789"
    exLet = "abcdefABCDEF"
    counter = 0 
    macAddress = ""
    while counter < 12:
        randomNum = random.randint(0,len(exNum)-1)
        randomLet = random.randint(0,len(exLet)-1)
        macAddress += str(exNum[randomNum])
        macAddress += str(exLet[randomLet])
        counter += 1
        macAddress += ":"
    print(macAddress)
    return macAddress

macGenerator()
'''
'''
ESERCIZIO 20
Scrivi una semplice funzione rimario,
a cui viene passato un elenco di parole come parametro e
che riceva una parola inserita dall'utente tramite la funzione input.
La funzione primaria dovrà confrontare la parola inserita dall'utente
con quelle presenti nell'elenco passato, alla ricerca di rime,
intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.
Le rime dovranno essere quindi mostrate in output dall'utente
'''
'''
def poesia (lista : list):
    parola = str(input("inserisci la parole con cui provare a far rime: "))
    lastLetterParola = parola[len(parola)-3] + parola[len(parola)-2] + parola[len(parola)-1]
    bars = []
    for parole in lista:
        last3Letters = parole[len(parole)-3] + parole[len(parole)-2] + parole[len(parole)-1]
        if lastLetterParola == last3Letters:
            bars.append(parole)
    print(bars)

lista = ["parola" , "parole" ,"scatola","giola","pola"]
poesia(lista)
'''
'''
Esercizio 21 
'''
'''
Scrivi una funzione "vendi_libri" che:
Controlla se il libro richiesto è presente sugli scaffali della libreria
Qualora il libro sia presente, ne decrementa il numero di copie
(eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato 
che la vendita non ha avuto successo

La funzione restituisce valore Booleano True o False in base all'esito della vendita.
'''
'''
library = {"pirates" : 0 , "willy" : 2}
orderBooks = {}
def sell_books(library : dict , orderBooks :dict):
    #print(library.get("pirates","valore non presente"))    
    #print(library["pirates"]) 
    searchingBooks = str(input("put the name of the book that you're looking for: "))
    for books in library:
        if searchingBooks == books: 
            library.update({searchingBooks: library.get(searchingBooks)-1})
            return True ,print("book present , sold")
        elif searchingBooks is not books:
            orderBooks.setdefault(searchingBooks, 1)
            return False ,print("book not present we are going to order it") 

sell_books(library,orderBooks)
print(orderBooks)
'''
'''
ESERCIZIO 22
Il ROT-13 è un semplice cifrario monoalfabetico,
in cui ogni lettera del messaggio da cifrare viene sostituita
con quella posta 13 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata,
o decriptarla se la stringa è già stata precedentemente codificata.
'''
'''
def rot13(phrase : str):
    alphab = "abcdefghijklmnopqrstuvwxyz"
    crypted = ""
    for lettere in phrase:
        for letters in alphab:
            if letters == lettere:
                if alphab.find(letters) >= 13:
                    crypted+=alphab[int(alphab.find(letters)-13)]+' '
                else:
                    crypted+=alphab[int(alphab.find(letters)-13)]+' '
    print(crypted)
    return crypted
                    
import codecs
def decod(stringa : str):
    print(codecs.encode(stringa, 'rot_13'))                

rot13("la scena")
decod(rot13("la scena"))
'''
'''
ESERCIZIO 23
Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.
'''
'''
def fattoriale(numero : int):
    if numero == 0:
        return 1
    else :
        return numero * fattoriale(numero - 1)

print(fattoriale(4))
'''
'''
ESERCIZIO 24
Nella serie di Fibonacci,
ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:

1, 1, 2, 3, 5, 8, 13 (...)

Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci,
 entro una soglia specifica impostata dall'utente.
'''
'''
FAILED
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

limite = int(input("Inserisci il numero di valori della serie che desideri vedere: "))

for num in range(1, limite+1):
    print(fibonacci(num))
'''
'''
ESERCIZIO 25
Scrivi una funzione che 
fornisca in output il nome del Sistema Operativo utilizzato 
con eventuali relative informazioni sulla release corrente.
'''
'''
import platform
 # Library per le informazioni di sistema "PLATFORM"

def sysInfo():
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")

sysInfo()
'''
'''
Esercizio 26
Scrivi una funzione che, dato un carattere in ingresso,
restituisca in output il codice ASCII associato al carattere passato.
'''
'''
def getAscii(carattere : str):
    print("il carattere ",carattere," in ascii è: ",ord(carattere))

getAscii("a")
'''
'''
Esercizio 027
Scrivi una funzione che calcoli la somma (espressa in MB) 
delle dimensioni dei file presenti nella cartella di lavoro.
'''
'''
FAILED
'''
'''
import os

def file_size():
    totale = 0
    cartella = os.getcwd()
    for file in os.listdir(cartella):
        totale += os.path.getsize(os.path.join(cartella, file))
    print(f"La somma delle dimensioni dei file presenti nella cartella '{cartella}' è: {(totale/1048576):.2f}MB")

file_size()

'''
'''
FAILED
'''
'''
import smtplib

def postino():
    print("""
    Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
    Server: smtp.gmail.com
    Porta: 587
    Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
    """)

    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    destinatario = input("Inserisci l'email del destinatario: ")
    oggetto = input("Inserisci l'oggetto della mail: ")
    messaggio = input("Ora puoi inserire il messaggio che vuoi inviare: ")
    contenuto = f"Subject: {oggetto}\n\n{messaggio}"
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login(username,password)
    print("Sto inviando...")
    email.sendmail(username, destinatario, contenuto)
    email.quit()
    print("Messaggio Inviato!")

postino()
'''
'''
ESERCIZIO 29
Scrivi una funzione "cercatrice" che scansioni un dato percorso di sistema alla ricerca di file di tipo pdf.
La funzione dovrà avere le seguenti caratteristiche:

    Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
    La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
    In fine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la scansione.
'''
'''
failed
'''
'''
import os

def cercatrice(percorso):
    if not os.path.isdir(percorso):
        print(f"Il percorso inserito '{percorso}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return None
    contatore = 0
    print(f"Sto effettuando la scansione di '{percorso}' alla ricerca di file .pdf\n")
    for cartella, sottocartelle, files in os.walk(percorso):
        for file in files:
            if file.endswith(".pdf"):
                pdf = os.path.join(cartella,file)
                print(f"Trovato file pdf: {pdf}\n")
                contatore += 1
    print(f"\nScansione Ultimata! Ho trovato {contatore} files con estensione pdf.")
'''
'''
Esercizio 30
Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:

    Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
    Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
    La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste
'''
'''
failed
'''
'''
import os
import shutil

def file_backup():
    print("Ciao! Questo script effettua copie di backup per file di un'estensione passata come input.\n")
    percorso = input("Inserisci il percorso da scansionare: ")
    if not os.path.isdir(percorso):
        print(f"Il percorso inserito '{percorso}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return file_backup()
    estensione = input("Che tipologia di file desideri salvare? [esempio: .jpg .pdf .epub]: ")
    backup_folder = input("Inserisci la cartella dove desideri salvare i tuoi file: ")
    if not os.path.isdir(backup_folder):
      	 os.makedirs(backup_folder)
    contatore = 0
    print(f"Sto effettuando la scansione di '{percorso}' alla ricerca di file '{estensione}'\n")
    for cartella, sottocartelle, files in os.walk(percorso):
        for file in files:
            if file.endswith(estensione):
                match = os.path.join(cartella,file)
                print(f"Trovato file {estensione}: {match}")
                shutil.copy(match,backup_folder)
                contatore += 1
    print("Copia Terminata")
    print(f"Ho trovato '{contatore}' files con estensione {estensione}, ora disponibili anche in '{backup_folder}'")
'''