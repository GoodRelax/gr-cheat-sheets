import re, sys

fonts_dir = 'C:/Users/good_/OneDrive/Documents/GitHub/gr-cheat-sheets/confucius/fonts'
with open(f'{fonts_dir}/kaisho.b64', 'r') as f:
    kaisho_b64 = f.read()
# Gyousho removed - using Kaisho for both kanbun and kundoku

import json

# Read TSV and generate DATA
tsv_path = 'C:/Users/good_/OneDrive/Documents/GitHub/gr-cheat-sheets/confucius/confucius.tsv'
# Try new file first (if original is locked by OneDrive)
alt_path = tsv_path.replace('.tsv', '_new.tsv')
import os
if os.path.exists(alt_path):
    tsv_path = alt_path

with open(tsv_path, 'rb') as f:
    tsv_data = f.read()
tsv_text = tsv_data.decode('shift_jis', errors='replace')

entries = []
for line in tsv_text.split('\r\n')[2:]:
    if not line.strip():
        continue
    fields = line.split('\t')
    if len(fields) >= 7:
        try:
            no = int(fields[0])
            entries.append({
                'no': no, 'category': fields[1], 'source': fields[2],
                'kanbun': fields[3], 'kundoku': fields[4],
                'hitokoto': fields[5], 'kaisetsu': fields[6],
            })
        except ValueError:
            pass

data_block = 'const DATA = ' + json.dumps(entries, ensure_ascii=False, indent=2) + ';'

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>エンジニアに贈る論語28選</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<style>
@font-face {{
  font-family: 'Kaisho';
  src: url(data:font/woff2;base64,{kaisho_b64}) format('woff2');
  font-display: swap;
}}
/* Gyousho removed - Kaisho used for all brush text */

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: 'Noto Sans JP', sans-serif;
  color: #2a2a2a;
  min-height: 100vh;
  background-color: #f5f0e6;
  background-image:
    radial-gradient(ellipse at 20% 50%, rgba(139,119,90,0.04) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(139,119,90,0.03) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 80%, rgba(160,140,100,0.04) 0%, transparent 50%),
    radial-gradient(circle at 30% 30%, rgba(180,160,120,0.06) 0%, transparent 30%),
    radial-gradient(circle at 70% 70%, rgba(180,160,120,0.05) 0%, transparent 25%),
    repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(139,119,90,0.012) 2px, rgba(139,119,90,0.012) 3px),
    repeating-linear-gradient(90deg, transparent, transparent 3px, rgba(139,119,90,0.008) 3px, rgba(139,119,90,0.008) 4px);
}}

