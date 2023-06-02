import csv
import hashlib
import sys
import os


def parse_csv(path_to_file):
    """
    Parse a CSV, skipping header, returns each row's contents as an array of arrays.

    *Example*
    Input CSV:
    "title1, title2, title3"
    "a,b,c"
    "1,2,3"

    Returns:
    [
        ["a", "b", "c"],
        ["1", "2", "3"]
    ]
    """

    # Initialize the result array
    out_array = []

    # First row flag. Used for CSV header detection
    first_row = True

    try:
        # Loop through the CSV file
        with open(path_to_file, encoding='utf-8-sig') as csv_file:
            read_out = csv.reader(csv_file)
            for row in read_out:
                # Handle if header row
                if first_row:
                    header = row
                    first_row = False
                else:
                    # To avoid problematic chars, replace them with an alternate
                    filtered_row = []
                    for item in row:
                        item = item.replace("\'", "ʹ")
                        item = item.replace("\"", "ʺ")
                        filtered_row.append(item)
                    out_array.append(filtered_row)
        return header, out_array
    except:
        return [], []


def show_help():
    """
    Show help with instructions on how to use the program
    """
    print("\n\n\n")
    print(f"Usage: {sys.argv[0]} <file1.csv> <file2.csv>")


def fingerprint(in_array, max_length=5):
    """
    Adds an additional element as a fingerprint.
    Fingerprint is generated via hash using existing data and can be truncated to a max length depending on need.

    *Example*
    Input:
    [
        ["a", "b", "c"],
        ["1", "2", "3"]
    ]

    Returns:
    [
        ["hexabcde", "a", "b", "c"],
        ["hex12345", "1", "2", "3"]
    ]
    """

    # The output array
    out_array = []

    # Loop through each row
    for row in in_array:
        # Convert the row into a single string
        single_string = " ".join(row)

        # Do a hash
        hash_object = hashlib.sha256()
        hash_object.update(single_string.encode("utf-8"))
        hashed_string = hash_object.hexdigest()

        # Add hash
        row.insert(0, hashed_string[:max_length])
        out_array.append(row)

    # Return the result
    return out_array


def run_me():
    """
    Takes in 2 input arguments of two CSVs.
    Compare the contents of the 2 CVSs
    returns a dict of the entries that overlaps both CSVs

    Note: Does not matter how many columns, this script dynamically adjusts
    """

    # [ERROR HANDLING] Check if expected inputs are there
    if not len(sys.argv) == 3:
        show_help()
        exit(0)

    # [ERROR HANDLING] Check if the input files exists
    if not os.path.exists(sys.argv[1]):
        print(f"File {sys.argv[1]} does not exist")
        exit(1)
    if not os.path.exists(sys.argv[2]):
        print(f"File {sys.argv[2]} does not exist")
        exit(1)

    # Parse the contents of the CSVs
    header1, input1_array = parse_csv(sys.argv[1])
    header2, input2_array = parse_csv(sys.argv[2])

    # [ERROR HANDLING] Check that the two CSV files have the same headers
    if not header1 == header2:
        print(f"Files {sys.argv[1]} and {sys.argv[2]} does not have the same headers! Can't compare.")
        exit(1)

    # Create a fingerprint of each user based on each line
    fingerprinted_input1_array = fingerprint(input1_array)
    fingerprinted_input2_array = fingerprint(input2_array)

    # Initialize the result output. Overlap dict
    overlap = {}

    # Compare the two fingerprinted arrays
    for item1 in fingerprinted_input1_array:
        for item2 in fingerprinted_input2_array:
            # If there is a match, add to the overlap list
            if item1[0] == item2[0]:
                # Initialize the entry
                overlap[item1[0]] = {}
                for i, element in enumerate(header1):
                    # Using item1[i] & header1[i] here, but it doesn't matter since item2[i] & header2[i] are the same
                    try:
                        overlap[item1[0]][header1[i]] = item1[i+1]
                    except:
                        # If there is a problem in the index due to bad columns in CSV, then skip
                        continue
    # Return result
    return overlap


""" ----------------------------------------------------------------------------------------------------------
UNIT TESTS
-----------------------------------------------------------------------------------------------------------"""

