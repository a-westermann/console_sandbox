

def convert_to_block_quote(text_lines: [str]) -> [str]:
    new_text = []
    for line in text_lines:
        new_text.append('>' + line)
    return new_text


with open('text', 'r') as note:
    note_text = note.readlines()
    block_quote_text = convert_to_block_quote(note_text)
open('text', 'w').writelines(block_quote_text)
