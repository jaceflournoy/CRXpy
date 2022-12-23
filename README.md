# CRXpy

CRXpy is a script that automates the process of submitting Chrome browser extensions to the [CRXcavator](https://crxcavator.io/) API for analysis. It reads in a list of extension IDs from a text file, and then iterates through the list, submitting each extension ID to the API and writing the results of the analysis to an output file.

## Requirements

- Python 3.x
- The following Python libraries:
  - `requests`
  - `json`
  - `time`
  - `io`
  - `urllib3`
  - `tkinter`

## Usage

To use CRXpy, you'll need an API key from [CRXcavator](https://crxcavator.io/user/settings). This is optional, but it allows you to submit more extensions for analysis.

1. Install the required libraries:

```pip install requests json time io urllib3 tkinter```

2. Clone or download this repository:

```git clone https://github.com/jaceflournoy/CRXpy.git```

3. Navigate to the directory containing the script:

```cd CRXpy```

4. Run the script:

```python crxpy.py```

When the script starts, it will prompt you to input your API key (if you have one), and then it will open a dialog window that allows you to select the text file containing the extension ID list. The script will then read in the extension IDs from the file, one per line, and submit them to the CRXcavator API for analysis. The results of the analysis will be written to an output file called output.txt.

# Limitations

The CRXcavator API has rate limits that may prevent you from submitting a large number of extensions at once.
The script may not work as expected if the CRXcavator API changes its structure or behavior.


# Credits

CRXpy was developed by Jace Flournoy and Arturo Magdaleno. It is available on GitHub at https://github.com/jaceflournoy/CRXpy.
