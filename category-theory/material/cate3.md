### Appendix G 補足: 実装スケルトン（Python）

オーガナイザーとサブエージェントの主要インターフェースをPythonのシグネチャとして定義する。実装はDIPに従いGraphRepositoryをインターフェースとして抽象化する。AIへの実装指示はこのスケルトンをANMSのノードIDと5W1Hタグと合わせて渡すこと。

---

**title: Data_Structures**
```python
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class STFBLayer(Enum):
    FOUNDATION  = 1
    REQUIREMENT = 2
    COMPONENT   = 3
    SCENARIO    = 4
    TEST        = 5
    META        = 6

class EdgeDirection(Enum):
    FORWARD = "forward"  # 外側→内側（CA依存方向）
    TRACE   = "trace"    # 内側→外側（トレーサビリティ用途限定）
    META    = "meta"     # メタ層からの横断評価

@dataclass
class SpecNode:
    id: str                        # 例: "FR-001", "CMP-003"
    stfb_layer: STFBLayer
    content_ref: str               # MDビューへの参照パス
    tags_5w1h: dict[str, str]      # {"why": "...", "what": "...", ...}

@dataclass
class SpecEdge:
    source: SpecNode
    target: SpecNode
    relation: str                  # 例: "STRUCTURED_BY", "CONSTRAINED_BY"
    direction: EdgeDirection

@dataclass
class SubGraph:
    nodes: list[SpecNode]
    edges: list[SpecEdge]
    context_summary: str           # オーガナイザーが生成したサルわか圧縮サマリー
    task_id: str

@dataclass
class TaskDefinition:
    task_id: str
    description: str               # 自然言語 x ANMS ハイブリッド記述
    why: str
    when: str
    who: str
    where: str
    what: str
    how: str
    root_node_ids: list[str]       # グラフ選定の起点ノードID群
```

---

**title: GraphRepository_Interface**
```python
from abc import ABC, abstractmethod

class GraphRepository(ABC):
    """
    Clean Architecture Framework層のインターフェース。
    Neo4j / Memgraph 等の具体実装はこのインターフェースを実装する。
    オーガナイザーはこのインターフェースにのみ依存する（DIP）。
    """

    @abstractmethod
    def get_node(self, node_id: str) -> SpecNode:
        """ノードIDでノードを取得する"""
        ...

    @abstractmethod
    def get_ancestors(self, node_id: str) -> list[SpecNode]:
        """
        forwardエッジを逆に辿り、Layer1まで祖先ノードを収集する。
        Context圧縮アルゴリズム step1 に対応。
        """
        ...

    @abstractmethod
    def get_subgraph(self, root_node_id: str, max_hops: int) -> SubGraph:
        """
        起点ノードからmax_hopsホップ以内のサブグラフを切り出す。
        グラフ選定 基準3（Capability_Fit）の打ち切りに使用する。
        """
        ...

    @abstractmethod
    def write_node(self, node: SpecNode) -> None:
        """サブエージェントの出力ノードをグラフに書き戻す（Combineフェーズ）"""
        ...

    @abstractmethod
    def write_edge(self, edge: SpecEdge) -> None:
        """サブエージェントの出力エッジをグラフに書き戻す（Combineフェーズ）"""
        ...

    @abstractmethod
    def validate_edge_direction(self, edge: SpecEdge) -> bool:
        """
        direction制約（forward/trace/meta）を検証する。
        Combineフェーズの矛盾検知に使用する。
        """
        ...
```

---

