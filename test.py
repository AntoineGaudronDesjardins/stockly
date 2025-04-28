import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", type=int, default=1)
args = parser.parse_args()

with open(f"tests/input{args.test}.txt", "r") as input_file, \
     open(f"tests/output{args.test}.txt", "r") as output_file:
    inputs = input_file.readlines()
    result = output_file.readlines()

process = subprocess.Popen(
    [sys.executable, "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

stdout, stderr = process.communicate(input="".join(inputs))

with open("tests/actual_output.txt", "w") as actual_output_file:
    actual_output_file.write(stdout)

print(stdout)
print(stderr)