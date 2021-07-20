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

import ipywidgets as widgets
from IPython.display import display
from pathlib import Path
import time
import csv
import math
import sys
import os

title_layout = widgets.Layout(width='500px', height='30px')
description_layout = widgets.Layout(width='500px')
textfield_placeholder = 'Hier eintippen...'

# diese Klasse wird automatisch erzeugt beim Erstellen einer Aufgabenserie
''' Logger Klasse '''


class Logger():
    def __init__(self, helptext):
        self.typed_solutions = []
        self.tries_until_correct = 0
        self.start_time = 0
        self.end_time = 0
        self.full_time = 0
        self.path = ""
        self.helptext = helptext
        self.used_help = False

    def setStartTime(self, time):
        self.start_time = time

    def setEndTime(self, time):
        self.end_time = time

    def setUsedHelp(self, used_help):
        self.used_help = used_help

    def setPath(self, path):
        self.path = path

    def addSolution(self, solution):
        self.typed_solutions.append(solution)

    def setTries(self):
        self.tries_until_correct = len(self.typed_solutions)

    def setFullTime(self):
        self.full_time = round(self.end_time - self.start_time, 2)

    def terminate(self):
        self.setFullTime()
        self.setTries()

    def writeToFile(self):
        help = ""
        if self.helptext == "":
            help = "None"
        elif self.used_help:
            help = "true"
        else:
            help = "false"
        with open(self.path, "a") as csvFile:
            writer = csv.writer(csvFile)
            row = [str(self.tries_until_correct), str(
                self.typed_solutions).replace(",", ";"), str(self.full_time), help]
            writer.writerow(row)
        csvFile.close()


''' Validierungungsfunktionen: '''
# Diese Funktion überprüft, ob ein Eingabefeld leer ist


def not_empty(button, userValue):
    if userValue != '':
        button.button_style = 'success'
        return True
    else:
        button.button_style = 'danger'
        return False

# Diese Funktion überprüft, ob eine gegebene Antwort mit der als "wahr" gesetzten Antwort überein stimmt
# nachdem der "Absenden" Button gedrückt wurde


def eval_submission(button, userValue, truth):
    evaluation_result = False
    if userValue == truth:
        button.button_style = 'success'
        evaluation_result = True
    elif type(truth) == list and userValue in truth:
        button.button_style = 'success'
        evaluation_result = True
    elif type(truth) == tuple and userValue >= truth[0] and userValue <= truth[1]:
        button.button_style = 'success'
        evaluation_result = True
    else:
        button.button_style = 'danger'
    return evaluation_result

# Diese Funktion überprüft, ob eine gegebene Antwort mit der als "wahr" gesetzten Antwort überein stimmt
# nachdem der "Absenden" Button gedrückt wurde, rundet ggf. den eingegebenen Wert


def eval_float_submission(button, userValue, truth, step):
    # überprüfen auf ungefähre Gleichheit (+step/1000000000 bewirkt aufrunden)
    if math.isclose(userValue+step/1000000000, truth, abs_tol=step/2.0):
        button.button_style = 'success'
        return True
    else:
        button.button_style = 'danger'
        return False


''' Widget-Bausteine: '''
# Dieser Button wird aktiviert, sobald eine Aufgabe richtig gelöst wurde
# wird er betätigt, öffnen sich die nächste Aufgabe der Serie im Accordion


def NextButton():
    return widgets.Button(
        description='Nächste Aufgabe',
        disabled=True,
        tooltip='Lösen Sie zuerst korrekt die Aufgabe.',
        icon='fa-arrow-right',
    )

# Diese Klasse ermöglicht das Erstellen einer Multiple Choice Frage
# die übergebenen options sind die Auswahlmöglichkeiten


class MultipleChoiceWidget():
    def __init__(self, options):
        self.items = []
        for current_option in options:
            option = widgets.Checkbox(value=False,
                                      description=current_option,
                                      disabled=False,
                                      # damit Text nicht mit "..." abgekürzt wird
                                      layout=widgets.Layout(width='90%')
                                      )
            self.items.append(option)
        self.box = widgets.VBox(self.items)

    def getValues(self):
        result = []
        for i in self.items:
            result.append(i.value)
        return result

    def getVBox(self):
        return self.box

    def display(self):
        self.box = widgets.VBox(self.items)
        display(self.box)

