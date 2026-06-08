import readline

print(r"""
     ██╗ █████╗ ██╗██╗     
     ██║██╔══██╗██║██║     
     ██║███████║██║██║     
██   ██║██╔══██║██║██║     
╚█████╔╝██║  ██║██║███████╗
 ╚════╝ ╚═╝  ╚═╝╚═╝╚══════╝

PyJail initialized.
Unauthorized escape attempts will be punished.
""")

suspicious = __builtins__.__import__
del __builtins__.__import__

while True:
    try:
        cmd = input(" jail$ ")

        if not cmd:
            continue

        result = eval(cmd)

        if result is not None:
            print(result)

    except EOFError:
        print("\n[!] Connection terminated. You remain imprisoned.")
        exit()

    except Exception as e:
        print(f"[!] Error: {e}")