# IPA プロジェクトマネージャ試験 用語辞典

PM 経験者向け。**実務経験だけでは埋まりにくい専門用語**(信頼性工学・意思決定技法・投資評価・組織論・リーダーシップ理論・テスト技法・見積モデルなど)を中心に、IPA プロジェクトマネージャ試験(特に午前II)の頻出語を収録。

- **列:** ✓(習得チェック)/ 用語 / 英語・正式名称 / 意味
- **使い方:** 覚えた語は ☐ を ☑ に置き換える。
- **関連:** 役割割当(RACI/DACI)の詳細は同フォルダの `raci-daci-rasic-comparison.md`。

---

## 0. 全体像:PMBOK 10 知識エリアと 5 プロセス群

**10 知識エリアの語呂合わせ(英語):**

> **I S**aw **T**wo **C**rows **Q**uickly **H**aving **C**offee And **R**eading **P**oetic **S**tories

| # | 知識エリア | English | 一言 |
|---|---|---|---|
| 1 | 統合 | **I**ntegration | 全体の調整・憲章・変更管理 |
| 2 | スコープ | **S**cope | 作業範囲(WBS) |
| 3 | スケジュール | **T**ime → Schedule | 日程(6th 版で Schedule に改称) |
| 4 | コスト | **C**ost | 予算・EVM |
| 5 | 品質 | **Q**uality | 品質保証・管理 |
| 6 | 資源 | **H**uman Resource → Resource | 人・物の調達と育成(6th 版で Resource) |
| 7 | コミュニケーション | **C**ommunications | 情報伝達 |
| 8 | リスク | **R**isk | 不確実性への対応 |
| 9 | 調達 | **P**rocurement | 外部委託・契約 |
| 10 | ステークホルダ | **S**takeholder | 利害関係者の関与 |

**5 プロセス群(IPECC):** 立ち上げ(Initiating)→ 計画(Planning)→ 実行(Executing)→ 監視・コントロール(Monitoring & Controlling)→ 終結(Closing)。

---

## 1. 統合・全体マネジメント

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | プロジェクト憲章 | Project Charter | PMを任命しプロジェクトを正式認可する文書 |
| ☐ | ベースライン | Baseline | 承認済みの基準計画。実績比較の基準 |
| ☐ | 構成管理 | Configuration Management | 成果物の版・状態を識別し変更を統制 |
| ☐ | 統合変更管理 | Integrated Change Control | 変更要求の全体影響を統合評価し承認する手続き |
| ☐ | 変更管理委員会 | CCB (Change Control Board) | 変更要求の承認可否を決める委員会 |
| ☐ | 教訓 | Lessons Learned | 得た知見を後続に活かす記録 |
| ☐ | フェーズゲート | Phase / Stage Gate | フェーズ移行可否を審査する管理点 |
| ☐ | PMO | Project Management Office | PM活動を標準化・支援する組織(支援型・<br />コントロール型・指揮型に大別) |
| ☐ | OPA / EEF | Organizational Process Assets / Enterprise Environmental Factors | 組織の資産(標準・教訓)と環境要因(規制・文化) |
| ☐ | ローリングウェーブ計画法 | Rolling Wave Planning | 直近を詳細に、先は粗く、進行に応じ段階的に詳細化する計画法 |

---

## 2. スコープ

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | プロダクト/プロジェクトスコープ | Product / Project Scope | 成果物の特性範囲 / 成果物を生む作業範囲 |
| ☐ | WBS | Work Breakdown Structure | 成果物を階層的に分解した作業構造 |
| ☐ | ワークパッケージ | Work Package | WBS最下位要素。見積・管理の最小単位 |
| ☐ | WBS辞書 | WBS Dictionary | 各WBS要素の作業内容・担当・期日等を記す文書 |
| ☐ | スコープクリープ | Scope Creep | 統制されずスコープが徐々に膨張する現象 |
| ☐ | ゴールドプレーティング | Gold Plating | 要求外の余分な作り込み(過剰品質) |
| ☐ | 要求事項トレーサビリティマトリックス | RTM | 要求と成果物の対応を追跡する表 |

