###A sample of using fabric to do some simple operations on remote boxes.  
from fabric.api import run, env, roles, local, put, cd
from datetime import datetime

### Dict for hostname and ip
CONST_DICT = {
        '6CU313Y9Z4': ['SVR2689HP380', '10.3.200.10'],
        '6CU313Y9Y7': ['SVR2690HP380', '10.3.200.11'], 
        '6CU313Y9YC': ['SVR2691HP380', '10.3.200.12'],
        '6CU313Y9YT': ['SVR2692HP380', '10.3.200.13'],
        '6CU313Y9Y3': ['SVR2693HP380', '10.3.200.14'],
        '6CU313Y9YY': ['SVR2694HP380', '10.3.200.15'],
        '6CU313Y9XV': ['SVR2695HP380', '10.3.200.16'],
        '6CU313Y9Z2': ['SVR2696HP380', '10.3.200.17'],
        '6CU313Y9YM': ['SVR2697HP380', '10.3.200.18'],
        '6CU313Y9ZB': ['SVR2698HP380', '10.3.200.19'],
        '6CU313Y9YH': ['SVR2699HP380', '10.3.200.20'],
        '6CU313Y9XZ': ['SVR2700HP380', '10.3.200.21'],
        '6CU313Y9YF': ['SVR2701HP380', '10.3.200.22'],
        '6CU313Y9Y5': ['SVR2702HP380', '10.3.200.23'],
        '6CU313Y9YK': ['SVR2703HP380', '10.3.200.24'],
        '6CU313Y9XX': ['SVR2704HP380', '10.3.200.25'],
        '6CU313Y9YR': ['SVR2705HP380', '10.3.200.26'],
        '6CU313Y9YW': ['SVR2706HP380', '10.3.200.27'],
        '6CU313Y9Y9': ['SVR2707HP380', '10.3.200.28'],
        '6CU313Y9YP': ['SVR2708HP380', '10.3.200.29'],
        }

#env.hosts = ['root@192.168.2.112', 'root@192.168.2.113']
env.roledefs = {
		'nt-dev-farm': ['root@10.3.200.10',
                       # 'root@10.3.200.11',
                       # 'root@10.3.200.12',
                        'root@10.3.200.13',
                        'root@10.3.200.14',
                        'root@10.3.200.15',
                        'root@10.3.200.16',
                        'root@10.3.200.17',
                        'root@10.3.200.18',
                        'root@10.3.200.19',
                        'root@10.3.200.20',
                        'root@10.3.200.21',
                        'root@10.3.200.22',
                        'root@10.3.200.23',
                        'root@10.3.200.24',
                        'root@10.3.200.25',
                        'root@10.3.200.26',
                        'root@10.3.200.27',
                        'root@10.3.200.28',
                        'root@10.3.200.29',
                        ],
		}

post_install_item = ["hostname", "serialnum", "ip addr"]

#@roles('nt-dev-farm')
def grub_disable_graph():
    grub_conf="/etc/default/grub"
    run('sed -i "11s/^/#/" %s' % grub_conf)
    run('sed -i "20s/#//g" %s' % grub_conf)
    run('update-grub')
    run('reboot now')

#@roles('nt-dev-farm')
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

#@roles('nt-dev-farm')
def post_install():
    sync_date()
    set_dns_server()   #this task doesn't work here, a strange bug
    set_hostname()
    set_ip()
    with open('post-install.list', 'a') as f:
        f.write("%s %s   %s \n" %(post_install_item[0], post_install_item[1], post_install_item[2]))

def test():
    time_stamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    local('sed -i "2chello %s \n/a" /tmp/fabtest.info' % time_stamp)
