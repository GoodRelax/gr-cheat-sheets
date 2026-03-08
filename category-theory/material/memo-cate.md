# 議論メモ

## AgentExecutor I/F定義（Appendix G スケルトン追記候補）

### 核心
ClaudeはFramework層。DIPによりANMSから見たら実装詳細に過ぎない。
ClaudeだろうとGPTだろうとGeminiだろうとANMSは知らない。

### I/F定義（最小限）
```python
class AgentExecutor(ABC):
    @abstractmethod
    def execute(
        self,
        subgraph: SubGraph,
        context_summary: str,  # サルわか圧縮済みのWhy
        role: str,             # エージェントのRole
    ) -> SubGraph:
        ...

    @abstractmethod
    def get_capability(self) -> Capability:
        # コンテキストウィンドウサイズ・ツール・モデル性能等
        ...
```

### ClaudeのAPIとの対応
| ANMSの概念 | Claudeの実装 |
| :--- | :--- |
| Role | System Prompt + SKILL.md |
| Capability | Tools定義（input_schema） |
| Context_Summary | System Promptの一部 |
| TaskDefinition | tool_useブロック（id + input） |
| SubGraph | コンテキストウィンドウに渡す内容 |

---

## SpecとTaskの分離 — ハーバードアーキテクチャ類比（Section 2 および Appendix G 補強）

### 核心
SpecグラフとTaskDefinitionは別物。同じバスに乗せない。

### ハーバードアーキテクチャとの対応
- Specグラフ = データメモリ（読み書き）
- TaskDefinition = 命令メモリ（実行）
- オーガナイザー = CPU（両方にアクセスできる唯一の存在）
- サブエージェント = データバス（SubGraph）しか持たない

### 含意
- オーガナイザーが高コストな理由：データバスと命令バスの両方を持つから（構造的必然）
- サブエージェントが低コストな理由：データバス（SubGraph）しか持たないから
- 5W1HはTaskDefinitionの構造体として管理し、SpecNodeのプロパティには追加しない
- 監査情報（5W1H等）はSpecグラフの外：Gitのコミットメッセージまたはサイドカーファイルで管理

### ノイマン型との違い
ノイマン型（Spec+Taskを同一構造）にするとデータと命令が干渉し、
スプリント毎の再編成時にSpecの汚染が起きる。
ハーバード型に分離することでSpecグラフの純粋性が保たれる。

---

## 準備フェーズの「静的」記述は不正確（Appendix G 要修正）

- Role定義・Capability選定はプロジェクト開始時に初期値を決めるが
- スプリント毎に動的に再編成される
- Agent_Config(n+1) = f(Sprint_Review(n), Graph_State(n))

### スプリントループは「認知→判断→操作」の3ステップ
- OODAではなく自動車運転モデルで十分
- 認知：Specグラフの現状＋レビュー観点チェック結果を読む（ObserveとOrientを畳み込む）
- 判断：技術的負債の芽・カバレッジの穴を特定し、次スプリントのタスク割りを決定
- 操作：エージェント編成を更新しサブエージェントを動かす
- OODAのOrientが独立している理由は「敵の行動予測（他者モデルの更新）」のためであり、ANMSには不要

---

## 忘却アルゴリズムの制約（big-anms-essay Section 5 追記候補）

### 核心
グラウンディング = f(自然言語)
f = Role × Context（掛け算。片方ゼロなら出力ゼロ）

### ANMSへの対応
- Role = エージェントのSTFB層での立ち位置
- Context = 上位層（Layer1・2）のノード群（なぜそれをやるのか）

### 忘却アルゴリズムへの含意
「最小コンテキストに削る」が原則だが、
**Contextの次元（上位層ノード）は忘却してはいけない**という制約が必要。

現状の論文（Section 5）では「忘却関手で最小化」とだけ書いてあり、
この制約が明示されていない。→ 追記が必要。

### 追記の方向
- 忘却の対象：タスク無関係な**同層・下位層**ノード
- 忘却してはいけないもの：**上位層のContext**（Layer1・2）
- 理由：「なんのためにやる仕事かわからんやつに、魂のこもった仕事はできない」
