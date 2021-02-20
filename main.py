# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == "__main__":
    from aiohttp.web import run_app
    from aiodav.app import create_app

    app = create_app(root="/")
    run_app(app)