---

## 3. スケジュール

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | アローダイアグラム | Arrow Diagram (ADM/PERT図) | 作業を矢線、結合点を丸で表す日程網図 |
| ☐ | PDM(プレシデンスダイアグラム) | Precedence Diagramming Method | 作業をノード、依存を矢線で結ぶ図法。<br />FS/SS/FF/SF の4依存関係を表現 |
| ☐ | クリティカルパス | Critical Path (CPM) | 全体工期を決める、余裕ゼロの最長経路 |
| ☐ | トータルフロート / フリーフロート | Total / Free Float | 全体工期を遅らせない総余裕 / <br />後続の最早開始を遅らせない余裕 |
| ☐ | PERT(三点見積りの期待値) | Program Evaluation and Review Technique | 期待値 te=(楽観+4×最可能+悲観)/6 |
| ☐ | PERT の標準偏差・分散 | Standard Deviation / Variance | σ=(悲観−楽観)/6、分散 σ²=((悲観−楽観)/6)² |
| ☐ | ファストトラッキング | Fast Tracking | 作業を並行実施し工期短縮(リスク増) |
| ☐ | クラッシング | Crashing | 資源投入で工期短縮(コスト増) |
| ☐ | 資源平準化 / 資源円滑化 | Resource Leveling / Smoothing | 制約に合わせ日程調整し工期延長を許容 / <br />フロート内で資源を平らに(工期は不変) |
| ☐ | リード / ラグ | Lead / Lag | 後続を前倒す時間 / 遅らせる時間 |
| ☐ | トレンドチャート | Trend Chart | 予算・実績・予測の推移を時系列で示す進捗管理図 |

---

## 4. コスト・EVM

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | PV / EV / AC | Planned Value / Earned Value / Actual Cost | 計画値 / 出来高(完了作業の予算換算) / 実コスト |
| ☐ | BAC / EAC / ETC / VAC | Budget / Estimate At Completion ほか | 完成時総予算 / 完成時見積(=BAC÷CPI 等) / <br />残作業見積(EAC−AC) / 完成時差異(BAC−EAC) |
| ☐ | SV / CV | Schedule / Cost Variance | SV=EV−PV(負で遅れ) / CV=EV−AC(負で超過) |
| ☐ | SPI / CPI | Schedule / Cost Performance Index | SPI=EV÷PV、CPI=EV÷AC(1未満で不良) |
| ☐ | TCPI | To-Complete Performance Index | 残予算で完成させるのに必要なコスト効率 |
| ☐ | アーンドスケジュール | Earned Schedule (ES) | EVMの遅れを「金額」でなく「時間」で評価する拡張 |
| ☐ | EVM | Earned Value Management | 出来高で進捗とコストを統合的に定量管理する手法 |

---

## 5. 見積技法

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 類推見積り | Analogous Estimating | 過去の類似案件実績を基にする概算(トップダウン) |
| ☐ | パラメトリック見積り | Parametric Estimating | 規模×単価など統計的関係式で見積もる |
| ☐ | ボトムアップ見積り | Bottom-Up Estimating | WBS最下位から積み上げる。精度高・工数大 |
| ☐ | 標準値法(積算法) | Standard Value Method | 標準化した作業の所要工数を積み上げて見積もる |
| ☐ | ファンクションポイント法 | Function Point (IFPUG) | 機能の種類と数からソフト規模を見積もる |
| ☐ | COCOMO | Constructive Cost Model | プログラム規模(LOC)から工数・期間を見積もるモデル |
| ☐ | COSMIC法 | COSMIC FFP | データ移動量からソフト機能規模を測る国際標準手法 |
| ☐ | LOC法 | Lines Of Code | ソース行数で規模を見積もる方式 |
| ☐ | プランニングポーカー | Planning Poker | 相対見積りをカードで合議するアジャイル技法 |

---

