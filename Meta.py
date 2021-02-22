import ipywidgets as widgets
import csv
import os
import time

#erstellt einen Slider, welcher rechts einen sich verändernden Text (je nach Stufe des Sliders) enthält
class Slider():
    def __init__(self):
        self.int_range = widgets.IntSlider(
            value=1,
            min=1,
            max=5,
            step=1,
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=False,
            readout_format='d',
            layout=widgets.Layout(width='200px')
        )

        self.blank = "&nbsp"*5

        self.t = widgets.HTML(value=self.blank + '<b>keine Erfahrung</b>' )
        
        self.hint = widgets.HTML(value='<i>Bitte Slider bewegen</i>')
        
        self.hbox = widgets.HBox([widgets.HTML("&nbsp &nbsp"),self.int_range, self.t])
        
        self.add_change_listener(self.int_range)
    
    #hier werden die Labels definiert    
    def add_change_listener(self, slider):
        def on_value_change(change):
            if change['new'] == 1:
                self.t.value = self.blank + '<b>keine Erfahrung</b>'
            if change['new'] == 2:
                self.t.value = self.blank + '<b>Anfänger</b>'
            if change['new'] == 3:
                self.t.value = self.blank + '<b>routiniert</b>'
            if change['new'] == 4:
                self.t.value = self.blank + '<b>fortgeschritten</b>'
            if change['new'] == 5:
                self.t.value = self.blank + '<b>Profi</b>'


        self.int_range.observe(on_value_change, names='value')
        
    def getValue(self):
        return self.hbox.children[1].value


    def getElements(self):
        return widgets.VBox([self.hbox, self.hint])

