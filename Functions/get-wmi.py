#!/usr/bin/python3
import wmi

## http://timgolden.me.uk/python/wmi/tutorial.html
## http://timgolden.me.uk/python/wmi/cookbook.html

c = wmi.WMI()
#  c = wmi.WMI("MachineB", user=r"MachineB\fred", password="secret")
for os in c.Win32_OperatingSystem():
    print(os.Caption) 

## This watches the for new processes starting and outputs them in terminal
# process_watcher = c.Win32_Process.watch_for("creation")
# while True:
#   new_process = process_watcher()
#   print(new_process.Caption)

##Logical Disk
# logical_disk = wmi.WMI(moniker="//./root/cimv2:Win32_LogicalDisk")
# c_drive = wmi.WMI(moniker='//./root/cimv2:Win32_LogicalDisk.DeviceID="C:"')

c = wmi.WMI()
# for disk in c.Win32_LogicalDisk(DriveType=3):
#for disk in c.Win32_LogicalDisk(["Caption", "Description", "FileSystem"], DriveType=3):
#wql = "SELECT * FROM Win32_LogicalDisk WHERE DriveType=3"
wql = "SELECT Caption, Description, FileSystem FROM Win32_LogicalDisk WHERE DriveType=3"
#wql = "SELECT Caption, Description FROM Win32_LogicalDisk WHERE DriveType <> 3"
for disk in c.query(wql):
    print(disk)

for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
      print(interface.Description, interface.MACAddress)
   for ip_address in interface.IPAddress:
     print(ip_address)
#   print