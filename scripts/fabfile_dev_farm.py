###A sample of using fabric to do some simple operations on remote boxes.

from fabric.api import run, env, roles, local, put, cd
from datetime import datetime

### Dict for hostname and ip
CONST_DICT = {
        '6CU313Y9Z4': ['SVR2689HP380', '10.3.220.110'],
        '6CU313Y9Y7': ['SVR2690HP380', '10.3.220.111'], 
        '6CU313Y9YC': ['SVR2691HP380', '10.3.220.112'],
        '6CU313Y9YT': ['SVR2692HP380', '10.3.220.113'],
        '6CU313Y9Y3': ['SVR2693HP380', '10.3.220.114'],
        '6CU313Y9YY': ['SVR2694HP380', '10.3.220.115'],
        '6CU313Y9XV': ['SVR2695HP380', '10.3.220.116'],
        '6CU313Y9Z2': ['SVR2696HP380', '10.3.220.117'],
        '6CU313Y9YM': ['SVR2697HP380', '10.3.220.118'],
        '6CU313Y9ZB': ['SVR2698HP380', '10.3.220.119'],
        '6CU313Y9YH': ['SVR2699HP380', '10.3.220.120'],
        '6CU313Y9XZ': ['SVR2700HP380', '10.3.220.121'],
        '6CU313Y9YF': ['SVR2701HP380', '10.3.220.122'],
        '6CU313Y9Y5': ['SVR2702HP380', '10.3.220.123'],
        '6CU313Y9YK': ['SVR2703HP380', '10.3.220.124'],
        '6CU313Y9XX': ['SVR2704HP380', '10.3.220.125'],
        '6CU313Y9YR': ['SVR2705HP380', '10.3.220.126'],
        '6CU313Y9YW': ['SVR2706HP380', '10.3.220.127'],
        '6CU313Y9Y9': ['SVR2707HP380', '10.3.220.128'],
        '6CU313Y9YP': ['SVR2708HP380', '10.3.220.129'],
        }

#env.hosts = ['root@192.168.2.112', 'root@192.168.2.113']
env.roledefs = {
		'nt-dev-farm': ['root@10.3.220.120',
                        'root@10.3.220.121',
                        'root@10.3.220.122',
                        'root@10.3.220.123',
                        'root@10.3.220.124',
                        'root@10.3.220.125',
                        'root@10.3.220.126',
                        'root@10.3.220.127',
                        'root@10.3.220.128',
                        'root@10.3.220.129',
                        ],
		}

post_install_item = ["hostname", "serialnum", "ip addr"]

@roles('nt-dev-farm')
def sync_date():
	###set timezone and sync time for ubuntu
	run('echo "Asia/Shanghai" | sudo tee /etc/timezone')
	run('dpkg-reconfigure --frontend noninteractive tzdata')
	run('ntpdate 192.168.100.59')
	run('hwclock --systohc')

	###set timezone and sync time for centos
	#run('rm /etc/localtime')
	#run('ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime')
	#run('ntpdate ntp.sjtu.edu.cn')

def scp():
	local("cd /home/alex/Codes/")
	local("tar cvf /tmp/code.tar cloudtool/")
	put('/tmp/code.tar', '/tmp/code.tar')
	with cd('/tmp/'):
		run('tar xvf code.tar')

@roles('nt-dev-farm')
def set_dns_server():
    dns_path = "/run/resolvconf/resolv.conf"
    run('sed -i "/nameserver/d" %s' % dns_path)
    run('echo "nameserver 10.2.0.51" >> %s' % dns_path)
    run('echo "nameserver 10.2.0.52" >> %s' % dns_path)
    run('cat /etc/resolv.conf')

def set_hostname():
    serial_num = run("dmidecode -s system-serial-number")
    hostname = CONST_DICT[serial_num][0]
    post_install_item[0] = hostname
    post_install_item[1] = serial_num
    run('hostname %s' % hostname)
    run('echo "%s" > /etc/hostname' % hostname)
    run('sed -i "2c127.0.1.1       %s.dev.nt.ctripcorp.com       %s" /etc/hosts' % (hostname, hostname))


def set_ip():
    serial_num = run("dmidecode -s system-serial-number")
    ip_addr = CONST_DICT[serial_num][1]
    post_install_item[2] = (ip_addr)
    network="/etc/network/interfaces"
    run('sed -i "/dhcp/d" %s' % network)
    run('echo "iface eth0 inet static" >> %s' % network)
    run('echo "address %s" >> %s' % (ip_addr, network))
    run('echo "netmask 255.255.255.0" >> %s' % network)
    run('echo "gateway 10.3.220.1" >> %s' % network)
    run('reboot now')

@roles('nt-dev-farm')
def post_install():
    syncdate()
    #set_dns_server()   this task doesn't work here, a strange bug
    set_hostname()
    set_ip()
    with open('post-install.list', 'a') as f:
        f.write("%s %s   %s \n" %(post_install_item[0], post_install_item[1], post_install_item[2]))

def test():
    time_stamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    local('touch /home/zhangliang/Codes/touch-flag-%s' %time_stamp) 
    sn = local('sudo dmidecode -s system-serial-number')
    print sn
