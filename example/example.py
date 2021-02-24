# import class
import interactiveLabCourse as interlab


def start():
    # define an Exercise
    title = 'Einleitung'
    description = '''
    Hier steht eine kleine Einleitung. Zum Beispiel eine kleine Problemstellung.<br>
    Das alles funktioniertt mit <b>HTML</b> inklusive Zeilenumbrüche.
    '''

    Einleitung = interlab.Exercise(title, description)

    # define a TextFieldExercise
    title = 'Aufgabe 1.1'
    subtitle = 'Aufgaben mit freier Texteingabe'
    description = '''
    Hier wird ein nicht leeres Textfeld erwartet. Sonst scheitert die Aufgabe.
    '''
    helptext = '{} können mit dem Helptext gegeben werden.'.format(
        interlab.href('https://de.wikipedia.org/wiki/Hinweis', 'Hinweise'))

    Aufgabe1_1 = interlab.TextFieldExercise(
        title, description, helptext=helptext, subtitle=subtitle)

    # define a TextAreaExercise
    title = 'Aufgabe 1.2'
    description = '''
    Hier wird ein nicht leerer Textbereich erwartet. Sonst scheitert die Aufgabe. Mehrzeilige Eingabe ist möglich.
    '''

    Aufgabe1_2 = interlab.TextAreaExercise(
        title, description, subtitle=subtitle)

    # define a IntField-Exercise
    title = 'Aufgabe 2.1'
    subtitle = 'Aufgaben mit numerischer Antwort'
    description = '''
    Hier wird eine Ganzzahl erwartet. Nur eine Antwort ist richtig.
    '''
    true_value = 42
    helptext = '42 ist die Antwort.'

    Aufgabe2_1 = interlab.IntFieldExercise(
        title, description, true_value, helptext=helptext, subtitle=subtitle)

    # define a FloatField-Exercise
    title = 'Aufgabe 2.2'
    description = '''
    Hier wird eine Gleitkommazahl erwartet. Nur eine Antwort ist richtig.
    '''
    true_value = 42.42
    helptext = '42.42 ist die Antwort.'

    Aufgabe2_2 = interlab.FloatFieldExercise(
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

    Aufgabe3_1 = interlab.SingleChoiceExercise(
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

    Aufgabe3_2 = interlab.SingleChoiceWithTextfield(
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

    Aufgabe4_1 = interlab.MultipleChoiceExercise(
        title, description, options, true_options, helptext=helptext, subtitle=subtitle)

    # define a MultipleChoiseExercise with TextArea

    title = 'Aufgabe 4.2'
    description = '''
    Genauso wie die vorherige Aufgabe, allerdings muss man hier noch etwas eingeben.
    Außerdem sind alle Optionen als richtig markiert.
    '''
    options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    helptext = 'Alle Optionen sind richtig.'

    Aufgabe4_2 = interlab.MultiChoiceWithTextfield(
        title, description, options, helptext=helptext, subtitle=subtitle)

    # define a CheckboxExercise

    title = 'Aufgabe 5'
    subtitle = 'Checkbox'
    description = '''
    Hier musst die Checkbox markiert werden, damit die Aufgabe erledigt werden kann.
    '''
    label = 'test'
    Aufgabe5 = interlab.CheckboxExercise(
        title, description, label, helptext=helptext, subtitle=subtitle)

    # create a list of exercises
    exercises = [Einleitung, Aufgabe1_1, Aufgabe1_2, Aufgabe2_1,
                 Aufgabe2_2, Aufgabe3_1, Aufgabe3_2, Aufgabe4_1, Aufgabe4_2, Aufgabe5]

    # create the series
    serie = interlab.Series(exercises, 'Serie1Logger.csv')

    display(serie.accordion)
