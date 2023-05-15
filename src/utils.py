def print_loading(text):
    BLUE_BG = "\033[44m"
    BLACK = "\033[30m"
    RESET = "\033[0m"
    print(f"{BLUE_BG}{BLACK} LOADING {RESET} {text}\n", flush=True)

def print_pass(text):
    GREEN_BG = "\033[42m"
    BLACK = "\033[30m"
    RESET = "\033[0m"
    print(f"{GREEN_BG}{BLACK} PASS {RESET} {text}\n", flush=True)

def print_fail(text):
    RED_BG = "\033[101m" 
    BLACK = "\033[30m"
    RESET = "\033[0m"
    print(f"{RED_BG}{BLACK} FAIL {RESET} {text}\n", flush=True)

def print_warning(text):
    YELLOW_BG = "\033[43m"
    BLACK = "\033[30m"
    RESET = "\033[0m"
    print(f"{YELLOW_BG}{BLACK} WARNING {RESET} {text}\n", flush=True)