## 6. CCPM・制約理論

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 制約理論 | TOC (Theory of Constraints) | 全体能力はボトルネックで決まる。そこに集中対処する |
| ☐ | クリティカルチェーン | Critical Chain (CCPM) | 資源制約を考慮した最長経路。バッファで管理 |
| ☐ | プロジェクトバッファ | Project Buffer | 全工程の末尾に置く全体の安全余裕 |
| ☐ | 合流バッファ | Feeding Buffer | 非クリティカル経路がクリティカルチェーンに合流する手前に置く余裕 |
| ☐ | 学生症候群 | Student Syndrome | 締切間際まで着手を先延ばしする心理 |
| ☐ | パーキンソンの法則 | Parkinson's Law | 仕事は与えられた時間をすべて使い切るまで膨張する |

---

## 7. 品質(QC七つ道具)

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 品質保証 / 品質管理 | QA / QC | プロセスを監査し品質を作り込む / 成果物を検査・測定 |
| ☐ | 検証 / 妥当性確認 | Verification / Validation | 仕様どおり正しく作ったか / 利用者の本来のニーズを満たすか |
| ☐ | 特性要因図 | Cause-and-Effect (Ishikawa) | 要因を魚の骨状に整理する図 |
| ☐ | パレート図 | Pareto Chart | 降順の棒+累積比率の折線。重点指向(80:20) |
| ☐ | 管理図 | Control Chart | 工程変動が管理限界内かを見る時系列図 |
| ☐ | ヒストグラム / 散布図 | Histogram / Scatter Diagram | 分布を区間別度数で表す / 2変数の相関を点で表す |
| ☐ | チェックシート / 層別 | Check Sheet / Stratification | データ採取の記録用紙 / 要因別に分類し傾向把握 |
| ☐ | 新QC七つ道具 | 7 New QC Tools | 親和図・連関図・系統図など言語データ整理の7手法 |
| ☐ | PDCA | Plan-Do-Check-Act | 計画・実行・評価・改善を回す継続的改善サイクル |
| ☐ | 品質コスト | Cost of Quality | 予防・評価・失敗(内部/外部)に要する総コスト |

---

## 8. テスト技法・レビュー・信頼度

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | ホワイトボックステスト | White-box Testing | 内部ロジックに基づきテストケースを作る |
| ☐ | ブラックボックステスト | Black-box Testing | 入力と期待結果に基づきテストケースを作る |
| ☐ | 同値分割 / 限界値分析 | Equivalence Partitioning / Boundary Value | 同じ振る舞いの値域を代表 / 境界付近を重点的に検査 |
| ☐ | デシジョンテーブル | Decision Table | 条件と動作の組合せを網羅的に整理する表 |
| ☐ | 直交表 | Orthogonal Array | 組合せを効率的に絞ってテストする統計的手法 |
| ☐ | カバレッジ(網羅率) | Code Coverage | 命令網羅(C0)・分岐網羅(C1)等のテスト網羅度 |
| ☐ | ウォークスルー | Walkthrough | 作成者主導で行う非公式レビュー |
| ☐ | インスペクション | Inspection | モデレータが主導する公式なレビュー |
| ☐ | ラウンドロビン | Round-robin Review | 参加者が順番に主導役を交代するレビュー |
| ☐ | 信頼度成長曲線 | Reliability Growth Curve | テスト時間に対する累積バグ検出数の曲線。<br />ゴンペルツ曲線・ロジスティック曲線でモデル化 |
| ☐ | 欠陥密度 | Defect Density | 規模(KLOC等)あたりの欠陥数 |

---

## 9. 信頼性・可用性(RASIS)

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | MTBF / MTTR | Mean Time Between Failures / To Repair | 平均故障間隔 / 平均修復時間 |
| ☐ | 稼働率(可用性) | Availability | MTBF ÷ (MTBF + MTTR) |
| ☐ | 直列/並列システムの稼働率 | Series / Parallel | 直列=A1×A2、並列=1−(1−A1)(1−A2) |
| ☐ | バスタブ曲線 | Bathtub Curve | 初期故障→偶発故障→摩耗故障の故障率推移 |
| ☐ | フェールセーフ | Fail-safe | 故障時に安全側へ向かわせる設計 |
| ☐ | フェールソフト | Fail-soft | 故障部を切り離し機能を縮退して稼働継続 |
| ☐ | フールプルーフ | Fool-proof | 誤操作をしても危険・誤動作に至らせない設計 |
| ☐ | フォールトトレラント | Fault Tolerant | 冗長化により故障しても全体機能を維持 |
| ☐ | ホット/ウォーム/コールドスタンバイ | Hot / Warm / Cold Standby | 待機系の準備度合い(即切替 / 一部準備 / 停止) |

