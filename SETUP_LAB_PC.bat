@echo off
rem One-time setup for a PC, for exam Programs 1 to 5. Double-click this file once.
rem After it finishes, double-clicking any Program_....py file in this folder runs it,
rem and OPEN_IDLE.bat opens IDLE with the right Python.
rem
rem It builds a private Python environment with OpenCV and NumPy in
rem   C:\Users\<you>\cv_lab_venv
rem and tells the Python launcher to use it, by saving the setting VIRTUAL_ENV.
rem Nothing already installed on the PC is changed or removed.
rem To undo: see README.md, section 3.

setlocal
title Computer Vision exam setup
cd /d "%~dp0"

echo ============================================================
echo   Computer Vision exam programs 1 to 5: one-time setup
echo ============================================================
echo.

if not exist requirements.txt goto not_extracted

set "VENV=%USERPROFILE%\cv_lab_venv"
set "VPY=%VENV%\Scripts\python.exe"

rem ---- 1. Is a working environment already there? Then reuse it. ----
"%VPY%" --version >nul 2>&1
if not errorlevel 1 goto have_venv

rem ---- 2. Find a Python to build the environment from. 3.12 is the tested one. ----
set "BASE="
for %%V in (3.12 3.13 3.11 3.10) do if not defined BASE (
    py -%%V -c "import sys" >nul 2>&1 && set "BASE=py -%%V"
)
if not defined BASE if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set "BASE="%LOCALAPPDATA%\Programs\Python\Python312\python.exe""
if defined BASE goto make_venv

rem ---- 3. No usable Python: install 3.12.10 for this user only (no admin needed). ----
echo No Python 3.10 to 3.13 was found on this PC.
echo Downloading Python 3.12.10 from python.org, 27 MB ...
set "INSTALLER=%TEMP%\python-3.12.10-amd64.exe"
curl -L --fail -o "%INSTALLER%" https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe
if errorlevel 1 goto no_download
rem Add the "py" launcher only if this PC does not already have one
set "LAUNCHER=1"
where py >nul 2>&1 && set "LAUNCHER=0"
echo Installing Python 3.12.10 for this user only. A progress window opens ...
start /wait "" "%INSTALLER%" /passive InstallAllUsers=0 PrependPath=0 Include_launcher=%LAUNCHER% InstallLauncherAllUsers=0 AssociateFiles=1 Include_test=0
set "BASE="%LOCALAPPDATA%\Programs\Python\Python312\python.exe""
%BASE% --version >nul 2>&1
if errorlevel 1 goto no_python

:make_venv
echo Building the environment with: %BASE%
echo Folder: %VENV%
%BASE% -m venv --clear "%VENV%"
"%VPY%" --version >nul 2>&1
if errorlevel 1 goto no_venv

:have_venv
echo Environment folder: %VENV%
"%VPY%" --version
echo.

rem ---- 4. Libraries: OpenCV 4 and NumPy, about 55 MB the first time ----
echo Installing OpenCV and NumPy. About 55 MB the first time ...
"%VPY%" -m pip install --disable-pip-version-check -r requirements.txt
if errorlevel 1 goto no_basic
echo.

rem ---- 5. Tell the Python launcher to use this environment on double-click ----
setx VIRTUAL_ENV "%VENV%" >nul
if errorlevel 1 echo WARNING: could not save the VIRTUAL_ENV setting. Double-click will not work.

rem ---- 6. Check both libraries by importing them ----
echo Checking the libraries ...
echo.
call :check "numpy"          "import numpy; print('  OK      numpy', numpy.__version__)"
call :check "OpenCV 4"       "import cv2; assert cv2.__version__[0] == '4'; print('  OK      OpenCV', cv2.__version__)"
echo.
echo Setup finished. Lines marked OK are ready.
echo You can now double-click any Program_....py file in this folder.
echo To use IDLE instead, double-click OPEN_IDLE.bat, open a program, press F5.
echo If a program opens in an editor instead of running, read README.md section 3.
echo.
pause
exit /b 0

:check
"%VPY%" -c %2 2>nul
if errorlevel 1 echo   FAILED  %~1
exit /b 0

:not_extracted
echo This file is being run from inside the zip.
echo Close this window, right-click the zip, choose Extract All,
echo then run SETUP_LAB_PC.bat from the extracted folder.
goto stop

:no_download
echo.
echo Could not download Python. Check the internet connection and run this file again.
echo Or install Python 3.12 by hand: README.md section 7.
goto stop

:no_python
echo.
echo Python 3.12 did not install. The PC may block installing software.
echo Ask the lab staff, or install Python 3.12 by hand: README.md section 7.
goto stop

:no_venv
echo.
echo Could not build the environment in %VENV%.
echo Read the message above, then see README.md section 9.
goto stop

:no_basic
echo.
echo OpenCV and NumPy did not install. Read the red text above.
echo Most often it is the internet connection: README.md section 9, error 6.
goto stop

:stop
echo.
pause
exit /b 1