# Dieser Button löst bei Betätigung die Überprüfung der eingebenenen Lösung aus


def SubmissionButton():
    return widgets.Button(
        description='Absenden',
        disabled=False,
        button_style='',  # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Anclicken, um abzusenden.',
        icon='check',
        layout=widgets.Layout(margin='40px 0px 0px 0px')
    )

# Diese Klasse definiert den unteren Aufbau einer Aufgabe
# Sie stellt eine Hilfsklasse dar und wird automatisch ausgeführt beim Erstellen einer Aufgabe


class Footer():
    def __init__(self, helptext):
        self.submissionButton = SubmissionButton()

        self.helpButton = widgets.Button(
            description='Tipp',
            disabled=False,
            button_style='',  # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Anclicken, um abzusenden.',
            icon='question',
            layout=widgets.Layout(margin='40px 0px 0px 0px')
        )
        self.helpButton.style.button_color = 'white'

        self.helpField = widgets.HTML(value='')
        self.helptext = helptext

        def show_help(button):
            self.helpField.value = "<i>" + self.helptext + "</i>"
        self.helpButton.on_click(show_help)

    def getLayoutedWidget(self):
        # TODO: schönere Ausgabe mit richtigem widgets.Layout
        if self.helptext == "":
            return self.submissionButton
        else:
            return widgets.VBox([widgets.HBox([self.submissionButton, self.helpButton]), self.helpField])


'''Basisklasse (Überschrift + Text)'''
# Dies ist die Basisklasse einer Aufgabe
# Alle Aufgabentypen erben von ihr


class Exercise:
    def __init__(self, title, description, subtitle=''):
        self.items = []
        if subtitle != "":
            self.createHeader(subtitle, description)
        else:
            self.createHeader(title, description)
        self.submissionBtn = None
        self.titleClean = title
        self.logger = Logger('')

    def createHeader(self, title, description):
        # Überschrift:
        self.title = widgets.HTML(value=headline(title))

        # Aufgabenstellung:
        self.description = widgets.HTML(value='<p>' + description + '</p>')

        self.items.extend([self.title, self.description])

    def createBody(self):
        pass

    def display(self):
        self.box = widgets.VBox(self.items)
        display(self.box)


'''Accordion Tab Klasse: definiert ein Tab eines Accordions'''
# Diese Klasse defniert das Aussehen eines Tabs eines Accordions
# Also wie eine einzelne Aufgabe in der Serie dargestellt wird


class AccordionTab:

    def __init__(self, title, exercise):
        self.title = title
        self.nextBtn = NextButton()
        items = exercise.items + [self.nextBtn]
        self.box = widgets.VBox(items)

        # Check wird benötigt, um zu überprüfen, ob dies die Introduction ist -> wird gesondert behandelt
        if exercise.submissionBtn != None:
            self.add_button_change_listener(exercise.submissionBtn)
        else:
            self.nextBtn.disabled = False

    # überprüft, ob eine Aufgabe korrekt gelöst wurde, anhand der Farbe des "Absenden" Buttons
    def add_button_change_listener(self, b):

        def handle_button_change(change):
            if change.new == "success":
                # aktiviert Next Button
                self.nextBtn.disabled = False
                # fügt ein neues Tooltip Label hinzu
                self.nextBtn.tooltip = "Anclicken, um die nächste Aufgabe zu öffnen."
                # deakiviert Absenden Button
                b.disabled = True
            # else:
            #    self.text.value=change

        b.observe(handle_button_change, names="button_style")


'''Series-Klasse: erstellt eine Aufgaben Serie aus übergebenen Aufgaben mit einem Accordion'''
# erstellt eine Aufgabenserie aus den ihr übergebenen Aufgaben
# loggt Meta Daten in ein File entsprechend des path


