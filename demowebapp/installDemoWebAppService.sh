#!/bin/sh
cp demowebapp.service /etc/systemd/system/demowebapp.service
systemctl daemon-reload
service demowebapp restart

