Made by @Locorock

INSTALLAZIONE WINDOWS: 
1 - Installa Python 3 dal sito https://www.python.org/ 
1a - Ricordati di spuntare la box con scritto: "ADD PYTHON TO PATH" in fondo alla schermata di installazione

2 - Esegui il file setup.bat nella cartella del programma

3a - Se usi Deluge devi usare la modalità lite che si attiva disabilitando classic mode/modalità classica nelle impostazioni
3b - Se usi QBittorrent devi abilitare interfaccia utente web nelle impostazioni

4 - Apri il client torrent che vuoi usare

5 - Esegui il file start.bat per avviare il programma

UTILIZZO:
- Il file config.json non dovrebbe essere toccato nella maggior parte dei casi
- Il file data.json permette di definire quali anime volete scaricare, le varie opzioni permettono di definire dei filtri extra che spiegherò in seguito (IL FILE DEVE SEMPRE MANTERE LA STRUTTURA DI FILE JSON CON LE GRAFFE ATTORNO AD OGNI RAGGRUPPAMENTO, BASTERA' MANTENERE LA STRUTTURA GIA' DISPONIBILE NEGLI ESEMPI. UN FATTORE IMPORTANTE E' QUELLO DI INSERIRE VIRGOLE IN TUTTI GLI ELEMENTI TRANNE L'ULTIMO DI UNA LISTA)

Episode, specifica quale prossimo episodio si cerca

Max Episode, specifica il totale degli episodi, con -1 il totale viene ignorato, con valori maggiori di 0 la voce verrà eliminata una volta superato il massimo 

Resolution, specifica la risoluzione richiesta (se vuoto "" ignora la risoluzione)

Group, specifica il gruppo di subbing richiesto (se vuoto "" ignora il gruppo)

Prefix0, specifica se gli episodi di numero minore di 10 vadano prefissati con uno "0" (01, 02, 03)

SpaceEpisode, definisce se verranno richiesti spazi attorno al numero dell'episodio

English-Translated, definisce se l'episodio cercato sia forzatamente sub-eng, con false questo filtro viene ignorato.

Except, definisce un termine (solo uno per ora) che non si vuole trovare nella ricerca (v0 ad esempio), se vuoto "" non si esclude niente 

- Il client torrent deve essere sempre avviato prima di avviare il programma oppure il programma non si avvierà

 