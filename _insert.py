import sys, re
sys.stdout.reconfigure(encoding='utf-8')
path = sys.argv[1]           # e.g. pages/manual-git.html
capfile = sys.argv[2]        # e.g. cap01.html
E = int(sys.argv[3])         # expected chapter count after insert
final = len(sys.argv) > 4 and sys.argv[4] == 'final'  # remove marker
c = open(path, encoding='utf-8').read()
cap = open(capfile, encoding='utf-8').read().rstrip('\n')
marker = '<!-- CHAPTERS_INSERT_HERE -->'
assert c.count(marker) == 1, f'marker count before = {c.count(marker)}'
if final:
    c = c.replace(marker, cap)
else:
    c = c.replace(marker, cap + '\n\n' + marker)
open(path, 'w', encoding='utf-8', newline='').write(c)

# ---- validation ----
mc = c.count(marker)
sc = c.count('<section class="chapter"')
assert mc == (0 if final else 1), f'marker={mc}'
assert sc == E, f'sections={sc} expected {E}'
for tag in ['section','pre','code','div','span']:
    o = len(re.findall(rf'<{tag}[\s>]', c)); cl = c.count(f'</{tag}>')
    assert o == cl, f'{tag}: {o}/{cl}'
for t in ['<pre">','<code">','<span">','<div">']:
    assert c.count(t) == 0, t
for de in ['&amp;gt;','&amp;lt;','&amp;amp;']:
    assert c.count(de) == 0, de
issues = []
for m in re.finditer(r'<pre><code>(.*?)</code></pre>', c, re.DOTALL):
    s = re.sub(r'<span class="[^"]+">', '', m.group(1)).replace('</span>', '')
    s = s.replace('&lt;','\x00').replace('&gt;','\x01').replace('&amp;','\x02').replace('&quot;','\x03')
    for ch in ['<','>']:
        if ch in s:
            i = s.index(ch); issues.append((ch, s[max(0,i-25):i+25]))
assert len(issues) == 0, issues
raw = sum(len(re.findall(r'=>', m.group(1))) for m in re.finditer(r'<pre><code>(.*?)</code></pre>', c, re.DOTALL))
assert raw == 0, f'raw arrows={raw}'
print(f'OK {sc} capitulos, marker={mc}, size={round(len(c)/1024)}KB')
