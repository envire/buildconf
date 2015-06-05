#! /bin/bash

CONF_REPO=envire/buildconf.git
RUBY=ruby
AUTOPROJ_BOOTSTRAP_URL=http://rock-robotics.org/stable/autoproj_bootstrap

set -e

if ! test -f $PWD/autoproj_bootstrap; then
    if which wget > /dev/null; then
        DOWNLOADER=wget
    elif which curl > /dev/null; then
        DOWNLOADER=curl
    else
        echo "I can find neither curl nor wget, either install one of these or"
        echo "download the following script yourself, and re-run this script"
        exit 1
    fi
    $DOWNLOADER $AUTOPROJ_BOOTSTRAP_URL
fi

$RUBY autoproj_bootstrap $@ git git@git.hb.dfki.de:$CONF_REPO branch=master push_to=git@git.hb.dfki.de:$CONF_REPO
if test "x$@" != "xlocaldev"; then
    . $PWD/env.sh
    autoproj update
    autoproj fast-build
fi
