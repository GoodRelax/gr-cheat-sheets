# Gherkin 徹底入門（A4 約10ページ相当）

**最終更新:** 2026-03-03  
**対象読者:** 要件定義・QA・開発・PM/EM、SDET、テスト自動化担当  
**目的:** Gherkin の概念・構文・実装連携・運用ベストプラクティスを、導入検討から日々の活用まで一気通貫で理解する

---

## 目次

1. エグゼクティブサマリ
2. Gherkin とは：定義・背景・位置づけ
3. Gherkin の基本構文（Feature/Rule/Scenario/Steps）
4. ステップの高度化：Scenario Outline、Examples、Data Table、DocString
5. タグ運用（@smoke 等）と実行フィルタ
6. Cucumber Expressions と正規表現の使い分け
7. 多言語ステップ定義（Java / JS / Python / Ruby / .NET）
8. プロジェクト構成と命名規約
9. BDD プロセス（Three Amigos / Example Mapping）
10. アンチパターンと改善パターン
11. CI/CD とレポーティング（JUnit/HTML/JSON）
12. 並列実行・データ分離・テスト安定化
13. 非機能要件・外部連携の扱い方
14. バージョニング・レビューフロー・運用ガイド
15. よくある質問（FAQ）
16. 参考情報と学習リソース

---

## 1. エグゼクティブサマリ

- **Gherkin** **がーきん** は、`Given/When/Then` で仕様を**自然言語で**記述し、ツール（Cucumber/SpecFlow/Behave 等）で**実行可能なテスト**として動かすための DSL（ドメイン固有言語）。
- **利点:** 仕様の曖昧さ低減・関係者間の共通言語化・テスト自動化との直結・ドキュメントの “生存（Living Doc）” 化。
- **導入の勘所:** UI 詳細を書きすぎない、1 ステップ 1 意図、タグで粒度を管理、データと手続の分離、CI による常時検証。
- **よくある落とし穴:** ステップが実装詳細に寄りすぎる、長大なシナリオ、環境依存データの混入、待機や時刻依存での**不安定化**。
- **最小成功条件:** 小さく始める（@smoke）、**Three Amigos** で合意形成 → 例（Example）先行 → 自動化の**責務分離**（Glue/Helper/Fixture）。

---

## 2. Gherkin とは：定義・背景・位置づけ

- **定義:** ビジネス・QA・開発の**全員が読める**仕様記述言語。ファイル拡張子は `.feature`。
- **背景:** BDD（Behavior-Driven Development）における**実行可能仕様（Executable Specification）**の核。
- **位置づけ:**
  - 要件のうち**振る舞い（何をすべきか）**を具体例で定義
  - テスト自動化の**入口**（ステップ定義でコードに接続）
  - 設計や内部構造の詳細（**どう実装するか**）は別レイヤが担当

### Gherkin の公式情報

- Gherkin の言語仕様を公式に管理しているのは **Cucumber（Cucumber Ltd.）**
  - https://cucumber.io/
- Cucumber は Gherkin の公式リファレンスを公開しており、Gherkin のパーサや言語定義の公式実装も GitHub 上で提供している。
  - **公式リファレンス:** https://cucumber.io/docs/gherkin/
  - **公式リポジトリ:** https://github.com/cucumber/gherkin
- PyPI の _gherkin‑official_ パッケージでも作者として **Cucumber Ltd.** が明記されている。

---

## 3. Gherkin の基本構文

- **Feature**: 機能の要約（ビジネス価値）
- **Rule**: 機能に対するビジネスルールのまとまり（任意）
- **Background**: すべてのシナリオに共通の前提
- **Scenario**: 1 つの具体例（Given/When/Then の流れ）
- **Steps**: `Given`（前提）, `When`（行為）, `Then`（検証）。`And` / `But` で連結可能
- **コメント**: `#` から行末

