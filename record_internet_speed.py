import time
import datetime
import subprocess

def test():
    now = datetime.datetime.now()
    results = subprocess.check_output('speedtest-cli')
    start = results.index('Download') + len('Download')+2
    end = results.index('Testing upload speed') - 2
    speed = results[start:end]
    return (str(now), speed)


while 1>0:
    print('testing')
    speed_records = open('speed_records.txt','a')
    try:
    	results = test()
        print results
    	speed_records.write( ','.join(results) + '\n' )
    	speed_records.close()
    except:
	print "error, just keep going"
    print('sleeping')
    time.sleep(60*10)
