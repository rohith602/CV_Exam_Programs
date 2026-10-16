# Computer Vision exam programs 1 to 5 (PGI25D07J)

Programs 1 to 5 from the practical record, the ones in the exam, as files that run on a normal Windows PC. All five read the same picture, `image.jpg`, and need only two libraries: OpenCV and NumPy.

## 1. What is in this folder

| File | Opens | Libraries it needs |
|---|---|---|
| `Program_1_Canny_Edge_Detection.py` | 1 picture window | opencv |
| `Program_2_Edge_Detection_Comparison.py` | 5 picture windows | opencv, numpy |
| `Program_3_Simple_Thresholding.py` | 5 picture windows | opencv |
| `Program_4_Image_Blurring.py` | 4 picture windows | opencv |
| `Program_5_Erosion_Dilation.py` | 3 picture windows | opencv, numpy |

Other files:

- `image.jpg`: the picture (960 x 540). To use another picture, replace this file and keep the name `image.jpg`.
- `SETUP_LAB_PC.bat`: double-click this once on each PC. It installs OpenCV and NumPy into a private Python environment. See section 3.
- `OPEN_IDLE.bat`: double-click this to open IDLE with the Python that has the libraries. See section 3, "Run the programs in IDLE".
- `requirements.txt`: the two libraries, for installing by hand.

## 2. Get the folder on a lab PC

Download the zip from GitHub. No sign-in is needed:

```
https://github.com/rohith602/CV_Exam_Programs/releases/latest/download/CV_Exam_Programs.zip
```

Or open https://github.com/rohith602/CV_Exam_Programs and click the green Code button, then Download ZIP. That zip names the folder `CV_Exam_Programs-main`; the files inside are the same.

## 3. Quick start

### In the lab, with the setup file

1. Save the zip to the PC's own drive, for example the Desktop.
2. Right-click the zip and choose Extract All. Do not work inside the zip: programs opened from an unextracted zip cannot find `image.jpg`.
3. Open the extracted folder and double-click `SETUP_LAB_PC.bat`. A black window opens and shows its progress. It downloads about 55 MB.
4. When it finishes it prints two lines, `OK numpy` and `OK OpenCV 4...`. Press any key to close the window.
5. Double-click any `Program_....py` file, or use IDLE as below.

You run the setup file once per PC and per Windows login. Running it again is harmless; it skips what is already done. If the full 17-program setup (`CV_Lab_Programs`) was already run on this login, this one finds the same environment and finishes in seconds.

If Windows shows a blue box "Windows protected your PC" when you double-click the setup file, click More info, then Run anyway. Windows shows this for files that came from the internet. To avoid it, right-click the zip before extracting, choose Properties, tick Unblock, and click OK.

### Run the programs in IDLE

IDLE is the small editor that is installed together with Python. Each Python on a PC has its own IDLE, and a program run from IDLE uses the libraries of that Python. The IDLE in the Start menu belongs to the PC's own Python, which usually does not have OpenCV. A program run from it stops at `ModuleNotFoundError: No module named 'cv2'` (section 9, error 10).

Open IDLE this way:

1. Run `SETUP_LAB_PC.bat` once on the PC, as described above.
2. Double-click `OPEN_IDLE.bat`. A window named "IDLE Shell" opens, with a `>>>` line.
3. In that window choose File, then Open, and pick a program. The code opens in a second window.
4. In the code window press F5, or choose Run, then Run Module. The picture windows open. Click one of them and press any key to close them all.
5. For the next program, repeat steps 3 and 4.

The setup file installs OpenCV only into its own environment, `cv_lab_venv`. It does not add OpenCV to the PC's normal Python, so only the IDLE opened with `OPEN_IDLE.bat` has it.

To check that this is the right IDLE, type these two lines on the `>>>` line, pressing Enter after each:

```
import cv2
cv2.__version__
```

| What it prints | Meaning |
|---|---|
| `'4.14.0'` | The IDLE from `OPEN_IDLE.bat`. Open a program and press F5 |
| Any other version, for example `'5.0.0'` | The PC's own Python, which happens to have OpenCV too. Programs 1 to 5 still work: with OpenCV 5.0.0 they produced exactly the same pictures as with 4.14.0 in the test |
| `ModuleNotFoundError: No module named 'cv2'` | The PC's own Python, without OpenCV. Close this IDLE and use `OPEN_IDLE.bat` |

