# BibTeX Filter

BibTeX Filter is a Python command-line tool that filters a BibTeX file to include only the entries cited in a Markdown file. It scans through the Markdown file and finds the citation keys, then searches the BibTeX file for entries with those keys and writes them to a new file.

## Usage

To use BibTeX Filter, you must have Python 3 installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

1. Clone this repository or download the script file (`filter_bib.py`) to your computer.

2. Open a command prompt or terminal window and navigate to the directory where the script file is located.

3. Run the script by typing the following command:

    ```
    python filter_bib.py path/to/markdown/file.md path/to/bibtex/file.bib
    ```

    Replace `path/to/markdown/file.md` with the path to your Markdown file and `path/to/bibtex/file.bib` with the path to your BibTeX file.

4. The filtered BibTeX file will be written to a file named `filtered.bib` in the current directory. You can specify a different output file using the `-o` or `--output` option:

    ```
    python filter_bib.py path/to/markdown/file.md path/to/bibtex/file.bib -o path/to/filtered/bibtex/file.bib
    ``` 

    This command will output the filtered BibTeX file to a file named `file.bib` in the directory `path/to/filtered/bibtex/`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Warning

So far this is entirely untested.
