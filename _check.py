import sys, re
sys.stdout.reconfigure(encoding='utf-8')
# Pré-checa um arquivo de capítulo: reporta < / > crus dentro de <pre><code>
# Uso: python _check.py capNN.html
f = sys.argv[1]
c = open(f, encoding='utf-8').read()
bad = []
for m in re.finditer(r'<pre><code>(.*?)</code></pre>', c, re.DOTALL):
    s = re.sub(r'<span class="[^"]+">', '', m.group(1)).replace('</span>', '')
    s = s.replace('&lt;', '\x00').replace('&gt;', '\x01').replace('&amp;', '\x02').replace('&quot;', '\x03')
    for ch in ['<', '>']:
        idx = 0
        while ch in s[idx:]:
            i = s.index(ch, idx)
            bad.append((ch, s[max(0, i-30):i+30]))
            idx = i + 1
if bad:
    print(f'CRU encontrado ({len(bad)}):')
    for ch, ctx in bad:
        print(f'  {ch!r}: ...{ctx}...')
    sys.exit(1)
print('OK: nenhum < / > cru em code')
