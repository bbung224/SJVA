#! /bin/sh
COUNT=0

while [ 1 ];
do
    git reset --hard
    git pull
    FILENAME="update_requirements.txt"
    if [ -f "$FILENAME" ] ; then
        pip install -r update_requirements.txt
    fi
    export FLASK_APP=sjva.py
    if [ ! -d "/app/migrations" ] && [ -f "/app/data/db/site.db" ]; then
        python -OO -m flask db init
    fi
    python -OO -m flask db migrate
    python -OO -m flask db upgrade
    python -OO sjva.py 9999 ${COUNT}
    RESULT=$?
    echo "EXIT CODE : ${RESULT}.............."
    if [ "$RESULT" = "1" ] || [ "$RESULT" = "2" ]; then
        echo 'REPEAT....'
    else
        echo 'FINISH....'
        break
    fi
    COUNT=`expr $COUNT + 1`
done