> **title:** 最小の Gherkin 例（日本語）
>
> ```gherkin
> Feature: ログイン機能
>   ユーザーとして安全にシステムへログインしたい
>
>   Background:
>     Given ユーザーがログインページを開いている
>
>   Scenario: 正しい資格情報でログインできる
>     When ユーザー名 "taro" とパスワード "P@ssw0rd" を入力する
>     And ログインボタンを押す
>     Then ダッシュボードが表示される
> ```
>
> 単一機能（ログイン）に対し、**共通の前提**（ログインページを開く）と**成功の具体例**を記述した最小パターンです。UI のセレクタ名や内部 API は書かず、**ユーザー視点の意図**を残しています。

---

## 4. ステップの高度化：Scenario Outline / Examples / Data Table / DocString

### 4.1 Scenario Outline（パラメタ化）

> **title:** Scenario Outline でテストケースを列挙
>
> ```gherkin
> Feature: ログイン機能
>   Scenario Outline: 入力パターン別のログイン可否
>     Given ユーザーがログインページを開いている
>     When ユーザー名 "<user>" とパスワード "<pass>" を入力する
>     And ログインボタンを押す
>     Then 結果は "<result>" である
>
>     Examples: 正常と異常
>       | user  | pass      | result   |
>       | taro  | P@ssw0rd  | success  |
>       | taro  | wrong     | failure  |
>       | blank | P@ssw0rd  | failure  |
> ```
>
> **複数の具体例**を表で列挙でき、シナリオ重複を防ぎます。Examples は**等価分割**・**境界値**の表現にも有効です。

### 4.2 Data Table（構造化データの入力）

> **title:** Data Table で複数レコードの前提を記述
>
> ```gherkin
> Feature: 商品検索
>   Scenario: インデックス済み商品をキーワードで検索できる
>     Given 以下の商品が登録されている
>       | id | name       | price |
>       | 1  | red_shoes  | 5000  |
>       | 2  | blue_shoes | 6000  |
>     When ユーザーが "shoes" を検索する
>     Then 検索結果に 2 件含まれる
> ```
>
> ステップ定義側でテーブルを**ドメインオブジェクト**にマッピングします。テストデータの**可読性と差分**が向上します。

### 4.3 DocString（長文・JSON 等のインライン）

> **title:** DocString で JSON リクエストを記述
>
> ```gherkin
> Feature: API のバリデーション
>   Scenario: 不正リクエストは 400 を返す
>     When ユーザーが次の JSON を送信する
>       """
>       {
>         "user": "taro",
>         "age": -1
>       }
>       """
>     Then ステータスコードは 400 である
> ```
>
> 長い本文や構造化データを**安全に埋め込む**ための機能です。改行や引用符をそのまま保持できます。

---

## 5. タグ運用（@smoke 等）と実行フィルタ

- シナリオや機能に `@smoke`, `@regression`, `@wip`, `@slow`, `@critical` などの**タグ**を付与
- CI で `@smoke` のみを**高速実行**、夜間に `@regression` を**網羅実行**などの戦略が可能

> **title:** タグ付け例
>
> ```gherkin
> @auth @smoke
> Feature: ログイン機能
>
> @positive @critical
> Scenario: 正しい資格情報でログインできる
>   ...
>
> @negative @slow
> Scenario: ロックアウトが発生する
>   ...
> ```
>
> タグは**粒度のコントロールノブ**です。CI のマトリクス実行（タグ × ブラウザ × 環境）に向いています。

---

## 6. Cucumber Expressions と正規表現の使い分け

- **Cucumber Expressions:** `{int}`, `{string}`, `{word}`, `{float}` など**読みやすい**パターン
- **正規表現:** 複雑な書式・否定など**細かい制御**が必要な時に使用

> **title:** Cucumber Expressions と 正規表現の対比
>
> ```gherkin
> Scenario: カートに商品を入れる
>   When ユーザーが product_id 123 をカートに追加する
>   Then カートの合計は 1 である
> ```
>
> 読みやすさ優先なら `{int}` を使います。入力書式が複雑な場合のみ正規表現を選びます。**保守性**の観点で、まずは Cucumber Expressions を推奨します。

---

