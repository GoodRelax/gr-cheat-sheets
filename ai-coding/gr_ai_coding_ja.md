# AIコーディングチートシート

## 呪文

- しついけ : 質問や意見があれば述べよ。
- さぎょか : 質問や意見があれば作業の前に述べて私の指示を待て。
- まだこ : まだコーティングするな。
- まだし : まだ仕様書を書くな。
- げんいた : 原因を究明し対策を提案せよ
- てんさ : 下記英文を添削し、添削後の英文/添削後の英文の和訳/添削個所の説明を出せ
- ぷろえ : 優秀かつ経験豊富な上級ソフトウェアエンジニアとして振る舞え
- こうきれ : KISS, YAGNI, DRY, SoC, SRP, OCP, LSP, ISP, DIP, SOLID, SLAP, LOD, CQS, POLA, PIE, CA, Naming, matters

## SW原則

| 用語           | 展開形                                | 意味                           |
| -------------- | ------------------------------------- | ------------------------------ |
| KISS           | Keep It Simple, Stupid                | 動作する最も単純な解決を選ぶ   |
| YAGNI          | You Aren’t Gonna Need It              | 必要になるまで機能を実装しない |
| DRY            | Don’t Repeat Yourself                 | 重複を避ける                   |
| SoC            | Separation of Concerns                | 関心ごとを分離する             |
| SRP            | Single Responsibility Principle       | 単一責任を守る                 |
| OCP            | Open/Closed Principle                 | 拡張に開き修正に閉じる         |
| LSP            | Liskov Substitution Principle         | 派生型は基底型と置換可能       |
| ISP            | Interface Segregation Principle       | 小さなインターフェースに分割   |
| DIP            | Dependency Inversion Principle        | 抽象に依存し具象に依存しない   |
| SOLID          | SRP, OCP, LSP, ISP, DIP               | オブジェクト指向設計の5原則    |
| SLAP           | Single Level of Abstraction Principle | 抽象度レベルを混在させない     |
| LOD            | Law of Demeter                        | 直接の協力者とのみやり取りする |
| CQS            | Command Query Separation              | 状態変更と取得を分離する       |
| POLA           | Principle of Least Astonishment       | 驚きを最小にする設計           |
| PIE            | Program Intently and Expressively     | 意図が明確に伝わるコードを書く |
| CA             | Clean Architecture                    | ユースケース中心の構造化       |
| Naming matters | Naming matters                        | 良い命名は理解性を高める       |

## 啓発

頭が古い昭和平成のエンジニアを2026年最新仕様にアップデートしたい。
近年のソフト開発の進化についてA4で20枚程度の情報量でレポートし、以下の書式で出力せよ。

## Output Format

- Output the entire content **as a single Markdown code block** so it can be copied in one go.
- **Enclose the entire Markdown with six backticks ` `````` ` at the beginning and end.** Specify its language as markdown.
- **Use these six backticks only once as the outermost enclosure.**
- **Never output speculation or fabrications.** If something is unclear or requires investigation, explicitly state so.
- This method is called **MCBSMD** (Multiple Code Blocks in a Single Markdown)

### Code and Diagram Block Rules

- As a rule, use Mermaid for diagrams. Use PlantUML only when the diagram cannot be expressed in Mermaid.
- Any diagrams or software code inside the Markdown must each be enclosed in their own code blocks using triple backticks ` ``` `.
- Each code block must specify a language or file type (e.g., ` ```python ` or ` ```mermaid `).
- Each code or diagram block must be preceded by a descriptive title in the format **title:**
  (e.g., `**System Architecture:**`, `**Login Flow:**`)
- Always follow the structure below for every code or diagram block:

  > **title:**
  >
  > ```language
  > (code or diagram content here without truncation or abbreviation)
  > ```
  >
  > Write the explanation for the code block here, immediately after the block, following a blank line.

- Do not write explanations inside the code blocks.
- In all diagrams, use only alphanumeric characters and underscores `_`. Do not use any other characters, as they can cause rendering errors.
- Output all diagram content without omission. Never use `...` or any shorthand.

### Diagram Label and Notation Rules

- All arrows and relationship lines in diagrams MUST have labels. Follow these notation rules:
  1. Mermaid `flowchart` and `graph`: place the label inside the arrow using pipes (e.g., `A -->|Label| B`)
  2. Other Mermaid diagrams / All PlantUML: place the label after the arrow using a colon (e.g., `A --> B : Label`)
- For line breaks in labels or node text:
  1. Mermaid: use `<br/>` inside a quoted string (e.g., `A -->|"Line1<br/>Line2"| B`, `A["Line1<br/>Line2"]`)
  2. PlantUML: use `\n` (e.g., `A -> B : Line1\nLine2`)

### Math Rules

- Use standard LaTeX notation for all mathematical formulas.
  1. Inline math: always use single dollar signs. Place a space before the opening `$`
     and a space after the closing `$`
     (e.g., `The function is $y = x + 1$ here.`)
  2. Block equations: always place `$$` on its own line, above and below the formula.
     Example:
     > $$
     > E = mc^2
     > $$


<p align="right">(c)2026 GoodRelax. MIT License.</p>
