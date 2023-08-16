::Make a directory and change the path to it
mkdir c:\Download\Python
cd c:\Download\Python

::Download python to a directory
curl https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe --output "C:\Download\Python\Python.exe" 

::Install Python and set environment path
Python.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0  

::Download pip, change directory, install pip
curl https://bootstrap.pypa.io/get-pip.py -o C:\Download\Python\get-pip.py
:: Change directory if required to cd c:\Download\Python
python get-pip.py

::Install pytube, required by the code to be executed for download utility
pip install pytube