import json
import subprocess

def run_os_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

# Happy path
output, error = run_os_command("python get_overlap.py data/Store1.csv data/Store2.csv")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Happy path")

# File not exist
not_exist = "data/i-dont-exist.csv"
output, error = run_os_command(f"python get_overlap.py {not_exist} {not_exist}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
assert f"File {not_exist} does not exist" in output.decode('utf-8'), "[FAIL][E2E] Expected message is not displayed"
print("[PASS][E2E] File not exist")

# No input
output, error = run_os_command("python get_overlap.py")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
assert "Usage" in output.decode('utf-8'), "[FAIL][E2E] Expected message is not displayed"
print("[PASS][E2E] No input")

# Wrong number of input
output, error = run_os_command("python get_overlap.py data/Store1.csv")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
assert "Usage" in output.decode('utf-8'), "[FAIL][E2E] Expected message is not displayed"
print("[PASS][E2E] Wrong number of input (too little)")

# Wrong number of input
output, error = run_os_command("python get_overlap.py data/Store1.csv data/Store1.csv data/Store1.csv")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
assert "Usage" in output.decode('utf-8'), "[FAIL][E2E] Expected message is not displayed"
print("[PASS][E2E] Wrong number of input (too many)")

# Bad columns in input file
file_given = "data/bad_columns.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Bad columns in CSV")

# Empty
file_given = "data/empty.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Empty CSV")

# International names
file_given = "data/international-names.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] International names CSV")

# Large CSV
print("[WARNING][E2E] Large CSV test. This could take up to 1 minute...")
large_file_given = "data/large-csv.csv"
happy_path_file = "data/happy_path.csv"
output, error = run_os_command(f"python get_overlap.py {large_file_given} {happy_path_file}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Large CSV")

# Non-Alphanumeric in CSV
file_given = "data/non-alphanumeric.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Non-alphanumeric CSV")

# Not CSV
file_given = "data/not-csv.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Not a CSV")

# Special characters in CSV
file_given = "data/special-characters.csv"
output, error = run_os_command(f"python get_overlap.py {file_given} {file_given}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
try:
    data = json.loads(output.decode('utf-8').replace("'", "\""))
    assert True
except:
    assert False, "[FAIL][E2E] Output is not a valid json"
print("[PASS][E2E] Special characters in CSV")

# Unmatched title
unmatched_csv_1 = "data/unmatched-title-1.csv"
unmatched_csv_2 = "data/unmatched-title-2.csv"
output, error = run_os_command(f"python get_overlap.py {unmatched_csv_1} {unmatched_csv_2}")
assert len(error) == 0, "[FAIL][E2E] There was error in the output"
assert not len(output) == 0, "[FAIL][E2E] There was an empty output"
assert "does not have the same headers" in output.decode('utf-8'), "[FAIL][E2E] Expected message is not displayed"
print("[PASS][E2E] Unmatched title in CSVs")
