# BibTeX-to-MD

A versatile python script that converts and cleans BibTeX files, renaming them to `.bib.md` for embedding in Obsidian, and wrapping them in backticks for rendering with the Pretty-BibTeX plugin. You can use this to get access to your Zotero collections from within Obsidian. Just export your collection, select "keep updated", and save it in the script's input folder. I have a folder in my documents called "Bibliographies" for this purpose. Run the script whenever you want to sync your exported collections to Obsidian, or set it on a daily schedule using Windows' built-in Task Scheduler.

## Future Directions

- Eliminate reliance on PrettyBibTeX and create custom format styles
- Add UI for configuring options
- Create equivalent javascript plugin for Obsidian
- Convert a single .bib into many .bib.mds based on groups (i.e. zotero collections). This would allow for just pointing to your entire live-updated zotero library file and processing all the groups into individual .bib.md files.

## To do
- Finish fixing description/readme.
- Add notes on known bugs
- Explain integration use case with obsidian
- Explain usage with task scheduler/hotkeys/obsidian script launcher
- Develop UI for options/possible integration into Obsidian

## Features

- Converts BibTeX files to Markdown with `.bib.md` extension
- Adds emojis to entry types for better visualization (can be customized)
- Removes any field not matching those specified in the script 
   - (note: by default, only author, title, journaltitle, and doi are enabled. This can be modified simply by adding the field name where those are mentioned in the script.)
- If it includes notes, it will be replaced with "YES". 
   - note: Currently can't figure out how to clean notes but plan on fixing this and possibly making it collapsible. 
- Copies the citekey to the bottom and checks if the citekey has an @ symbol, if not, it will add one 
   - (for usage with Pandoc Reference List and other Obsidian plugins that identify citekeys in notes)

## Requirements

- Python 3.x

## Usage

1. download the python script (see releases)

2. Update the `input_directory` and `output_directory` variables in the script with the appropriate paths:

   ```python
   input_directory = 'path/to/source/bibs'
   output_directory = 'path/to/obsidian/output/folder'
   ```

3. Run the script 

   ```
   python bibtex-to-md.py
   ```
- (note: you could also launch it by selecting "Python" as the default system app for .py files):

4. The processed `.bib.md` files will be saved in the specified output directory.

## Example

Input BibTeX file:

```
@article{Doe.2021,
  author = {Doe, John},
  title = {A great paper},
  journaltitle = {Journal of Great Papers},
  date = {2016-05-03},
  pages = {5119--5124},
  doi = {10.1234/5678},
  note = {This is a note},
}
```

Output Markdown file:

````
```bibtex
@📄article{Doe.2021,
  author = {Doe, John},
  title = {A great paper},
  journaltitle = {Journal of Great Papers},
  doi = {10.1234/5678},
  note = {YES},
}
```
@Doe2021"
````


What it looks like in Obsidian:


![image](https://user-images.githubusercontent.com/125603964/228305512-e1dee90b-acb8-45fc-a4bf-583aae8baaaa.png)

## To modify this code for your purpose, you can:

1. Change the list of fields to include or exclude fields as needed.
2. Change the formatting of the output by editing the content of `output_lines` as required.
3. Add emojis to the library of entry types for items other than article and book. e.g. 🎓thesis 
