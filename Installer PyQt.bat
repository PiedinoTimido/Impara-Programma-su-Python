@echo off
REM Questo script installa PyQt6 usando pip.
REM Assicurati di avere Python e pip installati e configurati nel tuo PATH.

echo Tentativo di installare PyQt6...

REM Esegui il comando pip per installare PyQt6
pip install PyQt6

REM Controlla se l'installazione è andata a buon fine
if %errorlevel% equ 0 (
    echo.
    echo PyQt6 installato con successo!
    echo Puoi chiudere questa finestra.
) else (
    echo.
    echo Si è verificato un errore durante l'installazione di PyQt6.
    echo Controlla i messaggi di errore qui sopra per maggiori dettagli.
    echo Assicurati che Python e pip siano correttamente installati e nel tuo PATH.
)

pause
REM La riga 'pause' mantiene la finestra aperta finché non premi un tasto,
REM così puoi leggere i messaggi di output.
