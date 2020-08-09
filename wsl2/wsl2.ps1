###   https://www.raymond.cc/blog/add-or-remove-windows-features-through-the-command-prompt/

Get-WindowsOptionalFeature -Online

Dism.exe /online /get-features /format:table | more.com

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Restart-Computer

wsl --set-default-version 2

