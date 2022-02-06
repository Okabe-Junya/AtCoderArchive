#!/bin/sh

if [ $# -ne 3 ]
then
    echo "Usage: $0 <dir_name> <start> <end>"
    exit 1
fi

cd $1
start=$2
end=$3
if [ $start -gt $end ]
then
    echo "<start> must be less than <end>"
    exit 1
fi
while [ $start -le $end ]
do
    # 0埋め
    tmp="000${start}"
    dir_name="${tmp: -3}"

    mkdir $dir_name
    cd $dir_name
    for var in a b c d e f
    do
        filename="${var}.py"
        touch $filename
    done
    cd ..
    start=`expr $start \+ 1`
done