## 7. 多言語ステップ定義（Java / JS / Python / Ruby / .NET）

> **title:** Java（Cucumber-JVM）
>
> ```java
> // src/test/java/steps/LoginSteps.java
> package steps;
>
> import io.cucumber.java.en.*;
> import static org.junit.jupiter.api.Assertions.*;
>
> public class LoginSteps {
>   @Given("ユーザーがログインページを開いている")
>   public void openLoginPage() {
>     // navigateTo("/login");
>   }
>
>   @When("ユーザー名 {string} とパスワード {string} を入力する")
>   public void inputCredentials(String user, String pass) {
>     // type("#username", user);
>     // type("#password", pass);
>   }
>
>   @When("ログインボタンを押す")
>   public void clickLogin() {
>     // click("#login");
>   }
>
>   @Then("ダッシュボードが表示される")
>   public void assertDashboard() {
>     // assertTrue(isVisible("#dashboard"));
>     assertTrue(true);
>   }
> }
> ```
>
> `io.cucumber.java.en.*` を用いた**Glue コード**の例です。UI 自動化ツール（Selenium/Playwright 等）呼び出しはここに集約します。

> **title:** JavaScript（Cucumber.js + Playwright）
>
> ```javascript
> // features/step_definitions/login.steps.js
> const { Given, When, Then } = require("@cucumber/cucumber");
> const { expect } = require("@playwright/test");
>
> Given("ユーザーがログインページを開いている", async function () {
>   await this.page.goto("https://example.com/login");
> });
>
> When(
>   "ユーザー名 {string} とパスワード {string} を入力する",
>   async function (user, pass) {
>     await this.page.fill("#username", user);
>     await this.page.fill("#password", pass);
>   },
> );
>
> When("ログインボタンを押す", async function () {
>   await this.page.click("#login");
> });
>
> Then("ダッシュボードが表示される", async function () {
>   await expect(this.page.locator("#dashboard")).toBeVisible();
> });
> ```
>
> `World` に `page` を注入して**ブラウザ操作**を行う典型パターンです。

> **title:** Python（Behave）
>
> ```python
> # features/steps/login_steps.py
> from behave import given, when, then
>
> @given('ユーザーがログインページを開いている')
> def step_open_login(context):
>     # context.browser.get("/login")
>     pass
>
> @when('ユーザー名 "{user}" とパスワード "{passw}" を入力する')
> def step_input_credentials(context, user, passw):
>     # context.page.fill("#username", user)
>     # context.page.fill("#password", passw)
>     pass
>
> @when('ログインボタンを押す')
> def step_click_login(context):
>     # context.page.click("#login")
>     pass
>
> @then('ダッシュボードが表示される')
> def step_assert_dashboard(context):
>     # assert context.page.is_visible("#dashboard")
>     assert True
> ```
>
> Behave は**デコレータ**でステップをバインドします。`context` に共有オブジェクトを載せます。

> **title:** Ruby（Cucumber-Ruby）
>
> ```ruby
> # features/step_definitions/login_steps.rb
> Given('ユーザーがログインページを開いている') do
>   # visit('/login')
> end
>
> When('ユーザー名 {string} とパスワード {string} を入力する') do |user, pass|
>   # fill_in 'username', with: user
>   # fill_in 'password', with: pass
> end
>
> When('ログインボタンを押す') do
>   # click_button 'login'
> end
>
> Then('ダッシュボードが表示される') do
>   # expect(page).to have_css('#dashboard')
> end
> ```
>
> もっとも古典的な実装です。Capybara との親和性が高いです。

