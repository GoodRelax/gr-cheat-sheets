
# Gherkin リファレンス (和訳)

 出典: [Cucumber - Gherkin Reference](https://cucumber.io/docs/gherkin/reference)（最終更新日: 2025年1月26日）

Gherkin は、実行可能な仕様に構造と意味を与えるための特別な[キーワード](#キーワード)を使用します。各キーワードは多くの自然言語に翻訳されています。このリファレンスでは英語を使用します。

Gherkin ドキュメントのほとんどの行は、[キーワード](#キーワード)のいずれかで始まります。

コメントは、フィーチャファイル内のどこでも、新しい行の先頭にのみ記述できます。ゼロ個以上のスペースの後にハッシュ記号（`#`）とテキストを続けます。

ブロックコメントは、現在 Gherkin ではサポートされていません。

インデントにはスペースまたはタブのいずれかを使用できます。推奨されるインデントレベルはスペース 2 つです。以下に例を示します：

**Gherkin の基本例：**

```gherkin
Feature: Guess the word

  # 最初の例は2つのステップを持つ
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # 2番目の例は3つのステップを持つ
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```

各ステップの末尾部分（キーワードの後）は、[ステップ定義](/docs/cucumber/step-definitions)と呼ばれるコードブロックにマッチングされます。

一部のキーワードにはコロン（`:`）が続きますが、続かないものもあることに注意してください。コロンが不要なキーワードの後にコロンを追加すると、テストは無視されます。

---

## キーワード

空行でない各行は、Gherkin の _キーワード_ で始まり、その後に任意のテキストを続ける必要があります。唯一の例外は、`Example`/`Scenario`、`Background`、`Scenario Outline`、`Rule` の行の下に配置される自由記述の説明文です。

主要なキーワードは以下の通りです：

- `Feature`
- `Rule`（Gherkin 6 以降）
- `Example`（または `Scenario`）
- `Given`、`When`、`Then`、`And`、`But`（ステップ用）（または `*`）
- `Background`
- `Scenario Outline`（または `Scenario Template`）
- `Examples`（または `Scenarios`）

副次的なキーワードもいくつかあります：

- `"""`（Doc Strings）
- `|`（Data Tables）
- `@`（タグ）
- `#`（コメント）

> **ローカライズ:** Gherkin は多くの[自然言語](#自然言語)に対応しており、それぞれの言語でこれらのキーワードに相当するものがあります。

---

### Feature

`Feature` キーワードの目的は、ソフトウェアの機能の高レベルな説明を提供し、関連するシナリオをグループ化することです。

Gherkin ドキュメントの最初の主要キーワードは、常に `Feature` でなければならず、その後にコロン（`:`）と機能を説明する短いテキストが続きます。

`Feature` の下に自由記述のテキストを追加して、さらに詳しい説明を記述できます。

これらの説明行は Cucumber の実行時には無視されますが、レポートツール（公式の HTML フォーマッタなど）では利用できます。

**Feature の例：**

```gherkin
Feature: Guess the word

  The word guess game is a turn-based game for two players.
  The Maker makes a word for the Breaker to guess. The game
  is over when the Breaker guesses the Maker's word.

  Example: Maker starts a game
```

名前とオプションの説明は、Cucumber にとって特別な意味を持ちません。機能の重要な側面（簡単な説明やビジネスルールのリストなど）を文書化するための場所です。

`Feature` の自由記述は、`Background`、`Rule`、`Example`、または `Scenario Outline`（またはそのエイリアスキーワード）で始まる行が現れると終了します。

`Feature` の上に[タグ](/docs/cucumber/api/#tags)を配置して、ファイルやディレクトリ構造とは独立に関連する機能をグループ化できます。

1つの `.feature` ファイルには、`Feature` を1つだけ持つことができます。

---

### Descriptions（説明文）

自由記述の説明文（`Feature` で前述したもの）は、`Example`/`Scenario`、`Background`、`Scenario Outline`、`Rule` の下にも配置できます。

キーワードで始まらない限り、何でも自由に記述できます。

説明文は Markdown 形式で記述でき、公式の HTML フォーマッタを含むフォーマッタがこれをサポートしています。

---

### Rule

（オプションの）`Rule` キーワードは、Gherkin v6 から導入されました。

`Rule` キーワードの目的は、実装すべき1つの _ビジネスルール_ を表現することです。フィーチャに対する追加情報を提供します。`Rule` は、この _ビジネスルール_ に属する複数のシナリオをグループ化するために使用されます。`Rule` には、その特定のルールを説明する1つ以上のシナリオを含める必要があります。

**Rule の例：**

```gherkin
# -- FILE: features/gherkin.rule_example.feature
Feature: Highlander

  Rule: There can be only One

    Example: Only One -- More than one alive
      Given there are 3 ninjas
      And there are more than one ninja alive
      When 2 ninjas meet, they will fight
      Then one ninja dies (but not me)
      And there is one ninja less alive

    Example: Only One -- One alive
      Given there is only 1 ninja alive
      Then they will live forever ;-)

  Rule: There can be Two (in some cases)

    Example: Two -- Dead and Reborn as Phoenix
      ...
```

---

### Example

これは、ビジネスルールを _具体的に説明する_ 例です。[ステップ](#ステップ)のリストで構成されます。

キーワード `Scenario` は、キーワード `Example` の同義語です。

ステップはいくつでも持てますが、1つの例につき 3〜5 ステップを推奨します。ステップが多すぎると、仕様やドキュメントとしての表現力が失われます。

仕様やドキュメントであると同時に、例は _テスト_ でもあります。全体として、例はシステムの _実行可能な仕様_ です。

例は以下のパターンに従います：

- 初期コンテキストの記述（`Given` ステップ）
- イベントの記述（`When` ステップ）
- 期待される結果の記述（`Then` ステップ）

---

### Steps（ステップ）

各ステップは `Given`、`When`、`Then`、`And`、または `But` で始まります。

Cucumber はシナリオ内の各ステップを、記述された順序で1つずつ実行します。Cucumber がステップを実行しようとする際、一致するステップ定義を探して実行します。

キーワードはステップ定義の検索時に考慮されません。つまり、`Given`、`When`、`Then`、`And`、`But` のステップで同じテキストを持つ別のステップを作成することはできません。

Cucumber は以下のステップを重複とみなします：

**重複するステップの例：**

```gherkin
Given there is money in my account
Then there is money in my account
```

これは制約のように見えるかもしれませんが、より曖昧さの少ない、明確なドメイン言語を考えることを強制します：

**改善されたステップの例：**

```gherkin
Given my account has a balance of £430
Then my account should have a balance of £430
```

#### Given

`Given` ステップは、システムの初期コンテキスト、つまりシナリオの _場面設定_ を記述するために使用されます。通常、_過去_ に起こったことを表します。

Cucumber が `Given` ステップを実行すると、オブジェクトの作成や設定、テストデータベースへのデータ追加など、システムを明確に定義された状態に設定します。

`Given` ステップの目的は、ユーザー（または外部システム）が（`When` ステップで）システムと対話を始める前に、**システムを既知の状態にすること**です。`Given` ではユーザーの操作について語ることを避けてください。ユースケースを作成する場合、`Given` は前提条件にあたります。

複数の `Given` ステップがあっても問題ありません（読みやすくするために、2番目以降は `And` や `But` を使用してください）。

例：

- Mickey と Minnie がゲームを開始した
- ログイン済みである
- Joe の残高が £42 である

#### When

`When` ステップは、イベントまたは _アクション_ を記述するために使用されます。ユーザーがシステムと対話することや、別のシステムによってトリガーされるイベントを表すことができます。

例：

- 単語を推測する
- 友達を招待する
- お金を引き出す

> **1922年を想像してください：** ほとんどのソフトウェアは、人が手動で行えること（ただし効率的ではない）を行います。テクノロジーやユーザーインターフェースについての前提を置かない例を考えてください。1922年、コンピュータがなかった時代を想像してください。実装の詳細は[ステップ定義](/docs/cucumber/step-definitions)に隠すべきです。

#### Then

`Then` ステップは、_期待される_ 結果やアウトカムを記述するために使用されます。

`Then` ステップのステップ定義では、_アサーション_ を使用して、_実際の_ 結果（システムが実際に行うこと）と _期待される_ 結果（ステップがシステムに行うべきと記述していること）を比較する必要があります。

結果は **観察可能な** 出力にすべきです。つまり、システムから _出てくるもの_（レポート、ユーザーインターフェース、メッセージ）であり、システムの奥深くに埋もれた動作（データベースのレコードなど）ではありません。

例：

- 推測した単語が間違いだったことを確認する
- 招待を受け取る
- カードが吸い込まれるべきである

`Then` ステップをデータベースの確認として実装したくなるかもしれませんが、その誘惑に耐えてください！ユーザー（または外部システム）が観察可能な結果のみを検証すべきであり、データベースの変更は通常それに該当しません。

#### And, But

連続する `Given` や `Then` がある場合、以下のように書くこともできます：

**連続するキーワードの例：**

```gherkin
Example: Multiple Givens
  Given one thing
  Given another thing
  Given yet another thing
  When I open my eyes
  Then I should see something
  Then I shouldn't see something else
```

あるいは、連続する `Given` や `Then` を `And` や `But` に置き換えることで、より流れるような構造にできます：

**And と But を使った例：**

```gherkin
Example: Multiple Givens
  Given one thing
  And another thing
  And yet another thing
  When I open my eyes
  Then I should see something
  But I shouldn't see something else
```

#### \*（アスタリスク）

Gherkin では、通常のステップキーワードの代わりにアスタリスク（`*`）を使用することもサポートしています。これは、ステップが実質的に _項目のリスト_ である場合に、`And` などの自然言語ではあまり読みやすくならないときに、箇条書きのように表現するのに便利です。

**アスタリスクを使ったステップの例：**

```gherkin
Scenario: All done
  Given I am out shopping
  * I have eggs
  * I have milk
  * I have butter
  When I check my list
  Then I don't need anything
```

---

### Background

`Feature` 内のすべてのシナリオで同じ `Given` ステップを繰り返していることに気づく場合があります。

すべてのシナリオで繰り返されているということは、それらのステップがシナリオの記述に _不可欠_ なものではなく、_付随的な詳細_ であることを示しています。そのような `Given` ステップを `Background` セクションにまとめることで、文字通り背景に移動できます。

`Background` は、後続のシナリオにコンテキストを追加します。1つ以上の `Given` ステップを含み、各シナリオの前（ただし [Before フック](/docs/cucumber/api/#hooks)の後）に実行されます。

`Background` は、最初の `Scenario`/`Example` の前に、同じインデントレベルで配置されます。

**Background の例：**

```gherkin
Feature: Multiple site support
  Only blog owners can post to a blog, except administrators,
  who can post to all blogs.

  Background:
    Given a global administrator named "Greg"
    And a blog named "Greg's anti-tax rants"
    And a customer named "Dr. Bill"
    And a blog named "Expensive Therapy" owned by "Dr. Bill"

  Scenario: Dr. Bill posts to his own blog
    Given I am logged in as Dr. Bill
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."

  Scenario: Dr. Bill tries to post to somebody else's blog, and fails
    Given I am logged in as Dr. Bill
    When I try to post to "Greg's anti-tax rants"
    Then I should see "Hey! That's not your blog!"

  Scenario: Greg posts to a client's blog
    Given I am logged in as Greg
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."
```

`Background` は `Rule` レベルでもサポートされています：

**Rule レベルの Background の例：**

```gherkin
Feature: Overdue tasks
  Let users know when tasks are overdue, even when using other
  features of the app

  Rule: Users are notified about overdue tasks on first use of the day
    Background:
      Given I have overdue tasks

    Example: First use of the day
      Given I last used the app yesterday
      When I use the app
      Then I am notified about overdue tasks

    Example: Already used today
      Given I last used the app earlier today
      When I use the app
      Then I am not notified about overdue tasks
```

`Feature` または `Rule` ごとに `Background` ステップのセットは1つだけ持つことができます。異なるシナリオに異なる `Background` ステップが必要な場合は、シナリオのセットをより多くの `Rule` や `Feature` に分割することを検討してください。

`Background` のより明示的でない代替手段については、[条件付きフック](/docs/cucumber/api/#conditional-hooks)を参照してください。

#### Background 使用のヒント

- クライアントが実際に知る必要がある状態でない限り、`Background` を使って**複雑な状態**を設定しないでください。
  - 例えば、ユーザー名やサイト名がクライアントにとって重要でない場合は、`Given I am logged in as a site owner` のような高レベルなステップを使用してください。
- `Background` セクションは**短く**保ちましょう。
  - クライアントはシナリオを読む際にこの内容を覚えておく必要があります。`Background` が 4 行を超える場合は、関係のない詳細を高レベルなステップに移動することを検討してください。
- `Background` セクションを**生き生き**とさせましょう。
  - 色のある名前を使い、物語を伝えるようにしてください。人間の脳は `"User A"`、`"User B"`、`"Site 1"` のような名前よりも、物語をはるかによく記憶します。
- シナリオは**短く**保ち、数が多くなりすぎないようにしましょう。
  - `Background` セクションが画面外にスクロールしてしまうと、読者は何が起きているかの全体像を把握できなくなります。高レベルなステップの使用や、`*.feature` ファイルの分割を検討してください。

---

### Scenario Outline

`Scenario Outline` キーワードは、異なる値の組み合わせで同じ `Scenario` を複数回実行するために使用できます。

キーワード `Scenario Template` は、キーワード `Scenario Outline` の同義語です。

異なる値を使うためにシナリオをコピー＆ペーストすると、すぐに冗長で退屈になります：

**コピーペーストによる繰り返しの例：**

```gherkin
Scenario: eat 5 out of 12
  Given there are 12 cucumbers
  When I eat 5 cucumbers
  Then I should have 7 cucumbers

Scenario: eat 5 out of 20
  Given there are 20 cucumbers
  When I eat 5 cucumbers
  Then I should have 15 cucumbers
```

これらの2つの類似したシナリオを `Scenario Outline` に集約できます。

シナリオアウトラインでは、`< >` で区切られたパラメータを持つテンプレートを使用して、より簡潔に表現できます：

**Scenario Outline の例：**

```gherkin
Scenario Outline: eating
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |
    |    20 |   5 |   15 |
```

---

### Examples

`Scenario Outline` には、1つ以上の `Examples`（または `Scenarios`）セクションが必要です。そのステップはテンプレートとして解釈され、直接実行されることはありません。代わりに、`Scenario Outline` はその下にある `Examples` セクションの各行（最初のヘッダー行を除く）に対して _1回ずつ_ 実行されます。

ステップでは、Examplesテーブルのヘッダーを参照する `<>` で区切られた _パラメータ_ を使用できます。Cucumber はステップをステップ定義とマッチングする _前に_、これらのパラメータをテーブルの値で置き換えます。

`Scenario Outline` の説明文でもパラメータを使用できます。

[マルチラインステップ引数](#ステップ引数)でもパラメータを使用できます。

---

## ステップ引数

場合によっては、1行に収まる以上のデータをステップに渡したいことがあります。この目的のために、Gherkin には `Doc Strings` と `Data Tables` があります。

### Doc Strings

`Doc Strings` は、ステップ定義に大きなテキストブロックを渡すのに便利です。

テキストは、それぞれ独立した行に置かれた3つのダブルクォートマークで区切られる必要があります：

**Doc Strings の例：**

```gherkin
Given a blog post named "Random" with Markdown body
  """
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
```

ステップ定義では、このテキストを見つけてパターンにマッチングさせる必要はありません。ステップ定義の最後の引数として自動的に渡されます。

開始の `"""` のインデントは重要ではありませんが、囲んでいるステップから 2 スペースのインデントが一般的です。ただし、トリプルクォート内のインデントは重要です。Doc String の各行は開始の `"""` に基づいてデデントされます。したがって、開始の `"""` の列を超えるインデントは保持されます。

Doc Strings は、3つのバッククォートを区切り文字として使用することもサポートしています：

**バッククォートを使った Doc Strings の例：**

````gherkin
Given a blog post named "Random" with Markdown body
  ```
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  ```
````

これは Markdown での記述に慣れている方にはなじみがあるかもしれません。

> **ツールのバッククォート対応:** 現行のすべての Cucumber バージョンがバッククォートを区切り文字としてサポートしていますが、テキストエディタなど多くのツールはまだ対応していません。

トリプルクォートの後にコンテンツの種類を注釈として付けることも可能です。以下のように、トリプルクォートの後にコンテンツタイプを指定します：

**コンテンツタイプ付き Doc Strings の例：**

```gherkin
Given a blog post named "Random" with Markdown body
  """markdown
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
```

> **ツールのコンテンツタイプ対応:** 現行のすべての Cucumber バージョンがコンテンツタイプをサポートしていますが、テキストエディタなど多くのツールはまだ対応していません。

---

### Data Tables

`Data Tables` は、ステップ定義に値のリストを渡すのに便利です：

**Data Tables の例：**

```gherkin
Given the following users exist:
  | name   | email              | twitter         |
  | Aslak  | aslak@cucumber.io  | @aslak_hellesoy |
  | Julien | julien@cucumber.io | @jbpros         |
  | Matt   | matt@cucumber.io   | @mattwynne      |
```

`Doc Strings` と同様に、`Data Tables` もステップ定義の最後の引数として渡されます。

#### テーブルセルのエスケープ

テーブルセル内で改行文字を使用したい場合は、`\n` と記述できます。セルの一部として `|` が必要な場合は、`\|` としてエスケープできます。`\` が必要な場合は、`\\` でエスケープします。

#### Data Table API

Cucumber は、ステップ定義内からテーブルを操作するための豊富な API を提供しています。詳細については、[Data Table API リファレンス](https://github.com/cucumber/cucumber-jvm/tree/main/datatable)を参照してください。

---

## 自然言語

Gherkin で使用する言語は、ユーザーやドメインエキスパートがドメインについて話す際に使用する言語と同じであるべきです。2つの言語間の翻訳は避けるべきです。

これが、Gherkin が [70以上の言語](/docs/gherkin/languages)に翻訳されている理由です。

以下は、ノルウェー語で書かれた Gherkin シナリオです：

**ノルウェー語の Gherkin 例：**

```gherkin
# language: no
Funksjonalitet: Gjett et ord

  Eksempel: Ordmaker starter et spill
    Naar Ordmaker starter et spill
    Saa maa Ordmaker vente paa at Gjetter blir med

  Eksempel: Gjetter blir med
    Gitt at Ordmaker har startet et spill med ordet "bloett"
    Naar Gjetter blir med paa Ordmakers spill
    Saa maa Gjetter gjette et ord paa 5 bokstaver
```

フィーチャファイルの最初の行に `# language:` ヘッダーを記述することで、使用する自然言語を Cucumber に指示できます。例えば、フランス語の場合は `# language: fr` とします。このヘッダーを省略すると、Cucumber はデフォルトで英語（`en`）を使用します。

一部の Cucumber 実装では、設定でデフォルト言語を指定することもできるため、すべてのファイルに `# language` ヘッダーを配置する必要はありません。

---


