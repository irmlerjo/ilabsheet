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
voila --port=$PORT --no-browser --enable_nbextensions=True SampleSinus.ipynb
