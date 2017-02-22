import datetime, sys, subprocess

def get_uptime():
    if sys.platform.startswith('win'):
        cmd = "net statistics server"
        p = subprocess.Popen(cmd, shell=True,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        (child_stdin, child_stdout) = (p.stdin, p.stdout)
        lines = child_stdout.readlines()
        child_stdin.close()
        child_stdout.close()
        lines = [line.strip() for line in lines if line.strip()]
        date, time, ampm = lines[1].split()[2:5]
        m, d, y = [int(v) for v in date.split('/')]
        H, M, _tmp = [int(v) for v in time.split(':')]
        if ampm.lower() == 'pm':
            H += 12
        now = datetime.datetime.now()
        then = datetime.datetime(y, m, d, H, M)
        diff = now - then
        uptime = diff
    else:
        with open('/proc/uptime') as f:
            s = datetime.timedelta(seconds=float(f.readline().split()[0])).total_seconds()
            uptime = '%d days, %d hours, %d minutes, %d seconds' % (
                s // 86400, s // 3600 % 24, s // 60 % 60, s % 60)
    return uptime
