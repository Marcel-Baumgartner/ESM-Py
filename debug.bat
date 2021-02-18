@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /log="CWinSCP.log" /ini=nul ^
  /command ^
    "open sftp://marcel:UnityBetterThanUnreal@mc.masusniper.de:1000/ -hostkey=""ssh-ed25519 255 D2CB2tmFa+oZjrU3IoQDPMTcuCCzayhzo5EvomwNcS8=""" ^
    "cd testarea" ^
    "put *.py" ^
    "put timecache" ^
    "put servers.xml" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

echo %WINSCP_RESULT%

plink.exe -batch -ssh marcel@mc.masusniper.de -P 1000 -pw UnityBetterThanUnreal "cd testarea; python3 main.py start mc.masusniper.de:2099"

pause

exit