The title bar ("IDLE Shell 3.12.8") does not tell them apart: the environment is built from the PC's Python 3.12, so both can show the same version.

The same thing without the bat file, from Command Prompt inside this folder:

```
py -m idlelib Program_1_Canny_Edge_Detection.py
```

`py` is the Python launcher, which uses the environment once the setup file has run. `-m idlelib` starts IDLE, and the file name is the program to open. Then press F5.

What is different in IDLE:

- Run a program with F5 from the code window. The `>>>` line takes one statement at a time, so a whole program pasted there does not run.
- If a picture window does not show, it may be behind the IDLE windows. Look for it on the taskbar.
- To stop a program that is still running, choose Shell, then Restart Shell in the IDLE Shell window.

### What the setup file changes on the PC

It does not remove or change any Python or library that is already installed. It adds:

| What | Where | How to remove it |
|---|---|---|
| A private Python environment with OpenCV and NumPy, about 150 MB | `C:\Users\<your user name>\cv_lab_venv` | Delete the folder |
| A Windows setting named `VIRTUAL_ENV` for your login | Windows user settings | `reg delete HKCU\Environment /v VIRTUAL_ENV /f` in Command Prompt |
| Python 3.12.10 for your login, only if the PC had no Python from 3.10 to 3.13 | `C:\Users\<your user name>\AppData\Local\Programs\Python\Python312` | Section 8 |

How it works: when you double-click a `.py` file, Windows passes it to the Python launcher (`py.exe`). The launcher normally picks the newest Python on the PC, which usually does not have OpenCV. If the setting `VIRTUAL_ENV` exists, the launcher uses the Python inside that folder instead. The setup file builds that folder and saves that setting.

One side effect: while the setting is saved, double-clicking any other `.py` file on that login, or typing `py` with no version number, also uses this environment. Typing `python` is not affected, and `py -3.14` still starts 3.14.

The branch of the setup file that installs Python 3.12.10 could not be tested where this folder was prepared, because that laptop already had Python 3.12. If that step fails in the lab, install Python by hand (section 7) and run the setup file again.

### If double-click does not run the program

- The program opens in an editor (VS Code, IDLE, Notepad): the PC is set to edit `.py` files, not run them. Use IDLE as above, or right-click a program, choose Open with, then Choose another app, pick Python, and choose Always.
- A black window flashes and disappears: the program stopped with an error. To read the error, click in the folder's address bar, type `cmd`, press Enter, then type `py Program_1_Canny_Edge_Detection.py` (with the name of the program that failed). Then look the message up in section 9.
- You did not run the setup file on this PC or this login, or its check list showed `FAILED`.

### By hand, without the setup file

Open Command Prompt (press the Windows key, type `cmd`, press Enter). Then type these lines one at a time. Change the path in the first line to wherever you extracted the folder.

```
cd C:\CV_Exam_Programs
python --version
python -m pip install -r requirements.txt
python Program_1_Canny_Edge_Detection.py
```

What each line does:

1. `cd` moves the Command Prompt into the folder, so that the file names in the next lines are found.
2. Shows the Python version. It should say 3.10 or newer (see section 5).
3. Installs OpenCV and NumPy into that Python.
4. Runs Program 1. A window with white edges on black opens. Click that window and press any key to close it.

If line 2 or 3 fails, go to section 4 and then section 9. A program run this way uses the `python` in Command Prompt, so in IDLE use that same Python's IDLE: `python -m idlelib`.

## 4. Check what the lab PC has

| Command | What it tells you |
|---|---|
| `python --version` | The version of the Python that runs when you type `python` |
| `py --version` | The version the Python launcher picks when you type `py` |
| `py -0p` | Every Python installed on the PC, with its folder. The one marked `*` is the launcher's default |
| `where python` | Every `python.exe` Windows can find, in the order it tries them. The first line is the one that runs |
| `python -m pip --version` | The pip version, and which Python that pip belongs to (read the path at the end) |
| `python -m pip list` | Every library installed for that Python, with versions |
| `python -c "import struct; print(struct.calcsize('P')*8)"` | Prints 64 or 32. It should be 64 |
| `python -c "import cv2; print(cv2.__version__)"` | The OpenCV version, or an error if it is not installed |

