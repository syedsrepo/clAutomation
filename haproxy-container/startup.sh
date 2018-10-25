systemctl enable rsyslog
systemctl enable collectd
systemctl enable haproxy
service collectd start
service rsyslog start
service haproxy start
i="0"
while [ $i -lt 4 ]
do
    echo "Running"
    sleep 2
done
