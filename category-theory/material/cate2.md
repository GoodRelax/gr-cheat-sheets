## Appendix G: タスク割り当てアルゴリズム — オーガナイザーによるDivide and Conquer

### 概要

オーガナイザーエージェントの仕事は2つの関手の合成である。

$$
\text{Organizer} = F_{decompose} \circ U_{compress}
$$

- $U_{compress}$ : 全体グラフを圧縮し、大義（Why）を抽出する忘却関手
- $F_{decompose}$ : 大義をサブタスクに分割し、サブエージェントへ具体化する自由関手

オーガナイザーはフルグラフへのアクセス権と最大のコンテキストウィンドウを必要とする、システム中で最高コストのコンポーネントである。その品質がシステム全体のアウトプット品質の上限を決定する。

---

### フェーズ1: 準備フェーズ（静的・プロジェクト起動時に一回）

**title: Phase1_Preparation_Flow**

```mermaid
flowchart TD
    Start["Project_Start"]
    R1["Step1<br/>Role_Definition<br/>エージェントの役割を定義"]
    R2["Step2<br/>Capability_Selection<br/>モデル・ツール・ウィンドウサイズを選定"]
    R3["Step3<br/>Role_x_Capability_Matrix<br/>役割と能力のマトリクスを確定"]

    Start -->|"kickoff"| R1
    R1 -->|"define"| R2
    R2 -->|"combine"| R3
```

準備フェーズでは、エージェントのロール（何者か）と能力・リソース（何ができるか）を静的に確定する。この2つは掛け算の関係であり、片方がゼロなら出力もゼロになる。

$$
\text{Agent} = \text{Role} \times \text{Capability}
$$

| 項目           | 内容                                             | ANMSでの対応                 |
| :------------- | :----------------------------------------------- | :--------------------------- |
| Role定義       | エージェントの責務・専門領域                     | STFB層での立ち位置           |
| Capability選定 | モデル性能・ツール・コンテキストウィンドウサイズ | 扱えるサブグラフの最大サイズ |

---

### フェーズ2: タスクフェーズ（動的・タスク毎に実行）

**title: Phase2_Task_Assignment_Flow**

```mermaid
flowchart TD
    T0["Task_Input<br/>自然言語 x ANMS ハイブリッド記述"]

    subgraph Step3["Step3 タスク定義"]
        T1["5W1H_Tagging<br/>Why When Who Where What How"]
        T2["Goal_Definition<br/>背景・目的・ゴールの明文化"]
        T1 -->|"structure"| T2
    end

    subgraph Step4["Step4 グラフ選定"]
        T3["Criterion1_Semantic_Proximity<br/>5W1Hタグとの意味的近さ"]
        T4["Criterion2_Context_Compression<br/>Layer1からタスク層までを圧縮<br/>Whyの断片を保持"]
        T5["Criterion3_Capability_Fit<br/>エージェントの能力に収まるサイズ"]
        T3 -->|"filter"| T4
        T4 -->|"trim"| T5
    end

    subgraph Divide["Divide"]
        T6["Subgraph_Extraction<br/>STFB層とドメイン境界で分割"]
        T7["Context_Summary_Generation<br/>オーガナイザーが大義を圧縮サマリー化"]
        T6 -->|"compress"| T7
    end

    subgraph Conquer["Conquer"]
        T8["SubAgent_A<br/>最小コンテキスト受領"]
        T9["SubAgent_B<br/>最小コンテキスト受領"]
        T10["SubAgent_C<br/>最小コンテキスト受領"]
    end

    subgraph Combine["Combine"]
        T11["Result_Integration<br/>出力をグラフに書き戻し"]
        T12["Conflict_Detection<br/>矛盾ノード・エッジの検知"]
        T13["Arbitration<br/>オーガナイザーによる調停"]
        T11 -->|"check"| T12
        T12 -->|"resolve"| T13
    end

    T0 -->|"input"| Step3
    Step3 -->|"defined"| Step4
    Step4 -->|"selected"| Divide
    T7 -->|"assign"| T8
    T7 -->|"assign"| T9
    T7 -->|"assign"| T10
    T8 -->|"output"| Combine
    T9 -->|"output"| Combine
    T10 -->|"output"| Combine
```

タスクフェーズはStep3（タスク定義）とStep4（グラフ選定）を経て、Divide・Conquer・Combineの3段階で実行される。

---

### グラフ選定の3基準

**title: Graph_Selection_Criteria**

```mermaid
flowchart LR
    Full["Full_Graph<br/>全ノード・全エッジ"]

    C1["Criterion1<br/>Semantic_Proximity<br/>5W1Hタグとの<br/>ベクトル距離が近いノード群"]
    C2["Criterion2<br/>Context_Compression<br/>Layer1からタスク層までの<br/>縦断パスを圧縮したサマリー"]
    C3["Criterion3<br/>Capability_Fit<br/>エージェントの<br/>ウィンドウサイズ以内"]

    Sub["SubGraph<br/>最小コンテキスト"]

    Full -->|"filter by"| C1
    C1 -->|"anchor by"| C2
    C2 -->|"trim to"| C3
    C3 -->|"output"| Sub
```

