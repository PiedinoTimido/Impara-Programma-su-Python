import time  # Importa il modulo time per usare la funzione sleep
import sys   # Importa il modulo sys per uscire dal programma

# Lezioni 1, 2, 3, 4 e 5 su Python
print("ATTENZIONE! PER ESEGUIRE I CODICI SPIEGATI IN QUESTA SERIE DI LEZIONI è NECESSARIO SCARICARE LA VERSIONE 3 DI PYTHON (tutte le sotto-versioni sono accettate! es 3.14)")
time.sleep(4)

while True: # Ciclo principale per tornare al menu
    print("\n--- MENU PRINCIPALE ---")
    print("Ciao! Benvenuto nel programma di lezioni Python! Scegli tra le seguenti opzioni qual è la migliore: ")
    print("1: Lezione 1 (Hello, World!)")
    print("2: Lezione 2 (Variabili)")
    print("3: Lezione 3 (Conversioni fra Stringhe e Numeri)")
    print("4: Lezione 4 (Operatori e Strutture di Controllo)")
    print("5: Lezione 5 (Le Strutture di Dati)")
    print("6: Esercizi")
    print("------------------------------------------------------------------")
    print("WORK IN PROGRESS, PREVIEW PRIVATA! NON SCATTARE SCREENSHOT O CONDIVIDERE IL PROGETTO!")
    print("Scrivi 'Esci' per uscire dal programma")
    Scelta_Generale = input("Scelta: ").lower() # Convertiamo l'input in minuscolo per facilitare il confronto

    if Scelta_Generale == "1": # Lezione 1 (Hello World)
        print("\n--- SEZIONE LEZIONE 1 (Hello World) ---")
        print("È stata scelta la lezione!")
        time.sleep(2)
        print("In questa prima lezione vedremo come fare la primissima stringa di codice mai fatta, l'Hello World!")
        time.sleep(2)
        print("Per scrivere l'Hello World bisogna usare la funzione print() che poi DEVE essere seguita da una parentesi.")
        time.sleep(2)
        print("Poi bisogna capire che cosa dovrai fare uscire dalla funzione print().")
        print("Se è un numero si può scrivere nelle parentesi senza nessuna aggiunta, se invece è una stringa, cioè una frase, bisogna aggiunger")
        time.sleep(2)
        print("Dato che è una frase dobbiamo usare le virgolette ed infine far partire il programma.")
        time.sleep(2)

        while True:
            RispostaLezioneHW = input("Ora prova tu, scrivi il comando print() con la frase Hello, World!: ")

            if RispostaLezioneHW == 'print("Hello, World!")':
                print("È corretto! Complimenti! Hai completato la lezione!")
                time.sleep(2)
                break
            else:
                print("Ops, sembra che sia sbagliato! Riprova e fai attenzione alla sintassi!")
    
    elif Scelta_Generale == "2": # Lezione 2 (Variabili, Operatori e Strutture di Controllo)
        print("\n--- SEZIONE LEZIONE 2 (Variabili, Operatori e Strutture di Controllo) ---")
        time.sleep(3)
        print("I programmi che usiamo ogni giorno si basano su variabili che sono come dei cassetti temporanei. Le variabili si dividono in Nomi e Tipi (o Classi).")
        time.sleep(3)
        print("Nella lezione 1 abbiamo visto che ci sono 2 tipi: le stringhe (testo) e i numeri. Ma ce n'è un terzo, i valori di verità che sono True (Vero) e False (Falso).")
        time.sleep(3)
        print("Invece, i nomi sono delle etichette che diamo alle variabili per capirne lo scopo velocemente.")
        time.sleep(3)
        print("Oltre alle variabili, che come dice il nome cambiano spesso, ci possono essere delle costanti.")
        time.sleep(3)
        print("Le costanti sono molto simili alle variabili, ma il loro valore non dovrebbe essere modificato durante l'esecuzione del programma. Anche per logica!")
        time.sleep(3)
        print("Prendiamo come esempio il Pi Greco (π), il suo valore è circa 3.14 ed è quindi inutile modificarlo.")
        time.sleep(3)
        print("Ora vedremo come fare un piccolo programma per chiedere all'utente una frase che poi il computer riscriverà.")
        time.sleep(3)
        
        NomeVariabile = input("Iniziamo creando una variabile: scegli un nome per essa (es. 'mia_frase'): ")
        
        print(f"Bel nome! Hai scelto '{NomeVariabile}'. Ora, per impostare il valore di una variabile usando l'input dell'utente, mettiamo un uguale '=' e usiamo la funzione input() senza spazi, seguita dalle parentesi.")
        print(f"La riga di codice completa dovrebbe essere: {NomeVariabile} = input()")
        
        while True:
            RispostaLezione = input(f"Prova a scrivere la parte di codice per assegnare l'input alla tua variabile '{NomeVariabile}': ")
            
            if RispostaLezione == '= input()':
                print("È corretto! Ottimo! Ora la tua variabile è pronta per ricevere l'input dell'utente.")
                time.sleep(2)
                print("Adesso, per far apparire una domanda all'utente quando chiederai l'input, devi mettere la domanda tra virgolette dentro le parentesi della funzione input().")
                print("Esempio: input(\"Qual è il tuo numero fortunato?\")")
                print("Nella tua riga di codice, la domanda 'Qual è il tuo numero fortunato?' andrà qui:")
                print(f"{NomeVariabile} = input(\"Qual è il tuo numero fortunato?\")")
                time.sleep(3)

                while True:
                    DomandaVariabile = input(f"Inserisci la domanda tra virgolette che vuoi che appaia: ") 
                    
                    if DomandaVariabile == '"Qual\'è il tuo numero fortunato?"' or DomandaVariabile == "\"Qual'è il tuo numero fortunato?\"":
                        print("È corretto! Ottimo! Ora, grazie a questa funzione, l'utente può inserire qualsiasi cosa e il valore verrà salvato nella tua variabile!")
                        time.sleep(2)
                        print("Infine, per visualizzare il contenuto della variabile, basta usare il comando print() e tra le parentesi scrivere il nome della tua variabile, SENZA LE DOPPIE VIRGOLETTE.")
                        print(f"L'istruzione completa dovrebbe essere: print({NomeVariabile})")
                        time.sleep(3)

                        while True:
                            RispostaFinale = input("Ora scrivi il comando print() per stampare il contenuto della tua variabile: ")
                            
                            if RispostaFinale == 'print(' + NomeVariabile + ')':
                                print("Perfetto! Hai completato la lezione! Hai imparato a creare, dare un nome e stampare una variabile!")
                                time.sleep(2)
                                break 
                            else:
                                print(f"Ops! Sembra che tu abbia sbagliato a scrivere il comando print() o il nome della variabile. Devi scrivere solo: print({NomeVariabile})")
                                print(f"Se non ti ricordi il nome della tua variabile, eccolo: {NomeVariabile}")
                                time.sleep(2)
                        break 
                    else:
                        print("Ops, è sbagliato. Assicurati di includere le virgolette e di scrivere la frase esattamente come richiesto (Qual'è il tuo numero fortunato?).")
                        print("Esempio di risposta corretta: \"Qual'è il tuo numero fortunato?\"")
                        time.sleep(2)
                break 
            else:
                print(f"Ops, sembra che sia sbagliato! Riprova e ricorda che devi aggiungere '= input()' dopo il nome della tua variabile '{NomeVariabile}'.")
                print(f"La riga di codice completa dovrebbe essere: {NomeVariabile} = input()")
                time.sleep(2)
        
        print("Fine della Lezione 2. Torno al menu principale.")
        time.sleep(2)

    elif Scelta_Generale == "3": # Lezione 3 (Conversioni fra Stringhe e Numeri)
        print("\n--- SEZIONE LEZIONE 3 (Conversioni fra Stringhe e Numeri) ---")
        time.sleep(2)
        print("Se sei interessato a creare un programma che verifica se l'età inserita dall'utente è valida, ad esempio per capire se puoi prendere la patente, ti ritrovi davanti a un problema:")
        time.sleep(2)
        print("Quando usi la funzione input(), tutti i dati inseriti sono trattati come stringhe, quindi non puoi eseguire operazioni numeriche (come addizioni, sottrazioni, o confronti con numeri) direttamente su di essi.")
        time.sleep(2)
        print("Prima di tutto, bisogna capire se l'input dell'utente è un numero. Per farlo, controlliamo che il valore inserito sia effettivamente composto da cifre.")
        time.sleep(2)
        print("Si usa la funzione `variabile.isdigit()`. Attenzione: questa funzione controlla se la stringa contiene SOLO cifre. Se vogliamo verificare che NON sia una parola, si usa `not` davanti: `if not variabile.isdigit():`")
        time.sleep(2)
        print("Quindi, il problema dell'utente che non inserisce un numero ma una stringa è aggiustato. Ma ora ritorna il problema dell'input: tutto quello digitato nell'input è una stringa!")
        time.sleep(2)
        print("Per questo, Python utilizza la funzione `int()` (per numeri interi) o `float()` (per numeri decimali). Ora farai uno script per capire come funziona.")
        time.sleep(3)

        while True:
            stringa1 = input("Iniziamo creando la variabile per l'input: Metti come nome della variabile 'eta_utente' e come domanda 'Quanti anni hai?': ")
            if stringa1 == 'eta_utente = input("Quanti anni hai?")':
                print("Ok! La prima riga è completata! Hai creato una variabile che chiederà all'utente la sua età.")
                time.sleep(2)
                print("Ora continuiamo verificando che l'input dell'utente sia effettivamente un numero, per evitare errori se digita del testo.")
                
                while True:
                    Stringa2 = input("Ora, per evitare che Python cerchi di convertire una frase in un numero, usa `if not variabile.isdigit():`. Scrivi il codice e ricorda che dopo aver scritto un `if` o `else` bisogna mettere i due punti `:`: ")
                    if Stringa2 == "if not eta_utente.isdigit():":
                        print("Ok! Perfetto! Hai aggiunto il controllo per assicurarti che l'input sia numerico.")
                        time.sleep(2)
                        print("Ora manca un passaggio fondamentale: convertire la stringa che l'utente ha digitato in un vero numero (un intero) con la funzione `int()`.")
                        
                        while True:
                            Stringa3 = input("Per convertire la stringa con `int()`, crea una nuova variabile (chiamiamola `eta_numerica`) e imposta il suo valore sulla versione `int` della variabile `eta_utente`. Scrivi così: `eta_numerica = int(eta_utente)`: ")
                            if Stringa3 == "eta_numerica = int(eta_utente)":
                                print("Complimenti! Hai completato la lezione 3! Hai imparato a convertire l'input da stringa a numero e a fare un controllo di base.")
                                print("Ricorda che di solito, dentro il blocco `if not ...:` dovresti aggiungere un messaggio di errore e un modo per uscire o riprovare, ma per ora ci siamo concentrati sulla conversione.")
                                time.sleep(4)
                                break
                            else:
                                print("Ops, sembra che ci sia un errore! Controlla la sintassi e riprova. Ricorda che è: `eta_numerica = int(eta_utente)`")
                                time.sleep(2)
                        break
                    else:
                        print("Ops, sembra che ci sia un errore! Controlla la sintassi e riprova. Ricorda il nome della variabile è 'eta_utente' e devi includere i due punti alla fine.")
                        time.sleep(2)
                break
            else:
                print("Ops, sembra che ci sia un errore! Controlla la sintassi e riprova. Ricorda di impostare la variabile 'eta_utente' con `input(\"Quanti anni hai?\")`.")
                print("La riga corretta è: `eta_utente = input(\"Quanti anni hai?\")`")
                time.sleep(2)
        
        print("Fine della Lezione 3. Torno al menu principale.")
        time.sleep(2)
        
    elif Scelta_Generale == "4": # Lezione 4 (Operatori e Strutture di Controllo)
        print("\n--- SEZIONE LEZIONE 4 (Operatori, Condizioni e Cicli) ---")
        time.sleep(2)
        print("In questa lezione vedremo come usare gli operatori per fare calcoli e confronti, le strutture di controllo per prendere decisioni e ripetere azioni e, infine, il significato di alcune parole chiave fondamentali di Python.")
        time.sleep(3)
        
        # --- PAROLE CHIAVE DI PYTHON ---
        print("\n--- PAROLE CHIAVE DI PYTHON ---")
        print("Le parole chiave (o keyword) sono parole speciali che hanno un significato preciso in Python. Non puoi usarle come nomi per le tue variabili o funzioni.")
        time.sleep(3)
        print("Ecco una lista di alcune delle più importanti parole chiave che incontrerai, con una breve spiegazione:")
        print("`print`: per stampare testo o valori a schermo (l'hai già usata!).")
        print("`if`, `elif`, `else`: per le strutture di controllo condizionali.")
        print("`for`, `while`: per i cicli e le iterazioni.")
        print("`break`: per uscire da un ciclo.")
        print("`continue`: per passare all'iterazione successiva di un ciclo.")
        print("`and`, `or`, `not`: per gli operatori logici.")
        print("`import`, `from`: per importare moduli e librerie (hai visto `import time`!).")
        print("`in`: per controllare se un elemento è presente in una sequenza (es. `for elemento in lista`).")
        print("`def`: per definire una funzione.")
        print("`return`: per restituire un valore da una funzione.")
        print("`class`: per definire una classe (usata nella programmazione a oggetti).")
        print("`try`, `except`, `finally`: per gestire gli errori (eccezioni).")
        print("`pass`: una dichiarazione che non fa nulla, usata come segnaposto.")
        time.sleep(12)
        print("\nCi sono molte altre parole chiave come `global`, `is`, `del`, `with`, `as`, `lambda`, `assert`, `exec`, `raise` e `yield`, ma le incontrerai più avanti nel tuo percorso. È utile sapere che esistono!")
        time.sleep(5)
        
        # --- OPERATORI ---
        print("\n--- OPERATORI ---")
        time.sleep(2)
        
        # --- Operatori Aritmetici ---
        print("\n**Operatori Aritmetici**")
        print("Questi operatori servono a fare calcoli matematici. Ecco i principali:")
        print("+  (addizione)")
        print("-  (sottrazione)")
        print("* (moltiplicazione)")
        print("/  (divisione normale, restituisce un numero decimale)")
        print("// (divisione intera, restituisce solo il numero intero)")
        print("%  (modulo, restituisce il resto della divisione)")
        print("** (esponenziale, eleva a potenza)")
        time.sleep(5)
        print("\nVediamo un esempio con i numeri e poi con le stringhe, dato che l'operatore `+` si comporta in modo diverso!")
        time.sleep(3)
        
        print("Esempio con i numeri:")
        print("numero1 = 10")
        print("numero2 = 3")
        print("somma = numero1 + numero2")
        print("modulo = numero1 % numero2 # 10 diviso 3 fa 3 con resto 1")
        print("print(f\"Somma: {somma}\")")
        print("print(f\"Modulo: {modulo}\")")
        time.sleep(4)
        
        print("Esempio con le stringhe:")
        print("saluto = \"Ciao, \"")
        print("nome = \"mondo!\"")
        print("messaggio = saluto + nome # Concatenazione (unione di stringhe)")
        print("print(messaggio)  # Il risultato è 'Ciao, mondo!'")
        time.sleep(4)
        print("Come vedi, l'operatore `+` ha due funzioni diverse a seconda del tipo di dato che usi!")
        time.sleep(3)
        
        # --- Operatori Relazionali ---
        print("\n**Operatori Relazionali**")
        print("Questi operatori confrontano due valori e restituiscono un valore di verità: **True** (Vero) o **False** (Falso).")
        time.sleep(3)
        print("Ecco i principali operatori relazionali:")
        print("== (uguale a)")
        print("!= (diverso da)")
        print(">  (maggiore di)")
        print("<  (minore di)")
        print(">= (maggiore o uguale a)")
        print("<= (minore o uguale a)")
        time.sleep(4)
        
        print("\nOra vediamo un esempio pratico con l'età.")
        time.sleep(2)
        while True:
            eta_utente = input("Per prima cosa, inserisci la tua età (un numero!): ")
            if not eta_utente.isdigit():
                print("Ops, l'età deve essere un numero! Riprova.")
                continue
            
            eta_numerica = int(eta_utente)
            
            print(f"La tua età è {eta_numerica}.")
            time.sleep(2)
            print("Verifichiamo se sei maggiorenne (maggiore o uguale a 18):")
            time.sleep(1)
            
            risultato_confronto = eta_numerica >= 18
            
            print(f"La verifica `eta_numerica >= 18` restituisce: {risultato_confronto}")
            time.sleep(2)
            break
            
        # --- Operatori Logici ---
        print("\n**Operatori Logici**")
        print("Questi operatori combinano più condizioni e restituiscono un valore di verità.")
        time.sleep(2)
        print("Ecco i principali:")
        print("**and** (vero se ENTRAMBE le condizioni sono vere)")
        print("**or** (vero se ALMENO UNA delle condizioni è vera)")
        print("**not** (inverte il valore di verità: True diventa False e viceversa)")
        time.sleep(4)
        
        print("\nEsempio di login con `and`:")
        print("username = 'admin'")
        print("password = '1234'")
        print("if username == 'admin' and password == '1234':")
        print("    print('Accesso consentito.')")
        print("else:")
        print("    print('Accesso negato.')")
        time.sleep(5)

        # --- Aritmetica Binaria e Operatori Bit a Bit ---
        print("\n--- ARITMETICA BINARIA E OPERATORI BIT A BIT ---")
        print("Questa è una sezione più avanzata. Lavoriamo sui **bit**, i mattoncini fondamentali dei numeri (0 e 1).")
        time.sleep(3)
        print("Per Python, puoi rappresentare un numero binario con il prefisso `0b`. Ad esempio, `0b101` è il numero 5.")
        time.sleep(3)
        
        print("\nEcco gli operatori bit a bit:")
        print("`&` (AND binario): Confronta i bit, se entrambi sono 1, il risultato è 1. Altrimenti 0.")
        print("`|` (OR binario): Confronta i bit, se almeno uno è 1, il risultato è 1. Altrimenti 0.")
        print("`^` (XOR binario): Confronta i bit, se sono diversi (uno 0 e uno 1), il risultato è 1. Altrimenti 0.")
        print("`~` (NOT binario): Inverte i bit (0 diventa 1 e 1 diventa 0).")
        print("`<<` (SHIFT a sinistra): Sposta i bit a sinistra, aggiungendo 0 a destra. Moltiplica per 2 per ogni shift.")
        print("`>>` (SHIFT a destra): Sposta i bit a destra, scartando i bit a destra. Divide per 2 per ogni shift.")
        time.sleep(8)

        print("\nEsempio pratico con i numeri decimali 5 (`0b101`) e 3 (`0b011`):")
        print("numero1 = 5  # Binario: 0b101")
        print("numero2 = 3  # Binario: 0b011")
        time.sleep(2)
        print(f"5 & 3 = {5 & 3} (0b101 & 0b011 = 0b001, che è 1)")
        print(f"5 | 3 = {5 | 3} (0b101 | 0b011 = 0b111, che è 7)")
        print(f"5 << 1 = {5 << 1} (0b101 << 1 = 0b1010, che è 10)")
        time.sleep(5)
        print("Gli operatori bit a bit sono usati in aree come la crittografia, i protocolli di rete o l'ottimizzazione di basso livello. Non ti preoccupare se all'inizio sembrano complessi, l'importante è sapere che esistono!")
        time.sleep(4)

        # --- STRUTTURE DI CONTROLLO CONDIZIONALI (if-elif-else) ---
        print("\n--- STRUTTURE DI CONTROLLO CONDIZIONALI (IF, ELIF, ELSE) ---")
        time.sleep(2)
        print("Le strutture di controllo ci permettono di eseguire del codice solo se una condizione è vera.")
        time.sleep(2)
        print("Il costrutto `if` è il più comune e si basa su condizioni `True` o `False`.")
        time.sleep(3)
        
        print("Vediamo un esempio completo con `if`, `elif` e `else` per controllare l'età.")
        time.sleep(2)
        
        while True:
            eta_patente_str = input("Inserisci la tua età per vedere se puoi prendere la patente in Italia (18 anni): ")
            if not eta_patente_str.isdigit():
                print("Inserisci un numero valido! Riprova.")
                continue
            
            eta_patente = int(eta_patente_str)
            
            print(f"Analizzo la tua età: {eta_patente}")
            time.sleep(1)
            
            if eta_patente >= 18:
                print("Complimenti! Puoi prendere la patente in Italia.")
            elif eta_patente >= 16:
                print("Non puoi prendere la patente per l'auto, ma puoi prendere il patentino per il motorino!")
            else:
                print("Non puoi ancora prendere la patente. Pazienza!")
            
            time.sleep(2)
            break

        # --- STRUTTURE DI CONTROLLO ITERATIVE (Cicli) ---
        print("\n--- STRUTTURE DI CONTROLLO ITERATIVE (CICLI) ---")
        time.sleep(2)
        print("I cicli ci permettono di ripetere un blocco di codice più volte, evitando di riscriverlo.")
        time.sleep(2)
        
        # --- Ciclo WHILE ---
        print("\n**Il ciclo `while`**")
        print("Il ciclo `while` ripete il suo codice **finché una condizione rimane vera**.")
        print("È utile quando non sai in anticipo quante volte devi ripetere un'azione.")
        time.sleep(3)
        
        print("Esempio: un semplice contatore da 1 a 5:")
        print("contatore = 1")
        print("while contatore <= 5:")
        print("    print(contatore)")
        print("    contatore = contatore + 1  # Questo aggiornamento è FONDAMENTALE!")
        time.sleep(5)
        
        print("Se non aggiorni il `contatore`, il ciclo non si fermerà mai! Si chiama **ciclo infinito**.")
        time.sleep(3)

        # --- Simulazione del ciclo DO-WHILE ---
        print("\n**Simulazione del ciclo `do-while`**")
        print("Python non ha un ciclo `do-while` nativo, ma possiamo simularlo con `while True` e un `break`.")
        time.sleep(3)
        print("La logica è: 'Esegui il codice **almeno una volta**, poi controlla la condizione'.")
        time.sleep(3)
        
        print("Esempio: chiedere un numero positivo all'utente:")
        print("while True:")
        print("    numero_str = input(\"Inserisci un numero positivo: \")")
        print("    if numero_str.isdigit():")
        print("        numero = int(numero_str)")
        print("        if numero > 0:")
        print("            print(\"Grazie! Hai inserito un numero positivo.\")")
        print("            break # Ferma il ciclo")
        print("    print(\"Input non valido. Riprova.\")")
        time.sleep(7)
        print("Il codice viene eseguito e solo se la condizione (`numero > 0`) è vera, il ciclo viene interrotto con `break`.")
        time.sleep(4)
        
        # --- Ciclo FOR ---
        print("\n**Il ciclo `for`**")
        print("Il ciclo `for` è usato per **scorrere gli elementi di una sequenza** (come una lista o un intervallo).")
        print("È perfetto quando sai già quante volte devi ripetere un'azione.")
        time.sleep(3)
        
        print("Esempio: stampare i numeri da 0 a 4 usando `range()`:")
        print("for i in range(5): # range(5) crea una sequenza di numeri da 0 a 4")
        print("    print(i)")
        time.sleep(4)
        
        print("\nEsempio: stampare ogni lettera di una parola:")
        print("parola = \"Python\"")
        print("for lettera in parola:")
        print("    print(lettera)")
        time.sleep(4)

        print("\nPerfetto! Ora sai usare gli operatori, le condizioni e i cicli. Ottimo lavoro!")
        time.sleep(2)
        
        print("Fine della Lezione 4. Torno al menu principale.")
        time.sleep(2)
        
    elif Scelta_Generale == "5": # Lezione 5 (Le Strutture di Dati)
        print("\n--- SEZIONE LEZIONE 5 (Le Strutture di Dati) ---")
        time.sleep(2)   
        print("Spesso si lavora con delle variabili ma se si vogliono memorizzare più valori, si usano le strutture di dati.")
        time.sleep(2)
        print("Prendiamo per esempio che siamo in un hotel e vogliamo memorizzare i nomi degli ospiti.")
        time.sleep(2)
        print("Per farlo, possiamo usare una lista, che è una struttura di dati che permette di memorizzare più valori in un'unica variabile.")
        time.sleep(2)
        print("Le strutture di dati di python sono le liste, le tuple, i dizionari, gli insiemi e le enumerazioni.")
        time.sleep(2)
        
        # --- Liste ---
        print("\n**Le Liste**")
        print("Le liste sono collezioni ordinate di elementi, che possono essere di qualsiasi tipo (numeri, stringhe, altri oggetti).")
        time.sleep(2)
        print("Si definiscono con le parentesi quadre `[]` e gli elementi sono separati da virgole.")
        time.sleep(2)
        print("Esempio di lista di nomi:")
        print("nomi_ospiti = ['Alice', 'Bob', 'Charlie']")
        time.sleep(2)
        print("Puoi accedere agli elementi della lista usando l'indice (partendo da 0):")
        print("print(nomi_ospiti[0])  # Stampa 'Alice'")
        time.sleep(2)
        print("Puoi aggiungere un elemento alla lista con `append()`:")
        print("nomi_ospiti.append('David')  # Aggiunge 'David' alla fine della lista")
        time.sleep(2)
        print("Puoi rimuovere un elemento con `remove()`:")
        print("nomi_ospiti.remove('Bob')  # Rimuove 'Bob' dalla lista")
        time.sleep(2)   
        print("Puoi anche ordinare la lista con `sort()`:") 
        print("nomi_ospiti.sort()  # Ordina la lista in ordine alfabetico")
        time.sleep(2)
        print("Le liste sono molto flessibili e utili per memorizzare collezioni di dati.")
        time.sleep(2)

        # --- ESERCIZI DI ALLENAMENTO - LISTE ---
        print("\n--- ESERCIZI DI ALLENAMENTO: LISTE ---")
        print("Mettiamo subito in pratica ciò che hai imparato!")
        
        # Esercizio 1: Creare una lista
        print("\n**Esercizio 1: Crea una lista di tuoi hobby.**")
        print("Crea una lista chiamata `i_miei_hobby` con almeno 3 hobby (es. 'lettura', 'cucina', 'sport').")
        while True:
            risposta_hobby = input("Scrivi la riga di codice per creare la lista: ")
            if risposta_hobby.strip() == "i_miei_hobby = ['lettura', 'cucina', 'sport']":
                print("Ottimo! Lista creata correttamente.")
                break
            else:
                print("Non è corretto. Ricorda di usare le parentesi quadre e le virgolette per le stringhe.")
                
        # Esercizio 2: Accedere a un elemento
        print("\n**Esercizio 2: Accedi e stampa il secondo elemento della tua lista.**")
        print("Ricorda che l'indice parte da 0!")
        while True:
            risposta_accesso = input("Scrivi la riga di codice per stampare il secondo hobby: ")
            if risposta_accesso.strip() == "print(i_miei_hobby[1])":
                print("Fantastico! Hai stampato l'elemento corretto.")
                break
            else:
                print("Sbagliato. L'indice del secondo elemento è 1, non 2. Riprova.")
                
        # Esercizio 3: Aggiungere un elemento
        print("\n**Esercizio 3: Aggiungi un nuovo hobby alla tua lista.**")
        print("Usa il metodo `append()` per aggiungere un hobby a tua scelta alla fine della lista `i_miei_hobby`.")
        while True:
            risposta_append = input("Scrivi la riga di codice per aggiungere un hobby: ")
            if risposta_append.strip() == "i_miei_hobby.append('viaggiare')":
                print("Perfetto! Il tuo hobby è stato aggiunto. La lista aggiornata è:")
                print("['lettura', 'cucina', 'sport', 'viaggiare']")
                break
            else:
                print("Non è corretto. Ricorda la sintassi `lista.append(elemento)`. Riprova.")
        
        # --- Tuple ---
        print("\n**Le Tuple**")
        print("Le tuple sono simili alle liste, ma sono **immutabili**, cioè non puoi modificarle dopo averle create.")
        time.sleep(2)
        print("Si definiscono con le parentesi tonde `()` e sono utili quando vuoi garantire che i dati non vengano modificati.")
        time.sleep(2)
        print("Esempio di tupla di coordinate:")
        print("coordinate = (10, 20)  # Tupla con due valori")
        time.sleep(2)
        print("Puoi accedere agli elementi della tupla come nelle liste, ma non puoi modificarli:")
        print("print(coordinate[0])  # Stampa 10")
        time.sleep(2)
        print("Le tuple sono utili per rappresentare dati che non devono cambiare, come le coordinate di un punto.")
        time.sleep(2)
        
        # --- ESERCIZI DI ALLENAMENTO - TUPLE ---
        print("\n--- ESERCIZI DI ALLENAMENTO: TUPLE ---")
        
        # Esercizio 4: Creare una tupla
        print("\n**Esercizio 4: Crea una tupla dei giorni della settimana (solo i primi tre).**")
        print("Creala con i nomi dei giorni: 'Lun', 'Mar', 'Mer'. Chiamala `giorni_lavorativi`.")
        while True:
            risposta_tupla = input("Scrivi la riga di codice per creare la tupla: ")
            if risposta_tupla.strip() == "giorni_lavorativi = ('Lun', 'Mar', 'Mer')":
                print("Esatto! Tupla creata correttamente.")
                break
            else:
                print("Sbagliato. Ricorda di usare le parentesi tonde `()`.")
        
        # Esercizio 5: Accedere a un elemento della tupla
        print("\n**Esercizio 5: Stampa il terzo giorno della tupla.**")
        while True:
            risposta_accesso_tupla = input("Scrivi la riga di codice per stampare il terzo elemento: ")
            if risposta_accesso_tupla.strip() == "print(giorni_lavorativi[2])":
                print("Corretto! Stai diventando un esperto!")
                break
            else:
                print("Sbagliato. Controlla l'indice corretto. Riprova.")
        
        # --- Dizionari ---
        print("\n**I Dizionari**")
        print("I dizionari sono strutture di dati che memorizzano coppie chiave-valore, simili a un elenco telefonico.")
        time.sleep(2)
        print("Si definiscono con le parentesi graffe `{}` e le chiavi sono uniche.")
        time.sleep(2)
        print("Esempio di dizionario di un contatto:")
        print("contatto = {'nome': 'Alice', 'telefono': '1234567890', 'email': 'alice@email.com'}")
        time.sleep(2)
        print("Puoi accedere ai valori usando le chiavi:")
        print("print(contatto['nome'])  # Stampa 'Alice'")
        time.sleep(2)
        print("Puoi aggiungere o modificare un elemento con la chiave:")
        print("contatto['indirizzo'] = 'Via Roma 1'  # Aggiunge un nuovo elemento")
        time.sleep(2)
        print("Puoi rimuovere un elemento con `del`:")
        print("del contatto['telefono']  # Rimuove l'elemento con chiave 'telefono'")
        time.sleep(2)
        print("I dizionari sono molto utili per memorizzare dati strutturati e accedervi rapidamente.")
        time.sleep(2) 
        
        # --- ESERCIZI DI ALLENAMENTO - DIZIONARI ---
        print("\n--- ESERCIZI DI ALLENAMENTO: DIZIONARI ---")
        
        # Esercizio 6: Creare un dizionario
        print("\n**Esercizio 6: Crea un dizionario per un libro.**")
        print("Crealo con le chiavi 'titolo', 'autore' e 'anno_pubblicazione'.")
        while True:
            risposta_dizionario = input("Scrivi la riga di codice per creare il dizionario `libro`: ")
            if risposta_dizionario.strip() == "libro = {'titolo': 'Il Signore degli Anelli', 'autore': 'J.R.R. Tolkien', 'anno_pubblicazione': 1954}":
                print("Ottimo! Dizionario creato correttamente.")
                break
            else:
                print("Non è corretto. Ricorda di usare le parentesi graffe `{}` e le coppie chiave-valore.")
                
        # Esercizio 7: Aggiungere un valore al dizionario
        print("\n**Esercizio 7: Aggiungi la chiave 'genere' al dizionario `libro`.**")
        while True:
            risposta_aggiungi_diz = input("Scrivi la riga di codice per aggiungere il genere 'Fantasy': ")
            if risposta_aggiungi_diz.strip() == "libro['genere'] = 'Fantasy'":
                print("Perfetto! Il dizionario è stato aggiornato. Ora contiene anche il genere.")
                break
            else:
                print("Sbagliato. Ricorda la sintassi `dizionario[chiave] = valore`. Riprova.")
        
        # --- Insiemi ---
        print("\n**Gli Insiemi**")
        print("Gli insiemi sono collezioni non ordinate di elementi unici, simili a un insieme matematico.")
        time.sleep(2)   
        print("Si definiscono con le parentesi graffe `{}` o con la funzione `set()`.")
        time.sleep(2)
        print("Esempio di insieme di numeri:")
        print("numeri_unici = {1, 2, 3, 4, 5}")
        time.sleep(2)
        print("Puoi aggiungere un elemento con `add()`:")
        print("numeri_unici.add(6)  # Aggiunge 6 all'insieme")
        time.sleep(2)
        print("Puoi rimuovere un elemento con `remove()`:")
        print("numeri_unici.remove(3)  # Rimuove 3 dall'insieme")
        time.sleep(2)
        print("Gli insiemi sono utili per operazioni matematiche come unioni, intersezioni e differenze tra collezioni di dati.")
        time.sleep(2)
        
        # --- ESERCIZI DI ALLENAMENTO - INSIEMI ---
        print("\n--- ESERCIZI DI ALLENAMENTO: INSIEMI ---")
        
        # Esercizio 8: Creare un insieme e aggiungere un elemento
        print("\n**Esercizio 8: Crea un insieme di colori e aggiungine uno nuovo.**")
        print("Crea un insieme `colori = {'rosso', 'verde', 'blu'}` e aggiungi 'giallo'.")
        while True:
            risposta_set = input("Scrivi le righe di codice: ")
            if risposta_set.strip() == "colori = {'rosso', 'verde', 'blu'}\ncolori.add('giallo')":
                print("Molto bene! L'insieme è stato aggiornato correttamente.")
                break
            else:
                print("Non è corretto. Controlla la sintassi per creare l'insieme e usare `add()`. Riprova.")
                
        # --- Enumerazioni ---
        print("\n**Le Enumerazioni**")
        print("Le enumerazioni (o enum) sono un modo per definire un insieme di costanti con nomi significativi.")
        time.sleep(2)
        print("In Python, puoi usare la libreria `enum` per creare enumerazioni.")
        time.sleep(2)
        print("Esempio di enumerazione dei giorni della settimana:")
        print("from enum import Enum")
        print("class Giorni(Enum):")
        print("    LUNEDI = 1")
        print("    MARTEDI = 2")
        print("    MERCOLEDI = 3")
        print("    GIOVEDI = 4")
        print("    VENERDI = 5")
        print("    SABATO = 6")
        print("    DOMENICA = 7")
        time.sleep(2)
        print("Puoi accedere ai valori dell'enumerazione usando il nome della classe e il nome del membro:")
        print("print(Giorni.LUNEDI)  # Stampa 'Giorni.LUNEDI'")
        time.sleep(2)
        print("Le enumerazioni sono utili per rappresentare insiemi di costanti con nomi significativi, migliorando la leggibilità del codice.")
        time.sleep(2)
        print("\nHai completato la Lezione 5! Ora conosci le principali strutture di dati di Python e come usarle.")
        print("Fine della Lezione 5. Torno al menu principale.")
        time.sleep(2)
    
    elif Scelta_Generale == "6": # Se l'utente sceglie "6" per gli esercizi
        while True: # Ciclo per la sezione esercizi per permettere di scegliere tra lezioni o tornare al menu
            print("\n--- SEZIONE ESERCIZI ---")
            print("Quale lezione di esercizi vuoi affrontare?")
            Scelta_Esercizi_Lezione = input("1 = Lezione 1, 2 = Lezione 2, 3 = Lezione 3, 4 = Lezione 4, 5 = Lezione 5, 6 = Torna al menu principale: ")

            if Scelta_Esercizi_Lezione == "1":
                while True: # Ciclo interno per gli esercizi della Lezione 1
                    print("\n--- ESERCIZI LEZIONE 1 ---")
                    print("1: Stampa una frase a piacere.")
                    print("2: Stampa 'Ciao Mondo' 3 volte.")
                    print("3: Stampa 'Ciao' e 'Mondo' su righe separate.")
                    print("4: Stampa 'Ciao Mondo' usando due stringhe diverse (nella stessa riga o su righe diverse).")
                    print("5: Stampa 'Rosso', 'Verde', 'Blu' su 3 stringhe diverse.")
                    print("6: Modifica l'esercizio 5 per stampare le parole su righe separate con un solo `print`.")
                    print("7: Modifica l'esercizio 5 per stampare le parole con una tabulazione tra di esse con un solo `print`.")
                    print("8: Stampa la figura a croce con più `print`.")
                    print("  +")
                    print(" +++")
                    print("  +")
                    print("9: Modifica l'esercizio 8 per stampare una piramide di asterischi con un solo `print`.")
                    print("  *")
                    print(" ***")
                    print("*****")
                    print("10: Modifica l'esercizio 9 per stampare una figura a rombo con un solo `print`.")
                    print(" * * ")
                    print("* * *")
                    print(" * * ")
                
                    time.sleep(2)
                
                    Scelta_Esercizio = input("Quale esercizio della Lezione 1 vuoi vedere? Inserisci il numero (1-10) o 'torna' per tornare alla selezione esercizi: ").lower()
                
                    if Scelta_Esercizio == "1":
                        print("\n--- Soluzione Esercizio 1 ---")
                        print("print(\"Questa è la mia frase a piacere!\")")
                        print("--- Fine Esercizio 1 ---\n")
                    elif Scelta_Esercizio == "2":
                        print("\n--- Soluzione Esercizio 2 ---")
                        print("print(\"Ciao Mondo\\n\" * 3)")
                        print("# Oppure:")
                        print("print(\"Ciao Mondo\")")
                        print("print(\"Ciao Mondo\")")
                        print("print(\"Ciao Mondo\")")
                        print("--- Fine Esercizio 2 ---\n")
                    elif Scelta_Esercizio == "3":
                        print("\n--- Soluzione Esercizio 3 ---")
                        print("print(\"Ciao\\nMondo\")")
                        print("--- Fine Esercizio 3 ---\n")
                    elif Scelta_Esercizio == "4":
                        print("\n--- Soluzione Esercizio 4 ---")
                        print("print(\"Ciao\", \"Mondo\")")
                        print("# Oppure:")
                        print("print(\"Ciao\")")
                        print("print(\"Mondo\")")
                        print("--- Fine Esercizio 4 ---\n")
                    elif Scelta_Esercizio == "5":
                        print("\n--- Soluzione Esercizio 5 ---")
                        print("print(\"Rosso\")")
                        print("print(\"Verde\")")
                        print("print(\"Blu\")")
                        print("--- Fine Esercizio 5 ---\n")
                    elif Scelta_Esercizio == "6":
                        print("\n--- Soluzione Esercizio 6 ---")
                        print("print(\"Rosso\\nVerde\\nBlu\")")
                        print("--- Fine Esercizio 6 ---\n")
                    elif Scelta_Esercizio == "7":
                        print("\n--- Soluzione Esercizio 7 ---")
                        print("print(\"Rosso\\tVerde\\tBlu\")")
                        print("--- Fine Esercizio 7 ---\n")
                    elif Scelta_Esercizio == "8":
                        print("\n--- Soluzione Esercizio 8 ---")
                        print("print(\"  +\")")
                        print("print(\" +++\")")
                        print("print(\"  +\")")
                        print("--- Fine Esercizio 8 ---\n")
                    elif Scelta_Esercizio == "9":
                        print("\n--- Soluzione Esercizio 9 ---")
                        print("print(\"  *\\n ***\\n*****\")")
                        print("--- Fine Esercizio 9 ---\n")
                    elif Scelta_Esercizio == "10":
                        print("\n--- Soluzione Esercizio 10 ---")
                        print("print(\" * * \\n* * *\\n * * \")")
                        print("--- Fine Esercizio 10 ---\n")
                    elif Scelta_Esercizio == "torna":
                        print("Torno alla selezione esercizi.")
                        time.sleep(1)
                        break 
                    else:
                        print("Esercizio non trovato o scelta non valida. Per favore, scegli un numero da 1 a 10 o digita 'torna'.")
                    time.sleep(2) 
            
            elif Scelta_Esercizi_Lezione == "2":
                while True: # Ciclo interno per gli esercizi della Lezione 2
                    print("\n--- ESERCIZI LEZIONE 2 ---")
                    print("Hai scelto di fare gli esercizi sulla Lezione 2: Variabili.")
                    print("1: Crea una variabile 'nome' e assegnale il tuo nome, poi stampala.")
                    print("2: Chiedi all'utente il suo colore preferito e stampalo, dicendo: 'Il tuo colore preferito è [colore].'")
                    print("3: Assegna il valore 10 a una variabile 'x' e 20 a una variabile 'y', poi stampa la loro somma.")
                    print("4: Crea una variabile 'saluto' con 'Ciao' e una variabile 'nome_persona' con un nome a tua scelta. Stampa 'saluto' e 'nome_persona' sulla stessa riga.")
                    print("5: Simula una costante: definisci `PI_GRECO = 3.14159` e stampane il valore. Spiega perché è una costante.")
                    print("6: Chiedi all'utente la sua città di nascita e salva l'input. Poi stampa la variabile con un messaggio.")
                    print("7: Chiedi all'utente la sua età e stampa un messaggio come: 'Hai [età] anni.'")
                    print("8: Definisci una variabile booleana `ha_patente = True`. Stampa il valore di questa variabile.")
                    print("9: Scrivi un programma che chieda all'utente il nome di un animale e il suo verso, poi stampi una frase come: 'Il [animale] fa [verso]'.")
                    print("10: Chiedi all'utente due numeri, salvali in variabili diverse, poi stampa il prodotto dei due numeri.")
                    
                    time.sleep(2)
                    Scelta_Esercizio = input("Quale esercizio della Lezione 2 vuoi vedere? Inserisci il numero (1-10) o 'torna' per tornare alla selezione esercizi: ").lower()

                    if Scelta_Esercizio == "1":
                        print("\n--- Soluzione Esercizio 1 ---")
                        print("nome = \"Alice\"")
                        print("print(nome)")
                        print("--- Fine Esercizio 1 ---\n")
                    elif Scelta_Esercizio == "2":
                        print("\n--- Soluzione Esercizio 2 ---")
                        print("colore_preferito = input(\"Qual è il tuo colore preferito?: \")")
                        print("print(f\"Il tuo colore preferito è {colore_preferito}.\")")
                        print("--- Fine Esercizio 2 ---\n")
                    elif Scelta_Esercizio == "3":
                        print("\n--- Soluzione Esercizio 3 ---")
                        print("x = 10")
                        print("y = 20")
                        print("somma = x + y")
                        print("print(somma)")
                        print("--- Fine Esercizio 3 ---\n")
                    elif Scelta_Esercizio == "4":
                        print("\n--- Soluzione Esercizio 4 ---")
                        print("saluto = \"Ciao\"")
                        print("nome_persona = \"Mario\"")
                        print("print(saluto, nome_persona)")
                        print("--- Fine Esercizio 4 ---\n")
                    elif Scelta_Esercizio == "5":
                        print("\n--- Soluzione Esercizio 5 ---")
                        print("PI_GRECO = 3.14159")
                        print("print(PI_GRECO)")
                        print("print(\"PI_GRECO è una costante perché il suo valore (circa 3.14) non cambia mai ed è fisso per definizione.\")")
                        print("--- Fine Esercizio 5 ---\n")
                    elif Scelta_Esercizio == "6":
                        print("\n--- Soluzione Esercizio 6 ---")
                        print("citta_nascita = input(\"In quale città sei nato?: \")")
                        print("print(f\"Sei nato a {citta_nascita}.\")")
                        print("--- Fine Esercizio 6 ---\n")
                    elif Scelta_Esercizio == "7":
                        print("\n--- Soluzione Esercizio 7 ---")
                        print("eta = input(\"Quanti anni hai?: \")")
                        print("print(f\"Hai {eta} anni.\")")
                        print("--- Fine Esercizio 7 ---\n")
                    elif Scelta_Esercizio == "8":
                        print("\n--- Soluzione Esercizio 8 ---")
                        print("ha_patente = True")
                        print("print(ha_patente)")
                        print("--- Fine Esercizio 8 ---\n")
                    elif Scelta_Esercizio == "9":
                        print("\n--- Soluzione Esercizio 9 ---")
                        print("animale = input(\"Qual è il tuo animale preferito?: \")")
                        print("verso = input(\"Quale verso fa questo animale?: \")")
                        print("print(f\"Il {animale} fa {verso}.\")")
                        print("--- Fine Esercizio 9 ---\n")
                    elif Scelta_Esercizio == "10":
                        print("\n--- Soluzione Esercizio 10 ---")
                        print("# Nota: Per eseguire l'operazione matematica, i numeri dovrebbero essere convertiti a int/float.")
                        print("# La lezione 3 ti mostrerà come farlo! Per ora, li gestiamo come stringhe.")
                        print("numero1 = input(\"Inserisci il primo numero: \")")
                        print("numero2 = input(\"Inserisci il secondo numero: \")")
                        print("# Per ora, mostriamo solo come combinare le stringhe, non fare calcoli diretti.")
                        print("print(f\"I numeri inseriti sono: {numero1} e {numero2}\")")
                        print("--- Fine Esercizio 10 ---\n")
                    elif Scelta_Esercizio == "torna":
                        print("Torno alla selezione esercizi.")
                        time.sleep(1)
                        break
                    else:
                        print("Esercizio non trovato o scelta non valida. Per favore, scegli un numero da 1 a 10 o digita 'torna'.")
                    time.sleep(2)

            elif Scelta_Esercizi_Lezione == "3":
                while True: # Ciclo interno per gli esercizi della Lezione 3
                    print("\n--- ESERCIZI LEZIONE 3 ---")
                    print("Hai scelto di fare gli esercizi sulla Lezione 3: Conversioni fra Stringhe e Numeri.")
                    print("1: Chiedi all'utente un numero, convertilo in intero e stampalo, verificandone il tipo con `type()`.")
                    print("2: Chiedi all'utente due numeri (stringhe), convertili in numeri interi e stampa la loro somma.")
                    print("3: Chiedi all'utente la sua età, verifica se è un numero. Se non lo è, stampa un errore. Se lo è, convertila in int e stampa: 'La tua età è: [età].'")
                    print("4: Chiedi all'utente un prezzo con decimali (es. 10.50), convertilo in float e stampalo.")
                    print("5: Chiedi all'utente il suo anno di nascita e calcola la sua età attuale, poi stampala (es. 'Hai X anni.').")
                    print("6: Chiedi all'utente una frase e un numero. Concatena la frase con il numero (convertendo il numero in stringa) e stampa il risultato.")
                    print("7: Chiedi all'utente due numeri. Moltiplicali e stampa il risultato.")
                    print("8: Crea un piccolo convertitore: chiedi all'utente una quantità in metri (numero con decimali) e convertila in centimetri, poi stampala.")
                    print("9: Chiedi all'utente un anno. Controlla se l'anno è numerico. Se non lo è, stampa 'Anno non valido'. Altrimenti, stampa 'Anno accettato'.")
                    print("10: Simula un calcolo BMI: chiedi peso (kg) e altezza (metri). Convertili in float e stampa 'Il tuo BMI è: [valore]'. (Formula: peso / (altezza * altezza) )")
                    
                    time.sleep(2)
                    Scelta_Esercizio = input("Quale esercizio della Lezione 3 vuoi vedere? Inserisci il numero (1-10) o 'torna' per tornare alla selezione esercizi: ").lower()

                    if Scelta_Esercizio == "1":
                        print("\n--- Soluzione Esercizio 1 ---")
                        print("numero_str = input(\"Inserisci un numero: \")")
                        print("numero_int = int(numero_str)")
                        print("print(f\"Il numero è: {numero_int}\")")
                        print("print(f\"Tipo del numero: {type(numero_int)}\")")
                        print("--- Fine Esercizio 1 ---\n")
                    elif Scelta_Esercizio == "2":
                        print("\n--- Soluzione Esercizio 2 ---")
                        print("num1_str = input(\"Inserisci il primo numero: \")")
                        print("num2_str = input(\"Inserisci il secondo numero: \")")
                        print("num1_int = int(num1_str)")
                        print("num2_int = int(num2_str)")
                        print("somma = num1_int + num2_int")
                        print("print(f\"La somma è: {somma}\")")
                        print("--- Fine Esercizio 2 ---\n")
                    elif Scelta_Esercizio == "3":
                        print("\n--- Soluzione Esercizio 3 ---")
                        print("eta_str = input(\"Quanti anni hai?: \")")
                        print("if not eta_str.isdigit():")
                        print("    print(\"Errore: L'età deve essere un numero!\")")
                        print("else:")
                        print("    eta_int = int(eta_str)")
                        print("    print(f\"La tua età è: {eta_int}.\")")
                        print("--- Fine Esercizio 3 ---\n")
                    elif Scelta_Esercizio == "4":
                        print("\n--- Soluzione Esercizio 4 ---")
                        print("prezzo_str = input(\"Inserisci un prezzo (es. 10.50): \")")
                        print("prezzo_float = float(prezzo_str)")
                        print("print(f\"Il prezzo è: {prezzo_float}\")")
                        print("--- Fine Esercizio 4 ---\n")
                    elif Scelta_Esercizio == "5":
                        print("\n--- Soluzione Esercizio 5 ---")
                        print("from datetime import datetime")
                        print("anno_nascita_str = input(\"In che anno sei nato?: \")")
                        print("anno_nascita_int = int(anno_nascita_str)")
                        print("anno_corrente = datetime.now().year")
                        print("eta_calcolata = anno_corrente - anno_nascita_int")
                        print("print(f\"Hai {eta_calcolata} anni.\")")
                        print("--- Fine Esercizio 5 ---\n")
                    elif Scelta_Esercizio == "6":
                        print("\n--- Soluzione Esercizio 6 ---")
                        print("frase = input(\"Inserisci una frase: \")")
                        print("numero = int(input(\"Inserisci un numero: \"))")
                        print("risultato = frase + str(numero)")
                        print("print(risultato)")
                        print("--- Fine Esercizio 6 ---\n")
                    elif Scelta_Esercizio == "7":
                        print("\n--- Soluzione Esercizio 7 ---")
                        print("num1_str = input(\"Inserisci il primo numero: \")")
                        print("num2_str = input(\"Inserisci il secondo numero: \")")
                        print("num1 = float(num1_str)")
                        print("num2 = float(num2_str)")
                        print("prodotto = num1 * num2")
                        print("print(f\"Il prodotto è: {prodotto}\")")
                        print("--- Fine Esercizio 7 ---\n")
                    elif Scelta_Esercizio == "8":
                        print("\n--- Soluzione Esercizio 8 ---")
                        print("metri_str = input(\"Inserisci la quantità in metri (es. 1.75): \")")
                        print("metri_float = float(metri_str)")
                        print("centimetri = metri_float * 100")
                        print("print(f\"{metri_float} metri corrispondono a {centimetri} centimetri.\")")
                        print("--- Fine Esercizio 8 ---\n")
                    elif Scelta_Esercizio == "9":
                        print("\n--- Soluzione Esercizio 9 ---")
                        print("anno_str = input(\"Inserisci un anno: \")")
                        print("if not anno_str.isdigit():")
                        print("    print(\"Anno non valido: deve essere un numero!\")")
                        print("else:")
                        print("    print(\"Anno accettato.\")")
                        print("--- Fine Esercizio 9 ---\n")
                    elif Scelta_Esercizio == "10":
                        print("\n--- Soluzione Esercizio 10 ---")
                        print("peso_str = input(\"Inserisci il tuo peso in kg (es. 70.5): \")")
                        print("altezza_str = input(\"Inserisci la tua altezza in metri (es. 1.75): \")")
                        print("peso = float(peso_str)")
                        print("altezza = float(altezza_str)")
                        print("bmi = peso / (altezza * altezza)")
                        print("print(f\"Il tuo BMI è: {bmi:.2f}\")")
                        print("--- Fine Esercizio 10 ---\n")
                    elif Scelta_Esercizio == "torna":
                        print("Torno alla selezione esercizi.")
                        time.sleep(1)
                        break
                    else:
                        print("Esercizio non trovato o scelta non valida. Per favore, scegli un numero da 1 a 10 o digita 'torna'.")
                    time.sleep(2)
            
            elif Scelta_Esercizi_Lezione == "4":
                while True: # Ciclo interno per gli esercizi della Lezione 4
                    print("\n--- ESERCIZI LEZIONE 4 ---")
                    print("Hai scelto di fare gli esercizi sulla Lezione 4: Operatori e Strutture di Controllo.")
                    print("1: Chiedi due numeri. Calcola e stampa la somma, la differenza, il prodotto, la divisione normale e il modulo.")
                    print("2: Chiedi un numero. Stampa 'Pari' se è divisibile per 2, altrimenti 'Dispari'.")
                    print("3: Chiedi l'età. Se l'età è tra 13 e 19 (inclusi), stampa 'Sei un adolescente'. Altrimenti, 'Non sei un adolescente'. Usa l'operatore `and`.")
                    print("4: Simula un sistema di voto. Chiedi un voto da 1 a 10. Se il voto è >= 6 E l'utente ha risposto 'sì' a 'Hai studiato?', stampa 'Promosso!'.")
                    print("5: Crea un ciclo `while` che conti da 10 a 1 e, una volta finito, stampi 'Decollo!'.")
                    print("6: Chiedi una password. Continua a chiederla in un ciclo `while` finché la password inserita non è 'segreto'.")
                    print("7: Usa un ciclo `for` per stampare tutti i numeri da 1 a 10.")
                    print("8: Usa un ciclo `for` per stampare il tuo nome una volta per ogni lettera, usando un `range`.")
                    print("9: Chiedi all'utente un numero. Usa un ciclo `for` per stampare una tabellina fino a 10 per quel numero.")
                    print("10: Simula un login con tre tentativi. Usa un ciclo `while` e una variabile `tentativi_rimanenti`.")
                    print("11: Scrivi un programma che chieda all'utente numeri in un ciclo `while`. Il ciclo deve fermarsi solo se l'utente inserisce 0.")
                    print("12: Chiedi una frase. Usa un ciclo `for` per stampare ogni parola della frase su una nuova riga.")
                    print("13: Simula un'operazione bancaria. Chiedi un PIN. Continua a chiederlo finché non è '1234'. Dopo 3 tentativi, stampa 'Carta bloccata'.")
                    print("14: Chiedi un numero. Stampa un conto alla rovescia da quel numero a 0 usando un ciclo `while`.")
                    print("15: Usa un ciclo `for` e `range()` per stampare i numeri pari da 2 a 20 (inclusi).")
                    
                    time.sleep(2)
                    Scelta_Esercizio = input("Quale esercizio della Lezione 4 vuoi vedere? Inserisci il numero (1-15) o 'torna' per tornare alla selezione esercizi: ").lower()

                    if Scelta_Esercizio == "1":
                        print("\n--- Soluzione Esercizio 1 ---")
                        print("num1 = float(input(\"Inserisci il primo numero: \"))")
                        print("num2 = float(input(\"Inserisci il secondo numero: \"))")
                        print("print(f\"Somma: {num1 + num2}\")")
                        print("print(f\"Differenza: {num1 - num2}\")")
                        print("print(f\"Prodotto: {num1 * num2}\")")
                        print("print(f\"Divisione: {num1 / num2}\")")
                        print("print(f\"Modulo (resto): {num1 % num2}\")")
                        print("--- Fine Esercizio 1 ---\n")
                    elif Scelta_Esercizio == "2":
                        print("\n--- Soluzione Esercizio 2 ---")
                        print("numero = int(input(\"Inserisci un numero intero: \"))")
                        print("if numero % 2 == 0:")
                        print("    print('Pari')")
                        print("else:")
                        print("    print('Dispari')")
                        print("--- Fine Esercizio 2 ---\n")
                    elif Scelta_Esercizio == "3":
                        print("\n--- Soluzione Esercizio 3 ---")
                        print("eta = int(input(\"Inserisci la tua età: \"))")
                        print("if eta >= 13 and eta <= 19:")
                        print("    print('Sei un adolescente.')")
                        print("else:")
                        print("    print('Non sei un adolescente.')")
                        print("--- Fine Esercizio 3 ---\n")
                    elif Scelta_Esercizio == "4":
                        print("\n--- Soluzione Esercizio 4 ---")
                        print("voto = int(input(\"Inserisci il tuo voto (1-10): \"))")
                        print("ha_studiato_str = input(\"Hai studiato? (sì/no): \").lower()")
                        print("ha_studiato = ha_studiato_str == 'sì' or ha_studiato_str == 'si'")
                        print("if voto >= 6 and ha_studiato:")
                        print("    print('Promosso!')")
                        print("else:")
                        print("    print('Bocciato.')")
                        print("--- Fine Esercizio 4 ---\n")
                    elif Scelta_Esercizio == "5":
                        print("\n--- Soluzione Esercizio 5 ---")
                        print("contatore = 10")
                        print("while contatore >= 1:")
                        print("    print(contatore)")
                        print("    time.sleep(1) # Rallenta il conto alla rovescia")
                        print("    contatore -= 1")
                        print("print('Decollo!')")
                        print("--- Fine Esercizio 5 ---\n")
                    elif Scelta_Esercizio == "6":
                        print("\n--- Soluzione Esercizio 6 ---")
                        print("password = ''")
                        print("while password != 'segreto':")
                        print("    password = input(\"Inserisci la password: \")")
                        print("print('Accesso effettuato!')")
                        print("--- Fine Esercizio 6 ---\n")
                    elif Scelta_Esercizio == "7":
                        print("\n--- Soluzione Esercizio 7 ---")
                        print("for i in range(1, 11):")
                        print("    print(i)")
                        print("--- Fine Esercizio 7 ---\n")
                    elif Scelta_Esercizio == "8":
                        print("\n--- Soluzione Esercizio 8 ---")
                        print("nome = \"Python\"")
                        print("for i in range(len(nome)):")
                        print("    print(nome[i])")
                        print("--- Fine Esercizio 8 ---\n")
                    elif Scelta_Esercizio == "9":
                        print("\n--- Soluzione Esercizio 9 ---")
                        print("numero = int(input(\"Inserisci un numero per la tabellina: \"))")
                        print("for i in range(1, 11):")
                        print("    print(f\"{numero} x {i} = {numero * i}\")")
                        print("--- Fine Esercizio 9 ---\n")
                    elif Scelta_Esercizio == "10":
                        print("\n--- Soluzione Esercizio 10 ---")
                        print("tentativi = 3")
                        print("while tentativi > 0:")
                        print("    user = input(\"Username: \")")
                        print("    pwd = input(\"Password: \")")
                        print("    if user == 'admin' and pwd == '1234':")
                        print("        print('Accesso consentito!')")
                        print("        break # Esce dal ciclo")
                        print("    else:")
                        print("        tentativi -= 1")
                        print(f"        Accesso negato. Tentativi rimanenti: {tentativi}")
                        print("else:")
                        print("    print('Troppi tentativi. Account bloccato.')")
                        print("--- Fine Esercizio 10 ---\n")
                    elif Scelta_Esercizio == "11":
                        print("\n--- Soluzione Esercizio 11 ---")
                        print("while True:")
                        print("    numero = int(input(\"Inserisci un numero (0 per uscire): \"))")
                        print("    if numero == 0:")
                        print("        print('Hai scelto di uscire.')")
                        print("        break")
                        print("    print(f\"Hai inserito il numero {numero}\")")
                        print("--- Fine Esercizio 11 ---\n")
                    elif Scelta_Esercizio == "12":
                        print("\n--- Soluzione Esercizio 12 ---")
                        print("frase = input(\"Inserisci una frase: \")")
                        print("parole = frase.split() # Separa la frase in una lista di parole")
                        print("for parola in parole:")
                        print("    print(parola)")
                        print("--- Fine Esercizio 12 ---\n")
                    elif Scelta_Esercizio == "13":
                        print("\n--- Soluzione Esercizio 13 ---")
                        print("tentativi = 0")
                        print("while tentativi < 3:")
                        print("    pin = input(\"Inserisci il PIN: \")")
                        print("    if pin == '1234':")
                        print("        print('PIN corretto. Benvenuto!')")
                        print("        break")
                        print("    else:")
                        print("        tentativi += 1")
                        print(f"        PIN errato. Tentativi rimanenti: {3 - tentativi}")
                        print("else:")
                        print("    print('Carta bloccata.')")
                        print("--- Fine Esercizio 13 ---\n")
                    elif Scelta_Esercizio == "14":
                        print("\n--- Soluzione Esercizio 14 ---")
                        print("numero = int(input(\"Inserisci un numero per il conto alla rovescia: \"))")
                        print("while numero >= 0:")
                        print("    print(numero)")
                        print("    time.sleep(1)")
                        print("    numero -= 1")
                        print("print('Fine del conto alla rovescia.')")
                        print("--- Fine Esercizio 14 ---\n")
                    elif Scelta_Esercizio == "15":
                        print("\n--- Soluzione Esercizio 15 ---")
                        print("# range(2, 21, 2) parte da 2, arriva fino a 20 (escluso 21) con un passo di 2")
                        print("for i in range(2, 21, 2):")
                        print("    print(i)")
                        print("--- Fine Esercizio 15 ---\n")
                    elif Scelta_Esercizio == "torna":
                        print("Torno alla selezione esercizi.")
                        time.sleep(1)
                        break
                    else:
                        print("Esercizio non trovato o scelta non valida. Per favore, scegli un numero da 1 a 15 o digita 'torna'.")
                    time.sleep(2)

            elif Scelta_Esercizi_Lezione == "5":
                while True: # Ciclo interno per gli esercizi della Lezione 5
                    print("\n--- ESERCIZI LEZIONE 5 ---")
                    print("Hai scelto di fare gli esercizi sulla Lezione 5: Strutture di Dati.")
                    print("1: Lista - Crea una lista di 5 frutti, aggiungine uno nuovo e stampala.")
                    print("2: Lista - Ordina alfabeticamente una lista di nomi e stampala.")
                    print("3: Tupla - Crea una tupla con 3 oggetti e stampa il primo e l'ultimo elemento.")
                    print("4: Dizionario - Crea un dizionario per un animale (chiavi: 'nome', 'specie', 'età'). Stampa il nome dell'animale.")
                    print("5: Dizionario - Aggiorna l'età dell'animale e stampa il dizionario aggiornato.")
                    print("6: Insieme - Crea un insieme con numeri da 1 a 5, aggiungi il numero 6 e rimuovi il 3. Stampa l'insieme finale.")
                    print("7: Insieme - Crea due insiemi di nomi. Stampa i nomi che sono presenti in entrambi (intersezione).")
                    print("8: Ciclo + Lista - Crea una lista di città e usa un ciclo `for` per stampare ogni città.")
                    print("9: Dizionario + Ciclo - Crea un dizionario di prodotti e prezzi. Usa un ciclo `for` per stampare ogni prodotto e il suo prezzo.")
                    print("10: Combinazione - Chiedi all'utente di inserire 3 numeri. Salvali in una lista. Stampa la somma dei numeri usando un ciclo `for`.")
                    
                    time.sleep(2)
                    Scelta_Esercizio = input("Quale esercizio della Lezione 5 vuoi vedere? Inserisci il numero (1-10) o 'torna' per tornare alla selezione esercizi: ").lower()
                    
                    if Scelta_Esercizio == "1":
                        print("\n--- Soluzione Esercizio 1 ---")
                        print("frutti = ['mela', 'banana', 'ciliegia', 'arancia', 'uva']")
                        print("frutti.append('kiwi')")
                        print("print(frutti)")
                        print("--- Fine Esercizio 1 ---\n")
                    elif Scelta_Esercizio == "2":
                        print("\n--- Soluzione Esercizio 2 ---")
                        print("nomi = ['Marco', 'Giulia', 'Andrea', 'Silvia']")
                        print("nomi.sort()")
                        print("print(nomi)")
                        print("--- Fine Esercizio 2 ---\n")
                    elif Scelta_Esercizio == "3":
                        print("\n--- Soluzione Esercizio 3 ---")
                        print("oggetti = ('tavolo', 'sedia', 'lampada')")
                        print("print(f\"Primo elemento: {oggetti[0]}\")")
                        print("print(f\"Ultimo elemento: {oggetti[-1]}\")")
                        print("--- Fine Esercizio 3 ---\n")
                    elif Scelta_Esercizio == "4":
                        print("\n--- Soluzione Esercizio 4 ---")
                        print("animale = {'nome': 'Fido', 'specie': 'cane', 'età': 5}")
                        print("print(animale['nome'])")
                        print("--- Fine Esercizio 4 ---\n")
                    elif Scelta_Esercizio == "5":
                        print("\n--- Soluzione Esercizio 5 ---")
                        print("animale = {'nome': 'Fido', 'specie': 'cane', 'età': 5}")
                        print("animale['età'] = 6")
                        print("print(animale)")
                        print("--- Fine Esercizio 5 ---\n")
                    elif Scelta_Esercizio == "6":
                        print("\n--- Soluzione Esercizio 6 ---")
                        print("numeri = {1, 2, 3, 4, 5}")
                        print("numeri.add(6)")
                        print("numeri.remove(3)")
                        print("print(numeri)")
                        print("--- Fine Esercizio 6 ---\n")
                    elif Scelta_Esercizio == "7":
                        print("\n--- Soluzione Esercizio 7 ---")
                        print("insieme1 = {'Alice', 'Bob', 'Charlie'}")
                        print("insieme2 = {'Charlie', 'David', 'Alice'}")
                        print("intersezione = insieme1.intersection(insieme2)")
                        print("print(intersezione)")
                        print("# Oppure: print(insieme1 & insieme2)")
                        print("--- Fine Esercizio 7 ---\n")
                    elif Scelta_Esercizio == "8":
                        print("\n--- Soluzione Esercizio 8 ---")
                        print("citta = ['Roma', 'Milano', 'Napoli']")
                        print("for c in citta:")
                        print("    print(c)")
                        print("--- Fine Esercizio 8 ---\n")
                    elif Scelta_Esercizio == "9":
                        print("\n--- Soluzione Esercizio 9 ---")
                        print("prodotti = {'pane': 2.50, 'latte': 1.20, 'uova': 3.00}")
                        print("for prodotto, prezzo in prodotti.items():")
                        print("    print(f\"Prodotto: {prodotto}, Prezzo: {prezzo}€\")")
                        print("--- Fine Esercizio 9 ---\n")
                    elif Scelta_Esercizio == "10":
                        print("\n--- Soluzione Esercizio 10 ---")
                        print("numeri_utente = []")
                        print("somma = 0")
                        print("for i in range(3):")
                        print("    num = int(input(f\"Inserisci il numero {i+1}: \"))")
                        print("    numeri_utente.append(num)")
                        print("for n in numeri_utente:")
                        print("    somma += n")
                        print("print(f\"La somma dei numeri è: {somma}\")")
                        print("--- Fine Esercizio 10 ---\n")
                    elif Scelta_Esercizio == "torna":
                        print("Torno alla selezione esercizi.")
                        time.sleep(1)
                        break
                    else:
                        print("Esercizio non trovato o scelta non valida. Per favore, scegli un numero da 1 a 10 o digita 'torna'.")
                    time.sleep(2)

            elif Scelta_Esercizi_Lezione == "6": # Torna al menu principale dalla selezione esercizi
                print("Torno al menu principale.")
                time.sleep(1)
                break
            else:
                print("Scelta non valida. Per favore, scegli 1, 2, 3, 4, 5 o 6.")
            time.sleep(2)
    
    elif Scelta_Generale == "esci": # Opzione per uscire dal programma
        print("Grazie per aver usato il programma! Arrivederci!")
        time.sleep(1)
        sys.exit() # Esce completamente dal programma
        
    else: # Se l'utente digita qualcosa di diverso dalle opzioni valide
        print("Scelta non valida. Per favore, scegli 1, 2, 3, 4, 5, 6 o digita 'Esci'.")
        time.sleep(2)