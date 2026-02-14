# Manimations Repository Template

Questa repository è pensata per definire una struttura comune a tutto il codice sorgente e relativi exports che vengono utilizzati per creare il materiale utilizzato nelle presentazioni delle varie rassegne.

La struttura intende seguire delle semplici regole di buonsenso per dare una buona organizzazione al codice e agli asset, per impedire alla vena creativa che accompagna la fase di creazione delle animazioni di prendere il sopravvento sullo spirito preciso e ordinato dell'informatico.

## Struttura
Alcune indicazioni generali:
- tutti i file sorgente delle animazioni dovrebbero essere memorizzati nella cartella `src/`, la cui organizzazione interna varia a seconda della scaletta della serata:
  - se la serata prevede più relazioni, è bene creare una cartella per relazione il cui nome include anche l'ordine di quest'ultima all'interno della scaletta (ad esempio, `04-archita` se l'intervento su Archita è al quarto posto tra gli interventi in scaletta);
- **anche se non è buona pratica**, tutti gli exports (_non eccessivamente pesanti_) generati dai file di codice devono essere memorizzati all'interno della cartella `exports/`, la cui organizzazione interna specchia perfettamente quella di `src/`;
- immagini o altri file utilizzati all'interno delle animazioni vanno salvati nella cartella `assets/`;
- naming convention per i file:
  - tutto in small caps per file,
  - parole separate da `-`,
  - quando si rende necessario inserire un numero, possibilmente precederlo da uno `0` se si tratta di una singola cifra (ad esempio: `9 => 09`);
