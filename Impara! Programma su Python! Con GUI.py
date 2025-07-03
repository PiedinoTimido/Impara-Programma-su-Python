import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTextEdit, QSizePolicy,
                             QScrollArea, QMessageBox) # Aggiunto QMessageBox per avvisi
from PyQt6.QtCore import Qt, QTimer # Aggiunto QTimer per delay se necessario

# --- CONTENUTO DELLE LEZIONI ---
# Ogni lezione è una lista di stringhe (frasi/paragrafi)
# Gli esercizi interattivi saranno gestiti separatamente nella logica della GUI.
lezioni_contenuto = {
    "1": [
        "ATTENZIONE! PER ESEGUIRE I CODICI SPIEGATI IN QUESTA SERIE DI LEZIONI è NECESSARIO SCARICARE LA VERSIONE 3 DI PYTHON (tutte le sotto-versioni sono accettate! es 3.14)",
        "--- SEZIONE LEZIONE 1 (Hello World) ---",
        "È stata scelta la lezione!",
        "In questa prima lezione vedremo come fare la primissima stringa di codice mai fatta, l'Hello World!",
        "Per scrivere l'Hello World bisogna usare la funzione print() che poi DEVE essere seguita da una parentesi.",
        "Poi bisogna capire che cosa dovrai fare uscire dalla funzione print().",
        "Se è un numero si può scrivere nelle parentesi senza nessuna aggiunta, se invece è una stringa, cioè una frase, bisogna aggiungere le virgolette.",
        "Dato che è una frase dobbiamo usare le virgolette ed infine far partire il programma.",
        # L'esercizio di input sarà un passo separato nella GUI
        "Ora prova tu, scrivi il comando print() con la frase Hello, World!:"
    ],
    "2": [
        "--- SEZIONE LEZIONE 2 (Variabili, Operatori e Strutture di Controllo) ---",
        "I programmi che usiamo ogni giorno si basano su variabili che sono come dei cassetti temporanei. Le variabili si dividono in Nomi e Tipi (o Classi).",
        "Nella lezione 1 abbiamo visto che ci sono 2 tipi: le stringhe (testo) e i numeri. Ma ce n'è un terzo, i valori di verità che sono True (Vero) e False (Falso).",
        "Invece, i nomi sono delle etichette che diamo alle variabili per capirne lo scopo velocemente.",
        "Oltre alle variabili, che come dice il nome cambiano spesso, ci possono essere delle costanti.",
        "Le costanti sono molto simili alle variabili, ma il loro valore non dovrebbe essere modificato durante l'esecuzione del programma. Anche per logica!",
        "Prendiamo come esempio il Pi Greco (π), il suo valore è circa 3.14 ed è quindi inutile modificarlo.",
        "Ora vedremo come fare un piccolo programma per chiedere all'utente una frase che poi il computer riscriverà.",
        # Esercizio 1: scegli un nome variabile
        "Iniziamo creando una variabile: scegli un nome per essa (es. 'mia_frase'): ",
        "Ottimo! Il nome che hai scelto è valido.",
        "Adesso, per far apparire una domanda all'utente che poi il computer riscriverà, si usa la funzione `input()`.",
        "La riga di codice completa dovrebbe essere: <nome_variabile> = input()",
        "Scrivi la parte che manca (solo ` = input()`): ",
        "Perfetto! Ora abbiamo la riga completa. Se volessi anche una domanda quando la chiedi all'utente?",
        "Esempio: nome = input(\"Come ti chiami?\")",
        "Inserisci la domanda tra virgolette che vuoi far apparire: ",
        "Ben fatto! Adesso il tuo programma chiederà una domanda. Ma come facciamo a vedere la risposta dell'utente?",
        "Infine, per visualizzare il contenuto della variabile, basta usare il comando print() con il nome della variabile.",
        "Scrivi la riga di codice completa per stampare la variabile (es. `print(mia_frase)`): ",
        "Complimenti! Hai completato la lezione sulle variabili. Ottimo lavoro!",
        "Fine della Lezione 2. Torno al menu principale."
    ],
    "3": [
        "--- SEZIONE LEZIONE 3 (Conversioni fra Stringhe e Numeri) ---",
        "Se sei interessato a creare un programma che verifica se l'età inserita dall'utente è valida, ad esempio per capire se puoi prendere la patente, ti ritrovi davanti a un problema:",
        "Quando usi la funzione input(), tutti i dati inseriti sono trattati come stringhe, quindi non puoi eseguire operazioni numeriche (come addizioni, sottrazioni, o confronti con numeri) direttamente su di essi.",
        "Prima di tutto, bisogna capire se l'input dell'utente è un numero. Per farlo, controlliamo che il valore inserito sia effettivamente composto da cifre.",
        "Si usa la funzione `variabile.isdigit()`. Attenzione: questa funzione controlla se la stringa contiene SOLO cifre. Se vogliamo verificare che NON sia una parola, si usa `not` davanti: `if not variabile.isdigit():`",
        "Quindi, il problema dell'utente che non inserisce un numero ma una stringa è aggiustato. Ma ora ritorna il problema dell'input: tutto quello digitato nell'input è una stringa!",
        "Per questo, Python utilizza la funzione `int()` (per numeri interi) o `float()` (per numeri decimali). Ora farai uno script per capire come funziona.",
        # Esercizio 1: crea la variabile eta_utente
        "Iniziamo creando la variabile per l'input: Metti come nome della variabile 'eta_utente' e come domanda 'Quanti anni hai?': ",
        "Ottimo! Ora hai la variabile `eta_utente` che conterrà l'input come stringa.",
        "Ora, per evitare che Python cerchi di convertire una frase in un numero, usa `if not variabile.isdigit():` seguito da `print(\"Input non valido!\")` e `continue` (per simulare la richiesta di un nuovo input se siamo in un ciclo, qui andiamo avanti per semplicità).",
        "Scrivi la riga di codice `if not eta_utente.isdigit():` e la riga successiva indentata con un messaggio di errore: ",
        "Perfetto! Adesso il tuo programma può gestire input non numerici.",
        "Per convertire la stringa con `int()`, crea una nuova variabile, ad esempio `eta_numerica`, e assegnale il risultato di `int(eta_utente)`.",
        "Scrivi la riga di codice `eta_numerica = int(eta_utente)`: ",
        "Complimenti! Ora hai convertito la stringa in un numero intero. Puoi fare operazioni matematiche con `eta_numerica`.",
        "Fine della Lezione 3. Torno al menu principale."
    ],
    "4": [
        "--- SEZIONE LEZIONE 4 (Operatori, Condizioni e Cicli) ---",
        "In questa lezione vedremo come usare gli operatori per fare calcoli e confronti, le strutture di controllo per prendere decisioni e ripetere azioni e, infine, il significato di alcune parole chiave fondamentali di Python.",
        "--- PAROLE CHIAVE DI PYTHON ---",
        "Le parole chiave (o keyword) sono parole speciali che hanno un significato preciso in Python. Non puoi usarle come nomi per le tue variabili o funzioni.",
        "Ecco una lista di alcune delle più importanti parole chiave che incontrerai, con una breve spiegazione:",
        "`print`: per stampare testo o valori a schermo (l'hai già usata!).",
        "`if`, `elif`, `else`: per le strutture di controllo condizionali.",
        "`for`, `while`: per i cicli e le iterazioni.",
        "`break`: per uscire da un ciclo.",
        "`continue`: per passare all'iterazione successiva di un ciclo.",
        "`and`, `or`, `not`: per gli operatori logici.",
        "`import`, `from`: per importare moduli e librerie (hai visto `import time`!).",
        "`in`: per controllare se un elemento è presente in una sequenza (es. `for elemento in lista`).",
        "`def`: per definire una funzione.",
        "`return`: per restituire un valore da una funzione.",
        "`class`: per definire una classe (usata nella programmazione a oggetti).",
        "`try`, `except`, `finally`: per gestire gli errori (eccezioni).",
        "`pass`: una dichiarazione che non fa nulla, usata come segnaposto.",
        "Ci sono molte altre parole chiave come `global`, `is`, `del`, `with`, `as`, `lambda`, `assert`, `exec`, `raise` e `yield`, ma le incontrerai più avanti nel tuo percorso. È utile sapere che esistono!",
        "--- OPERATORI ---",
        "**Operatori Aritmetici**",
        "Questi operatori servono a fare calcoli matematici. Ecco i principali:",
        "+  (addizione)",
        "-  (sottrazione)",
        "* (moltiplicazione)",
        "/  (divisione normale, restituisce un numero decimale)",
        "// (divisione intera, restituisce solo il numero intero)",
        "%  (modulo, restituisce il resto della divisione)",
        "** (esponenziale, eleva a potenza)",
        "Vediamo un esempio con i numeri e poi con le stringhe, dato che l'operatore `+` si comporta in modo diverso!",
        "Esempio con i numeri:",
        "numero1 = 10",
        "numero2 = 3",
        "somma = numero1 + numero2",
        "modulo = numero1 % numero2 # 10 diviso 3 fa 3 con resto 1",
        f"print(\"Somma: {10 + 3}\")", # Ho inserito il risultato per la GUI
        f"print(\"Modulo: {10 % 3}\")", # Ho inserito il risultato per la GUI
        "Esempio con le stringhe:",
        "saluto = \"Ciao, \"",
        "nome = \"mondo!\"",
        "messaggio = \"Ciao, \" + \"mondo!\" # Concatenazione (unione di stringhe)",
        "print(messaggio)  # Il risultato è 'Ciao, mondo!'",
        "Come vedi, l'operatore `+` ha due funzioni diverse a seconda del tipo di dato che usi!",
        "**Operatori Relazionali**",
        "Questi operatori confrontano due valori e restituiscono un valore di verità: **True** (Vero) o **False** (Falso).",
        "Ecco i principali operatori relazionali:",
        "== (uguale a)",
        "!= (diverso da)",
        ">  (maggiore di)",
        "<  (minore di)",
        ">= (maggiore o uguale a)",
        "<= (minore o uguale a)",
        "Ora vediamo un esempio pratico con l'età.",
        # Esercizio età (input)
        "Inserisci la tua età (un numero!): ", # Richiesta input
        "Verifichiamo se sei maggiorenne (maggiore o uguale a 18):",
        # Risultato dell'esercizio età verrà mostrato dinamicamente
        "**Operatori Logici**",
        "Questi operatori combinano più condizioni e restituiscono un valore di verità.",
        "Ecco i principali:",
        "**and** (vero se ENTRAMBE le condizioni sono vere)",
        "**or** (vero se ALMENO UNA delle condizioni è vera)",
        "**not** (inverte il valore di verità: True diventa False e viceversa)",
        "Esempio di login con `and`:",
        "username = 'admin'",
        "password = '1234'",
        "if username == 'admin' and password == '1234':",
        "    print('Accesso consentito.')",
        "else:",
        "    print('Accesso negato.')",
        "--- ARITMETICA BINARIA E OPERATORI BIT A BIT ---",
        "Questa è una sezione più avanzata. Lavoriamo sui **bit**, i mattoncini fondamentali dei numeri (0 e 1).",
        "Per Python, puoi rappresentare un numero binario con il prefisso `0b`. Ad esempio, `0b101` è il numero 5.",
        "Ecco gli operatori bit a bit:",
        "`&` (AND binario): Confronta i bit, se entrambi sono 1, il risultato è 1. Altrimenti 0.",
        "`|` (OR binario): Confronta i bit, se almeno uno è 1, il risultato è 1. Altrimenti 0.",
        "`^` (XOR binario): Confronta i bit, se sono diversi (uno 0 e uno 1), il risultato è 1. Altrimenti 0.",
        "`~` (NOT binario): Inverte i bit (0 diventa 1 e 1 diventa 0).",
        "`<<` (SHIFT a sinistra): Sposta i bit a sinistra, aggiungendo 0 a destra. Moltiplica per 2 per ogni shift.",
        "`>>` (SHIFT a destra): Sposta i bit a destra, scartando i bit a destra. Divide per 2 per ogni shift.",
        "Esempio pratico con i numeri decimali 5 (`0b101`) e 3 (`0b011`):",
        f"numero1 = 5  # Binario: 0b101",
        f"numero2 = 3  # Binario: 0b011",
        f"5 & 3 = {5 & 3} (0b101 & 0b011 = 0b001, che è 1)",
        f"5 | 3 = {5 | 3} (0b101 | 0b011 = 0b111, che è 7)",
        f"5 << 1 = {5 << 1} (0b101 << 1 = 0b1010, che è 10)",
        "Gli operatori bit a bit sono usati in aree come la crittografia, i protocolli di rete o l'ottimizzazione di basso livello. Non ti preoccupare se all'inizio sembrano complessi, l'importante è sapere che esistono!",
        "--- STRUTTURE DI CONTROLLO CONDIZIONALI (IF, ELIF, ELSE) ---",
        "Le strutture di controllo ci permettono di eseguire del codice solo se una condizione è vera.",
        "Il costrutto `if` è il più comune e si basa su condizioni `True` o `False`.",
        "Vediamo un esempio completo con `if`, `elif` e `else` per controllare l'età.",
        # Esercizio età patente (input)
        "Inserisci la tua età per vedere se puoi prendere la patente in Italia (18 anni): ", # Richiesta input
        # Risultato dell'esercizio patente verrà mostrato dinamicamente
        "--- STRUTTURE DI CONTROLLO ITERATIVE (CICLI) ---",
        "I cicli ci permettono di ripetere un blocco di codice più volte, evitando di riscriverlo.",
        "**Il ciclo `while`**",
        "Il ciclo `while` ripete il suo codice **finché una condizione rimane vera**.",
        "È utile quando non sai in anticipo quante volte devi ripetere un'azione.",
        "Esempio: un semplice contatore da 1 a 5:",
        "contatore = 1",
        "while contatore <= 5:",
        "    print(contatore)",
        "    contatore = contatore + 1  # Questo aggiornamento è FONDAMENTALE!",
        "Se non aggiorni il `contatore`, il ciclo non si fermerà mai! Si chiama **ciclo infinito**.",
        "**Simulazione del ciclo `do-while`**",
        "Python non ha un ciclo `do-while` nativo, ma possiamo simularlo con `while True` e un `break`.",
        "La logica è: 'Esegui il codice **almeno una volta**, poi controlla la condizione'.",
        "Esempio: chiedere un numero positivo all'utente:",
        "while True:",
        "    numero_str = input(\"Inserisci un numero positivo: \")",
        "    if numero_str.isdigit():",
        "        numero = int(numero_str)",
        "        if numero > 0:",
        "            print(\"Grazie! Hai inserito un numero positivo.\")",
        "            break # Ferma il ciclo",
        "    print(\"Input non valido. Riprova.\")",
        "Il codice viene eseguito e solo se la condizione (`numero > 0`) è vera, il ciclo viene interrotto con `break`.",
        "**Il ciclo `for`**",
        "Il ciclo `for` è usato per **scorrere gli elementi di una sequenza** (come una lista o un intervallo).",
        "È perfetto quando sai già quante volte devi ripetere un'azione.",
        "Esempio: stampare i numeri da 0 a 4 usando `range()`:",
        "for i in range(5): # range(5) crea una sequenza di numeri da 0 a 4",
        "    print(i)",
        "Esempio: stampare ogni lettera di una parola:",
        "parola = \"Python\"",
        "for lettera in parola:",
        "    print(lettera)",
        "Perfetto! Ora sai usare gli operatori, le condizioni e i cicli. Ottimo lavoro!",
        "Fine della Lezione 4. Torno al menu principale."
    ],
    "5": [
        "--- SEZIONE LEZIONE 5 (Le Strutture di Dati) ---",
        "Spesso si lavora con delle variabili ma se si vogliono memorizzare più valori, si usano le strutture di dati.",
        "Prendiamo per esempio che siamo in un hotel e vogliamo memorizzare i nomi degli ospiti.",
        "Per farlo, possiamo usare una lista, che è una struttura di dati che permette di memorizzare più valori in un'unica variabile.",
        "Le strutture di dati di python sono le liste, le tuple, i dizionari, gli insiemi e le enumerazioni.",
        "**Le Liste**",
        "Le liste sono collezioni ordinate di elementi, che possono essere di qualsiasi tipo (numeri, stringhe, altri oggetti).",
        "Si definiscono con le parentesi quadre `[]` e gli elementi sono separati da virgole.",
        "Esempio di lista di nomi:",
        "nomi_ospiti = ['Alice', 'Bob', 'Charlie']",
        "Puoi accedere agli elementi della lista usando l'indice (partendo da 0):",
        "print(nomi_ospiti[0])  # Stampa 'Alice'",
        "Puoi aggiungere un elemento alla lista con `append()`:",
        "nomi_ospiti.append('David')  # Aggiunge 'David' alla fine della lista",
        "Puoi rimuovere un elemento con `remove()`:",
        "nomi_ospiti.remove('Bob')  # Rimuove 'Bob' dalla lista",
        "Puoi anche ordinare la lista con `sort()`:",
        "nomi_ospiti.sort()  # Ordina la lista in ordine alfabetico",
        "Le liste sono molto flessibili e utili per memorizzare collezioni di dati.",
        "--- ESERCIZI DI ALLENAMENTO: LISTE ---",
        "Mettiamo subito in pratica ciò che hai imparato!",
        "**Esercizio 1: Crea una lista di tuoi hobby.**",
        "Crea una lista chiamata `i_miei_hobby` con almeno 3 hobby (es. 'lettura', 'cucina', 'sport').",
        # Esercizio 1 Input
        "Scrivi la riga di codice per creare la lista: ",
        "Ottimo! La tua lista è stata creata.",
        "**Esercizio 2: Accedi e stampa il secondo elemento della tua lista.**",
        "Ricorda che l'indice parte da 0!",
        # Esercizio 2 Input
        "Scrivi la riga di codice per stampare il secondo hobby: ",
        "Corretto! Hai stampato il secondo elemento.",
        "**Esercizio 3: Aggiungi un nuovo hobby alla tua lista.**",
        "Usa il metodo `append()` per aggiungere un hobby a tua scelta alla fine della lista `i_miei_hobby`.",
        # Esercizio 3 Input
        "Scrivi la riga di codice per aggiungere un hobby: ",
        "Ben fatto! Hai aggiunto un nuovo hobby alla lista.",
        "**List Comprehension**",
        "La list comprehension è un modo conciso per creare liste in Python.",
        "Permette di creare una nuova lista applicando un'espressione a ogni elemento di una sequenza (es. un'altra lista) e filtrando gli elementi in base a una condizione.",
        "La sintassi generale è: `[espressione for elemento in sequenza if condizione]`",
        "Esempio: creare una lista con i quadrati dei numeri da 0 a 9:",
        "quadrati = [x**2 for x in range(10)]",
        "Esempio: creare una lista con i numeri pari da 0 a 9:",
        "numeri_pari = [x for x in range(10) if x % 2 == 0]",
        "La list comprehension rende il codice più leggibile e compatto, soprattutto per operazioni semplici.",
        "Ora che hai visto le liste, passiamo alle altre strutture di dati.",
        "**Le Tuple**",
        "Le tuple sono simili alle liste, ma sono **immutabili**, cioè non puoi modificarle dopo averle create.",
        "Si definiscono con le parentesi tonde `()` e sono utili quando vuoi garantire che i dati non vengano modificati.",
        "Esempio di tupla di coordinate:",
        "coordinate = (10, 20)  # Tupla con due valori",
        "Puoi accedere agli elementi della tupla come nelle liste, ma non puoi modificarli:",
        "print(coordinate[0])  # Stampa 10",
        "Le tuple sono utili per rappresentare dati che non devono cambiare, come le coordinate di un punto.",
        "--- ESERCIZI DI ALLENAMENTO: TUPLE ---",
        "**Esercizio 4: Crea una tupla dei giorni della settimana (solo i primi tre).**",
        "Creala con i nomi dei giorni: 'Lun', 'Mar', 'Mer'. Chiamala `giorni_lavorativi`.",
        # Esercizio 4 Input
        "Scrivi la riga di codice per creare la tupla: ",
        "Perfetto! Hai creato la tupla `giorni_lavorativi`.",
        "**Esercizio 5: Stampa il terzo giorno della tupla.**",
        # Esercizio 5 Input
        "Scrivi la riga di codice per stampare il terzo elemento: ",
        "Bravo! Hai accesso al terzo elemento della tupla.",
        "**I Dizionari**",
        "I dizionari sono strutture di dati che memorizzano coppie chiave-valore, simili a un elenco telefonico.",
        "Si definiscono con le parentesi graffe `{}` e le chiavi sono uniche.",
        "Esempio di dizionario per un utente:",
        "utente = {'nome': 'Anna', 'eta': 30, 'citta': 'Roma'}",
        "Puoi accedere ai valori usando le chiavi:",
        "print(utente['nome'])  # Stampa 'Anna'",
        "Puoi aggiungere o modificare elementi:",
        "utente['lavoro'] = 'Ingegnere' # Aggiunge una nuova chiave-valore",
        "utente['eta'] = 31 # Modifica il valore di 'eta'",
        "--- ESERCIZI DI ALLENAMENTO: DIZIONARI ---",
        "**Esercizio 6: Crea un dizionario per un libro.**",
        "Il dizionario deve avere chiavi 'titolo', 'autore' e 'anno'. Assegna valori a tua scelta.",
        "Chiamalo `mio_libro`.",
        # Esercizio 6 Input
        "Scrivi la riga di codice per creare il dizionario: ",
        "Ottimo! Hai creato il dizionario `mio_libro`.",
        "**Esercizio 7: Stampa l'autore del libro dal tuo dizionario.**",
        # Esercizio 7 Input
        "Scrivi la riga di codice per stampare l'autore: ",
        "Corretto! Hai recuperato l'autore.",
        "Complimenti! Hai completato la lezione sulle Strutture di Dati. Ottimo lavoro!",
        "Fine della Lezione 5. Torno al menu principale."
    ],
    "6": [
        "--- SEZIONE ESERCIZI ---",
        "Benvenuto nella sezione Esercizi! Qui potrai mettere in pratica ciò che hai imparato.",
        "**Esercizio 1: Calcolatrice Semplice**",
        "Scrivi un programma che chieda all'utente due numeri e stampi la loro somma.",
        "Utilizza `input()` per ottenere i numeri e `int()` per convertirli. Poi usa `print()` per il risultato.",
        "Scrivi il tuo codice Python qui sotto (puoi scriverlo riga per riga):",
        "1. Inserisci la prima riga (es. `num1_str = input(\"Inserisci il primo numero: \")`):", # L6_EX1_NUM1_STR
        "2. Inserisci la riga per convertire `num1_str` in intero (es. `num1 = int(num1_str)`):", # L6_EX1_NUM1_INT
        "3. Inserisci la seconda riga (es. `num2_str = input(\"Inserisci il secondo numero: \")`):", # L6_EX1_NUM2_STR
        "4. Inserisci la riga per convertire `num2_str` in intero (es. `num2 = int(num2_str)`):", # L6_EX1_NUM2_INT
        "5. Inserisci la riga per calcolare la somma (es. `somma = num1 + num2`):", # L6_EX1_SOMMA
        "6. Inserisci la riga per stampare il risultato (es. `print(f\"La somma è: {somma}\")`):", # L6_EX1_PRINT
        "Complimenti! Hai completato la calcolatrice semplice.",
        "Fine Esercizi. Torno al menu principale."
    ]
}

