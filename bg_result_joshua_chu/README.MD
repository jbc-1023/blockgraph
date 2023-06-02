<h1>Option 1: Usage via Python</h1>
<code>python get_overlap.py [path-to-file1] [path-to-file2]</code>

Requirements:
<ul>
    <li>Python 3 installed (No additional/external libraries needed)</li>
    <li>Two CSV files are required</li>
    <li>Both CSV files need to have matching headers (columns)</li>
</ul>

<h1>Option 2: Usage via Docker</h1>
<code>docker build blockgraph:demo</code>
<br>
<code>docker run blockgraph:demo</code>
<br>
<br>
Requirements:

<ul>
    <li>Docker</li>
</ul>

<h1>Description</h1>

How it works:
<ol>
    <li>Programs runs internal tests first.</li>
    <li>User enters 2 CSV files as inputs. If on Docker, the two demo CSVs will be used.</li>
    <li>Checks if CSVs exists.</li>
    <li>Checks if both CSVs have same header.</li>
    <li>Generates a unique hash as fingerprint id for each line item.</li>
    <li>Loop through all line items of both CSVs and compare the fingerprints.</li>
    <li>Output all line items that has fingerprint that exists on both CSVs as dict in console.</li>
</ol>

<h1>Embeded unit tests</h1>
<ul>
    <li>test_parse_csv()</li>
    <ul>
        <li>"Happy path" aka normal path</li>
        <li>CSV not exist</li>
        <li>CSV Not proper format <i>(I know it's called out to not need checking but I put it in anyway because it didn't feel right to leave it out)</i></li>
        <li>No CSV path given</li>
        <li>Read CSV with large number of lines (1 million)</li>
        <li>CSV with values that's not alphanumeric (international)</li>
        <li>CSV with values that's special characters</li>
    </ul>
    <li>fingerprint()</li>
    <ul>
        <li>"Happy path" aka normal path</li>
        <li>Two same entries results in same fingerprint</li>
        <li>Two same entries but in different columns result in different fingerprint</i></li>
        <li>Empty</li>
        <li>Zero fingerprint max length given</li>
        <li></li>
        <li>Valid array given for fingerprinting but all values are empty</li>
        <li>Array with values that's not alphanumeric (international)</li>
        <li>Array with values that's special characters</li>
    </ul>
    
</ul>

<h1>E2E tests</h1>
This is different than the embedded tests. Embedded tests runs against the internal functions (unit tests) while these
tests run from the perspective of the end user (or customer)

To run the E2E tests <code>python E2E_tests.py</code>
<ul>
    <li>"Happy path" outputs a valid json</li>
    <li>Input CSV not exist</li>
    <li>No input</li>
    <li>Incorrect amount of input</li>
    <li>Bad columns in CSV</li>
    <li>Empty in CSV</li>
    <li>International names in CSV</li>
    <li>Large CSV (1 million lines)</li>
    <li>Non Alphanumeric in CSV. Test limitation, output has single quotes and cannot be used for comparison for dict json</li>
    <li>Not a CSV</li>
    <li>Special characters in CSV</li>
    <li>Unmatched titles CSV</li>
</ul>

<h1>Notes</h1>
<ul>
    <li><code>test_data_generator.py</code> was used to generate the <code>large-csv.csv</code> testdata file. Limited random First and Last names are chosen intentionally so that there's higher chance of overlaps for further tests if needed.</li>
    <li>Developed in PyCharm so <code>.idea</code> folder is included</li>
</ul>

