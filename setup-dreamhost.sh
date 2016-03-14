#!/bin/bash

VENVPATH=$HOME/maintaincomposure.com
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



function install_python3 {
    wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
    tar zxvf Python-3.5.1.tgz
    cd Python-3.5.1
    ./configure --prefix=$HOME/opt/python-3.5.1
    make
    make install
}

function add_to_path {
    if ! grep -q "python-3.5.1/bin" "$HOME/.bash_profile"; then
        echo "export PATH=$HOME/opt/python-3.5.1/bin:\$PATH" >> $HOME/.bash_profile
        source $HOME/.bash_profile
    fi
}

function update_pip {
    pip3 install --update pip
}

function cleanup_python3 {
    rm $HOME/Python-3.5.1.tgz
    rm $HOME/Python-3.5.1/ -r
}

function make_virtualenv {
    $HOME/opt/python-3.5.1/bin/pyvenv $VENVPATH
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

function install_mysqlclient {
    #un and reinstall mysqlclient.  make sure you're in the virtualenv
    #/usr/bin/yes | pip3 uninstall mysqlclient
    pip3 install mysqlclient
}

function clone_project {
    cd $VENVPATH
    git clone https://github.com/adamski52/pet-project.git
}

function do_work {
    clear

    if [ $SHUTUP = 0 ]; then
        echo "If you're not on a Dreamhost VPS, abandon now or else. You've been warned."
        pause 4
    fi

    confirm "Installation of Python 3" install_python3

    #confirm "Cleanup of Python 3 source" cleanup_python3

    confirm "Add Python 3 to PATH" add_to_path

    confirm "Installation of virtualenv" make_virtualenv

    source $VENVPATH/bin/activate

    confirm "Update pip" update_pip

    confirm "Installation of mysqlclient" install_mysqlclient

    confirm "Installation of django" install_django

    confirm "Installation of djangorestframework" install_drf

    confirm "Clone project from github" clone_project

    clear
    
    echo "Great success."
}

do_work
