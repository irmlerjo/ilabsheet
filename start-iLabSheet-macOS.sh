#!/usr/bin/env bash

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

#test if there is already one open jupyter
jupyter_test=$(eval "jupyter notebook list")

if [[ ! $jupyter_test =~ "http" ]]
then
	jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password='' > /dev/null 2>&1 &
	sleep 5
fi

if [ -n "$2" ]
then
	notebook_location="http://localhost:8888/notebooks/$2"
else
	notebook_location="http://localhost:8888"
fi

/Applications/Chromium.app/Contents/MacOS/Chromium --app="data:text/html,<html><body><script>window.moveTo(0,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='$notebook_location';</script></body></html>" &


voila_test=$(eval "curl localhost:8866")
if [[ ! $voila_test =~ "voila" ]]
then
	voila --no-browser > /dev/null 2>&1 &
	sleep 2
fi

#path starts behind .../render/

s1="data:text/html,<html><body><script>window.moveTo(window.screen.width/2,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='http://localhost:8866/voila/render/"
s2="';</script></body></html>"
s3=$s1$1$s2

/Applications/Chromium.app/Contents/MacOS/Chromium --app=$s3

jupyter notebook list








