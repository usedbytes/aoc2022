#!/bin/sh
# http://stackoverflow.com/a/12694189
DIR="${BASH_SOURCE%/*}"
if [[ ! -d "$DIR" ]]
then
	DIR="$PWD"
fi

DAY=$1
if [ -z $1 ]
then
	DAY=$(date "+%d")
fi

export D=${DIR}/${DAY}

mkdir ${D}
cp -n ${DIR}/template.go ${D}/puzzle.go
cd ${D}
