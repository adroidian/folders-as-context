from pathlib import Path
import re
import yaml

base = Path(__file__).resolve().parent
skill = base / 'skills/software-development/folders-as-context/SKILL.md'
content = skill.read_text()
assert content.startswith('---'), 'frontmatter must start at byte 0'
m = re.search(r'\n---\s*\n', content[3:])
assert m, 'missing closing frontmatter'
frontmatter = content[3:m.start()+3]
fm = yaml.safe_load(frontmatter)
assert isinstance(fm, dict), 'frontmatter must be a map'
assert fm.get('name') == 'folders-as-context'
assert 'description' in fm and len(fm['description']) <= 1024
assert len(content) <= 100000
terms = [
    'Zari', 'Pacmans', 'James', 'Unraid', 'Mercy', 'Vesper', 'Companion',
    '/home/aaron', '/Users/pacmans', 'TELEGRAM_BOT_TOKEN', 'DISCORD_BOT_TOKEN',
]
for term in terms:
    hits = []
    for p in base.rglob('*'):
        if '.git' in p.parts or not p.is_file() or p.name == 'validate_package.py':
            continue
        if term.lower() in p.read_text(errors='ignore').lower():
            hits.append(str(p.relative_to(base)))
    assert not hits, (term, hits)
print('validated frontmatter and private scan')
print('file_count', sum(1 for p in base.rglob('*') if p.is_file() and '.git' not in p.parts))