> **title:** C#（SpecFlow）
>
> ```csharp
> // Steps/LoginSteps.cs
> using TechTalk.SpecFlow;
> using FluentAssertions;
>
> [Binding]
> public class LoginSteps
> {
>     [Given(@"ユーザーがログインページを開いている")]
>     public void GivenOpenLogin()
>     {
>         // Navigate("/login");
>     }
>
>     [When(@"ユーザー名 ""(.*)"" とパスワード ""(.*)"" を入力する")]
>     public void WhenInputCredentials(string user, string pass)
>     {
>         // Type("#username", user);
>         // Type("#password", pass);
>     }
>
>     [When(@"ログインボタンを押す")]
>     public void WhenClickLogin()
>     {
>         // Click("#login");
>     }
>
>     [Then(@"ダッシュボードが表示される")]
>     public void ThenDashboardVisible()
>     {
>         true.Should().BeTrue();
>     }
> }
> ```
>
> SpecFlow は .NET 向けの代表格。`[Binding]` 属性でステップ定義クラスを宣言します。

---

## 8. プロジェクト構成と命名規約

- `/features`: `.feature` ファイル（ドメイン別にサブフォルダ）
- `/features/step_definitions`: ステップ定義（言語別）
- `/features/support`: Hooks（before/after）、World セットアップ
- `/fixtures` や `/testdata`: **テストデータ**の外出し
- 命名は「**ユースケース（機能）** → ファイル」「**振る舞い** → シナリオ」へ揃える

> **title:** 典型的なディレクトリ構成
>
> ```text
> project_root
> ├─ features
> │  ├─ auth
> │  │  ├─ login.feature
> │  │  └─ lockout.feature
> │  ├─ catalog
> │  │  └─ search.feature
> │  ├─ step_definitions
> │  │  ├─ login.steps.js
> │  │  └─ search.steps.js
> │  └─ support
> │     ├─ hooks.js
> │     └─ world.js
> ├─ fixtures
> │  └─ users.json
> └─ ci
>    └─ pipeline.yaml
> ```
>
> 機能単位の**疎結合**と、ステップ定義の**再利用**を両立します。テストデータは**固定化**し、環境ごとの差分は構成ファイルで吸収します。

---

## 9. BDD プロセス（Three Amigos / Example Mapping）

> **title:** BDD コラボレーション（Three Amigos）
>
> ```mermaid
> sequenceDiagram
>   participant PO as Product_Owner
>   participant QA as QA_Engineer
>   participant DEV as Developer
>   PO->>QA: ユーザーストーリーの目的を共有
>   QA->>DEV: 例と境界条件を列挙
>   DEV->>PO: 実装観点からの制約を提示
>   PO->>DEV: 受け入れ基準を確定
>   QA->>PO: Gherkin 下書きを提示
>   DEV->>QA: 実行可能性の確認
>   PO->>QA: 仕様合意
> ```
>
> 要件（PO）・品質（QA）・実装（DEV）の**3 者合意**で “曖昧さ” を先に潰し、Gherkin を**合意の記録**とします。

> **title:** Gherkin が入る自動化パイプライン
>
> ```mermaid
> flowchart LR
>   A[User_Story] -->|Refine| B[Examples_in_Gherkin]
>   B -->|Commit| C[Version_Control]
>   C -->|Trigger| D[CI_Run_Smoke]
>   D -->|Report| E[Living_Documentation]
>   E -->|Feedback| A
> ```
>
> 仕様→テスト→レポートが循環し、**変更に強い仕様**が維持されます。

---

## 10. アンチパターンと改善パターン

- **UI 詳細だらけ**（クリック/セレクタ連発）→ **意図ベース**へ（「ログインする」「商品を追加する」）
- **1 シナリオが長い**（10 ステップ超）→ **関心ごとで分割**、Outline で網羅
- **Then が複数観点**（UI + DB + ログ）→ **最重要な “振る舞いの結果” のみ**に絞る。下層の詳細検証は別テストへ
- **不安定化**（待機、時間依存）→ **リトライ/明示待機/テストダブル**の導入、テストデータの**固定化**

> **title:** “実装寄り” を “意図寄り” にリライト
>
> ```gherkin
> # 悪い例（実装詳細）
> When #username に "taro" を入力して #password に "P@ssw0rd" を入力して #login をクリックする
> Then #dashboard が 1 秒以内に表示される
>
> # 良い例（意図）
> When ユーザー名 "taro" とパスワード "P@ssw0rd" を入力する
> And ログインボタンを押す
> Then ダッシュボードが表示される
> ```
>
> 仕様は**意図（何を）**を語り、**手段（どうやって）**は Glue に閉じ込めます。