---

## 10. リスク

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 定性的 / 定量的リスク分析 | Qualitative / Quantitative Risk Analysis | 確率×影響度で優先順位付け / 影響を数値化 |
| ☐ | 発生確率・影響度マトリックス | Probability-Impact Matrix | 確率×影響でリスクを格付けする表 |
| ☐ | リスクブレークダウンストラクチャ | RBS | リスクを源泉別に階層分解した一覧 |
| ☐ | 期待金額価値 | EMV (Expected Monetary Value) | 発生確率×金額影響の総和。決定木で使用 |
| ☐ | デシジョンツリー | Decision Tree | 選択肢と確率で期待値を比較する分析図 |
| ☐ | 感度分析 / トルネード図 | Sensitivity Analysis / Tornado | 各変数が結果に与える影響度を分析・可視化 |
| ☐ | モンテカルロ法 | Monte Carlo Simulation | 乱数の反復試行で結果の分布を求める手法 |
| ☐ | リスク対応(脅威 / 好機) | Threat / Opportunity Responses | 回避・転嫁・軽減・受容 / 活用・共有・強化・受容 |
| ☐ | コンティンジェンシー予備 | Contingency Reserve | 既知リスク用。コストベースライン内、PM裁量 |
| ☐ | マネジメント予備 | Management Reserve | 未知リスク用。ベースライン外、上位承認が必要 |
| ☐ | 二次リスク / 残存リスク | Secondary / Residual Risk | 対応実施で新たに生じる / 対応後にも残る |
| ☐ | デルファイ法 | Delphi Method | 専門家の匿名回答を収束させ予測・合意を得る |

---

## 11. 意思決定・分析技法

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | AHP(階層分析法) | Analytic Hierarchy Process | 評価項目を一対比較で重み付けし代替案を総合評価 |
| ☐ | ペイオフマトリクス | Payoff Matrix | 戦略×状態で利得を整理する意思決定表 |
| ☐ | マクシミン原理 | Maximin | 各案の最悪結果の中で最善を選ぶ(悲観的基準) |
| ☐ | マクシマックス原理 | Maximax | 各案の最良結果の中で最善を選ぶ(楽観的基準) |
| ☐ | ミニマックス後悔 | Minimax Regret | 機会損失(後悔)の最大値が最小の案を選ぶ |
| ☐ | 線形計画法 | Linear Programming | 制約下で目的関数を最大/最小化する最適化手法 |
| ☐ | 待ち行列理論 | Queueing Theory | 到着・サービス率から待ち時間・行列長を分析 |

---

## 12. 投資評価・経済性

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 正味現在価値 | NPV (Net Present Value) | 将来CFを割引いた現在価値の合計−初期投資。正で投資価値あり |
| ☐ | 内部収益率 | IRR (Internal Rate of Return) | NPV=0 となる割引率。高いほど有利 |
| ☐ | 投資利益率 | ROI (Return on Investment) | 利益 ÷ 投資額 |
| ☐ | 回収期間法 | Payback Period (PBP) | 投資額を回収するまでの期間で評価 |
| ☐ | 割引キャッシュフロー | DCF (Discounted Cash Flow) | 将来CFを割引率で現在価値に換算する考え方 |
| ☐ | 損益分岐点 | Break-Even Point | 売上と総費用が等しくなる点 |
| ☐ | 総保有コスト | TCO (Total Cost of Ownership) | 導入から運用・廃棄までの総コスト |

---

