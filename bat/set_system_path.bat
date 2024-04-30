@echo off
powershell -Command "Start-Process cmd -Verb RunAs"
::START c:\Windows\System32\runas.exe /user:Administrator /savecred cmd.exe

set /p dirpath=Enter the directory to add to path?
setx /M path "%PATH%;%dirpath%"
:: setx /M path "%PATH%;C:\Program Files\Git\bin" = system wide (means any windows account can access it)
:: setx path "%PATH%;C:\Program Files\Git\bin" = user wide (only the current user can access it)
:: set PATH="%PATH%;C:\Program Files\Git\bin" = session wide (for the current session only)
::powershell string based  [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\Git\bin", "Machine")
::powershell setx PATH "$env:path;C:\Program Files\Git\bin" -m

::backup
echo %PATH% > C:\Users\%UserName%\Documents\path-backup.txt
:: %PATH% can be used to have a dirty version
pause
:end 
