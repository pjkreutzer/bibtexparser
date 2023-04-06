import argparse
import re

# Set up the argument parser
parser = argparse.ArgumentParser(description="Filter a BibTeX file to include only the entries cited in a Markdown file.")
parser.add_argument("markdown_file", help="the path to the Markdown file")
parser.add_argument("bibtex_file", help="the path to the BibTeX file")
parser.add_argument("-o", "--output", help="the path to the output file (default: filtered.bib)", default="filtered.bib")
args = parser.parse_args()

# Read the entire BibTeX file
with open(args.bibtex_file, "r") as f:
    bib_data = f.read()

# Get a list of all the BibTeX keys
all_keys = re.findall(r"@(\w+){([^,]+),", bib_data)

# Read the entire markdown file
with open(args.markdown_file, "r") as f:
    md_data = f.read()

# Get a list of all the citation keys in the markdown file
citation_keys = re.findall(r"@\w+\{\s*([^,\}]+)", md_data)

# Filter the list of all keys to include only the ones used in the markdown file
filtered_keys = [key for key in all_keys if key[1] in citation_keys]

# Generate the filtered BibTeX file by concatenating the relevant BibTeX entries
filtered_bib = ""
for key in filtered_keys:
    entry_start = bib_data.find("@" + key[0] + "{" + key[1])
    entry_end = bib_data.find("}", entry_start) + 1
    filtered_bib += bib_data[entry_start:entry_end] + "\n"

# Write the filtered BibTeX file to a new file
with open(args.output, "w") as f:
    f.write(filtered_bib)

print("Filtered BibTeX file written to", args.output)
