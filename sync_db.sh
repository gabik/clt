#!/bin/bash
tables=`mysql -p$1 << EOF
use django_clt;
show tables;
EOF`

for i in $tables
do
	mysql -p$1 << EOF
		use django;
		drop table $i;
EOF
done

python manage.py syncdb

