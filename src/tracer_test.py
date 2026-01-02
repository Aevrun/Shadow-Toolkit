import sys


def program(input: str) -> None:
    if "bug" in input:
        raise ValueError("Crash found!")
    return

def trace_it(frame,event, arg):
    if event == 'line':
        print(f"Executed Line: {frame.f_lineno}")
    return trace_it


sys.settrace(trace_it)

program("bug")

sys.settrace(None)