#!/bin/sh
pip install flask
dateval=`date`
echo $dateval > /home/syeds/git/clAutomation/demowebapp/pip-info.log
pip show flask >> /home/syeds/git/clAutomation/demowebapp/pip-info.log
/usr/local/bin/demowebapp 5001
