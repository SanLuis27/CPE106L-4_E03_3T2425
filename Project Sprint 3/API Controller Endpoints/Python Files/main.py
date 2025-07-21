# main.py

import argparse
import sys

def run_gui():
    import tkinter as tk
    from login_ui import LoginApp

    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

def run_api():
    import uvicorn
    uvicorn.run("login_api:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RePlate Login System")
    parser.add_argument(
        "--mode",
        choices=["gui", "api"],
        default="gui",
        help="Choose whether to run the GUI or the API server"
    )
    args = parser.parse_args()

    if args.mode == "gui":
        run_gui()
    elif args.mode == "api":
        run_api()
    else:
        print("Invalid mode. Use --mode gui or --mode api.")
        sys.exit(1)
