# Manimations Repository Template

Questa repository è pensata per definire una struttura comune a tutto il codice sorgente e relativi exports che vengono utilizzati per creare il materiale utilizzato nelle presentazioni delle varie rassegne.

La struttura intende seguire delle semplici regole di buonsenso per dare una buona organizzazione al codice e agli asset, per impedire alla vena creativa che accompagna la fase di creazione delle animazioni di prendere il sopravvento sullo spirito preciso e ordinato dell'informatico.

## Come compilare un'animazione
### Prerequisiti software
1. Questo progetto utilizza `uv` (doc. ufficiale: https://docs.astral.sh/uv/) come project manager di Python.
    - installalo guardando la documentazione ufficiale oppure tramite il seguente comando:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Assicurati di aver installato le dipendenze necessarie a `manim` per poter funzionare correttamente (i.e. su MacOS. `cairo`, `pkg-config`, consulta la [documentazione](https://docs.manim.community/en/stable/installation/uv.html) per le istruzioni di installazione personalizzate per il tuo OS.)

> [!IMPORTANT] 
> **Versione Python** — Versione di Python richiesta: 3.13 (vedasi il file [`.python-version`](.python-version))
    
> [!IMPORTANT]
> **LaTex** — Anche se la guida ufficiale di Manim segnala LaTex come dipendenza opzionale per Manim, è caldamente consigliato installarlo in qualsiasi caso (altrimenti oggetti come `Tex` o `MathTex` non sono utilizzabili).
> - Ricorda: riavvia il sistema una volta installato tutto quanto!

3. Una volta fatto, è possibile lanciare il seguente comando per verificare la correttezza delle installazioni effettuate:
```sh
uv run manim checkhealth
```

Verrà mostrato nel terminale un risultato del genere:
```sh
Checking whether your installation of Manim Community is healthy...
- Checking whether manim is on your PATH ... PASSED
- Checking whether the executable belongs to manim ... PASSED
- Checking whether latex is available ... PASSED
- Checking whether dvisvgm is available ... PASSED
```
- assicurarsi di avere tutte le voci spuntate con `PASSED`!

### Da linea di comando
Aprendo un terminale nella root del progetto, è possibile digitare
```sh
uv run manim -pqm TestScene.py
```

Per semplificare la compilazione è possibile utilizzare il wrapper di Manim `manimw.py`, presente all'interno della root del progetto.

Le opzioni da riga di comando che il wrapper accetta sono visualizzabili digitando: 
```sh
./manimw.py -h
```
che produrrà un output simile:
```sh
usage: manimw.py [-h] [-a] [-r {16:9,16:10}] [-q {l,m,h}] [-m] [file] [scene]

positional arguments:
  file                  Path to the manim .py file
  scene                 Specific Scene class

options:
  -h, --help            show this help message and exit
  -a, --all             Compile everything in src/
  -r, --ratio {16:9,16:10}
  -q, --quality {l,m,h}
                        Choose the quality of the rendering — l: low, m: medium,
                        h: high
  -m, --media           Choose to keep media/ folder (default: False)
```

> N.B.: se non è possibile eseguire il file, assicurarsi che sia effettivamente un eseguibile. Usare quindi il comando `chmod u+x ./manimw.py`.

Alcune note sullo script `manimw.py`:
1. non è necessario (ma si può comunque fare) eseguire lo script utilizzando `python3`
2. capisce autonomamente se la manimazione produce un video oppure un'immagine
3. capisce autonomamente, qualora si trattasse di un video, se è diviso in sezioni (i.e. se viene fatto utilizzo di `self.next_section()` all'interno dello script)
4. replica la struttura di cartelle di `src` in una nuova cartella `exports`

## Struttura
Alcune indicazioni generali:
- tutti i file sorgente delle animazioni dovrebbero essere memorizzati nella cartella `src/`, la cui organizzazione interna varia a seconda della scaletta della serata:
  - se la serata prevede più relazioni, è bene creare una cartella per relazione il cui nome include anche l'ordine di quest'ultima all'interno della scaletta (ad esempio, `04-Archita` se l'intervento su Archita è al quarto posto tra gli interventi in scaletta);
  - ogni sottocartella riprende il numero della cartella padre + il numero della sottoparte (i.e. `04-Archita/04-01-Storia/`)
- immagini o altri file utilizzati all'interno delle animazioni vanno salvati nella cartella `assets/`;
- naming convention per i file:
  - usare il PascalCase per i file (i.e. `NomeMoltoLungo.py`),
  - quando si rende necessario inserire un numero, possibilmente precederlo da uno `0` se si tratta di una singola cifra (ad esempio: `9 => 09`);
