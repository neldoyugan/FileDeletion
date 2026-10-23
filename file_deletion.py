import os
from tkinter import Tk, filedialog, messagebox
from send2trash import send2trash


def normalize_windows_path(path):
    return os.path.abspath(os.path.normpath(path))


# Hide the main Tkinter window
root = Tk()
root.withdraw()

# Ask whether to delete a file or folder
delete_folder = messagebox.askyesno(
    "What do you want to delete?",
    "Click Yes for Folder\n"
    "Click No for File"
)

# Open File Explorer
if delete_folder:
    selected_path = filedialog.askdirectory(
        title="Select a folder to delete"
    )
else:
    selected_path = filedialog.askopenfilename(
        title="Select a file to delete"
    )

# Check if something was selected
if selected_path:
    selected_path = normalize_windows_path(selected_path)

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Move this to the Recycle Bin?\n\n{selected_path}"
    )

    if confirm:
        try:
            if not os.path.exists(selected_path):
                raise FileNotFoundError(
                    f"The selected file or folder no longer exists:\n{selected_path}"
                )

            # Move to Recycle Bin
            send2trash(selected_path)

            messagebox.showinfo(
                "Success",
                "The file or folder was moved to the Recycle Bin."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Unable to delete:\n\n{error}"
            )
    else:
        messagebox.showinfo(
            "Cancelled",
            "Deletion was cancelled."
        )
else:
    messagebox.showinfo(
        "No Selection",
        "No file or folder was selected."
    )

root.destroy()
