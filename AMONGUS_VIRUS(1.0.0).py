import ctypes
import time

def show_windows_error():
    """
    Function to show a Windows 10-style error message using ctypes.
    """
    ctypes.windll.user32.MessageBoxW(
        None,
        "HAHAHHAHHAHAHAHHAHHAHAHAHHAAH UR FUCKED",
        "AMONGUS",
        0x10 | 0x0
    )

if __name__ == "__main__":
    while True:
        show_windows_error()
        time.sleep(1)
