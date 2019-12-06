export {{PATH}}=/appliaction/Python/bin/
pid=`ps -ef|grep 'python3 __init__.py'|awk '{printf $2}'`
echo $pid
kill -9 $pid
rm -rf nohup.out
nohup python3 __init__.py &
