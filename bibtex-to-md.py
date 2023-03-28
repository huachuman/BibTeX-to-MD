import os
import re
import glob

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()
    fields = ['author', 'title', 'doi', 'journaltitle', 'note']
    pattern = re.compile(r'(' + '|'.join(fields) + r')\s*=')
    entry_pattern = re.compile(r'@\w+\{[^,]+,')
    entry_emojis = {'article': '📄', 'book': '📕'}
    output_lines = []
    for line in input_text.split('\n'):
        if entry_pattern.match(line.strip()):
            output_lines.append('```bibtex')
            citekey = line.split('{')[1].split(',')[0]
            entry_type = line.split('@')[1].split('{')[0]
            emoji = entry_emojis.get(entry_type, '')
            output_lines.append('@' + emoji + entry_type + '{' + citekey + ',')
        elif pattern.match(line.strip()) or line.strip() == '}':
            if line.strip().startswith('note'):
                output_lines.append('  note = {YES},')
            else:
                output_lines.append(line)
            if line.strip() == '}':
                output_lines.append('```')
                if not citekey.startswith('@'):
                    citekey = '@' + citekey
                output_lines.append(citekey)
                output_lines.append('')
    output_text = '\n'.join(output_lines)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_text)

input_directory = 'path/to/source/bibs'
output_directory = 'path/to/obsidian/output/folder'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for input_file in glob.glob(os.path.join(input_directory, '*.bib')):
    output_file = os.path.join(output_directory, os.path.basename(input_file).replace('.bib', '.bib.md'))
    process_file(input_file, output_file)
