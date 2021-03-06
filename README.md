## Leipzig iLabSheet | Dokumentation

Mit dem Leipzig Interactive Laboratory Worksheet (Leipzig iLabSheet) können interaktive Aufgabenblätter formuliert werden, welche einem Nutzer die Möglichkeiten geben Antworten zu verschiedenen Aufgabentypen zu beantworten. Er erhält ein direktes Feedback, ob seine Lösung korrekt ist. Optional können Hilfstexte zu einer Aufgabe hinzugefügt werden. 

Leipzig iLabSheet ist eine Open Education Resource (siehe auch Lizenzierung), die das bekannte Python-Tool Jupyter Notebook um eine Komponente zur Integration interaktiver Kursaufgaben erweitert. Das Backend ist in Python 3 geschrieben. 

Leipzig iLabSheet wird seit 2019 an der Universität Leipzig von der [Arbeitsgruppe Maschinelles Lernen](https://nmi.informatik.uni-leipzig.de/ml-group/) entwickelt.


### Requirements:
Diese Applikation benötigt eine [Python 3](https://www.python.org/downloads/) Installation. Die Anwendung wurde auf der Python-Version [3.9.5](https://www.python.org/downloads/release/python-395/) getestet und läuft damit einwandfrei.

Die notwendigen Python-Packages können mit dem folgenden Befehl installiert werden:

```sh
pip install -r requirements.txt
```
#### Linux und MacOS

Zusätlich wird auf Linux und MacOS zur Nutzung der fertigen Aufgabenserien [Chromium Browser](https://www.chromium.org/getting-involved/download-chromium) benötigt.

#### Windows

Auf Windows wird zur Nutzung der fertigen Aufgabenserien eine Installation von [Google Chrome](https://www.google.com/chrome/) (im Standard-Installationsordner) benötigt. Wir empfehlen die Nutzung der 64-Bit Version. Falls das nicht möglich ist, müssen die Pfade zur Google-Chrome-dict executable im Skript angepasst werden.

Ferner ist es be Windows erforderlich, dass der Pfad für Python in die Path-Variable eingefügt wird. Hierfür gibt es eine Anleietung [hier](https://datatofish.com/add-python-to-windows-path/).

Zusätlich wird [PowerShell 7.1](https://docs.microsoft.com/de-de/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-7.1) benötigt, um die Anwendung zu starten. Laden und installieren Sie hierfür die entsprechende `.msi`-Datei für Ihren Rechner auf [PowerShell Release v7.1.3](https://github.com/PowerShell/PowerShell/releases/tag/v7.1.3). Alternativ finden Sie hier die Links für [32-Bit](https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/PowerShell-7.1.3-win-x86.msi) und [64-Bit](https://github.com/PowerShell/PowerShell/releases/download/v7.1.3/PowerShell-7.1.3-win-x64.msi). 

Außerdem muss auf das PowerShell-Skript Zugriff gewährt werden. Hierfür werden die Eigenschaften des Skriptes mit einem Rechtklick geöffnet und das Feld `Zulassen` wird markiert:
![Bild](images_doc/unblock_ps1_script.png)

Danach lässt sich das Skript ausführen.

### Aufbau einer Aufgabenserie
Der Aufbau einer Aufgabenserie ist wie am folgenden Bild dargestellt.
![Bild](images_doc/Tool_snap.PNG)
Jede Aufgabenserie besteht aus einem alle Aufgaben zusammenfassenden Element (1), einem sogenannten *Accordion*.
Eine einzelne Aufgabe (2) hat einen Bezeichner im *Accordion* (3) und einen wahlweise unabhängigen Titel (4).
Außerdem hat eine Aufgabe einen Aufgabentext (5), ein Feld mit Interaktionsmöglichkeiten (6), ein Button, mit dem eine Lösung bestätigt werden kann (7) und ein Button mit dem ggf. eine nächste Aufgabe des *Accordions* aufgerufen werden kann.
Es ist zu betonen, dass je nach Aufgabentyp die Nutzeroberfläche varrieren kann. Es folgt eine schemachtische Auflistung der Aufgabentypen.

### Aufgabentypen
#### Multiple Choice
Es können mehrere Antwortmöglichkeiten ausgewählt werden. Dabei wird überprüft, ob die richtige bzw. die richtigen Antwort(en) ausgewählt wurden.

#### Textfeld oder Textbereich
Es können eine oder mehrere Zeilen Text geschrieben werden. Dabei findet keine Überprüfung des Textes statt. Es wird nur überprüft, ob ein Text eingegeben wurde.

#### Int- und Floatfeld
Es kann ein Zahlenwert eingegeben werden. Dieser wird mit dem richtigen Wert verglichen. 

#### Single Choice
Es wird überprüft, ob die Checkbox ausgewählt wurde.

#### Slider
Es wird überprüft, ob die gewählte Zahl den richtigen Wert enstrpicht oder im vorgegebenen Zahlenintervall liegt. Falls der Slider für Stringwerte verwendet wird, wird der gewählte Wert mit dem richtigen Wert verglichen.

#### Bedienung:
Es können verschiedene Bausteine zusammengesetzt werden, welche in der Python Klasse  
*iLabSheet* enthalten sind. Diese sollte daher stets zu Anfang jeder Aufgabe importiert werden, z.B.
```python
import iLabSheet as ils
```
Zunächst müssen die einzelnen Aufgaben definiert werden und ggf. die Lösung der zu überprüfenden Größe angegeben werden, z. B.:

```python
title = 'Aufgabe 2'
subtitle = 'Multiplikation'
description = 'Rechnen Sie 7 * 6.'
true_value = 42
helptext = '42 ist die Antwort.'
Aufgabe2 = ils.IntFieldExercise(title, description, true_value, helptext=helptext, subtitle=subtitle)
```
Anschließend müssen alle Aufgabe als Python Liste zusammengefasst werden, z. B.:

```python
exercises = [Aufgabe1, Aufgabe2]
```
Diese Liste kann dann genutzt werden, um eine Aufgabeserie zu initialisieren, z. B.: 

```python
loggingPath = 'path/to/logging'
series = ils.Series(exercises, loggingPath)
```

Anschließend kann die Serie mittels des *display* Befehls angezeigt werden, z. B.:

```python
display(series)
```

Ein Beispiel einer Aufgabenserie stellt das [SeriesTest](https://git.informatik.uni-leipzig.de/ml-group/tools-dev/ml-course/blob/master/HandsOns/HandsOn_1.py) dar. Der Aufbau kann als Vorlage für eigene Aufgabenserien genutzt werden. Außerdem wird hier die Funktionsweise nochmals ausführlich kommentiert. 

#### Dynamische Überprüfung der Antworten:
Zum jetztigen Zeitpunkt sind die richtigen Antworten der Aufgabenserien als feste Werte eingetragen. In der Zukunft soll es auch die Möglichkeit geben, die richtigen Antworten zum Zeitpunkt der Ausführung dynamisch zu berechnen.  


#### Bedienung von Fertigen Aufgabenserien:
Es stehen bereits fertige Aufgabeserien zur Verfügung, welche durch ein *Linux Bash Skript* in einem geteilten Fenster geöffnet werden können. Auf der einen Hälfte des Bildschirmes wird das virtuelle, interaktive Aufgabenblatt zum Eintragen der Lösungen geöffnet, während auf der anderen Hälfte ein jupyter notebook zum Programmieren geöffnet wird. 
Dazu wird das Python Package *voila* genutzt und der frei zugängliche Browser *Chromium*. Zu beachten ist, dass die Skripte nur für Linux und Chromium funktionieren. Ein beispielhafter Aufruf auf könnte wie folgt aussehen:

für Linux:

```sh
sh ./start-iLabSheet-Linux.sh NameDerAufgabenSerie.ipynb
```

für MacOS:
```sh
sh ./start-iLabSheet-macOS.sh NameDerAufgabenSerie.ipynb

```

für Windows (innerhalb der PowerShell 7.1):

```ps1
.\start-iLabSheet-Windows.ps1 NameDerAufgabenSerie.ipynb
```

#### Logging:
Es wird automatisch ein Loggingfile erstellt, in dem angegebenen Pfad. In ihm werden verschiedene Nutzungsdaten im `csv` Format gespeichert und können entsprechend vom Administrator beliebig ausgewertet werden.

&nbsp;
----------------------------------------------------------------------------------------------------

## Lizenzierung von Leipzig iLabSheet
GNU General Public License 3 ([GPLv3](https://www.gnu.org/licenses/gpl-3.0.de.html)) <br>
Universität Leipzig | [Arbeitsgruppe Maschinelles Lernen](https://nmi.informatik.uni-leipzig.de/ml-group/)

Diese Maßnahme wird mitfinanziert durch Steuermittel auf der Grundlage des von den Abgeordneten des Sächsischen Landtages beschlossenen Haushaltes.

----------------------------------------------------------------------------------------------------





