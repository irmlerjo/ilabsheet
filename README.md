# Dokumentation

## Ziel:
Mit diesem Tool können interaktive Aufgaben formuliert werden, welche einem Nutzer die Möglichkeiten geben Antworten zu verschiedenen Aufgabentypen zu beantworten. Er erhält ein direktes Feedback, ob seine Lösung korrekt ist. Optional können Hilfstexte zu einer Aufgabe hinzugefügt werden. 
Das Backend ist in Python 3 geschrieben. 

## Requirements:
Diese Applikation benötigt eine [Python 3](https://www.python.org/downloads/) Installation.

Die notwendigen Python-Packages können mit dem folgenden Befehl installiert werden:

```sh
pip install -r requirements.txt
```

Zusätlich wird zur Nutzung der fertigen Aufgabenserien [Chromium Browser](https://www.chromium.org/getting-involved/download-chromium) benötigt.

## Aufbau einer Aufgabenserie
Der Aufbau einer Aufgabenserie ist wie am folgenden Bild dargestellt.
![Bild](/images_doc/Tool_snap.PNG)
Jede Aufgabenserie besteht aus einem alle Aufgaben zusammenfassenden Element (1), einem sogenannten *Accordion*.
Eine einzelne Aufgabe (2) hat einen Bezeichner im *Accordion* (3) und einen wahlweise unabhängigen Titel (4).
Außerdem hat eine Aufgabe einen Aufgabentext (5), ein Feld mit Interaktionsmöglichkeiten (6), ein Button, mit dem eine Lösung bestätigt werden kann (7) und ein Button mit dem ggf. eine nächste Aufgabe des *Accordions* aufgerufen werden kann.
Es ist zu betonen, dass je nach Aufgabentyp die Nutzeroberfläche varrieren kann. Es folgt eine schemachtische Auflistung der Aufgabentypen.

## Aufgabentypen
### Multiple Choice
Es können mehrere Antwortmöglichkeiten ausgewählt werden. Dabei wird überprüft, ob die richtige bzw. die richtigen Antwort(en) ausgewählt wurden.

### Textfeld oder Textbereich
Es können eine oder mehrere Zeilen Text geschrieben werden. Dabei findet keine Überprüfung des Textes statt. Es wird nur überprüft, ob ein Text eingegeben wurde.

### Int- und Floatfeld
Es kann ein Zahlenwert eingegeben werden. Dieser wird mit dem richtigen Wert verglichen. 

### Single Choice
Es wird überprüft, ob die Checkbox ausgewählt wurde.

### Bedienung:
Es können verschiedene Bausteine zusammengesetzt werden, welche in der Python Klasse  
*interactiveLabCourse* enthalten sind. Diese sollte daher stets zu Anfang jeder Aufgabe importiert werden, z.B.
```python
import interactiveLabCourse as interlab
```
Zunächst müssen die einzelnen Aufgaben definiert werden und ggf. die Lösung der zu überprüfenden Größe angegeben werden, z. B.:

```python
title = 'Aufgabe 2'
subtitle = 'Multiplikation'
description = 'Rechnen Sie 7 * 6.'
true_value = 42
helptext = '42 ist die Antwort.'
Aufgabe2 = interlab.IntFieldExercise(title, description, true_value, helptext=helptext, subtitle=subtitle)
```
Anschließend müssen alle Aufgabe als Python Liste zusammengefasst werden, z. B.:

```python
exercises = [Aufgabe1, Aufgabe2]
```
Diese Liste kann dann genutzt werden, um eine Aufgabeserie zu initialisieren, z. B.: 

```python
loggingPath = 'path/to/logging'
series = interlab.interlab.Series(exercises, loggingPath)
```

Anschließend kann die Serie mittels des *display* Befehls angezeigt werden, z. B.:

```python
display(series)
```

Ein Beispiel einer Aufgabenserie stellt das [SeriesTest](https://git.informatik.uni-leipzig.de/ml-group/tools-dev/ml-course/blob/master/HandsOns/HandsOn_1.py) dar. Der Aufbau kann als Vorlage für eigene Aufgabenserien genutzt werden. Außerdem wird hier die Funktionsweise nochmals ausführlich kommentiert. 

### Dynamische Überprüfung der Antworten:
Zum jetztigen Zeitpunkt sind die richtigen Antworten der Aufgabenserien als feste Werte eingetragen. In der Zukunft soll es auch die Möglichkeit geben, die richtigen Antworten zum Zeitpunkt der Ausführung dynamisch zu berechnen.  


### Bedienung von Fertigen Aufgabenserien:
Es stehen bereits fertige Aufgabeserien zur Verfügung, welche durch ein *Linux Bash Skript* in einem geteilten Fenster geöffnet werden können. Auf der einen Hälfte des Bildschirmes wird das virtuelle, interaktive Aufgabenblatt zum Eintragen der Lösungen geöffnet, während auf der anderen Hälfte ein jupyter notebook zum Programmieren geöffnet wird. 
Dazu wird das Python Package *voila* genutzt und der frei zugängliche Browser *Chromium*. Zu beachten ist, dass die Skripte nur für Linux und Chromium funktionieren. Ein beispielhafter Aufruf könnte wie folgt aussehen:
```sh
sh ./start-split-screen.sh NameDerAufgabenSerie
```

oder für MacOS:

```sh
sh ./start-split-screen-macOS.sh NameDerAufgabenSerie
```

### Logging:
Es wird automatisch ein Loggingfile erstellt, in dem angegebenen Pfad. In ihm werden verschiedene Nutzungsdaten im `csv` Format gespeichert und können entsprechend vom Administrator beliebig ausgewertet werden.





