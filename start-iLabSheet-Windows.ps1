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

$jupyter_test = Invoke-Expression "jupyter notebook list"
if (-not ($jupyter_test -match "http"))
{
    $path = pwd
    jupyter notebook --no-browser --notebook-dir=$path --NotebookApp.token='' --NotebookApp.password='' 2>&1 &
	Start-Sleep -s 5
}

Start-Process -FilePath 'C:\Program Files\Google\Chrome\Application\chrome.exe' --app="data:text/html,<html><body><script>window.moveTo(0,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='http://localhost:8888';</script></body></html>" &

$voila_test = Invoke-Expression "curl localhost:8866"

if (-not ($voila_test -match "voila"))
{
    voila --no-browser 2>&1 &
    Start-Sleep -s 2
}

$s1="data:text/html,<html><body><script>window.moveTo(window.screen.width/2,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='http://localhost:8866/voila/render/"
$s2="';</script></body></html>"
$s3= -join($s1,$args[0],$s2)

Start-Process -FilePath 'C:\Program Files\Google\Chrome\Application\chrome.exe' --app=$s3

jupyter notebook list