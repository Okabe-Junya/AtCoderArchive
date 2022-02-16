#!/bin/sh

if [ $# -ne 2 ]
then
    echo "Usage: $0 <start> <end>"
    exit 1
fi

start=$1
end=$2
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
    for var in 0 1 2 3 4 5 6 7 8 9
    do
        filename="${start}.${var}.py"
        touch $filename
    done
    cd ..
    start=`expr $start \+ 1`
done