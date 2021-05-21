#
#    _ __        __   ______           __
#   (_) /LEIPZIG/ /  / __/ /  ___ ___ / /_
#  / / /__/ _ `/ _ \_\ \/ _ \/ -_) -_) __/
# /_/____/\_,_/_.__/___/_//_/\__/\__/\__/
#   INTERACTIVE LABORATORY WORKSHEET
#
#
# A Project by
# Machine Learning Group | UNIVERSITÄT LEIPZIG
# nmi.informatik.uni-leipzig.de/ml-group
#
# Code Authors: Benjamin Schindler, Marlo Kriegs, Emre Arkan
# Licence: CC-BY SA 4.0
#
# Diese Maßnahme wird mitfinanziert durch Steuermittel auf der Grundlage des
# von den Abgeordneten des Sächsischen Landtages beschlossenen Haushaltes.
#
#

import iLabSheet as ils


def start():
    # define an Exercise
    title = 'Leipzig Interactive Laboratory Worksheet (Leipzig iLabSheet)'
    description = '''
    <p>
    Das {} ist eine Open Education Resource, die das bekannte Python-Tool Jupyter Notebook um eine Komponente zur Integration interaktiver Kursaufgaben erweitert.
    Leipzig iLabSheet wird seit 2019 an der Universität Leipzig von der {} unter der Leitung von Thomas Schmid entwickelt (Codeautoren: Benjamin Schindler, Marlo Kriegs, Emre Arkan).
    <p>
    <p>
    <h4>Lizenzierung</h4>
    Creative Commons Namensnennung 4.0 International ({})
    <br>Universität Leipzig | {}
    <p>    
    <br>Diese Maßnahme wird mitfinanziert durch Steuermittel auf der Grundlage des von den Abgeordneten des Sächsischen Landtages beschlossenen Haushaltes.
    '''.format(
        ils.href('https://git.informatik.uni-leipzig.de/ml-group/tools/iLabCourse/',
                 'Leipzig Interactive Laboratory Worksheet (Leipzig iLabSheet)'),
        ils.href('https://nmi.informatik.uni-leipzig.de/ml-group/',
                 'Arbeitsgruppe Maschinelles Lernen'),
        ils.href(
            'https://creativecommons.org/licenses/by/4.0/deed.de', 'CC BY 4.0'),
        ils.href('https://nmi.informatik.uni-leipzig.de/ml-group/', 'Arbeitsgruppe Maschinelles Lernen'))

    Einleitung = ils.Exercise(title, description)

    # define a TextFieldExercise
    title = 'Aufgabe 1.1'
    subtitle = 'Aufgaben mit freier Texteingabe'
    description = '''
    Hier wird ein nicht leeres Textfeld erwartet. Sonst scheitert die Aufgabe.
    '''
    helptext = '{} können mit dem Helptext gegeben werden.'.format(
        ils.href('https://de.wikipedia.org/wiki/Hinweis', 'Hinweise'))

    Aufgabe1_1 = ils.TextFieldExercise(
        title, description, helptext=helptext, subtitle=subtitle)

    # define a TextAreaExercise
    title = 'Aufgabe 1.2'
    description = '''
    Hier wird ein nicht leerer Textbereich erwartet. Sonst scheitert die Aufgabe. Mehrzeilige Eingabe ist möglich.
    '''

    Aufgabe1_2 = ils.TextAreaExercise(
        title, description, subtitle=subtitle)

    # define a IntField-Exercise
    title = 'Aufgabe 2.1'
    subtitle = 'Aufgaben mit numerischer Antwort'
    description = '''
    Hier wird eine Ganzzahl erwartet. Nur eine Antwort ist richtig.
    '''
    true_value = 42
    helptext = '42 ist die Antwort.'

    Aufgabe2_1 = ils.IntFieldExercise(
        title, description, true_value, helptext=helptext, subtitle=subtitle)

    # define a FloatField-Exercise
    title = 'Aufgabe 2.2'
    description = '''
    Hier wird eine Gleitkommazahl erwartet. Nur eine Antwort ist richtig.
    '''
    true_value = 42.42
    helptext = '42.42 ist die Antwort.'

    Aufgabe2_2 = ils.FloatFieldExercise(
        title, description, true_value, helptext=helptext, subtitle=subtitle)

    # define a SingleChoice-Exercise
    title = 'Aufgabe 3.1'
    subtitle = 'Single Choice'
    description = '''
    Bei diesem Aufgabentyp kann immer nur eine Option ausgewählt werden. 
    Allerdings ist es möglich, mehrere von den Option als richtig zu markieren. 
    Dazu muss eine die Exercise mit einer Liste von richtigen Optionen initialisiert werden.
    '''
    helptext = 'Erste und letzte sind richtig.'

    options = ['Option 1', 'Option 2', 'Option 3']
    true_option = ['Option 1', 'Option 3']

    Aufgabe3_1 = ils.SingleChoiceExercise(
        title, description, options, true_option, helptext=helptext, subtitle=subtitle)

    # define a SingleChoice-Exercise with Text Field
    title = 'Aufgabe 3.2'
    description = '''
    Wie die vorherige Aufgabe, hier muss eine alternative_option mit angegeben werden. 
    Wenn diese Option gewählt wird, dann darf der Textbereich nicht leer sein 
    Es ist wieder möglich, mehrere von den Option als richtig zu markieren. 
    '''
    helptext = 'Option 1 ist richtig. Sonstiges kann auch ausgewählt werden, aber dann mit Texteingabe.'

    options = ['Option 1', 'Option 2', 'Sonstiges']
    alternative_option = 'Sonstiges'
    true_option = 'Option 1'

    Aufgabe3_2 = ils.SingleChoiceWithTextfield(
        title, description, options, true_option, alternative_option, helptext=helptext, subtitle=subtitle)

    # define a MultipleChoiseExercise
    title = 'Aufgabe 4.1'
    subtitle = 'Multiple Choice'
    description = '''
    Hier können mehrere Optionen gewählt werden.
    Die Aufgabe ist erst erledigt, wenn alle gewählten Optionen mit den richtigen Werten übereinstimmen.
    '''
    options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    true_options = [True, False, False, True]
    helptext = 'Erste und letzte sind richtig.'

    Aufgabe4_1 = ils.MultipleChoiceExercise(
        title, description, options, true_options, helptext=helptext, subtitle=subtitle)

    # define a MultipleChoiseExercise with TextArea

    title = 'Aufgabe 4.2'
    description = '''
    Genauso wie die vorherige Aufgabe, allerdings muss man hier noch etwas eingeben.
    Außerdem sind alle Optionen als richtig markiert.
    '''
    options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    helptext = 'Alle Optionen sind richtig.'

    Aufgabe4_2 = ils.MultiChoiceWithTextfield(
        title, description, options, helptext=helptext, subtitle=subtitle)

    # define a CheckboxExercise

    title = 'Aufgabe 5'
    subtitle = 'Checkbox'
    description = '''
    Hier musst die Checkbox markiert werden, damit die Aufgabe erledigt werden kann.
    '''
    label = 'Bitte markieren'
    Aufgabe5 = ils.CheckboxExercise(
        title, description, label, subtitle=subtitle)

    title = 'Aufgabe 6.1'
    subtitle = 'Slider'
    description = '''
    Hier musst eine Ganzzahl mit dem Slider gewählt werden. Es können mehrere richtige Lösungen als Liste gegeben werden.
    Zusätzlich ist es möglich durch Eingabe eines Tuples (z.B. (5,10)) einen Bereich anzugeben, in dem alle Zahlen als Korrekt gelten. Dabei geht es um ein geschlossenes Intervall.
    Außerdem lässt sich die Schrittgröße des Slieders mithilfe des Parameters 'step' einstellen.
    Mit den Parametern 'min_value' und 'max_value', kann das Zahlenintervall des Sliders definiert werden. Ferner lässt sich der Text hinter dem Slider mit dem Parameter 'value_unit' definieren. 
    Hier kann zum Beispiel die Einheit angegeben werden. Standardwert ist das Prozentzeichen. 
    '''
    helptext = 'Alle Werte zwischen 70 und 85 sind richtig.'
    Aufgabe6_1 = ils.IntSliderExercise(
        title, description, (70, 85), min_value=0, max_value=100, step=5, value_unit='%', helptext=helptext, subtitle=subtitle)

    title = 'Aufgabe 6.2'
    subtitle = 'Slider'
    description = '''
    Hier musst eine Gleitkommazahl mit dem Slider gewählt werden. Es können mehrere richtige Lösungen als Liste gegeben werden.
    Zusätzlich ist es möglich durch Eingabe eines Tuples (z.B. (5,10)) einen Bereich anzugeben, in dem alle Zahlen als Korrekt gelten. Dabei geht es um ein geschlossenes Intervall.
    Außerdem lässt sich die Schrittgröße des Slieders mithilfe des Parameters 'step' einstellen.
    Mit den Parametern 'min_value' und 'max_value', kann das Zahlenintervall des Sliders definiert werden. Ferner lässt sich der Text hinter dem Slider mit dem Parameter 'value_unit' definieren. 
    Hier kann zum Beispiel die Einheit angegeben werden. Standardwert ist das Prozentzeichen. 
    '''
    helptext = 'Alle Werte zwischen 3.2 und 6.4 sind richtig.'
    Aufgabe6_2 = ils.FloatSliderExercise(
        title, description, (3.2, 6.4), min_value=0.1, max_value=10, step=0.1, value_unit='€', helptext=helptext, subtitle=subtitle)

    title = 'Aufgabe 6.3'
    subtitle = 'Slider'
    description = '''
    Hier musst eine Textwert mit dem Slider gewählt werden. Hier wird eine Liste mit Strings erwartet, die die Optionen des Sliders angibt.
    Es können mehrere richtige Lösungen als Liste gegeben werden. Falls keine richtige Lösung übergeben wird, sind alle Optionen richtig.
    '''
    Aufgabe6_3 = ils.TextSliderExercise(
        title, description, options=['Alle', 'Werte', 'sind', 'richtig'], subtitle=subtitle)

    # create a list of exercises
    exercises = [Einleitung, Aufgabe1_1, Aufgabe1_2, Aufgabe2_1, Aufgabe2_2, Aufgabe3_1,
                 Aufgabe3_2, Aufgabe4_1, Aufgabe4_2, Aufgabe5, Aufgabe6_1, Aufgabe6_2, Aufgabe6_3]

    # create the series
    serie = ils.Series(exercises, 'Serie1Logger.csv')

    display(serie.accordion)
