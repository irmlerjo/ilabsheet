#!/usr/bin/env bash
#test if there is already one open jupyter
jupyter_test=$(eval "jupyter notebook list")

if [[ ! $jupyter_test =~ "http" ]]
then
	jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password='' > /dev/null 2>&1 &
	sleep 5
fi

/Applications/Chromium.app/Contents/MacOS/Chromium --app="data:text/html,<html><body><script>window.moveTo(0,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='http://localhost:8888';</script></body></html>" &


voila_test=$(eval "curl localhost:8866")
if [[ ! $voila_test =~ "voila" ]]
then
	voila --no-browser > /dev/null 2>&1 &
	sleep 2
fi

#path starts behind .../render/
#chromium-browser --app="data:text/html,<html><body><script>window.moveTo(1000,0);window.resizeTo(900,1020);window.location='http://localhost:8866/voila/render/Aufgaben/HandsOn_1.ipynb';</script></body></html>" &

s1="data:text/html,<html><body><script>window.moveTo(window.screen.width/2,0);window.resizeTo(window.screen.width/2,window.screen.height);window.location='http://localhost:8866/voila/render/"
s2="';</script></body></html>"
s3=$s1$1$s2

/Applications/Chromium.app/Contents/MacOS/Chromium --app=$s3

jupyter notebook list








