#!/bin/sh
pip install flask
dateval=`date`
echo $dateval > /home/syeds/git/clAutomation/demowebapp/pip-info.log
pip show flask >> /home/syeds/git/clAutomation/demowebapp/pip-info.log
/usr/local/bin/demowebapp 5001 &
/usr/local/bin/demowebapp 5002 &
/usr/local/bin/demowebapp 5003 &
/usr/local/bin/demowebapp 5004 & 

sleep infinity