---

## 11. CI/CD とレポーティング

- **スイート設計:** `@smoke` を PR 時に、`@regression` を夜間に、`@critical` をデプロイ前に
- **出力:** JUnit/XML, JSON, HTML レポート（履歴比較・トレンド分析）
- **失敗時のアーティファクト:** スクリーンショット、HAR、ログ、動画

> **title:** CI の最小パイプライン（擬似 YAML）
>
> ```yaml
> name: bdd-pipeline
> on:
>   pull_request:
>   push:
> jobs:
>   smoke:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>       - uses: actions/setup-node@v4
>       - run: npm ci
>       - run: npx cucumber-js --tags "@smoke" --format html:reports/smoke.html
>       - uses: actions/upload-artifact@v4
>         with:
>           name: smoke-report
>           path: reports/smoke.html
>   regression:
>     if: github.event_name == 'push' && github.ref == 'refs/heads/main'
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>       - uses: actions/setup-node@v4
>       - run: npm ci
>       - run: npx cucumber-js --tags "@regression" --format json:reports/regression.json
> ```
>
> タグを**ブランチ/イベント**に応じて切り替え、レポートをアーティファクト化します。

---

## 12. 並列実行・データ分離・テスト安定化

- **並列化:** シナリオ単位の独立性を高め、**共有状態の排除**（DB/キャッシュ/セッション）
- **テストデータ:** 事前に**固定化**（フィクスチャ）し、ID 衝突や漏れを回避
- **安定化:** 冪等 API の利用、**明示的な待機条件**（UI は要素の表示/非表示、API は完了ポーリング）
- **時間依存:** 擬似クロックや注入可能な `Clock` で**凍結**し、$ \text{Flakiness} \propto f(\text{Time}, \text{Asynchrony}) $ を最小化

---

## 13. 非機能要件・外部連携の扱い方

- Gherkin は**振る舞い（機能）**に強い一方、**性能・セキュリティ・可用性**などは補助的に扱う
- 非機能は**計測や検証の事実**を Then に含めると実用的（例：応答時間閾値、監査ログ出力の有無）
- 外部 API 連携は**テストダブル**（WireMock 等）で**決定論**を確保

> **title:** 性能しきい値の例
>
> ```gherkin
> Feature: 検索の性能
>   Scenario: 上位 100 件の検索は 500ms 未満で返る
>     When ユーザーが "shoes" を検索する
>     Then 応答時間は 500ms 未満である
> ```
>
> 測定はステップ定義で行い、**閾値とシナリオ**を仕様に残します。

---

## 14. バージョニング・レビューフロー・運用ガイド

- `.feature` は**コードと同等**に Pull Request でレビュー
- **レビューチェックリスト:**
  1. シナリオは**ユーザー価値**を表しているか
  2. ステップは**意図ベース**で、**1 ステップ 1 行為**か
  3. データは Examples / Table / Fixture に**分離**されているか
  4. タグが**テスト戦略**と合っているか（@smoke/@regression/@critical）
  5. ネーミングが**一貫**しているか（機能/ルール/シナリオ）

> **title:** レビューフローの図解
>
> ```mermaid
> flowchart TD
>   Author[Author_Feature_Branch] -->|Open_PR| Reviewers[Peer_Reviewers]
>   Reviewers -->|Comments| Author
>   Author -->|Fix| Reviewers
>   Reviewers -->|Approve| Main[Main_Branch]
>   Main -->|CI_Regression| Reports[Reports_Dashboard]
> ```
>
> 仕様は**常にレビュー**され、CI の結果が**フィードバック**として戻ります。

---

## 15. よくある質問（FAQ）

**Q1. Gherkin で UI セレクタ名を書いてはいけないの？**  
A. 禁止ではありませんが、**保守性が下がる**ため推奨しません。Gherkin は**意図**、Glue が**手段**という分離が原則です。

