import sys
import subprocess

if __name__ == "__main__":
    subprocess.run("echo '::error:: Intentional error'")
    sys.exit(1)
    # print("Hola")
