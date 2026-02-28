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
- **Enclose the entire Markdown with six backticks ` `````` ` at the beginning and end to prevent Markdown splitting.** Specify its language as markdown.
- **Use the six backticks only once as the outermost enclosure.**
- Any UML diagrams or software code inside the Markdown must each be enclosed in their own code blocks using three backticks ` ``` `.
  This creates a structure where multiple three backticks blocks are nested inside the outer six backticks block to prevent Markdown splitting.
- Precede each code/UML block with a descriptive [Title Name]: and a blank line.
- Prefix each inner code block with a language or file type, for example: ` ```python `
- As a rule, use Mermaid for UML diagrams. Use PlantUML only when Mermaid cannot represent the diagram.
- Use only alphanumeric characters and underscores `_` in UML.
- Write explanations only outside UML blocks, and placed immediately after the corresponding UML but within the Markdown.
- Output all required UML contents completely, without omission.
- Never truncate or abbreviate code or UML content using `...` or similar shortcuts.
- All arrows and relationship lines in UML diagrams (including dashed lines and bidirectional links) must have labels, and the following notation rules must be strictly followed:
  1. For Mermaid `flowchart` and `graph`: include the label inside the arrow definition using pipes
     (example: `A -->|Label| B`)
  2. For all other Mermaid diagrams and all PlantUML diagrams: include the label at the end using a colon
     (example: `A --> B : Label`)
- For line breaks within labels or node text:
  - Mermaid: use `<br/>` inside a quoted string (example: `A -->|"Line1<br/>Line2"| B` or `A["Line1<br/>Line2"]`)
  - PlantUML: use `\n` (example: `A -> B : Line1\nLine2`)
- Use standard LaTeX notation for mathematical formulas.
- Always enclose inline math in single dollar signs `$` (e.g., `$E=mc^2$`) and display math (block equations) in double signs `$$`.
- **Never output speculation or fabrications.** If something is unclear or requires investigation, explicitly state so.
- This method is called **MCBSMD** (Multiple Code Block in Single MarkDown).


<p align="right">(c)2026 GoodRelax. MIT License.</p>