**Q2. 一つのシナリオに複数の Then を書いていい？**  
A. 可能ですが、**失敗原因の特定**が難しくなります。重要な結果に絞るか、シナリオを**分割**するのが無難です。

**Q3. 日本語で書いても大丈夫？**  
A. 主要ツールは**多言語対応**です。文字エンコーディングは UTF-8 を推奨します。

**Q4. モバイル/組込み/バックエンドでも使える？**  
A. Yes。UI だけでなく、API、メッセージング、バッチ、デバイス制御の**振る舞い**にも適用できます。

**Q5. 既存の手動テスト手順書はどう移行する？**  
A. まずは**受け入れ基準（意図）**を抽出 → 成功/失敗の**例**に再構成 → 重要な経路から**@smoke** を自動化。

---

## 16. 参考情報と学習リソース（概念）

- **公式ドキュメント群（キーワード別）**
  - Gherkin 基本構文、タグ、Outline、Data Table、DocString
  - Cucumber（JVM/JS/Ruby）、Behave（Python）、SpecFlow（.NET）
- **キーワードでの探索のヒント**
  - “Cucumber Expressions vs Regular Expressions”
  - “Three Amigos BDD” / “Example Mapping”
  - “Living documentation cucumber report”

> もし特定ツール（例：Cucumber.js + Playwright、SpecFlow + Selenium）の**社内標準**や**既存テンプレート**があれば、それをベースに命名規約・タグ戦略・CI 設定を合わせると導入が最短です。

---

# 付録

## A. サンプル Feature（日本語・英語併記）

> **title:** 日本語版 Feature
>
> ```gherkin
> Feature: カート機能
>   ユーザーとして、商品をカートに追加して購入準備をしたい
>
>   Rule: 在庫がある商品だけ追加できる
>     Background:
>       Given ユーザーが空のカートを持っている
>
>     Scenario: 在庫あり商品は追加できる
>       Given 商品 "red_shoes" の在庫が 5 ある
>       When ユーザーが "red_shoes" をカートに追加する
>       Then カートの合計点数は 1 である
>
>     Scenario: 在庫切れ商品は追加できない
>       Given 商品 "blue_shoes" の在庫が 0 である
>       When ユーザーが "blue_shoes" をカートに追加する
>       Then エラーメッセージ "在庫切れです" が表示される
> ```
>
> **ルール**を使って意図を示し、**背景**で共通前提をまとめた構造です。

> **title:** 英語版（同内容）
>
> ```gherkin
> Feature: Shopping Cart
>   As a shopper, I want to add products to my cart to prepare for purchase
>
>   Rule: Only in-stock items can be added
>     Background:
>       Given the user has an empty cart
>
>     Scenario: Add an in-stock product
>       Given the product "red_shoes" has 5 in stock
>       When the user adds "red_shoes" to the cart
>       Then the cart item count is 1
>
>     Scenario: Prevent adding an out-of-stock product
>       Given the product "blue_shoes" has 0 in stock
>       When the user adds "blue_shoes" to the cart
>       Then the error message "Out of stock" is shown
> ```
>
> 多言語でも**意味同一**の Feature を保てば、国際チームでもレビューが容易です。

---

## B. ステップ定義の再利用ガイド

> **title:** “意図ベース” の語彙を標準化する
>
> ```text
> 語彙例（推奨）
> - ユーザーが <ページ> を開いている
> - ユーザーが <商品> を検索する
> - ユーザーが <商品> をカートに追加する
> - 結果は <result> である
> - エラーメッセージ "<msg>" が表示される
> ```
>
> 語彙を共通化することで**再利用性**が増し、ステップ定義の**爆発**を抑制できます。

---

## C. アーキテクチャ全体図（Gherkin→自動化）