A PC can have several Pythons at once. On the laptop where this folder was prepared, `python --version` said 3.13.9 (Anaconda) while `py --version` said 3.14.5, and a third one (3.12.8) was also installed. A library installed for one of them is invisible to the others. That is the most common reason for "I installed it but it still says module not found".

To be sure the library goes into the same Python that runs your program, always install with `python -m pip install ...` and run with `python ...`, both using the same word (`python` in both, or `py -3.12` in both).

## 5. Which Python version works

| Python | Result |
|---|---|
| 3.12 | Tested (October 2026). Use this if you can choose. |
| 3.10, 3.11, 3.13, 3.14 | OpenCV and NumPy have ready-made Windows files for these. Not tested here. |
| 3.9 or older | Not tested. pip falls back to older OpenCV and NumPy releases. Install 3.12 instead (section 7). |

If the lab PC has several Pythons, pick one with the launcher: write `py -3.12` wherever this file says `python`. Example: `py -3.12 -m pip install -r requirements.txt` and `py -3.12 Program_1_Canny_Edge_Detection.py`.

`requirements.txt` says `opencv-python<5`, so the setup file installs OpenCV 4.14, the version used for the full record. Plain `pip install opencv-python` now installs OpenCV 5.0. Programs 1 to 5 work with both: run with 4.14.0 and with 5.0.0, all 18 picture windows were identical. OpenCV 5 matters only for Programs 10 and 11b of the full record, which use detectors that 5.0 removed.

## 6. Run a program and close it

After the setup file has been run, double-click the program, or open it in IDLE and press F5. Or from Command Prompt:

```
python Program_3_Simple_Thresholding.py
```

Type `python Pro` and press Tab to let Windows complete the file name.

To close: click one of the picture windows, then press any key. All of them close together and the program ends. The X button also works, but when several windows are open you have to close each one.

What you should see with the supplied `image.jpg`, from the test run:

| Program | Output |
|---|---|
| 1 | White outlines of the two men on a black background |
| 2 | Original, Sobel, Prewitt, Laplacian and Canny windows |
| 3 | Five black and white versions: Binary, Binary Inverted, Truncated, Set to Zero, Set to Zero Inverted |
| 4 | Original and three blurred copies |
| 5 | Grey original, a darker eroded copy and a brighter dilated copy |

Each program takes 1 to 4 seconds on a laptop with an i5 processor.

## 7. Install Python 3.12 if it is missing

With the installer:

1. Download "Windows installer (64-bit)" for Python 3.12 from https://www.python.org/downloads/windows/
2. Run it. On the first screen tick "Add python.exe to PATH". Without this tick, typing `python` does not work.
3. Click "Install Now". This installs for your user only and needs no administrator password.
4. Close Command Prompt and open a new one. An already open window does not see the new Python.
5. Check with `python --version`.

Or from Command Prompt, if the PC has winget (Windows 10 and 11 normally do):

```
winget install Python.Python.3.12
```

## 8. Uninstall a Python version

On a college lab PC, ask the lab staff first. The PC is shared, other subjects may need the version you want to remove, and it may ask for an administrator password. In most cases you do not need to uninstall anything: installing 3.12 beside the others and typing `py -3.12` does the job.

To uninstall with the mouse:

1. Open Settings, then Apps, then Installed apps (on Windows 10: Apps and features).
2. Type `python` in the search box.
3. Click the three dots beside the version to remove, for example "Python 3.14.5 (64-bit)", and choose Uninstall.
4. "Python Launcher" is a separate entry. Leave it if any other Python stays on the PC, because it is what makes `py` work.

To uninstall from Command Prompt:

```
winget list --name Python
winget uninstall --id Python.Python.3.14
```

The first line lists what is installed with an Id for each. The second removes the one whose Id you give; change `3.14` to the version you mean.

After uninstalling, open a new Command Prompt and run `py -0p` and `where python` to confirm it is gone. Libraries installed for that Python are gone with it, and an environment made from it stops working: delete `cv_lab_venv` and run the setup file again.

To remove only a library, not Python:

```
python -m pip uninstall opencv-python
```

## 9. Errors and fixes

### 1. `ModuleNotFoundError: No module named 'cv2'`

OpenCV is not installed for the Python that ran the program. The name you import (`cv2`) and the name you install are different:

```
python -m pip install "opencv-python<5"
```

Keep the quotes. For `No module named 'numpy'`, install `numpy`. If pip answers "Requirement already satisfied" and the error stays, the PC has two Pythons and pip used the other one. See section 4.

