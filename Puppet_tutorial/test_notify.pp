file {"/home/alex/MyPythonCode/Puppet_tutorial/sys.info":
	content => "${ipaddress},\n ${hostname}, \n ${fqdn}, \n ${operatingsystem}"
}