# --- Classe principale della GUI ---
class ProgrammaLezioniPython(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Impara Python! - Lezioni Interattive')
        self.setGeometry(100, 100, 900, 700) # Dimensioni della finestra aumentate

        self.lezione_corrente = None # Tiene traccia della lezione selezionata (es. lezioni_contenuto["1"])
        self.indice_frase = 0        # Indice della frase corrente nella lezione
        self.dati_esercizio = {}     # Dizionario per tenere traccia dello stato degli esercizi e dati raccolti
        self.frasi_visualizzate = [] # Lista per tenere traccia delle frasi già mostrate
        self.stato_esercizio_corrente = None # Tiene traccia di quale esercizio è attivo

        self.setup_ui()
        self.mostra_menu_principale() # Mostra il menu all'avvio

    def setup_ui(self):
        # Layout principale verticale
        main_layout = QVBoxLayout()

        # Sezione Menu / Selezione Lezione
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(QLabel("Seleziona Lezione:"))
        self.buttons_lezioni = []
        for i in range(1, 6): # Per Lezione 1 a 5
            btn = QPushButton(f"Lezione {i}")
            btn.clicked.connect(lambda _, i=i: self.carica_lezione(str(i)))
            self.buttons_lezioni.append(btn)
            menu_layout.addWidget(btn)

        # Aggiungi il pulsante Esercizi
        btn_esercizi = QPushButton("Esercizi")
        btn_esercizi.clicked.connect(lambda: self.carica_lezione("6")) # Ora carica la lezione 6
        self.buttons_lezioni.append(btn_esercizi)
        menu_layout.addWidget(btn_esercizi)

        main_layout.addLayout(menu_layout)
        main_layout.addSpacing(10)

        # Area di visualizzazione della lezione (QTextEdit per testo formattato e scorrevole)
        self.display_area = QTextEdit()
        self.display_area.setReadOnly(True)
        self.display_area.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth) # Va a capo automaticamente
        self.display_area.setFontPointSize(12) # Dimensione del testo leggermente aumentata
        
        # Rendiamo l'area di visualizzazione scorrevole se il contenuto è troppo lungo
        scroll_area_lezione = QScrollArea()
        scroll_area_lezione.setWidgetResizable(True)
        scroll_area_lezione.setWidget(self.display_area)
        
        # Imposta una policy di espansione per far occupare a display_area tutto lo spazio possibile
        self.display_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(scroll_area_lezione)

        # Sezione Navigazione Frase
        nav_layout = QHBoxLayout()
        self.btn_indietro = QPushButton("← Indietro")
        self.btn_indietro.clicked.connect(self.frase_precedente)
        self.btn_indietro.setEnabled(False) # Disabilita all'inizio
        nav_layout.addWidget(self.btn_indietro)

        self.label_frase_status = QLabel("Menu Principale")
        self.label_frase_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_layout.addWidget(self.label_frase_status)

        self.btn_avanti = QPushButton("Avanti →")
        self.btn_avanti.clicked.connect(self.frase_successiva)
        self.btn_avanti.setEnabled(False) # Disabilita all'inizio
        nav_layout.addWidget(self.btn_avanti)
        main_layout.addLayout(nav_layout)

        # Sezione Input Utente per esercizi
        input_layout = QHBoxLayout()
        self.label_input_domanda = QLabel("Input:")
        self.label_input_domanda.setVisible(False) # Nascosto all'inizio
        input_layout.addWidget(self.label_input_domanda)
        
        self.input_esercizio = QLineEdit()
        self.input_esercizio.setPlaceholderText("Digita la tua risposta qui...")
        self.input_esercizio.setVisible(False) # Nascosto all'inizio
        self.input_esercizio.setStyleSheet("font-size: 11pt;") # Questo è il modo corretto per impostare la dimensione del font per QLineEdit con stili CSS
        self.input_esercizio.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed) # Ingrandisce l'input
        self.input_esercizio.returnPressed.connect(self.handle_esercizio_input) # Collega l'invio alla funzione
        input_layout.addWidget(self.input_esercizio)

        self.btn_invia_esercizio = QPushButton("Invia")
        self.btn_invia_esercizio.clicked.connect(self.handle_esercizio_input)
        self.btn_invia_esercizio.setVisible(False) # Nascosto all'inizio
        input_layout.addWidget(self.btn_invia_esercizio)
        
        main_layout.addLayout(input_layout)

        # Pulsante Torna al Menu Principale e Esci
        bottom_buttons_layout = QHBoxLayout()
        self.btn_torna_menu = QPushButton("Torna al Menu Principale")
        self.btn_torna_menu.clicked.connect(self.mostra_menu_principale)
        bottom_buttons_layout.addWidget(self.btn_torna_menu)
        
        self.button_esci = QPushButton('Esci dal Programma')
        self.button_esci.clicked.connect(self.close)
        bottom_buttons_layout.addWidget(self.button_esci)
        main_layout.addLayout(bottom_buttons_layout)

        self.setLayout(main_layout)
    
    def mostra_menu_principale(self):
        self.lezione_corrente = None
        self.indice_frase = 0
        self.dati_esercizio = {} # Resetta lo stato dell'esercizio
        self.frasi_visualizzate = [] # Resetta le frasi visualizzate
        self.stato_esercizio_corrente = None # Resetta lo stato dell'esercizio corrente
        self.display_area.clear()
        
        self.display_area.insertHtml(
            "<h3 style='color: #FF8C00;'>ATTENZIONE! PER ESEGUIRE I CODICI SPIEGATI IN QUESTA SERIE DI LEZIONI è NECESSARIO SCARICARE LA VERSIONE 3 DI PYTHON (tutte le sotto-versioni sono accettate! es 3.14)</h3>"
            "<p style='font-weight: bold; color: #555;'>WORK IN PROGRESS, PREVIEW PRIVATA! NON SCATTARE SCREENSHOT O CONDIVIDERE IL PROGETTO!</p>"
            "<h2 style='color: #4CAF50;'>--- MENU PRINCIPALE ---</h2>"
            "<p>Ciao! Benvenuto nel programma di lezioni Python! Scegli tra le seguenti opzioni qual è la migliore: </p>"
            "<p><b>1: Lezione 1 (Hello, World!)</b></p>"
            "<p><b>2: Lezione 2 (Variabili)</b></p>"
            "<p><b>3: Lezione 3 (Conversioni fra Stringhe e Numeri)</b></p>"
            "<p><b>4: Lezione 4 (Operatori e Strutture di Controllo)</b></p>"
            "<p><b>5: Lezione 5 (Le Strutture di Dati)</b></p>"
            "<p><b>6: Esercizi</b></p>"
        )
        self.label_frase_status.setText("Menu Principale")
        self.btn_indietro.setEnabled(False)
        self.btn_avanti.setEnabled(False)
        self.nascondi_input_esercizio()

    def carica_lezione(self, numero_lezione):
        if numero_lezione in lezioni_contenuto:
            self.lezione_corrente = lezioni_contenuto[numero_lezione]
            self.indice_frase = 0
            self.dati_esercizio = {} # Resetta i dati dell'esercizio per la nuova lezione
            self.frasi_visualizzate = [] # Inizializza la lista per la nuova lezione
            self.stato_esercizio_corrente = None # Resetta lo stato dell'esercizio
            self.display_area.clear() # Pulisce la display area prima di iniziare
            self.mostra_frase_corrente()
            self.abilita_navigazione()
            self.nascondi_input_esercizio()
        else:
            QMessageBox.warning(self, "Errore", "Lezione non trovata o non ancora implementata.")
            self.mostra_menu_principale() # Torna al menu se la lezione non esiste

    def abilita_navigazione(self):
        self.btn_indietro.setEnabled(self.indice_frase > 0)
        self.btn_avanti.setEnabled(self.indice_frase < len(self.lezione_corrente) - 1)

    def get_lezione_numero(self):
        # Trova la chiave della lezione corrente
        for num, contenuto in lezioni_contenuto.items():
            if contenuto == self.lezione_corrente:
                return num
        return None

    def aggiorna_display_area(self):
        # Pulisce e riscrive tutte le frasi visualizzate finora
        self.display_area.clear()
        for frase in self.frasi_visualizzate:
            # Aggiungi formattazione semplice per il codice (backticks)
            formatted_frase = frase.replace("`", "<tt>").replace("`", "</tt>")
            if frase.startswith("---") and frase.endswith("---"):
                self.display_area.append(f"<h3 style='color: #4682B4;'>{formatted_frase}</h3>")
            elif frase.startswith("**") and frase.endswith("**"):
                self.display_area.append(f"<p><strong>{formatted_frase.strip('**')}</strong></p>")
            elif formatted_frase.startswith("Esempio:") or formatted_frase.startswith("numero") or formatted_frase.startswith("saluto") or formatted_frase.startswith("if") or formatted_frase.startswith("for") or formatted_frase.startswith("while"):
                 # Tenta di identificare blocchi di codice
                self.display_area.append(f"<pre style='background-color:#eee; padding:5px; border-radius:4px;'><code>{formatted_frase}</code></pre>")
            else:
                self.display_area.append(f"<p>{formatted_frase}</p>")
        
        # Scorre automaticamente fino in fondo
        self.display_area.verticalScrollBar().setValue(self.display_area.verticalScrollBar().maximum())

    def mostra_frase_corrente(self):
        if self.lezione_corrente is not None:
            if 0 <= self.indice_frase < len(self.lezione_corrente):
                frase = self.lezione_corrente[self.indice_frase]
                
                # Aggiungi la frase corrente alla lista delle frasi visualizzate
                if self.indice_frase == len(self.frasi_visualizzate):
                    self.frasi_visualizzate.append(frase)
                
                self.aggiorna_display_area()
                
                self.label_frase_status.setText(f"Lezione {self.get_lezione_numero()}: Frase {self.indice_frase + 1}/{len(self.lezione_corrente)}")

                self.nascondi_input_esercizio() # Nascondi per default
                self.stato_esercizio_corrente = None # Resetta lo stato dell'esercizio

                # --- Gestione specifica per gli esercizi interattivi ---
                lezione_num = self.get_lezione_numero()

                if lezione_num == "1" and frase.startswith("Ora prova tu, scrivi il comando print()"):
                    self.mostra_input_esercizio("L1_HW_INPUT")
                    self.label_input_domanda.setText("Il tuo codice:")
                
                # Lezione 2
                elif lezione_num == "2":
                    if frase.startswith("Iniziamo creando una variabile: scegli un nome per essa"):
                        self.mostra_input_esercizio("L2_VAR_NOME")
                        self.label_input_domanda.setText("Nome variabile:")
                    elif frase.startswith("Scrivi la parte che manca (solo ` = input()`):"):
                        self.mostra_input_esercizio("L2_VAR_ASSIGN")
                        self.label_input_domanda.setText("Parte codice:")
                    elif frase.startswith("Inserisci la domanda tra virgolette che vuoi far apparire:"):
                        self.mostra_input_esercizio("L2_VAR_QUESTION")
                        self.label_input_domanda.setText("Domanda:")
                    elif frase.startswith("Scrivi la riga di codice completa per stampare la variabile"):
                        self.mostra_input_esercizio("L2_VAR_PRINT")
                        self.label_input_domanda.setText("Codice print():")

                # Lezione 3
                elif lezione_num == "3":
                    if frase.startswith("Iniziamo creando la variabile per l'input: Metti come nome della variabile 'eta_utente'"):
                        self.mostra_input_esercizio("L3_CONV_VAR_ETA")
                        self.label_input_domanda.setText("Codice variabile:")
                    elif frase.startswith("Scrivi la riga di codice `if not eta_utente.isdigit():`"):
                        self.mostra_input_esercizio("L3_CONV_ISDIGIT")
                        self.label_input_domanda.setText("Codice if:")
                    elif frase.startswith("Scrivi la riga di codice `eta_numerica = int(eta_utente)`:"):
                        self.mostra_input_esercizio("L3_CONV_INT")
                        self.label_input_domanda.setText("Codice int():")

                # Lezione 4
                elif lezione_num == "4":
                    if frase.startswith("Inserisci la tua età (un numero!): "):
                        self.mostra_input_esercizio("L4_REL_ETA_INPUT")
                        self.label_input_domanda.setText("La tua età:")
                    elif frase.startswith("Inserisci la tua età per vedere se puoi prendere la patente in Italia (18 anni): "):
                        self.mostra_input_esercizio("L4_COND_ETA_PATENTE_INPUT")
                        self.label_input_domanda.setText("La tua età:")

                # Lezione 5
                elif lezione_num == "5":
                    if frase.startswith("Scrivi la riga di codice per creare la lista: "):
                        self.mostra_input_esercizio("L5_LIST_1")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per stampare il secondo hobby: "):
                        self.mostra_input_esercizio("L5_LIST_2")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per aggiungere un hobby: "):
                        self.mostra_input_esercizio("L5_LIST_3")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per creare la tupla: "):
                        self.mostra_input_esercizio("L5_TUPLE_1")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per stampare il terzo elemento: "):
                        self.mostra_input_esercizio("L5_TUPLE_2")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per creare il dizionario: "):
                        self.mostra_input_esercizio("L5_DICT_1")
                        self.label_input_domanda.setText("Il tuo codice:")
                    elif frase.startswith("Scrivi la riga di codice per stampare l'autore: "):
                        self.mostra_input_esercizio("L5_DICT_2")
                        self.label_input_domanda.setText("Il tuo codice:")
                
                # Lezione 6 (Esercizi)
                elif lezione_num == "6":
                    if frase.startswith("1. Inserisci la prima riga (es. `num1_str = input"):
                        self.mostra_input_esercizio("L6_EX1_NUM1_STR")
                        self.label_input_domanda.setText("Riga 1:")
                    elif frase.startswith("2. Inserisci la riga per convertire `num1_str` in intero"):
                        self.mostra_input_esercizio("L6_EX1_NUM1_INT")
                        self.label_input_domanda.setText("Riga 2:")
                    elif frase.startswith("3. Inserisci la seconda riga (es. `num2_str = input"):
                        self.mostra_input_esercizio("L6_EX1_NUM2_STR")
                        self.label_input_domanda.setText("Riga 3:")
                    elif frase.startswith("4. Inserisci la riga per convertire `num2_str` in intero"):
                        self.mostra_input_esercizio("L6_EX1_NUM2_INT")
                        self.label_input_domanda.setText("Riga 4:")
                    elif frase.startswith("5. Inserisci la riga per calcolare la somma"):
                        self.mostra_input_esercizio("L6_EX1_SOMMA")
                        self.label_input_domanda.setText("Riga 5:")
                    elif frase.startswith("6. Inserisci la riga per stampare il risultato"):
                        self.mostra_input_esercizio("L6_EX1_PRINT")
                        self.label_input_domanda.setText("Riga 6:")

            else: # Fine della lezione
                self.display_area.append("<p style='font-weight: bold; color: #007bff;'>Fine della lezione! Puoi tornare al menu principale o sfogliare le lezioni.</p>")
                self.label_frase_status.setText(f"Lezione {self.get_lezione_numero()}: Fine")
                self.btn_avanti.setEnabled(False)
                self.nascondi_input_esercizio()

        self.abilita_navigazione()

    def frase_successiva(self):
        if self.lezione_corrente is not None and self.indice_frase < len(self.lezione_corrente) - 1:
            self.indice_frase += 1
            self.mostra_frase_corrente()

    def frase_precedente(self):
        if self.lezione_corrente is not None and self.indice_frase > 0:
            self.indice_frase -= 1
            # Quando si torna indietro, vogliamo che tutte le frasi fino a quel punto siano visibili
            self.frasi_visualizzate = self.lezione_corrente[:self.indice_frase + 1]
            self.mostra_frase_corrente()
    
    def mostra_input_esercizio(self, id_esercizio):
        self.label_input_domanda.setVisible(True)
        self.input_esercizio.setVisible(True)
        self.btn_invia_esercizio.setVisible(True)
        self.input_esercizio.clear() # Pulisce l'input precedente
        self.input_esercizio.setFocus() # Mette il focus sull'input
        self.stato_esercizio_corrente = id_esercizio # Imposta lo stato dell'esercizio corrente
        self.btn_avanti.setEnabled(False) # Disabilita il pulsante avanti durante l'esercizio

    def nascondi_input_esercizio(self):
        self.label_input_domanda.setVisible(False)
        self.input_esercizio.setVisible(False)
        self.btn_invia_esercizio.setVisible(False)
        self.stato_esercizio_corrente = None # Resetta lo stato dell'esercizio

    def handle_esercizio_input(self):
        user_input = self.input_esercizio.text().strip()
        lezione_num = self.get_lezione_numero()

        # Feedback immediato nell'area di visualizzazione
        self.display_area.append(f"<p style='color: #0000FF;'><b>Il tuo input:</b> {user_input}</p>")
        
        # Logica per Lezione 1: Hello World
        if self.stato_esercizio_corrente == "L1_HW_INPUT":
            if user_input.lower() == "print(\"hello, world!\")" or user_input.lower() == "print('hello, world!')":
                self.display_area.append("<p style='color: green;'>Corretto! Hai scritto il tuo primo Hello, World! in Python.</p>")
                self.nascondi_input_esercizio()
                self.frase_successiva() # Passa alla frase successiva
            else:
                self.display_area.append("<p style='color: red;'>Sbagliato. Assicurati di usare `print(\"Hello, World!\")` con le virgolette e la P minuscola.</p>")
                QMessageBox.warning(self, "Riprova", "Controlla la sintassi esatta.")

        # Logica per Lezione 2: Variabili
        elif lezione_num == "2":
            if self.stato_esercizio_corrente == "L2_VAR_NOME":
                if user_input.replace(" ", "").replace("_", "").isalnum() and not user_input[0].isdigit():
                    self.dati_esercizio['nome_variabile'] = user_input.replace(" ", "_") # Normalizza il nome
                    self.display_area.append(f"<p style='color: green;'>Nome variabile '{self.dati_esercizio['nome_variabile']}' accettato!</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Nome variabile non valido. Deve iniziare con una lettera o underscore e contenere solo lettere, numeri o underscore.</p>")
                    QMessageBox.warning(self, "Riprova", "Nome variabile non valido.")
            
            elif self.stato_esercizio_corrente == "L2_VAR_ASSIGN":
                expected_input = "= input()"
                if user_input.strip() == expected_input:
                    self.display_area.append("<p style='color: green;'>Corretto! Hai assegnato l'input alla variabile.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La risposta attesa è ` = input()`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")
            
            elif self.stato_esercizio_corrente == "L2_VAR_QUESTION":
                # Verifica se l'input è tra virgolette e non è vuoto
                if (user_input.startswith('"') and user_input.endswith('"')) or \
                   (user_input.startswith("'") and user_input.endswith("'")):
                    if len(user_input) > 2: # Almeno un carattere tra virgolette
                        self.dati_esercizio['domanda_input'] = user_input.strip()
                        self.display_area.append(f"<p style='color: green;'>Domanda '{self.dati_esercizio['domanda_input']}' accettata!</p>")
                        self.nascondi_input_esercizio()
                        self.frase_successiva()
                    else:
                         self.display_area.append("<p style='color: red;'>La domanda non può essere vuota.</p>")
                         QMessageBox.warning(self, "Riprova", "La domanda non può essere vuota.")
                else:
                    self.display_area.append("<p style='color: red;'>La domanda deve essere racchiusa tra virgolette doppie o singole.</p>")
                    QMessageBox.warning(self, "Riprova", "Ricorda le virgolette.")
            
            elif self.stato_esercizio_corrente == "L2_VAR_PRINT":
                nome_var = self.dati_esercizio.get('nome_variabile', 'mia_frase')
                expected_print = f"print({nome_var})"
                if user_input.strip().lower() == expected_print.lower():
                    self.display_area.append(f"<p style='color: green;'>Corretto! Hai stampato la variabile '{nome_var}'.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append(f"<p style='color: red;'>Sbagliato. La risposta attesa è `print({nome_var})`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")

        # Logica per Lezione 3: Conversioni
        elif lezione_num == "3":
            if self.stato_esercizio_corrente == "L3_CONV_VAR_ETA":
                expected_code_part1 = "eta_utente = input(\"Quanti anni hai?\")"
                expected_code_part2 = "eta_utente = input('Quanti anni hai?')"
                if user_input.strip() == expected_code_part1 or user_input.strip() == expected_code_part2:
                    self.dati_esercizio['eta_var_name'] = 'eta_utente' # Memorizza il nome della variabile
                    self.display_area.append("<p style='color: green;'>Corretto! Hai creato la variabile `eta_utente` con l'input.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La sintassi corretta è `eta_utente = input(\"Quanti anni hai?\")`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")

            elif self.stato_esercizio_corrente == "L3_CONV_ISDIGIT":
                expected_if = "if not eta_utente.isdigit():"
                expected_print = "print(\"Input non valido!\")" # O con virgolette singole
                expected_print2 = "print('Input non valido!')"
                
                # Permetti di ricevere le due righe separate o una dopo l'altra
                if 'L3_CONV_ISDIGIT_STATE' not in self.dati_esercizio:
                    self.dati_esercizio['L3_CONV_ISDIGIT_STATE'] = 0

                if self.dati_esercizio['L3_CONV_ISDIGIT_STATE'] == 0:
                    if user_input.strip() == expected_if:
                        self.display_area.append("<p style='color: green;'>Prima riga corretta! Adesso inserisci la riga di `print()` indentata.</p>")
                        self.dati_esercizio['L3_CONV_ISDIGIT_STATE'] = 1
                        self.input_esercizio.clear() # Pulisce per il prossimo input
                    else:
                        self.display_area.append("<p style='color: red;'>Sbagliato. Assicurati di scrivere `if not eta_utente.isdigit():`</p>")
                        QMessageBox.warning(self, "Riprova", "Controlla la condizione `if`.")
                elif self.dati_esercizio['L3_CONV_ISDIGIT_STATE'] == 1:
                    if user_input.strip() == expected_print or user_input.strip() == expected_print2:
                        self.display_area.append("<p style='color: green;'>Seconda riga corretta! Hai gestito l'input non numerico.</p>")
                        self.nascondi_input_esercizio()
                        self.frase_successiva()
                    else:
                        self.display_area.append("<p style='color: red;'>Sbagliato. Assicurati che il messaggio di errore sia indentato e corretto.</p>")
                        QMessageBox.warning(self, "Riprova", "Controlla il messaggio di errore.")

            elif self.stato_esercizio_corrente == "L3_CONV_INT":
                expected_conversion = "eta_numerica = int(eta_utente)"
                if user_input.strip() == expected_conversion:
                    self.display_area.append("<p style='color: green;'>Corretto! Hai convertito la stringa in numero intero.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La sintassi attesa è `eta_numerica = int(eta_utente)`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la conversione con `int()`.")

        # Logica per Lezione 4: Operatori Relazionali e Condizioni
        elif lezione_num == "4":
            if self.stato_esercizio_corrente == "L4_REL_ETA_INPUT":
                try:
                    eta = int(user_input)
                    if eta >= 0:
                        self.display_area.append(f"<p>La tua età è: {eta} anni.</p>")
                        self.display_area.append(f"<p style='font-weight: bold;'>Sei maggiorenne? {eta >= 18}</p>")
                        self.nascondi_input_esercizio()
                        self.frase_successiva()
                    else:
                        self.display_area.append("<p style='color: red;'>L'età non può essere negativa.</p>")
                        QMessageBox.warning(self, "Errore", "L'età deve essere un numero positivo.")
                except ValueError:
                    self.display_area.append("<p style='color: red;'>Input non valido. Inserisci un numero intero per l'età.</p>")
                    QMessageBox.warning(self, "Errore", "Inserisci un numero valido.")

            elif self.stato_esercizio_corrente == "L4_COND_ETA_PATENTE_INPUT":
                try:
                    eta = int(user_input)
                    self.display_area.append(f"<p>Hai inserito: {eta} anni.</p>")
                    if eta >= 18:
                        self.display_area.append("<p style='color: green;'>Congratulazioni! Puoi prendere la patente in Italia.</p>")
                    else:
                        self.display_area.append("<p style='color: orange;'>Mi dispiace, non hai ancora l'età per prendere la patente in Italia.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                except ValueError:
                    self.display_area.append("<p style='color: red;'>Input non valido. Inserisci un numero intero per l'età.</p>")
                    QMessageBox.warning(self, "Errore", "Inserisci un numero valido.")

        # Logica per Lezione 5: Strutture di Dati
        elif lezione_num == "5":
            if self.stato_esercizio_corrente == "L5_LIST_1":
                # Controllo base per una lista di almeno 3 elementi
                if user_input.strip().startswith("i_miei_hobby = [") and user_input.strip().endswith("]"):
                    try:
                        # Tenta di eseguire il codice per vedere se è una lista valida
                        exec(user_input, globals(), self.dati_esercizio) # Esegui nel contesto del dizionario esercizio
                        if 'i_miei_hobby' in self.dati_esercizio and isinstance(self.dati_esercizio['i_miei_hobby'], list) and len(self.dati_esercizio['i_miei_hobby']) >= 3:
                            self.display_area.append("<p style='color: green;'>Corretto! Hai creato la tua lista di hobby.</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Assicurati che sia una lista con almeno 3 elementi.</p>")
                            QMessageBox.warning(self, "Riprova", "Formato lista o numero elementi errato.")
                    except Exception as e:
                        self.display_area.append(f"<p style='color: red;'>Errore di sintassi nel tuo codice: {e}</p>")
                        QMessageBox.warning(self, "Errore", "Errore di sintassi.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta per la creazione di una lista.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla le parentesi quadre e il nome della variabile.")
            
            elif self.stato_esercizio_corrente == "L5_LIST_2":
                # Esempio: print(i_miei_hobby[1])
                expected_start = "print(i_miei_hobby["
                expected_end = "])"
                if user_input.strip().startswith(expected_start) and user_input.strip().endswith(expected_end):
                    try:
                        # Estrai l'indice e prova a stamparlo (simulazione)
                        index_str = user_input.strip()[len(expected_start):-len(expected_end)]
                        index = int(index_str)
                        if 'i_miei_hobby' in self.dati_esercizio and index < len(self.dati_esercizio['i_miei_hobby']):
                            self.display_area.append(f"<p style='color: green;'>Corretto! Il secondo hobby è: {self.dati_esercizio['i_miei_hobby'][index]}.</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Indice non valido o lista non trovata. Ricorda l'indice parte da 0.</p>")
                            QMessageBox.warning(self, "Riprova", "Indice non valido.")
                    except (ValueError, IndexError):
                        self.display_area.append("<p style='color: red;'>Sintassi o indice non valido. Esempio: `print(i_miei_hobby[1])`.</p>")
                        QMessageBox.warning(self, "Riprova", "Controlla sintassi o indice.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta. Assicurati di usare `print(nome_lista[indice])`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")

            elif self.stato_esercizio_corrente == "L5_LIST_3":
                # Esempio: i_miei_hobby.append('nuoto')
                expected_start = "i_miei_hobby.append("
                expected_end = ")"
                if user_input.strip().startswith(expected_start) and user_input.strip().endswith(expected_end):
                    try:
                        hobby_to_add = user_input.strip()[len(expected_start):-len(expected_end)]
                        if 'i_miei_hobby' in self.dati_esercizio and hobby_to_add:
                            # Aggiungi realmente l'elemento alla lista
                            eval(f"self.dati_esercizio['i_miei_hobby'].append({hobby_to_add})") # Eval è potente, usalo con cautela
                            self.display_area.append(f"<p style='color: green;'>Corretto! Nuovo hobby '{hobby_to_add.strip('\'" ')}' aggiunto. La tua lista aggiornata è: {self.dati_esercizio['i_miei_hobby']}</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Non hai specificato un hobby da aggiungere o la lista non esiste.</p>")
                            QMessageBox.warning(self, "Riprova", "Manca l'hobby o la lista.")
                    except Exception as e:
                        self.display_area.append(f"<p style='color: red;'>Errore di sintassi: {e}</p>")
                        QMessageBox.warning(self, "Errore", "Errore di sintassi.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta. Esempio: `i_miei_hobby.append('nuoto')`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")

            elif self.stato_esercizio_corrente == "L5_TUPLE_1":
                # Controllo base per una tupla di 3 elementi
                if user_input.strip().startswith("giorni_lavorativi = (") and user_input.strip().endswith(")"):
                    try:
                        exec(user_input, globals(), self.dati_esercizio)
                        if 'giorni_lavorativi' in self.dati_esercizio and isinstance(self.dati_esercizio['giorni_lavorativi'], tuple) and len(self.dati_esercizio['giorni_lavorativi']) == 3:
                            self.display_area.append("<p style='color: green;'>Corretto! Hai creato la tupla dei giorni lavorativi.</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Assicurati che sia una tupla con esattamente 3 elementi.</p>")
                            QMessageBox.warning(self, "Riprova", "Formato tupla o numero elementi errato.")
                    except Exception as e:
                        self.display_area.append(f"<p style='color: red;'>Errore di sintassi nel tuo codice: {e}</p>")
                        QMessageBox.warning(self, "Errore", "Errore di sintassi.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta per la creazione di una tupla.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla le parentesi tonde e il nome della variabile.")

            elif self.stato_esercizio_corrente == "L5_TUPLE_2":
                # Esempio: print(giorni_lavorativi[2])
                expected_start = "print(giorni_lavorativi["
                expected_end = "])"
                if user_input.strip().startswith(expected_start) and user_input.strip().endswith(expected_end):
                    try:
                        index_str = user_input.strip()[len(expected_start):-len(expected_end)]
                        index = int(index_str)
                        if 'giorni_lavorativi' in self.dati_esercizio and index < len(self.dati_esercizio['giorni_lavorativi']) and index == 2: # Specifico per il terzo elemento
                            self.display_area.append(f"<p style='color: green;'>Corretto! Il terzo giorno è: {self.dati_esercizio['giorni_lavorativi'][index]}.</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Indice non valido o tupla non trovata. Ricorda che il terzo elemento è all'indice 2.</p>")
                            QMessageBox.warning(self, "Riprova", "Indice errato.")
                    except (ValueError, IndexError):
                        self.display_area.append("<p style='color: red;'>Sintassi o indice non valido. Esempio: `print(giorni_lavorativi[2])`.</p>")
                        QMessageBox.warning(self, "Riprova", "Controlla sintassi o indice.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta. Assicurati di usare `print(nome_tupla[indice])`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")
            
            elif self.stato_esercizio_corrente == "L5_DICT_1":
                # Controllo base per un dizionario con chiavi specifiche
                if user_input.strip().startswith("mio_libro = {") and user_input.strip().endswith("}"):
                    try:
                        exec(user_input, globals(), self.dati_esercizio)
                        if 'mio_libro' in self.dati_esercizio and isinstance(self.dati_esercizio['mio_libro'], dict) and \
                           all(key in self.dati_esercizio['mio_libro'] for key in ['titolo', 'autore', 'anno']):
                            self.display_area.append("<p style='color: green;'>Corretto! Hai creato il dizionario del libro.</p>")
                            self.nascondi_input_esercizio()
                            self.frase_successiva()
                        else:
                            self.display_area.append("<p style='color: red;'>Assicurati che il dizionario contenga le chiavi 'titolo', 'autore' e 'anno'.</p>")
                            QMessageBox.warning(self, "Riprova", "Chiavi mancanti o formato errato.")
                    except Exception as e:
                        self.display_area.append(f"<p style='color: red;'>Errore di sintassi nel tuo codice: {e}</p>")
                        QMessageBox.warning(self, "Errore", "Errore di sintassi.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta per la creazione di un dizionario.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla le parentesi graffe e il nome della variabile.")

            elif self.stato_esercizio_corrente == "L5_DICT_2":
                # Esempio: print(mio_libro['autore'])
                expected_start_single = "print(mio_libro['autore'])"
                expected_start_double = "print(mio_libro[\"autore\"])"
                if user_input.strip() == expected_start_single or user_input.strip() == expected_start_double:
                    if 'mio_libro' in self.dati_esercizio and 'autore' in self.dati_esercizio['mio_libro']:
                        self.display_area.append(f"<p style='color: green;'>Corretto! L'autore è: {self.dati_esercizio['mio_libro']['autore']}.</p>")
                        self.nascondi_input_esercizio()
                        self.frase_successiva()
                    else:
                        self.display_area.append("<p style='color: red;'>Dizionario o chiave 'autore' non trovata.</p>")
                        QMessageBox.warning(self, "Riprova", "Dizionario o chiave errata.")
                else:
                    self.display_area.append("<p style='color: red;'>Sintassi non corretta. Esempio: `print(mio_libro['autore'])`.</p>")
                    QMessageBox.warning(self, "Riprova", "Controlla la sintassi.")

        # Logica per Lezione 6: Esercizi (Calcolatrice Semplice)
        elif lezione_num == "6":
            if self.stato_esercizio_corrente == "L6_EX1_NUM1_STR":
                expected = "num1_str = input(\"Inserisci il primo numero: \")"
                expected_alt = "num1_str = input('Inserisci il primo numero: ')"
                if user_input.strip() == expected or user_input.strip() == expected_alt:
                    self.dati_esercizio['L6_num1_str_code'] = user_input.strip()
                    self.display_area.append("<p style='color: green;'>Corretto! Passiamo alla prossima riga.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. Controlla la sintassi esatta per l'input.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi errata.")
            
            elif self.stato_esercizio_corrente == "L6_EX1_NUM1_INT":
                expected = "num1 = int(num1_str)"
                if user_input.strip() == expected:
                    self.dati_esercizio['L6_num1_int_code'] = user_input.strip()
                    self.display_area.append("<p style='color: green;'>Ottimo! Hai convertito il primo numero.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La sintassi per la conversione è `num1 = int(num1_str)`.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi errata.")

            elif self.stato_esercizio_corrente == "L6_EX1_NUM2_STR":
                expected = "num2_str = input(\"Inserisci il secondo numero: \")"
                expected_alt = "num2_str = input('Inserisci il secondo numero: ')"
                if user_input.strip() == expected or user_input.strip() == expected_alt:
                    self.dati_esercizio['L6_num2_str_code'] = user_input.strip()
                    self.display_area.append("<p style='color: green;'>Corretto! Passiamo alla prossima riga.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. Controlla la sintassi esatta per il secondo input.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi errata.")
            
            elif self.stato_esercizio_corrente == "L6_EX1_NUM2_INT":
                expected = "num2 = int(num2_str)"
                if user_input.strip() == expected:
                    self.dati_esercizio['L6_num2_int_code'] = user_input.strip()
                    self.display_area.append("<p style='color: green;'>Ottimo! Hai convertito il secondo numero.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La sintassi per la conversione è `num2 = int(num2_str)`.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi errata.")

            elif self.stato_esercizio_corrente == "L6_EX1_SOMMA":
                expected = "somma = num1 + num2"
                if user_input.strip() == expected:
                    self.dati_esercizio['L6_somma_code'] = user_input.strip()
                    self.display_area.append("<p style='color: green;'>Corretto! La somma è calcolata.</p>")
                    self.nascondi_input_esercizio()
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. La sintassi per la somma è `somma = num1 + num2`.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi errata.")

            elif self.stato_esercizio_corrente == "L6_EX1_PRINT":
                # Accetta f-string o concatenazione semplice
                expected_fstring_prefix = "print(f\""
                expected_fstring_suffix = "\")"
                expected_concat_prefix = "print(\"La somma è: \""
                
                is_correct = False
                if user_input.strip().startswith(expected_fstring_prefix) and user_input.strip().endswith(expected_fstring_suffix):
                    if "{somma}" in user_input.strip():
                        is_correct = True
                elif "print(\"La somma è: \" + str(somma))" in user_input.strip(): # Un'altra forma comune
                    is_correct = True
                elif "print('La somma è: ' + str(somma))" in user_input.strip():
                    is_correct = True

                if is_correct:
                    self.display_area.append("<p style='color: green;'>Fantastico! Hai stampato il risultato della somma.</p>")
                    self.nascondi_input_esercizio()
                    # Simula l'esecuzione dell'esercizio completo e mostra il risultato
                    self.display_area.append("<p style='font-weight: bold;'>Esecuzione del tuo codice completo:</p>")
                    self.display_area.append("<pre style='background-color:#e0ffe0; padding:5px; border-left: 3px solid green;'>")
                    self.display_area.append(self.dati_esercizio.get('L6_num1_str_code', ''))
                    self.display_area.append(self.dati_esercizio.get('L6_num1_int_code', ''))
                    self.display_area.append(self.dati_esercizio.get('L6_num2_str_code', ''))
                    self.display_area.append(self.dati_esercizio.get('L6_num2_int_code', ''))
                    self.display_area.append(self.dati_esercizio.get('L6_somma_code', ''))
                    self.display_area.append(user_input.strip())
                    self.display_area.append("</pre>")
                    self.display_area.append("<p style='font-weight: bold;'>(L'output del tuo codice simulato apparirebbe qui se fosse un ambiente di esecuzione reale.)</p>")
                    QMessageBox.information(self, "Esercizio Completato", "Complimenti! Hai completato l'esercizio della Calcolatrice Semplice!")
                    self.frase_successiva()
                else:
                    self.display_area.append("<p style='color: red;'>Sbagliato. Controlla la sintassi per stampare la variabile `somma`.</p>")
                    QMessageBox.warning(self, "Riprova", "Sintassi per la stampa errata.")


        self.input_esercizio.clear() # Pulisce l'input dopo l'invio


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgrammaLezioniPython()
    window.show()
    sys.exit(app.exec())



    