## 13. 調達・契約

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 内外製分析 | Make-or-Buy | 自製か購入かを判断する分析 |
| ☐ | RFI / RFP / RFQ | Request For Information / Proposal / Quotation | 情報提供依頼 / 提案依頼 / 見積依頼 |
| ☐ | SOW | Statement Of Work | 調達対象の作業範囲記述書 |
| ☐ | 定額契約 | Firm Fixed Price (FFP) | 価格固定。供給者がコストリスクを負う |
| ☐ | 実費償還契約 | Cost Reimbursable | 実費+報酬。買い手がコストリスクを負う |
| ☐ | T&M契約 | Time and Material | 工数と材料の実費で精算する中間型契約 |
| ☐ | 請負契約 | — | 仕事の完成を約す。完成責任あり、指揮命令は受注者側 |
| ☐ | 準委任契約 | — | 業務の遂行を約す。完成責任なし、善管注意義務を負う(SES等) |
| ☐ | 偽装請負 | — | 実態は労働者派遣なのに請負を装う違法状態 |
| ☐ | 多段階契約 | — | 工程ごとに分けて契約(超上流は準委任、開発は請負 等) |
| ☐ | 検収 | Acceptance | 成果物が要件を満たすか確認して受け入れる行為 |
| ☐ | 契約不適合責任 | — | 成果物が契約内容に適合しない場合の責任(旧・瑕疵担保責任) |
| ☐ | 下請法 | — | 親事業者の下請に対する不当行為を規制する法律 |

---

## 14. 組織・体制

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | 機能型組織 | Functional Organization | 職能別の縦割り。PMの権限は弱い |
| ☐ | プロジェクト型組織 | Projectized Organization | PMに強い権限。メンバはプロジェクト専任 |
| ☐ | マトリックス型組織 | Matrix Organization | 機能とプロジェクトが交差。弱い/バランス/強いに大別 |
| ☐ | ブルックスの法則 | Brooks' Law | 遅れているプロジェクトへの要員追加は更に遅らせる |
| ☐ | OBS | Organizational Breakdown Structure | 組織を階層分解し責任を対応づける構造 |

---

## 15. リーダーシップ・動機づけ理論

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | マズローの欲求5段階 | Maslow's Hierarchy of Needs | 生理的→安全→社会的→承認→自己実現 |
| ☐ | ハーズバーグの二要因理論 | Two-Factor (Motivation-Hygiene) | 満足を生む動機づけ要因と、不満を防ぐ衛生要因は別物 |
| ☐ | X理論・Y理論 | McGregor's Theory X / Y | 人は怠ける(X、統制必要)/ 人は自律的(Y) |
| ☐ | 期待理論 | Expectancy Theory (Vroom) | 動機=期待×道具性×誘意性 |
| ☐ | SL理論(状況対応型) | Situational Leadership | 部下の成熟度に応じて指示/説得/参加/委任を使い分ける |
| ☐ | PM理論 | PM Theory (三隅二不二) | P機能(目標達成)とM機能(集団維持)の2軸で類型化 |
| ☐ | タックマンモデル | Tuckman Model | 形成→混乱→統一→機能→散会の5段階 |
| ☐ | コンフリクトマネジメント | Conflict Management | 対立への5対処(対決/協力・妥協・鎮静・強制・撤退) |

---

## 16. 開発プロセス・アジャイル

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | ウォーターフォール | Waterfall | 後戻りせず上流から下流へ進む逐次型 |
| ☐ | 反復型 / 漸進型 | Iterative / Incremental | 繰り返し / 段階的に開発を進めるモデル |
| ☐ | スパイラルモデル | Spiral | リスク評価を軸に反復するモデル |
| ☐ | プロトタイピング | Prototyping | 試作品で要求を早期に確認する手法 |
| ☐ | XP(エクストリームプログラミング) | Extreme Programming | 反復・テスト重視のアジャイル手法群 |
| ☐ | ペアプログラミング | Pair Programming | 2人1組で実装・即時レビューする XP プラクティス |
| ☐ | テスト駆動開発 | TDD (Test-Driven Development) | テストを先に書いてから実装する |
| ☐ | リファクタリング | Refactoring | 外部振る舞いを変えずに内部構造を改善 |
| ☐ | CI / CD | Continuous Integration / Delivery | 統合・リリースを継続的に自動化する |
| ☐ | カンバン / WIP制限 | Kanban / Work In Progress Limit | 作業を可視化し仕掛り数の上限で流れを管理 |
| ☐ | ベロシティ / バーンダウンチャート | Velocity / Burndown Chart | 1スプリントの完了量実績 / 残作業量の推移図 |
| ☐ | MVP | Minimum Viable Product | 価値検証のための最小限の製品 |

