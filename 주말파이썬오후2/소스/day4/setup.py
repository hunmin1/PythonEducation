#python컴파일 방법 
from distutils.core import setup
import py2exe

#http://www.dreamy.pe.kr/zbxe/CodeClip/15123

setup(
#windows = ["01.py"],
zipfile = None,
console = ["quiz03.py"],
)

#c:\python34\python.exe setup.py py2exe 