### 2. `'python' is not recognized as an internal or external command`

Python is not installed, or it was installed without "Add python.exe to PATH". Try `py --version`. If that works, write `py` wherever this file says `python`. If neither works, install Python (section 7).

A related case: typing `python` opens the Microsoft Store, or prints "Python was not found; run without arguments to install from the Microsoft Store". Windows has a placeholder `python.exe` that does this. Use `py` instead, or turn the placeholder off in Settings, Apps, Advanced app settings, App execution aliases (switch off both "python.exe" and "python3.exe").

### 3. `Image not found!`

Often with a line above it: `can't open/read file: check file path/integrity`. Each program looks for `image.jpg` in its own folder, so the picture is not beside the program. The usual causes: the program was opened from inside the zip without extracting, one program was copied somewhere else on its own, or `image.jpg` was renamed. Keep the programs and `image.jpg` together.

### 4. `ERROR: Could not find a version that satisfies the requirement ...` and `ERROR: No matching distribution found for ...`

pip found no file of that library for this Python. Causes, most likely first: there is no internet (pip then prints several "Retrying" warnings before this error), the Python is too old (section 5), or the Python is 32-bit. Check with `python --version` and the 64/32 command in section 4.

### 5. `Could not install packages due to an OSError: [WinError 5] Access is denied`

Python was installed for all users and your login cannot write into its folder. Use the setup file, which installs into your own user folder, or add `--user`: `python -m pip install --user -r requirements.txt`.

### 6. pip stops with `ReadTimeoutError`, `ProxyError`, `SSLError` or `CERTIFICATE_VERIFY_FAILED`

The college network is slow or sends traffic through a proxy. Try in this order:

1. Run the same command (or the setup file) again. pip keeps what it already downloaded.
2. Give it more time: add `--timeout 100`.
3. Ask the lab staff for the proxy address and add `--proxy http://address:port`.
4. Use a phone hotspot for the install.

### 7. `cv2.error: ... The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support`

Appears at `cv2.imshow`. The PC has `opencv-python-headless`, a version of OpenCV with no windows. Replace it:

```
python -m pip uninstall opencv-python-headless
python -m pip install --force-reinstall "opencv-python<5"
```

### 8. The program seems frozen, or the picture window says "Not responding"

It is waiting for a key. Click a picture window and press any key. See section 6.

### 9. Double-clicking a program does nothing, or a black window flashes and disappears

Double-clicking runs the file with the Python launcher's default Python, which usually has no OpenCV until the setup file has run. The program then stops at once with error 1 and the window closes. Run `SETUP_LAB_PC.bat` first. If it has been run and a program still closes at once, follow "If double-click does not run the program" in section 3.

### 10. In IDLE: `ModuleNotFoundError: No module named 'cv2'`, although the setup file showed `OK`

This IDLE belongs to a different Python from the one the setup file prepared. It happens when IDLE is opened from the Start menu, or by right-click and "Edit with IDLE". Close it and open IDLE with `OPEN_IDLE.bat` (section 3, "Run the programs in IDLE").

## 10. What differs from the printed record

The code is the record's code. Each change is marked in the file with a comment `# CHANGED from the record:`.

| Program | Change |
|---|---|
| 1 to 5 | Two lines added near the top: `import os` and `os.chdir(os.path.dirname(os.path.abspath(__file__)))`. They make the program work inside its own folder, so `image.jpg` is found however the program is started (double-click, IDLE or Command Prompt). `__file__` is the program's own path, `dirname` takes the folder part, and `chdir` moves there |
| 1 to 5 | Picture name `bird.png` or `tree.jpg` became `image.jpg` |
| 1 | Got the "Image not found" check the others already had |

If you type a program from the record in the exam, the two `os` lines are not needed when you run it from IDLE with F5, because IDLE starts the program in its own folder. Only the picture name has to match the file that is there.

## 11. Versions used in the test

Python 3.12.8 (64-bit) on Windows 11, opencv-python 4.14.0.94, numpy 2.5.4.

`image.jpg` is the sample photo `zidane.jpg` from the Ultralytics YOLO repository, reduced to 960 x 540 so its windows fit on a small monitor.

The full set of 17 record programs, with TensorFlow, PyTorch and the rest, is a separate folder (`CV_Lab_Programs`). This folder is only the five exam programs.
