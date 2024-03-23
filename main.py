import sys
import os

if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    print(f"::error file={file_name}::")

    raise ValueError("Error with value error")
    # print("Error message mereketengue")
    # sys.exit(1)
    # print("Hola")