def test_parse_csv():
    # CSV "happy path"
    header, out_array = parse_csv(path_to_file="data/happy_path.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 0
    assert not len(out_array) == 0

    # CSV path not exist
    header, out_array = parse_csv(path_to_file="data/i-dont-exist.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert len(header) == 0
    assert len(out_array) == 0

    # CSV not proper format
    header, out_array = parse_csv(path_to_file="data/not-csv.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 0
    assert len(out_array) == 0

    # Empty path given
    header, out_array = parse_csv(path_to_file="")
    assert type(header) is list
    assert type(out_array) is list
    assert len(header) == 0
    assert len(out_array) == 0

    # CSV improperly formatted columns
    header, out_array = parse_csv(path_to_file="data/bad_columns.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 0
    assert not len(out_array) == 0

    # Really large CSV (1 million lines)
    header, out_array = parse_csv(path_to_file="data/large-csv.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 1
    assert not len(out_array) == 0

    # Non alphanumeric names
    header, out_array = parse_csv(path_to_file="data/non-alphanumeric.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 1
    assert not len(out_array) == 0

    # International names
    header, out_array = parse_csv(path_to_file="data/international-names.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 1
    assert not len(out_array) == 0

    # Valid but empty CSV
    header, out_array = parse_csv(path_to_file="data/empty.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 1
    assert len(out_array) == 0

    # Special characters in CSV
    header, out_array = parse_csv(path_to_file="data/special-characters.csv")
    assert type(header) is list
    assert type(out_array) is list
    assert not len(header) == 1
    assert not len(out_array) == 0

def test_fingerprint():

    # Sample good data
    good_array = [
        ["Sophia", "Smith", "28", "Hawaii"],
        ["Emma", "Nguyen", "57", "Kentucky"],
        ["Noah", "Williams", "82", "South Carolina"],
        ["Liam", "Brown", "42", "Tennessee"],
        ["Olivia", "Wong", "33", "Mississippi"],
        ["William", "Garcia", "68", "Maine"],
        ["Isabella", "Miller", "25", "California"],
        ["James", "Davis", "19", "Alabama"],
        ["Emily", "Kim", "72", "North Dakota"]
    ]

    # Normal "happy path"
    result = fingerprint(in_array=good_array)
    assert type(result) is list
    assert not len(result) == 0

    # Normal "happy path" generates the same hash
    result1 = fingerprint(in_array=[["test"]])
    result2 = fingerprint(in_array=[["test"]])
    assert type(result1) is list
    assert type(result2) is list
    assert not len(result1) == 0
    assert not len(result2) == 0
    assert result1 == result2

    # Normal "happy path" generates the same hash if data is same but different elements
    result1 = fingerprint(in_array=[["", "test"]])
    result2 = fingerprint(in_array=[["test", ""]])
    assert type(result1) is list
    assert type(result2) is list
    assert not len(result1) == 0
    assert not len(result2) == 0
    assert not result1 == result2

    # Empty array
    result = fingerprint(in_array=[])
    assert type(result) is list
    assert len(result) == 0

    # Empty 0 max length
    result = fingerprint(in_array=good_array, max_length=0)
    assert type(result) is list
    assert not len(result) == 0

    # Empty elements in array
    result = fingerprint(in_array=[["", "", ""]])
    assert type(result) is list
    assert not len(result) == 0

    # International values
    result = fingerprint(in_array=[
        ["李", "华", "28", "Hawaii"],
        ["山田", "花子", "57", "Kentucky"],
        ["지현", "박", "49", "Louisiana"]
    ])
    assert type(result) is list
    assert not len(result) == 0

    # Special characters
    result = fingerprint(in_array=[
        ["Mary-Jane", "Smith", "28", "Hawaii"],
        ["Emma", "O'Connor", "57", "Kentucky"],
        ["André", "Williams", "82", "South Carolina"],
    ])
    assert type(result) is list
    assert not len(result) == 0


"""
    Main entry point
"""
if __name__ == '__main__':
    """
    This script is for demo purposes. This is not scalable as it stands. In actual production, DBs would be used to make
    searching and finding much more efficient.
    """

    # Tests
    test_parse_csv()
    test_fingerprint()

    # Run program
    print(run_me())

