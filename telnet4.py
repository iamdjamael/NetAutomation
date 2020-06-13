import getpass
import telnetlib

HOST = "localhost"
user = input("Telnet Username : ")
password = getpass.getpass()

f = open ('myswitches')

for ip in f:
    ip = ip.strip()
    print ("Configuring Switch : " + (ip))
    HOST = ip

    tn = telnetlib.Telnet(Host)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"vlan 6\n")
    tn.write(b"name Python_VLAN_6\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))