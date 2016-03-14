#!/bin/bash

#Install XQuartz: http://xquartz.macosforge.org/landing/
#brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi
#pip3 install hg+http://bitbucket.org/pygame/pygame


WAIT=4
TIMELEFT=$WAIT
SHUTUP=0
if [ "$1" = "-f" ]; then
    SHUTUP=1
fi

function confirm {
    if [ "$SHUTUP" = 1 ]; then
        ($2)
        return
    fi

    let TIMELEFT=$WAIT
    while [ $TIMELEFT -gt 0 ]; do
        clear
        echo "About to execute: $1."
        echo " "
        echo "CTRL+C to abort.  Will continue in $TIMELEFT seconds."
        sleep 1
        let TIMELEFT=TIMELEFT-1
    done
    clear
    echo "Executing: $1."
    ($2)
}

function install_homebrew {
    # remove homebrew if present
    #ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
    
    # install homebrew again
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
}


function install_python3 {
    # un and reinstall python3
    #/usr/bin/yes | brew ununinstall python3
    brew install python3
    
    # need to set python3 in path?
}

function install_virtualenv {
    # un and reinstall virtualenv for python 3
    #/usr/bin/yes | pip3 uninstall virtualenv
    pip3 install virtualenv
    
    mkdir ~/Projects

    # setup our virtual env
    virtualenv ~/Projects/env
}


function install_django {
    # install django
    #/usr/bin/yes | pip3 uninstall django
    pip3 install django
}

function install_drf {
    #install drf
    #/usr/bin/yes | pip3 uninstall djangorestframework
    pip3 install djangorestframework
}

function install_mysql {
    #un and reinstall mysql
    #brew uninstall mysql
    brew install mysql
}

function install_mysqlclient {
    #un and reinstall mysqlclient.  make sure you're in the virtualenv
    #/usr/bin/yes | pip3 uninstall mysqlclient
    pip3 install mysqlclient
}

function setup_database {
    # create database defaults if not present
    mysql -uroot --execute="CREATE SCHEMA IF NOT EXISTS storybook"
}

function sync_database {
   # migrate and runsync
   python3 manage.py makemigrations api
   python3 manage.py migrate 
}

function do_work {
    clear

    if [ $SHUTUP = 0 ]; then
        echo "If you're not on a Mac, abandon now or else. You've been warned."
        pause 4
    fi

    confirm "(Re)installation of Homebrew" install_homebrew

    confirm "(Re)installation of Python 3" install_python3

    confirm "(Re)installation of mysql" install_mysql

    confirm "Empty schema creation, if not present" setup_database

    confirm "(Re)installation of virtual env" install_virtualenv

    source ~/Projects/env/bin/activate

    confirm "(Re)installation of mysqlclient" install_mysqlclient

    confirm "(Re)installation of django" install_django

    confirm "(Re)installation of djangorestframework" install_drf

    confirm "Migration and sync of database" sync_database

    clear
    
    echo "Great success."
}

do_work
