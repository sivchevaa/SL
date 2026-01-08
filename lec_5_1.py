from pathlib import Path

files = ['accounts.txt', 'details.csv', 'invite.docx']
doc_path = Path('/Users/Ani/Documents/lecture_files_sl')

for file_name in files:
    file_path = doc_path / file_name
    file_path.write_text(f'Hello {file_name}')