---

## 17. スクラム(詳細)

スクラムは、複雑な問題に適応的に取り組むための**軽量なフレームワーク**。1〜4週間の固定期間「スプリント」を繰り返し、各スプリントで価値ある「インクリメント」を生む。構成は **3 ロール・5 イベント・3 作成物**(3-5-3)。

- **3 ロール:** プロダクトオーナー(PO)/ スクラムマスター(SM)/ 開発者
- **5 イベント:** スプリント(器)+ スプリントプランニング / デイリースクラム / スプリントレビュー / スプリントレトロスペクティブ
- **3 作成物:** プロダクトバックログ / スプリントバックログ / インクリメント(各々にゴール=確約が紐づく)

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | スクラム | Scrum | スプリント単位で反復する代表的アジャイルフレームワーク |
| ☐ | プロダクトオーナー | Product Owner (PO) | プロダクト価値の最大化に責任を持ち、バックログを管理する |
| ☐ | スクラムマスター | Scrum Master (SM) | スクラムの理解と実践を支援し、障害を除去するサーバントリーダー |
| ☐ | 開発者 | Developers | インクリメントを作る作業を担うメンバ |
| ☐ | スプリント | Sprint | 1〜4週の固定反復期間(タイムボックス)。他イベントの器 |
| ☐ | スプリントプランニング | Sprint Planning | スプリントの目標と実施作業を計画するイベント |
| ☐ | デイリースクラム | Daily Scrum | 開発者が毎日行う15分の進捗同期 |
| ☐ | スプリントレビュー | Sprint Review | 成果(インクリメント)を関係者に提示し検査する |
| ☐ | スプリントレトロスペクティブ | Sprint Retrospective | プロセス自体を振り返り改善するイベント |
| ☐ | プロダクトバックログ | Product Backlog | 優先順位付きの要求一覧。POが管理 |
| ☐ | スプリントバックログ | Sprint Backlog | そのスプリントで実施する作業一覧 |
| ☐ | インクリメント | Increment | スプリントで完成した、リリース可能な成果の積み上がり |
| ☐ | 完成の定義 | DoD (Definition of Done) | 「完成」とみなすために満たすべき品質基準 |
| ☐ | ストーリーポイント / ユーザーストーリー | Story Point / User Story | 規模の相対見積単位 / 利用者視点の要求記述 |

---

## 18. 標準・横断概念

| ✓ | 用語 | 英語・正式名称 | 意味 |
|---|---|---|---|
| ☐ | PMBOK | PMBOK Guide | PMIによるPM知識体系 |
| ☐ | JIS Q 21500 | ISO 21500 | プロジェクトマネジメントの国際/日本規格 |
| ☐ | 共通フレーム | SLCP-JCF | ソフトウェアライフサイクルプロセスの共通枠組み |
| ☐ | CMMI | Capability Maturity Model Integration | プロセス成熟度を5段階で評価するモデル |
| ☐ | ITIL | ITIL | ITサービスマネジメントのベストプラクティス集 |
| ☐ | SLA | Service Level Agreement | 提供するサービス水準を合意する契約 |
| ☐ | QCD | Quality / Cost / Delivery | 品質・コスト・納期の3制約 |
| ☐ | 制約条件 / トレードオフ | Constraint / Trade-off | 範囲・時間・コスト等の制限 / 一方を立てれば他方が犠牲 |
