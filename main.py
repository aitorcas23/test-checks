import subprocess
import sys

if __name__ == "__main__":
    subprocess.call(
        "echo '::error file=main.py,line=1,title=Where is this title?::Send error from python script'",
        shell=True,
    )
    raise ValueError("Error with value error")
    # print("Error message mereketengue")
    # sys.exit(1)
    # print("Hola")
