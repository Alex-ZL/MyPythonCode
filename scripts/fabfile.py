###A sample of using fabric to do some simple operations on remote boxes.

from fabric.api import run, env, roles, local, put, cd

#env.hosts = ['root@192.168.2.112', 'root@192.168.2.113']
env.roledefs = {
		'agent': ['root@192.168.2.112'],
		'master': ['root@192.168.2.113'],
		}

def syncdate():
	###set timezone and sync time for ubuntu
	#run('echo "Asia/Shanghai" | sudo tee /etc/timezone')
	#run('dpkg-reconfigure --frontend noninteractive tzdata')
	#run('ntpdate ntp.server.com')
	#run('hwclock --systohw')

	###set timezone and sync time for centos
	run('rm /etc/localtime')
	run('ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime')
	run('ntpdate ntp.sjtu.edu.cn')


def start():
	run("echo 'the test start...'")

def touch():
	run("touch /tmp/fab-flag")

def write(man):
	str_cmd="echo 'hi, this is a message from %s!' >> /tmp/fab-flag" % man
	run(str_cmd)

def scp():
	local("cd /home/alex/Codes/")
	local("tar cvf /tmp/code.tar cloudtool/")
	put('/tmp/code.tar', '/tmp/code.tar')
	with cd('/tmp/'):
		run('tar xvf code.tar')
def display():
	run("cat /tmp/fab-flag")

def clear():
	run("rm /tmp/fab-flag")

@roles('agent')
def test(arg="Man"):
	start()
	touch()
	write(arg)
	display()
	scp()

@roles('master')
def hello(name="world"):
	run("echo 'special message from %s to master' >> /tmp/fab-flag" % name)
	run("cat /tmp/fab-flag")
	syncdate()