class Series:
    def __init__(self, exercises, path):
        self.accordion = widgets.Accordion()
        self.exercises = exercises
        self.currentExercise = 0
        Path('Log').mkdir(parents=True, exist_ok=True)
        self.path = os.path.join("Log", str(os.getlogin()) + "_" + path)

        self.initLoggingFile()
        self.addPathToLoggers()
        # zuerst wird die Einleitung hinzugefügt
        self.addIntroduction(exercises[0])

    def addPathToLoggers(self):
        for exercise in self.exercises:
            if hasattr(exercise, "logger"):
                exercise.logger.setPath(self.path)

    def initLoggingFile(self):
        loggingHeader = ["Anzahl_Versuche",
                         "Lösungen", "Zeit", "Hilfe_genutzt"]
        with open(self.path, "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(loggingHeader)
        csvFile.close()

    def addIntroduction(self, introduction):
        accordion_tab = AccordionTab(introduction.titleClean, introduction)
        self.accordion.children += (accordion_tab.box,)
        self.accordion.set_title(self.currentExercise, accordion_tab.title)
        self.accordion.selected_index = 0

        def next_btn_clicked(b):
            if self.currentExercise+1 <= len(self.exercises)-1:
                self.currentExercise += 1
                self.addExercise(self.exercises[self.currentExercise])
                self.accordion.selected_index = self.currentExercise
                b.disabled = True

                # startet den Timer des nächsten Loggers
                self.exercises[self.currentExercise].logger.setStartTime(
                    time.time())

        accordion_tab.nextBtn.on_click(next_btn_clicked)

    def addExercise(self, exercise):
        accordion_tab = AccordionTab(str(exercise.titleClean), exercise)
        self.accordion.children += (accordion_tab.box,)
        self.accordion.set_title(
            str(self.currentExercise), str(accordion_tab.title))

        # Titel des letzten "Nächste Aufgabe" Button ändern
        if(len(self.accordion.children) == len(self.exercises)):
            accordion_tab.nextBtn.description = 'Beende Aufgabenserie'
            accordion_tab.nextBtn.layout=widgets.Layout(width='10%')


        def next_btn_clicked(b):
            last_solution = True
            if self.currentExercise+1 <= len(self.exercises)-1:

                # beende Timer für aktuelle Aufgabe
                self.exercises[self.currentExercise].logger.setEndTime(
                    time.time())
                self.exercises[self.currentExercise].logger.terminate()
                self.exercises[self.currentExercise].logger.writeToFile()

                self.currentExercise += 1
                # starte nächsten Timer
                self.exercises[self.currentExercise].logger.setStartTime(
                    time.time())

                # füge neue Aufgabe hinzu
                self.addExercise(self.exercises[self.currentExercise])

                # wähle neuen Tab aus
                self.accordion.selected_index = self.currentExercise

                # deaktiviere alten "Nächste Aufgabe" Button
                b.disabled = True

                last_solution = False

            if len(self.accordion.children) == len(self.exercises) and last_solution:
                # also "Beende Aufgabenserie" wurde gedrückt
                # beende timer
                self.exercises[self.currentExercise].logger.setEndTime(
                    time.time())
                self.exercises[self.currentExercise].logger.terminate()
                self.exercises[self.currentExercise].logger.writeToFile()

                b.disabled = True

        # add next_btn_clicked function to next button
        accordion_tab.nextBtn.on_click(next_btn_clicked)


'''Textfeld-Klasse (Absenden überprüft auf nicht-leeren Textinhalt)'''


class TextFieldExercise(Exercise):

    def __init__(self, title, description, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext)
        self.logger = Logger(helptext)

    def createBody(self, helptext):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.Text(
            value='',
            placeholder=textfield_placeholder,
            description='Antwort:',
            disabled=False
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            # "," durch "." ersetzen, da Logging File im csv Format ist
            solution = self.interactiveElement.value
            if (type(solution) == str):
                if ("," in solution):
                    solution = solution.replace(",", ".")
            self.logger.addSolution(solution)
            not_empty(footer.submissionButton, self.interactiveElement.value)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton

# wie Textfeld, jedoch sind mehrzeilige Texte möglich


class TextAreaExercise(Exercise):

    def __init__(self, title, description, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext)
        self.logger = Logger(helptext)

    def createBody(self, helptext):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.Textarea(
            value='',
            placeholder=textfield_placeholder,
            description='Antwort:',
            disabled=False
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            not_empty(footer.submissionButton, self.interactiveElement.value)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


'''Ganzzahlfeld-klasse (Absenden überprüft auf Gleichheit mit true-value)'''


class IntFieldExercise(Exercise):

    def __init__(self, title, description, true_value, min_value=0, max_value=100, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, true_value, min_value, max_value)
        self.logger = Logger(helptext)

    def createBody(self, helptext, true_value, min_value, max_value):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.BoundedIntText(
            value=0,
            min=min_value,
            max=max_value,
            step=1,
            description='Antwort:',
            disabled=False
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_submission(footer.submissionButton,
                            self.interactiveElement.value, true_value)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


'''Floatfeld-klasse (Absenden überprüft auf Gleichheit mit true-value)'''


class FloatFieldExercise(Exercise):

    def __init__(self, title, description, true_value, min_value=0, max_value=100, step=0.1, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, true_value, min_value, max_value, step)
        self.logger = Logger(helptext)

    def createBody(self, helptext, true_value, min_value, max_value, step):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.BoundedFloatText(
            value=0,
            min=min_value,
            max=max_value,
            step=step,
            description='Antwort:',
            disabled=False
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_float_submission(
                footer.submissionButton, self.interactiveElement.value, true_value, step)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


''' Textfield must not be empty. Every option is True '''


class MultiChoiceWithTextfield(Exercise):

    def __init__(self, title, description, options, preselection=None, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, options, preselection)
        self.logger = Logger(helptext)

    def createBody(self, helptext, options, preselection):
        # Anwortmöglichkeiten
        # Antwortmöglichkeit
        self.interactiveElement = widgets.RadioButtons(
            options=options,
            description='Antwort:',
            disabled=False,
            layout=widgets.Layout(width="95%"),
            value=preselection
        )

        # Textarea, falls "Sonstiges" ausgewählt wird
        textfield = widgets.Textarea(
            value='',
            placeholder=textfield_placeholder,
            description=' ',
            disabled=False,
            layout=widgets.Layout(height="75px")
        )

        self.items.append(self.interactiveElement)
        self.items.append(textfield)

        placeholder = widgets.HTML("<br>")
        self.items.append(placeholder)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            # logge gewählte Option + Begründung
            self.logger.addSolution(
                self.interactiveElement.value + ": " + textfield.value)
            not_empty(footer.submissionButton, textfield.value)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


'''SingleChoice-Klasse (Absenden überprüft ob angeklicktes Feld mit true_option übereinstimmt)'''


class SingleChoiceExercise(Exercise):

    def __init__(self, title, description, options, true_option, preselection=None, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, options, true_option, preselection)
        self.logger = Logger(helptext)

    def createBody(self,  helptext, options, true_option, preselection):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.RadioButtons(
            options=options,
            description='Antwort:',
            disabled=False,
            value=preselection,
            layout=widgets.Layout(width="100%", flex_flow='nowrap')
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_submission(footer.submissionButton,
                            self.interactiveElement.value, true_option)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


class SingleChoiceWithTextfield(Exercise):
    def __init__(self, title, description, options, true_option, alternative_option=[], preselection=None, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        if alternative_option == []:
            alternative_option = true_option
        self.createBody(helptext, options, true_option,
                        alternative_option, preselection)
        self.logger = Logger(helptext)

    def createBody(self, helptext, options, true_option, alternative_option, preselection):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.RadioButtons(
            options=options,
            description='Antwort:',
            disabled=False,
            value=preselection,
            layout=widgets.Layout(width="100%", flex_flow='nowrap')
        )

        # Textarea, falls "Sonstiges" ausgewählt wird
        textfield = widgets.Textarea(
            value='',
            placeholder=textfield_placeholder,
            description=' ',
            disabled=False if preselection == alternative_option or str(
                preselection) in alternative_option or true_option == alternative_option else True,
            layout=widgets.Layout(height="75px")
        )

        # change listener
        def on_value_change(change):

            if change['new'] == alternative_option or change['new'] in alternative_option:
                textfield.disabled = False
                textfield.value = ''
            elif change['new'] != alternative_option or change['new'] not in alternative_option:
                textfield.disabled = True
                textfield.value = ''

        self.interactiveElement.observe(on_value_change, names='value')

        self.items.append(self.interactiveElement)
        self.items.append(textfield)

        placeholder = widgets.HTML("<br>")
        self.items.append(placeholder)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            if alternative_option == true_option == self.interactiveElement.value:
                text = textfield.value
                self.logger.addSolution(text)
                if not_empty(footer.submissionButton, text):
                    eval_submission(footer.submissionButton,
                                    self.interactiveElement.value, true_option)
            elif self.interactiveElement.value == true_option != alternative_option:
                text = textfield.value
                self.logger.addSolution(text)
                eval_submission(footer.submissionButton,
                                self.interactiveElement.value, true_option)
            elif self.interactiveElement.value == alternative_option or self.interactiveElement.value in alternative_option:
                text = textfield.value
                self.logger.addSolution(text)
                if not_empty(footer.submissionButton, text):
                    eval_submission(
                        footer.submissionButton, self.interactiveElement.value, alternative_option)
            else:
                self.logger.addSolution(self.interactiveElement.value)
                eval_submission(footer.submissionButton,
                                self.interactiveElement.value, true_option)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


'''CheckBox-Klasse (Absenden überprüft, ob der Checkbox markiert wurde)'''


class CheckboxExercise(Exercise):

    def __init__(self, title, description, label, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, label)
        self.logger = Logger(helptext)

    def createBody(self, helptext, label):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.Checkbox(
            value=False,
            description=label,
            disabled=False
        )

        self.items.append(self.interactiveElement)

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_submission(footer.submissionButton,
                            self.interactiveElement.value, True)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton


'''MultipleChoice-Klasse (Absenden überprüft ob angeklickte Felder mit true_choices (Liste aus Booleans) übereinstimmt)'''


class MultipleChoiceExercise(Exercise):

    def __init__(self, title, description, options, true_options, helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, options, true_options)
        self.logger = Logger(helptext)

    def createBody(self, helptext, options, true_options):
        # Antwortmöglichkeit
        self.interactiveElement = MultipleChoiceWidget(options)

        self.items.append(self.interactiveElement.getVBox())

        # Footer:
        footer = Footer(helptext)

        def send_submission(button):
            answer = self.interactiveElement.getValues()
            self.logger.addSolution(answer)
            if type(true_options) == int:
                answer = list(answer).count(True)
            eval_submission(footer.submissionButton,
                            answer, true_options)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)

        footer.submissionButton.on_click(send_submission)
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton

'''Slider für ganze Zahlen (Absenden überprüft auf Gleichheit mit true_value bzw. ob der Wert im Intervall liegt)'''


class IntSliderExercise(Exercise):
    def __init__(self, title, description, true_value, min_value=0, max_value=100, step=1, value_unit='%', helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, true_value, min_value,
                        max_value, step, value_unit)
        self.add_change_listener(self.interactiveElement, value_unit)

    def createBody(self, helptext, true_value, min_value, max_value, step, value_unit):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.IntSlider(
            value=min_value,
            min=min_value,
            max=max_value,
            step=step,
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=False,
            readout_format='d',
            layout=widgets.Layout(width='200px')
        )
        self.blank = "&nbsp"*3
        self.t = widgets.HTML(value="{}{} {}".format(
            self.blank, self.interactiveElement.value, value_unit))
        self.hint = widgets.HTML(value='<i>Bitte Slider bewegen</i>')
        self.hbox = widgets.HBox(
            [widgets.HTML("&nbsp &nbsp"), self.interactiveElement, self.t])

        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_submission(footer.submissionButton,
                            self.interactiveElement.value, true_value if type(true_value) != tuple else [i for i in range(true_value[0], true_value[1] + 1, step)])

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)
        footer.submissionButton.on_click(send_submission)

        self.items.append(self.getElements())
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton

    def add_change_listener(self, slider, value_unit):
        def on_value_change(change):
            self.t.value = "{}{} {}".format(
                self.blank, change['new'], value_unit)
        self.interactiveElement.observe(on_value_change, names='value')

    def getValue(self):
        return self.hbox.children[1].value

    def getElements(self):
        return widgets.VBox([self.hbox, self.hint])


'''Slider für gleitkomma Zahlen (Absenden überprüft auf Gleichheit mit true_value bzw. ob der Wert im Intervall liegt)'''


class FloatSliderExercise(Exercise):
    def __init__(self, title, description, true_value, min_value=0, max_value=10, step=0.1, value_unit='', helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, true_value, min_value,
                        max_value, step, value_unit)
        self.add_change_listener(self.interactiveElement, value_unit)

    def createBody(self, helptext, true_value, min_value, max_value, step, value_unit):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.FloatSlider(
            value=min_value,
            min=min_value,
            max=max_value,
            step=step,
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=False,
            readout_format='d',
            layout=widgets.Layout(width='200px')
        )
        self.blank = "&nbsp"*3
        self.t = widgets.HTML(value="{}{} {}".format(
            self.blank, self.interactiveElement.value, value_unit))
        self.hint = widgets.HTML(value='<i>Bitte Slider bewegen</i>')
        self.hbox = widgets.HBox(
            [widgets.HTML("&nbsp &nbsp"), self.interactiveElement, self.t])

        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(self.interactiveElement.value)
            eval_submission(footer.submissionButton,
                            self.interactiveElement.value, true_value)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)
        footer.submissionButton.on_click(send_submission)

        self.items.append(self.getElements())
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton

    def add_change_listener(self, slider, value_unit):
        def on_value_change(change):
            self.t.value = "{}{} {}".format(
                self.blank, change['new'], value_unit)
        self.interactiveElement.observe(on_value_change, names='value')

    def getValue(self):
        return self.hbox.children[1].value

    def getElements(self):
        return widgets.VBox([self.hbox, self.hint])


'''Slider mit String als Werte (Absenden überprüft auf Gleichheit mit true_values. Wenn true_value nicht gesetzt ist, sind alle Werte richtig.)'''


class TextSliderExercise(Exercise):
    def __init__(self, title, description, options, true_values=[], helptext='', subtitle=''):
        super().__init__(title, description, subtitle)
        self.createBody(helptext, options, true_values)
        self.add_change_listener(self.interactiveElement, options)

    def createBody(self, helptext, options, true_values):
        # Antwortmöglichkeit
        self.interactiveElement = widgets.IntSlider(
            value=0,
            min=0,
            max=len(options)-1,
            step=1,
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=False,
            readout_format='d',
            layout=widgets.Layout(width='200px')
        )
        self.blank = "&nbsp"*3
        self.t = widgets.HTML(value="{}{}".format(
            self.blank, options[self.interactiveElement.value]))
        self.hint = widgets.HTML(value='<i>Bitte Slider bewegen</i>')
        self.hbox = widgets.HBox(
            [widgets.HTML("&nbsp &nbsp"), self.interactiveElement, self.t])

        footer = Footer(helptext)

        def send_submission(button):
            self.logger.addSolution(options[self.interactiveElement.value])
            eval_submission(footer.submissionButton,
                            options[self.interactiveElement.value], true_values if true_values != [] else options)

        def send_logger(b):
            self.logger.setUsedHelp(True)

        footer.helpButton.on_click(send_logger)
        footer.submissionButton.on_click(send_submission)

        self.items.append(self.getElements())
        self.items.append(footer.getLayoutedWidget())

        self.submissionBtn = footer.submissionButton

    def add_change_listener(self, slider, options):
        def on_value_change(change):
            self.t.value = "{}{}".format(self.blank, options[change['new']])
        self.interactiveElement.observe(on_value_change, names='value')

    def getValue(self):
        return self.hbox.children[1].value

    def getElements(self):
        return widgets.VBox([self.hbox, self.hint])


'''HTML Makros'''
# benötigt für eine schönere Formatierung


def href(url, text):
    output = '''<a href="''' + url + '''" target="_blank" title="''' + text + \
        '''" style="color:blue; text-decoration: underline;">''' + text + '''</a>'''
    return output


def headline(text):
    return ' <b> <font size="+1">' + text + '</font size="+1"></b>'