**title: OrganizerAgent_Skeleton**
```python
class OrganizerAgent:
    """
    システム中で最高コストのコンポーネント。
    フルグラフへのアクセス権と最大コンテキストウィンドウを必要とする。
    U_compress と F_decompose の合成として動作する。
    """

    def __init__(self, graph: GraphRepository):
        self._graph = graph

    # -------------------------------------------------------
    # Phase2 Step3: タスク定義
    # -------------------------------------------------------
    def define_task(self, raw_input: str) -> TaskDefinition:
        """
        自然言語 x ANMS ハイブリッド入力を受け取り、
        5W1Hタグ付きのTaskDefinitionに構造化する。
        LLMを使って自然言語部分をANMSノードIDにグラウンディングする。

        grounding = f(自然言語)
        f = Role x Context
        """
        ...

    # -------------------------------------------------------
    # Phase2 Step4: グラフ選定（3基準パイプライン）
    # -------------------------------------------------------
    def select_subgraph(
        self,
        task: TaskDefinition,
        agent_window_size: int,         # 基準3: エージェントの能力上限
    ) -> SubGraph:
        """
        3基準パイプラインでサブグラフを選定する。
        1. 意味的近さ（5W1Hタグとのベクトル距離）
        2. Context圧縮（Layer1からタスク層の縦断パスを圧縮）
        3. 能力適合（agent_window_sizeで打ち切り）
        """
        # 基準1: 意味的近さでノード候補を絞る
        candidate_nodes = self._filter_by_semantic_proximity(task)

        # 基準2: Context圧縮（核心・最高コスト操作）
        context_summary = self._compress_context(task, candidate_nodes)

        # 基準3: ウィンドウサイズで打ち切り
        subgraph = self._trim_to_capability(
            candidate_nodes, context_summary, agent_window_size
        )
        return subgraph

    def _filter_by_semantic_proximity(
        self, task: TaskDefinition
    ) -> list[SpecNode]:
        """
        5W1Hタグのベクトルと各ノードのベクトル距離を計算し、
        閾値以内のノード群を返す。
        """
        ...

    def _compress_context(
        self, task: TaskDefinition, candidates: list[SpecNode]
    ) -> str:
        """
        Context圧縮アルゴリズム（基準2の核心）。
        1. 起点ノードからLayer1まで祖先を収集
        2. 5W1Hタグを持つノードをパス上から抽出
        3. LLMでサルわか自然言語サマリーを生成（最高コスト）

        捨てるべきは詳細であってWhyではない。
        """
        ...

    def _trim_to_capability(
        self,
        candidates: list[SpecNode],
        context_summary: str,
        window_size: int,
    ) -> SubGraph:
        """
        ノード群をwindow_sizeに収まるよう優先度順に打ち切る。
        context_summaryは必ず含める（Whyの断片は削らない）。
        """
        ...

    # -------------------------------------------------------
    # Divide: サブタスクへの分割
    # -------------------------------------------------------
    def divide(
        self, subgraph: SubGraph, agent_roles: list[str]
    ) -> list[tuple[str, SubGraph]]:
        """
        SubGraphをSTFB層とドメイン境界で分割し、
        各サブエージェントに割り当てる (agent_role, subgraph) のリストを返す。
        """
        ...

    # -------------------------------------------------------
    # Combine: 出力の統合と矛盾検知
    # -------------------------------------------------------
    def combine(self, results: list[tuple[str, SubGraph]]) -> None:
        """
        サブエージェントの出力を受け取り、グラフに書き戻す。
        矛盾パターンを検知し、必要に応じてサブエージェントへ差し戻す。
        Divideの分割精度が高いほどここでの矛盾は減る。
        """
        for agent_id, result in results:
            for edge in result.edges:
                if not self._graph.validate_edge_direction(edge):
                    self._handle_conflict(agent_id, edge)
                    continue
                self._graph.write_edge(edge)
            for node in result.nodes:
                self._graph.write_node(node)

    def _handle_conflict(self, agent_id: str, edge: SpecEdge) -> None:
        """
        矛盾エッジの調停。差し戻し or ADRノード追加 or 強制修正。
        """
        ...
```

---

**title: SubAgent_Skeleton**
```python
class SubAgent:
    """
    低コスト・専門特化コンポーネント。
    オーガナイザーから最小コンテキスト（SubGraph）を受け取り実行する。
    フルグラフへのアクセス権は不要。
    """

    def __init__(self, role: str, capability: dict):
        self.role = role
        self.capability = capability  # モデル名・ツール・ウィンドウサイズ等

    def execute(self, subgraph: SubGraph) -> SubGraph:
        """
        SubGraphとcontext_summary（サルわか圧縮サマリー）を受け取り、
        タスクを実行して結果SubGraphを返す。
        context_summaryがWhyの断片を保持しているため、
        局所最適に陥らない実行が可能になる。
        """
        ...
```

---

**AIへの実装指示テンプレート**

上記スケルトンをAIに実装させる際は以下のフォーマットで渡すこと。
```markdown
## 実装タスク

### Role
あなたは GraphRepository の Neo4j 実装を担当するエンジニアエージェントです。

### Context（Why）
このリポジトリは ANMS 大規模スケーリングシステムにおける
Read Model（CQRS構成）を担います。
仕様要素間の依存関係をリアルタイムにクエリするために存在します。

### What
GraphRepository インターフェースの Neo4j 実装クラス Neo4jGraphRepository を実装してください。

### 対象ノードID
- CMP-001 (GraphRepository Interface)
- CMP-002 (Neo4jGraphRepository)

### 制約
- direction制約（forward/trace/meta）の検証ロジックを必ず実装すること
- get_ancestors は Layer1 まで再帰的に辿ること
- 接続情報は環境変数から取得すること
```