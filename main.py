
import platform
import wifi
import socket

my_system = platform.uname()
#SSID =
#ip_address = socket.gethostbyname(SSID)

print(f"System: {my_system.system}") #OS Name
print(f"OS Version: {my_system.version}") #OS VERSION
print(f"Computer Name: {my_system.node}") #Comp Name
print(f"Processor: {my_system.processor}") #PROCESSOR
print(f"Architecture: {my_system.machine}") #MACHINE TYPE

print(f"")

print(f"")##SSID
#print(f"IP-Address: " + ip_address)##IP ADDRESS

print(f"")

print(f"Python Version: {platform.python_version()}")##PYTHON VERSION
print(f"Java Version: {platform.java_ver()}")##JAVA VERSION