/* ===== HEADER BAR ===== */
.header-bar {{
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 900px;
  margin: 0 auto;
  padding: 0.8rem 1rem;
  background-color: #f5f0e6;
  border-bottom: 1px solid rgba(139,119,90,0.2);
}}
.header-bar h1 {{
  font-family: 'Kaisho', serif;
  font-size: 1.15rem;
  letter-spacing: 0.1em;
  color: #2a2a2a;
  white-space: nowrap;
}}
.nav {{
  display: flex;
  align-items: center;
  gap: 0.8rem;
}}
.nav-btn {{
  background: none;
  border: 1px solid #b8a88a;
  color: #6a5a4a;
  font-size: 1rem;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.nav-btn:hover {{ background: rgba(196,62,42,0.08); border-color: #c43e2a; color: #c43e2a; }}
.nav-info {{
  font-size: 0.85rem;
  color: #8a7a6a;
  text-align: center;
  min-width: 5rem;
}}

/* ===== MAIN DISPLAY ===== */
.display {{
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1rem;
}}

/* Vertical text area */
.tategaki-area {{
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 2rem;
  padding: 1.5rem 1rem;
  height: max(280px, calc(100vh - 310px));
  border-top: 1px solid rgba(139,119,90,0.2);
  border-bottom: 1px solid rgba(139,119,90,0.2);
  overflow: hidden;
}}

.tategaki-col {{
  writing-mode: vertical-rl;
  text-orientation: mixed;
  white-space: pre-line;
  line-height: 2;
  max-height: 100%;
}}

.source-col {{
  font-family: 'Kaisho', serif;
  font-size: 0.8rem;
  color: #a09080;
  letter-spacing: 0.1em;
  order: 3;
  line-height: 1.8;
}}

.kanbun-col {{
  font-family: 'Kaisho', serif;
  font-size: 2rem;
  color: #1a1a1a;
  text-shadow:
    0.5px 0.5px 0px rgba(0,0,0,0.2),
    -0.3px 0px 1px rgba(0,0,0,0.06);
  letter-spacing: 0.08em;
  order: 2;
}}

.kundoku-col {{
  font-family: 'Kaisho', serif;
  font-size: 1.35rem;
  color: #3a3a3a;
  letter-spacing: 0.03em;
  line-height: 1.9;
  order: 1;
  -webkit-text-stroke: 0.4px #3a3a3a;
}}

/* Buttons inline with text */
.btn-area {{
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem 0;
}}
.btn-row {{
  display: flex;
  align-items: flex-start;
  gap: 0.8rem;
}}
.toggle-btn {{
  font-family: 'Noto Sans JP', sans-serif;
  font-weight: 500;
  font-size: 0.8rem;
  background: transparent;
  border: 1.5px solid #c43e2a;
  color: #c43e2a;
  padding: 0.3rem 0.9rem;
  border-radius: 1.5rem;
  cursor: pointer;
  transition: all 0.25s;
  white-space: nowrap;
  flex-shrink: 0;
}}
.toggle-btn:hover {{ background: rgba(196,62,42,0.06); }}
.toggle-btn.active {{ background: #c43e2a; color: #fff; }}

.reveal-text {{
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.4s ease, opacity 0.3s ease;
  line-height: 1.7;
}}
.reveal-text.show {{
  max-height: 300px;
  opacity: 1;
}}
.hitokoto-text {{
  font-family: 'Noto Sans JP', sans-serif;
  font-weight: 700;
  font-size: 1.05rem;
  color: #c43e2a;
}}
.kaisetsu-text {{
  font-size: 0.9rem;
  color: #4a4a4a;
  line-height: 1.8;
}}

/* ===== TABLE ===== */
.list-section {{
  max-width: 900px;
  margin: 1.5rem auto 3rem;
  padding: 0 1rem;
}}
.list-section h2 {{
  font-family: 'Noto Sans JP', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  color: #8a7a6a;
  margin-bottom: 0.8rem;
  padding-left: 0.3rem;
}}

.list-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}}
.list-table thead th {{
  background: rgba(139,119,90,0.12);
  padding: 0.5rem 0.6rem;
  text-align: left;
  font-weight: 500;
  color: #6a5a4a;
  border-bottom: 2px solid rgba(139,119,90,0.25);
  white-space: nowrap;
}}
.list-table tbody tr {{
  cursor: pointer;
  transition: background 0.15s;
  border-bottom: 1px solid rgba(139,119,90,0.1);
}}
.list-table tbody tr:hover {{ background: rgba(196,62,42,0.05); }}
.list-table tbody tr.selected {{
  background: rgba(196,62,42,0.1);
  border-left: 3px solid #c43e2a;
}}
.list-table td {{
  padding: 0.55rem 0.6rem;
  vertical-align: top;
}}
.list-table .col-no {{ width: 2.5rem; text-align: center; color: #8a7a6a; }}
.list-table .col-cat {{ width: 3.5rem; }}
.list-table .col-src {{ width: 6rem; font-size: 0.82rem; }}
.list-table .col-kanbun {{ }}
.list-table .col-kundoku {{ font-size: 0.85rem; color: #5a5a5a; }}

.cat-badge {{
  display: inline-block;
  font-size: 0.72rem;
  padding: 0.1rem 0.45rem;
  border-radius: 0.8rem;
  font-weight: 500;
}}
.cat-manabi {{ background: rgba(59,130,246,0.12); color: #2563eb; }}
.cat-shisei {{ background: rgba(196,62,42,0.1); color: #c43e2a; }}

/* ===== RESPONSIVE ===== */
@media (max-width: 600px) {{
  .header-bar {{ flex-direction: column; gap: 0.5rem; align-items: center; }}
  .header-bar h1 {{ font-size: 1rem; }}
  .tategaki-area {{ gap: 1rem; min-height: 180px; padding: 1.2rem 0.5rem; }}
  .kanbun-col {{ font-size: 1.5rem; }}
  .kundoku-col {{ font-size: 1.05rem; }}
  .source-col {{ font-size: 0.7rem; }}
  .list-table {{ font-size: 0.78rem; }}
  .list-table .col-kundoku {{ display: none; }}
  .hitokoto-text {{ font-size: 1rem; }}
  .btn-row {{ flex-direction: column; }}
}}
</style>
</head>
<body>

<header class="header-bar">
  <h1>エンジニアに贈る論語28選</h1>
  <div class="nav">
    <button class="nav-btn" id="prevBtn" aria-label="前へ">&larr;</button>
    <div class="nav-info" id="navLabel">No.1 / 28</div>
    <button class="nav-btn" id="nextBtn" aria-label="次へ">&rarr;</button>
  </div>
</header>

<section class="display">
  <div class="tategaki-area">
    <div class="tategaki-col kundoku-col" id="kundokuDisplay"></div>
    <div class="tategaki-col kanbun-col" id="kanbunDisplay"></div>
    <div class="tategaki-col source-col" id="sourceDisplay"></div>
  </div>

  <div class="btn-area">
    <div class="btn-row">
      <button class="toggle-btn" id="hitokotoBtn">一言</button>
      <div class="reveal-text" id="hitokotoReveal">
        <div class="hitokoto-text" id="hitokotoText"></div>
      </div>
    </div>
    <div class="btn-row">
      <button class="toggle-btn" id="kaisetsuBtn">解説</button>
      <div class="reveal-text" id="kaisetsuReveal">
        <div class="kaisetsu-text" id="kaisetsuText"></div>
      </div>
    </div>
  </div>
</section>

<section class="list-section">
  <h2>一覧</h2>
  <table class="list-table">
    <thead>
      <tr>
        <th class="col-no">No.</th>
        <th class="col-cat">分類</th>
        <th class="col-src">出典</th>
        <th class="col-kanbun">漢文</th>
        <th class="col-kundoku">書き下し文</th>
      </tr>
    </thead>
    <tbody id="listBody"></tbody>
  </table>
</section>

<script>
{data_block}

let currentIndex = 0;
const _q = (s) => document.querySelector(s);
const _qa = (s) => document.querySelectorAll(s);

function showEntry(idx) {{
  currentIndex = idx;
  const d = DATA[idx];
  _q('#navLabel').textContent = 'No.' + d.no + ' / ' + DATA.length;
  _q('#sourceDisplay').textContent = d.source;
  _q('#kanbunDisplay').textContent = d.kanbun.replace(/ {{2,}}/g, '\\n');
  _q('#kundokuDisplay').textContent = d.kundoku.replace(/[\\u3000]{{2,}}| {{2,}}/g, '\\n');
  _q('#hitokotoText').textContent = d.hitokoto;
  _q('#kaisetsuText').textContent = d.kaisetsu;
  _q('#hitokotoReveal').classList.remove('show');
  _q('#kaisetsuReveal').classList.remove('show');
  _q('#hitokotoBtn').classList.remove('active');
  _q('#kaisetsuBtn').classList.remove('active');
  _qa('#listBody tr').forEach((tr, i) => tr.classList.toggle('selected', i === idx));
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function buildTable() {{
  const tbody = _q('#listBody');
  DATA.forEach((d, i) => {{
    const tr = document.createElement('tr');
    const cc = d.category === '学び' ? 'cat-manabi' : 'cat-shisei';
    tr.innerHTML = '<td class="col-no">' + d.no + '</td>'
      + '<td class="col-cat"><span class="cat-badge ' + cc + '">' + d.category + '</span></td>'
      + '<td class="col-src">' + d.source + '</td>'
      + '<td class="col-kanbun">' + d.kanbun.replace(/ {{2,}}/g, ' ') + '</td>'
      + '<td class="col-kundoku">' + d.kundoku.replace(/[\\u3000]{{2,}}| {{2,}}/g, ' ') + '</td>';
    tr.addEventListener('click', () => showEntry(i));
    tbody.appendChild(tr);
  }});
}}

_q('#hitokotoBtn').addEventListener('click', () => {{
  _q('#hitokotoReveal').classList.toggle('show');
  _q('#hitokotoBtn').classList.toggle('active');
}});
_q('#kaisetsuBtn').addEventListener('click', () => {{
  _q('#kaisetsuReveal').classList.toggle('show');
  _q('#kaisetsuBtn').classList.toggle('active');
}});
_q('#prevBtn').addEventListener('click', () => showEntry((currentIndex - 1 + DATA.length) % DATA.length));
_q('#nextBtn').addEventListener('click', () => showEntry((currentIndex + 1) % DATA.length));
document.addEventListener('keydown', (e) => {{
  if (e.key === 'ArrowLeft') showEntry((currentIndex - 1 + DATA.length) % DATA.length);
  if (e.key === 'ArrowRight') showEntry((currentIndex + 1) % DATA.length);
}});

buildTable();
showEntry(0);
</script>
</body>
</html>"""

with open('C:/Users/good_/OneDrive/Documents/GitHub/gr-cheat-sheets/confucius/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Written {len(html)} bytes ({len(html)//1024}KB)')