> **title:** Gherkin から自動化への流れ
>
> ```mermaid
> flowchart LR
>   FEAT[Feature_Files] -->|Bind| GLUE[Step_Definitions]
>   GLUE -->|Call| HELP[Helper_Library]
>   HELP -->|Operate| SUT[System_Under_Test]
>   GLUE -->|Assert| REPORT[Test_Reports]
>   REPORT -->|Publish| LIVING[Living_Documentation]
> ```
>
> `Feature` は Glue にバインドされ、Helper で**副作用**を隔離し、**責務分離**を実現します。

---

## D. 実行コマンド例（概念）

> **title:** JS（cucumber-js）
>
> ```bash
> npx cucumber-js --tags "@smoke and not @wip" \
>   --format progress \
>   --format html:reports/smoke.html
> ```
>
> タグ式（and/or/not）で**柔軟に選別**できます。

> **title:** JVM（maven-surefire）
>
> ```bash
> mvn -q -Dtest=RunCukesTest test \
>   -Dcucumber.filter.tags="@regression" \
>   -Dcucumber.plugin="json:reports/regression.json"
> ```
>
> プラグインで**複数フォーマット**を同時出力します。

> **title:** .NET（SpecFlow+Runner）
>
> ```bash
> dotnet test --filter TestCategory=smoke
> ```
>
> カテゴリ（=タグ）でフィルタリングします。

---

## E. チェックリスト（導入～運用）

- [ ] Three Amigos で**受け入れ基準**と**例**を合意
- [ ] 最優先の**ユーザージャーニー**から @smoke を作る
- [ ] ステップは**意図ベース**、1 ステップ 1 行為
- [ ] データは Examples / Table / Fixture へ分離
- [ ] タグ戦略（@smoke/@regression/@critical/@wip）を定義
- [ ] CI に組み込み、PR ごとに **@smoke** を自動実行
- [ ] レポートを**可視化**（ダッシュボード）し、品質トレンドをレビュー
- [ ] 不安定テストは**隔離・修繕**し、常にグリーンを維持

---

## 日本語対応

### ✅ Gherkin は日本語で書けるの？

**はい、書けます。**  
Gherkin は **自然言語に近い構文**で書けるため、日本語の `.feature` ファイルも普通に利用できます。  
実際に、日本語での記述例も多数紹介されています。 [\[it-biz.online\]](https://it-biz.online/it-skills/gherkin/)

---

### ✅ 日本語に対応しているツールはある？

はい、多くのツールが **日本語 Gherkin に対応**しています。

#### ● VSCode の拡張機能「Gherkin Support」

- `.feature` ファイルの日本語構文を完全サポート
- 日本語キーワード：
  - 機能（Feature）
  - 背景（Background）
  - シナリオ
  - 前提（Given）
  - もし（When）
  - ならば（Then）
  - かつ（And） など
- 日本語のサンプルも同梱 [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=Enokisan.gherkin-support)

#### ● Cucumber / Karate / Apidog など主要ツール

すべて日本語で書いた Gherkin を解釈できます。

- Gherkin 自体が **英語・日本語など自然言語に近い形式で書ける**設計
- 日本語のシナリオ例も活用可能 [\[it-biz.online\]](https://it-biz.online/it-skills/gherkin/), [\[apidog.com\]](https://apidog.com/jp/blog/gherkin-guide-bdd-api-testing-jp/)

---

### 📝 日本語での Gherkin 例（実際に使える）

```gherkin
# language: ja
機能: ログイン機能
  システムにログインできるようにしたい

  背景:
    前提 システムが起動している

  シナリオ: 正常ログイン
    前提 ユーザー "田中" が登録されている
    もし ユーザー名 "tanaka" でログインする
    ならば ログインが成功する
    かつ ホーム画面が表示される
```

これは VSCode 拡張「Gherkin Support」に含まれる日本語例と同等形式です。 [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=Enokisan.gherkin-support)

## まとめ

Gherkin は**仕様＝テスト**を実現し、関係者全員の**共通言語**として機能します。成功の鍵は、

1. **意図**を中心に書く、
2. **データと手段**を分離する、
3. **タグと CI** で継続的に回す、  
   の 3 点に集約されます。小さく始めて学びを回し、スイートを**戦略的に拡張**していきましょう。
