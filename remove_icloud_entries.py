import winreg
from contextlib import suppress
import itertools

def subkeys(path, hkey=winreg.HKEY_LOCAL_MACHINE, flags=0):
    with suppress(WindowsError), winreg.OpenKey(hkey, path, 0, winreg.KEY_READ|flags) as k:
        for i in itertools.count():
            yield winreg.EnumKey(k, i)

def subvalues(path,  hkey=winreg.HKEY_LOCAL_MACHINE, flags=0):
    with suppress(WindowsError), winreg.OpenKey(hkey, path, 0, winreg.KEY_READ|flags) as k:
        for i in itertools.count():
            yield winreg.EnumValue(k, i)

value_name = "System.IsPinnedToNamespaceTree"

roots = [
    "HKEY_CLASSES_ROOT\CLSID",
    "HKEY_CLASSES_ROOT\WOW6432Node\CLSID"
]

hkey = winreg.HKEY_CLASSES_ROOT
root_key = "CLSID"
for subkey in subkeys(path="CLSID", hkey=hkey):
    print(f"Key: {subkey}")
    for subvalue in subvalues(f"{root_key}\\{subkey}", hkey):
            print(f"Value: {subvalue}")
    print()