3つの基準は順序を持つフィルタリングパイプラインである。

| 基準           | 操作                       | 忘却の対象               | 保持するもの                    |
| :------------- | :------------------------- | :----------------------- | :------------------------------ |
| 1. 意味的近さ  | ベクトル距離でノードを絞る | 無関係なドメインのノード | タスクと意味的に近いノード群    |
| 2. Context圧縮 | Layer1→タスク層を縦断圧縮  | 詳細な中間ノード         | Whyの断片（大義の欠片）         |
| 3. 能力適合    | ウィンドウサイズで打ち切り | 優先度の低いノード       | Role×Capabilityに収まる最大情報 |

基準2が設計の核心である。**捨てるべきは詳細であってWhyではない。** Layer1（Foundation・Glossary）の全ノードを渡す必要はないが、タスクの大義に繋がるパスは圧縮されて必ず残る。これはJPEGの量子化において低周波成分（構造的な輪郭）を保持し高周波成分（細部）を捨てる操作と同型である。

---

### Context圧縮アルゴリズム（基準2の詳細）

オーガナイザーによるContext圧縮は以下の手順で実行する。

**title: Context_Compression_Algorithm**

```mermaid
flowchart TD
    A["Target_Node<br/>タスクの対象ノード（起点）"]
    B["Trace_Upward<br/>forwardエッジを逆に辿り<br/>Layer1まで祖先ノードを収集"]
    C["Extract_Why_Path<br/>5W1Hタグを持つノードを<br/>パス上から抽出"]
    D["Compress_Summary<br/>オーガナイザーが<br/>自然言語サマリーを生成<br/>（サルわか翻訳）"]
    E["Attach_as_Context_Node<br/>サマリーをContext_Nodeとして<br/>サブグラフに付与"]

    A -->|"step1 trace"| B
    B -->|"step2 filter"| C
    C -->|"step3 compress"| D
    D -->|"step4 attach"| E
```

手順3「サルわか翻訳」がオーガナイザーの最高コスト操作である。Layer1からタスク層までの縦断的な意味を、サブエージェントが扱える粒度の自然言語に圧縮する。この圧縮の質がサブエージェントのアウトプット品質を直接規定する。

$$
\text{Context\_Node} = U_{compress}(\text{Path}(\text{Layer1} \to \text{Target\_Node}))
$$

---

### Combineフェーズの矛盾検知

サブエージェントの出力をグラフに書き戻す際、以下の矛盾パターンを検知する。

| 矛盾パターン         | 検知方法                                      | 調停方法                                   |
| :------------------- | :-------------------------------------------- | :----------------------------------------- |
| エッジ方向の違反     | direction制約（forward/trace/meta）チェック   | オーガナイザーが該当ノードを差し戻し       |
| STFB層の逆転依存     | source.stfb_layer と target.stfb_layer の比較 | 依存方向を修正または設計判断（ADR）を追加  |
| 同一ノードの競合更新 | Git diff による衝突検出                       | オーガナイザーが調停しコミット             |
| 5W1Hタグとの意味乖離 | 出力ノードのベクトルとタスクタグの距離計算    | サブエージェントへ差し戻しまたは再タスク化 |

Combineフェーズの調停コストもオーガナイザーに集中する。**Divideの分割精度が高いほどCombineの矛盾は減る。** 良いオーガナイザーは前段のDivideで矛盾の種を摘む。

---

### コスト構造のまとめ

**title: Cost_Distribution**

```mermaid
flowchart LR
    O["Organizer_Agent<br/>最高コスト<br/>フルグラフアクセス<br/>最大ウィンドウ<br/>最高性能モデル"]
    S1["SubAgent_A<br/>低コスト<br/>最小コンテキスト<br/>専門特化"]
    S2["SubAgent_B<br/>低コスト<br/>最小コンテキスト<br/>専門特化"]
    S3["SubAgent_C<br/>低コスト<br/>最小コンテキスト<br/>専門特化"]

    O -->|"compress and assign"| S1
    O -->|"compress and assign"| S2
    O -->|"compress and assign"| S3
    S1 -->|"output"| O
    S2 -->|"output"| O
    S3 -->|"output"| O
```

オーガナイザーのコストが高い理由は構造的必然である。$U_{compress} \circ F_{decompose}$ の合成操作はフルグラフの理解を前提とし、圧縮サマリーの生成は高い抽象化能力を要求する。サブエージェントが低コストで高品質な出力を出せるのは、オーガナイザーが高コストの前処理を担っているからである。これは優秀な中間管理職が経営理念を現場の言葉に翻訳することで、現場が迷わず動ける構造と同型である。
