@echo off
rem Opens IDLE with the Python that has the libraries for these programs.
rem Run SETUP_LAB_PC.bat once on this PC before using this file.
rem In IDLE: File, Open, pick a program, then press F5 to run it.

set "PYW=%USERPROFILE%\cv_lab_venv\Scripts\pythonw.exe"
if not exist "%PYW%" goto no_setup

rem start in this folder, so the File, Open box shows the programs
cd /d "%~dp0"
start "" "%PYW%" -m idlelib
exit /b 0

:no_setup
echo.
echo The Python environment was not found at %USERPROFILE%\cv_lab_venv
echo Double-click SETUP_LAB_PC.bat first, wait for it to finish, then open this file again.
echo.
pause
exit /b 1