#Hauptfunktion zum Starten der Meta Daten Umfrage    
def start():    
    #grafische Elemente
    newline = widgets.HTML(value='<p></p>')

    def headline(text):
         return ' <b> <font size="+1">' +  text + '</font size="+1"></b>'

    #header 
    header = headline("Umfrage")
    header_element = widgets.HTML(header)

    ##############Studiengang##################################
    description = "1) Bitte wählen Sie unten Ihren Studiengang aus."
    t1 = widgets.HTML(value='<p>' + description + '</p>' )
    options = ["M.Sc. Informatik","M.Sc. Bioinformatik","M.Sc. Wirtschaftsinformatik","M.Sc. Digital Humanities","Sonstige"]
    s1 = widgets.RadioButtons(
                                        options=options,
                                        description='         ',
                                        disabled=False
                                    )
    ###Textarea, falls "Sonstiges" ausgewählt wird
    sonstiges = widgets.Textarea(
    value='Hier eintippen',
    placeholder='Hier eintippen',
    description=' ',
    disabled=True,
    layout = widgets.Layout(height="25px")
    )
    #change listener
    def on_value_change(change):
        if change['new'] == 'Sonstige':
            sonstiges.disabled = False
            sonstiges.value = ""
        if change['new'] != 'Sonstige':
            sonstiges.disabled = True
            sonstiges.value ='Hier eintippen'
        

    s1.observe(on_value_change, names='value')

    #############Andere Module#################################
    description2 = "2) Haben Sie bereits eines der folgenden Module besucht?"
    t2 = widgets.HTML(value='<p>' + description2 + '</p>' )
    options2 = ["Künstliche Neuronale Netze und Maschinelles Lernen (10-202-2128)", "Neuroinspirierte Informationsverarbeitung (10-202-2104)", "Statistisches Lernen (09-INF-BIO1)"]
    items = []
    for current_option in options2:
        option = widgets.Checkbox(value=False,
                                  description= current_option,
                                  disabled=False,
                                  layout=widgets.Layout(width='90%')
                                 )
        items.append(option)
    box = widgets.VBox(items)


    ##############Programmiersprache############################
    description3 = "3) Bitte wählen Sie Ihre bevorzugte Programmiersprache aus für das Praktikum."
    t3 = widgets.HTML(value='<p>' + description3 + '</p>' )
    options3 = ["Python","R"]
    s3 = widgets.RadioButtons(
                                        options=options3,
                                        description='         ',
                                        disabled=False
                                    )

    ###############Selbsteinschätzung###########################
    description4 = "4) Schätzen Sie Ihre praktischen Fähigkeiten, bzw. Erfahrungen in folgenden Bereichen ein, indem Sie den Regler verschieben"
    blanks = widgets.HTML(value='&nbsp;&nbsp;')
    t4 = widgets.HTML(value='<p>' + description4 + '</p>')


    ##Python
    description5 = "&nbsp;&nbsp;&nbsp;4.1) Programmiererfahrung in Python"
    t5 = widgets.HTML(value='<p>' + description5 + '</p>', layout=widgets.Layout(width='250px'))
    slider1 = Slider()
    hbox1 = widgets.HBox([t5,blanks,slider1.hbox])
   
    ##R
    description6 = "&nbsp;&nbsp;&nbsp;4.2) Programmiererfahrung in R"
    t6 = widgets.HTML(value='<p>' + description6 + '</p>', layout=widgets.Layout(width='250px'))
    slider2 = Slider()
    hbox2 = widgets.HBox([t6,blanks,slider2.hbox])
   
    ##Selbsteinschätzung: Kenntnisse in Mathematik/ Statistik/ Datenanalyse
    description7 = "&nbsp;&nbsp;&nbsp;4.3)Statistik/ Datenanalyse"
    t7 = widgets.HTML(value='<p>' + description7 + '</p>', layout=widgets.Layout(width='250px'))
    slider3 = Slider()
    hbox3 = widgets.HBox([t7,blanks,slider3.hbox])

    ##Selbsteinschätzung: Kenntnisse in Datenerhebung 
    description8 = "&nbsp;&nbsp;&nbsp;4.4) (Empirische) Datenerhebung"
    t8 = widgets.HTML(value='<p>' + description8 + '</p>', layout=widgets.Layout(width='250px'))
    slider4 = Slider()
    hbox4 = widgets.HBox([t8,blanks,slider4.hbox])
   
    ##Selbsteinschätzung: Kenntnisse Maschinellem Lernen
    description9 = "&nbsp;&nbsp;&nbsp;4.5) Maschinelles Lernen"
    t9 = widgets.HTML(value='<p>' + description9 + '</p>', layout=widgets.Layout(width='250px'))
    slider5 = Slider()
    hbox5 = widgets.HBox([t9,blanks,slider5.hbox])

    send_btn = widgets.Button(
        description='Absenden',
        disabled=False,
        button_style='',
        tooltip='Absenden ',
        icon='check'
    )

    path = os.getlogin()+"_Meta.csv"
    def writeLogfile(b):
        b.disabled = True
        loggingHeader = ["Studiengang","Module","Programmiersprache","SE1","SE2","SE3","SE4","SE5","Zeitstempel"]
        if s1.value == "Sonstige":
            studiengang = sonstiges.value
        else:
            studiengang = s1.value
        result = []
        for s in items:
            if s.value == True:
                result.append(s.description.split("(")[1].replace(")",""))
        module = result
        progspr = s3.value
        se1 = slider1.getValue()
        se2 = slider2.getValue()
        se3 = slider3.getValue()
        se4 = slider4.getValue()
        se5 = slider5.getValue()
        with open(path, "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(loggingHeader)
            writer.writerow([str(studiengang),str(module).replace(",",";"),str(progspr),str(se1),str(se2),str(se3),str(se4),str(se5),str(time.asctime().replace(" ","_"))])
        csvFile.close()

    send_btn.on_click(writeLogfile)

    display(header_element,t1,s1,sonstiges,
             newline,t2,box,newline,t3,s3,newline,newline,t4,hbox1,newline,hbox2,newline,hbox3,newline,hbox4,newline,hbox5,newline,newline,newline,send_btn)

