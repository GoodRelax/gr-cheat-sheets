# GoodRelax Naming Cheat Sheet

| Category      | 品詞   | Word         | ニュアンス                             | 使用例                      | 備考                                                |
| :------------ | :----- | :---------- | :------------------------------------- | :------------------------- | :-------------------------------------------------- |
| General       | 形容詞 | sync         | 同期操作                               | syncCall                    | 実行をブロックする                                  |
| General       | 形容詞 | async        | 非同期操作                             | asyncOperation              | ノンブロッキング実行                                |
| General       | 形容詞 | online       | ネットワークに接続されている           | onlineUsers                 | アクティブな接続                                    |
| General       | 形容詞 | offline      | 接続されていない                       | offlineMode                 | ネットワーク接続がない                              |
| General       | 形容詞 | inactive     | 現在アクティブではない                 | inactiveUser                | 休止状態                                            |
| General       | 形容詞 | invalid      | 基準を満たしていない                   | invalidInput                | バリデーションに失敗                                |
| General       | 形容詞 | concurrent   | 同時実行                               | concurrentTasks             | 一度に複数の操作を行う（並行）                      |
| General       | 形容詞 | parallel     | 並列実行パス                           | parallelProcessing          | 横並びでの実行                                      |
| General       | 形容詞 | sequential   | 順次的な実行                           | sequentialExecution         | 順序付けられた処理                                  |
| General       | 形容詞 | realtime     | 即時/ライブ更新                        | realtimeData                | 有意な遅延がない                                    |
| General       | 形容詞 | hidden       | 表示されない/アクセス不可              | hiddenField                 | 意図的に隠されている                                |
| General       | 形容詞 | critical     | 必須/優先度が高い                      | criticalSection             | 特別な注意が必要                                    |
| General       | 形容詞 | fatal        | 回復不能なエラー状態                   | fatalError                  | システムが継続できない                              |
| General       | 形容詞 | ready        | 使用準備ができている                   | readyState                  | 初期化完了                                          |
| General       | 形容詞 | ok           | 許容範囲内/成功                        | okStatus                    | 肯定的な確認                                        |
| General       | 名詞   | request      | サービスの呼び出し                     | httpRequest                 | サービスを要求する                                  |
| General       | 名詞   | response     | サービスの応答                         | httpResponse                | 要求への回答                                        |
| General       | 名詞   | client       | サービスの利用者                       | httpClient                  | サービスを要求する側                                |
| General       | 名詞   | host         | サーバー/コンテナ                      | hostName                    | サービスが稼働する場所                              |
| General       | 名詞   | consumer     | データ処理を行う側                     | messageConsumer             | 受信して処理する                                    |
| General       | 名詞   | supplier     | 値を提供する側                         | dataSupplier                | データの供給源                                      |
| General       | 名詞   | listener     | イベントの監視者                       | eventListener               | 通知を待機する                                      |
| General       | 名詞   | handler      | イベント/要求を処理するもの            | eventHandler                | 発生した事象に応答する                              |
| General       | 名詞   | callback     | 後で実行される関数                     | callbackFunction            | 遅延実行                                            |
| General       | 名詞   | event        | 発生した事象の通知                     | clickEvent                  | 何かが起きたこと                                    |
| General       | 名詞   | signal       | 通知の仕組み                           | processSignal               | プロセス間通信                                      |
| General       | 名詞   | message      | 通信の単位                             | errorMessage                | 情報のパッケージ                                    |
| General       | 名詞   | packet       | ネットワークデータの単位               | dataPacket                  | 送信されるデータの束                                |
| General       | 名詞   | payload      | 実際に運ばれるデータ                   | messagePayload              | 中核となるコンテンツ                                |
| General       | 名詞   | body         | 主要なコンテンツ部分                   | requestBody                 | messageのペイロード                                 |
| General       | 名詞   | header       | メタデータセクション                   | httpHeader                  | 記述的な情報                                        |
| General       | 名詞   | data         | 情報のペイロード                       | userData                    | 生の（加工されていない）情報                        |
| General       | 名詞   | content      | 実際のデータ/中身                      | pageContent                 | 実質的な情報                                        |
| General       | 名詞   | context      | 実行環境                               | applicationContext          | 取り巻く状態/データ                                 |
| General       | 名詞   | model        | データ構造/表現                        | dataModel                   | ドメインの表現                                      |
| General       | 名詞   | entity       | ドメインオブジェクト                   | userEntity                  | ビジネスモデルオブジェクト                          |
| General       | 名詞   | object       | 汎用的なインスタンス                   | dataObject                  | 汎用的なコンテナ                                    |
| General       | 名詞   | view         | ユーザーインターフェース表現           | dataView                    | 表示レイヤー                                        |
| General       | 名詞   | list         | 順序付きのコレクション                 | itemList                    | シーケンシャルなコンテナ                            |
| General       | 名詞   | stream       | データの流れ                           | fileStream                  | 連続したデータシーケンス                            |
| General       | 名詞   | iterator     | 順次アクセサー                         | listIterator                | コレクションを横断（走査）する                      |
| General       | 名詞   | generator    | シーケンスを作成するもの               | idGenerator                 | 要求に応じて値を生成する                            |
| General       | 名詞   | cache        | 高速アクセス用ストレージ               | cacheManager                | パフォーマンスの最適化                              |
| General       | 名詞   | buffer       | 一時的な保存領域                       | dataBuffer                  | 中間的な保持スペース                                |
| General       | 名詞   | pool         | 再利用可能なリソースセット             | connectionPool              | 共有リソース                                        |
| General       | 名詞   | session      | 状態を持つ対話                         | userSession                 | 会話のコンテキスト                                  |
| General       | 名詞   | account      | ユーザーアカウントデータ               | userAccount                 | アイデンティティのコンテナ                          |
| General       | 名詞   | preferences  | ユーザー設定（好み）                   | userPreferences             | カスタマイズオプション                              |
| General       | 名詞   | settings     | 構成値                                 | appSettings                 | 調整可能なパラメータ                                |
| General       | 名詞   | action       | 実行可能な操作                         | actionHandler               | 実行すべきコマンド                                  |
| General       | 名詞   | transaction  | アトミックな操作単位                   | databaseTransaction         | 「全か無か」の操作                                  |
| General       | 名詞   | savepoint    | ロールバック用のチェックポイント       | transactionSavepoint        | 部分的なコミットポイント                            |
| General       | 名詞   | alert        | 通知メッセージ                         | alertDialog                 | ユーザーへの警告または情報                          |
| General       | 名詞   | failure      | 失敗した結果                           | operationFailure            | 成功しなかった                                      |
| General       | 名詞   | success      | 成功した結果                           | operationSuccess            | 意図した通りに完了した                              |
| General       | 名詞   | resource     | システム資産                           | fileResource                | 利用可能な項目                                      |
| General       | 名詞   | mutex        | 相互排他ロック                         | resourceMutex               | 同時アクセスを防ぐ                                  |
| General       | 名詞   | semaphore    | 計数による同期                         | resourceSemaphore           | アクセス数を制御する                                |
| General       | 名詞   | uri          | リソース識別子                         | resourceUri                 | 統一識別子                                          |
| General       | 名詞   | url          | Webアドレス                            | pageUrl                     | Web上の場所                                         |
| General       | 名詞   | endpoint     | APIアクセスポイント                    | apiEndpoint                 | 特定のURL/アドレス                                  |
| General       | 名詞   | port         | 通信のエンドポイント                   | serverPort                  | ネットワークアドレス                                |
| General       | 名詞   | route        | パス/マッピング                        | apiRoute                    | ハンドラへのURLマッピング                           |
| General       | 名詞   | utility      | ヘルパー関数                           | stringUtility               | 再利用可能なツール                                  |
| General       | 名詞   | api          | アプリケーションインターフェース       | apiClient, externalApi      | 外部通信インターフェース                            |
| General       | 名詞   | record       | データエントリー                       | databaseRecord              | 単一のデータ項目                                    |
| General       | 動詞   | accept       | 受信に同意する                         | acceptConnection()          | 入ってくるものを承認する                            |
| General       | 動詞   | reject       | 拒否/失敗させる                        | reject(request)             | 辞退する                                            |
| General       | 動詞   | allow        | 許可を与える                           | allowAccess()               | アクションを有効にする                              |
| General       | 動詞   | deny         | 許可を拒否する                         | denyAccess()                | アクションをブロックする                            |
| General       | 動詞   | open         | アクセス可能にする                     | open(file)                  | アクセスを開始する                                  |
| General       | 動詞   | close        | 終了/閉じる                            | closeConnection()           | リソースをシャットダウンする                        |
| General       | 動詞   | lock         | 排他的アクセス権を取得する             | lock(resource)              | 同時使用を防ぐ                                      |
| General       | 動詞   | unlock       | ロックを解除する                       | unlock(resource)            | アクセスを許可する                                  |
| General       | 動詞   | bind         | 関連付ける/接続する                    | bindEvent()                 | リンクさせる                                        |
| General       | 動詞   | unbind       | 関連付けを解除する                     | unbind(event)               | 切断する                                            |
| General       | 動詞   | attach       | 接続する                               | attachListener()            | 関連付ける                                          |
| General       | 動詞   | detach       | 切断する                               | detachListener()            | 関連付けを削除する                                  |
| General       | 動詞   | mount        | 取り付ける/利用可能にする              | mount(component)            | システムにインストールする                          |
| General       | 動詞   | unmount      | 取り外す/分離する                      | unmount(component)          | システムからアンインストールする                    |
| General       | 動詞   | subscribe    | 通知を登録する                         | subscribe(topic)            | イベントをリッスンする                              |
| General       | 動詞   | unsubscribe  | 購読をキャンセルする                   | unsubscribe(topic)          | リッスンを停止する                                  |
| General       | 動詞   | join         | 結合する/待機する                      | join(threads)               | マージまたは同期する                                |
| General       | 動詞   | merge        | 統合する                               | merge(branches)             | 一つにする                                          |
| General       | 動詞   | split        | 部分に分割する                         | split(string, delimiter)    | 切り離す                                            |
| General       | 動詞   | enqueue      | キュー（待ち行列）に追加する           | enqueue(item)               | 末尾に追加する                                      |
| General       | 動詞   | dequeue      | キューから取り除く                     | dequeue()                   | 先頭から取り出す                                    |
| General       | 動詞   | pop          | スタックから取り除く                   | pop()                       | 一番上から取り出す                                  |
| General       | 動詞   | peek         | 取り除かずに見る                       | peek()                      | 非破壊的な参照                                      |
| General       | 動詞   | serialize    | シリアル形式に変換する                 | serialize(object)           | 送信可能な状態にする                                |
| General       | 動詞   | deserialize  | シリアル形式から変換する               | deserialize(bytes)          | オブジェクトを再構築する                            |
| General       | 動詞   | encode       | エンコード形式に変換する               | encode(data)                | フォーマットを変換する                              |
| General       | 動詞   | decode       | エンコード済みから変換する             | decode(data)                | エンコーディングを逆変換する                        |
| General       | 動詞   | deploy       | 環境にリリースする                     | deploy()                    | 利用可能にする                                      |
| General       | 動詞   | apply        | 適用/実行する                          | applyChanges()              | 効力を発生させる                                    |
| General       | 動詞   | commit       | 変更を確定する                         | commitTransaction()         | 恒久的なものにする                                  |
| General       | 動詞   | rollback     | 変更を取り消す                         | rollback()                  | 以前の状態に戻す                                    |
| General       | 動詞   | authenticate | 本人確認をする                         | authenticateUser()          | 誰であるかを確認する                                |
| General       | 動詞   | authorize    | アクセス権限を与える                   | authorizeAction()           | 何ができるかを確認する                              |
| General       | 動詞   | pause        | 一時停止する                           | pause()                     | 実行を中断する                                      |
| General       | 動詞   | resume       | 一時停止から再開する                   | resume()                    | 実行を再開する                                      |
| General       | 動詞   | await        | 完了を待つ                             | await result                | 準備ができるまで一時停止                            |
| General       | 動詞   | break        | ループ/ブロックを抜ける                | break                       | 制御フローからの脱出                                |
| General       | 動詞   | continue     | 次の反復へスキップする                 | continue                    | ループ制御                                          |
| General       | 動詞   | yield        | 値を産出/一時停止する                  | yield value                 | 値を返す、または制御を譲る                          |
| General       | 動詞   | dispatch     | ルーティング/送信する                  | dispatchEvent()             | ハンドラへ転送する                                  |
| General       | 動詞   | broadcast    | 全員に送信する                         | broadcastMessage()          | 1対多の送信                                         |
| General       | 動詞   | multicast    | グループに送信する                     | multicast(message)          | 1対多（ターゲット指定）                             |
| General       | 動詞   | unicast      | 1人の受信者に送信する                  | unicast(message)            | 1対1の送信                                          |
| General       | 動詞   | notify       | 知らせる/警告する                      | notify(observer)            | 通知を送る                                          |
| General       | 動詞   | publish      | 公開する                               | publish(event)              | 購読者にブロードキャストする                        |
| General       | 動詞   | log          | イベント/データを記録する              | log(message)                | ログに書き込む                                      |
| General       | 動詞   | info         | 情報を記録する                         | info(message)               | 情報レベルのロギング                                |
| General       | 動詞   | warn         | 警告を記録する                         | warn(message)               | 警告（アラート）レベルのロギング                    |
| General       | 動詞   | trace        | 詳細な記録を行う                       | trace(message)              | デバッグレベルのロギング                            |
| General       | 動詞   | debug        | 問題を診断する                         | debugMode()                 | 開発時の検査                                        |
| General       | 動詞   | monitor      | 観察/追跡する                          | monitor(metric)             | 継続的に監視する                                    |
| General       | 動詞   | parse        | 構造を解析する                         | parse(json)                 | 構造データに変換する                                |
| General       | 動詞   | pass         | 渡す/通過させる                        | pass(value)                 | 引き渡す                                            |
| General       | 動詞   | transform    | 変換/形態を変える                      | transform(data)             | 構造を変更する                                      |
| General       | 動詞   | fold         | 畳み込む/集約する                      | fold(fn, initial)           | 要素を結合する                                      |
| General       | 動詞   | gain         | 獲得する/増やす                        | gainAccess()                | 手に入れる                                          |
| General       | 動詞   | lose         | 失う/減らす                            | loseConnection()            | 持っていない状態になる                              |
| General       | 動詞   | maximize     | 最大化する                             | maximize()                  | 最も大きくする                                      |
| General       | 動詞   | minimize     | 最小化する                             | minimize()                  | 最も小さくする                                      |
| General       | 動詞   | release      | リソースを解放する                     | release(lock)               | 放棄する                                            |
| General       | 動詞   | trigger      | 実行のきっかけを作る                   | trigger(event)              | アクションを開始させる                              |
| General       | 動詞   | invalidate   | 無効としてマークする                   | invalidateCache()           | 使用不可にする                                      |
| Status        | 形容詞 | active       | 現在実行中/稼働中                      | isActive                    | inactiveの対義語                                    |
| Status        | 形容詞 | enabled      | 対話可能/使用可能                      | isEnabled                   | 意図的にオンにされている                            |
| Status        | 形容詞 | disabled     | 対話不可/使用不可                      | isDisabled                  | 意図的にオフにされている                            |
| Status        | 形容詞 | visible      | 画面に表示されている                   | isVisible                   | 見ることができる                                    |
| Status        | 形容詞 | available    | 準備完了かつアクセス可能               | isAvailable                 | 今すぐに使える                                      |
| Status        | 形容詞 | valid        | 全ての基準を満たしている               | isValid                     | バリデーション通過済み                              |
| Status        | 形容詞 | empty        | 何も含まれていない                     | isEmpty                     | 要素が存在しない(hasNoItems)                        |
| Status        | 形容詞 | completed    | 終了/完了済み                          | isCompleted                 | タスクが終了した                                    |
| Status        | 形容詞 | pending      | 完了待ち                               | isPending                   | 進行中                                              |
| Status        | 動詞   | is           | 真偽状態のチェック                     | isValid, isReady            | 標準的なBooleanアクセサ                             |
| Status        | 動詞   | has          | 所有/包含のチェック                    | hasRole('admin')            | 所持しているかを確認する                            |
| Validation    | 動詞   | check        | 簡易的な検査                           | checkPermission()           | しばしばBooleanを返す                               |
| Validation    | 動詞   | validate     | ルールを深く検査する                   | validateInput()             | エラーを返すか例外を投げる                          |
| Validation    | 動詞   | verify       | 真実性/認証を確認する                  | verifySignature()           | セキュリティ文脈でよく使われる                      |
| Validation    | 動詞   | assert       | 厳密なチェック（偽の場合はクラッシュ） | assert(x > 0)               | テスト/内部ロジック用                               |
| Validation    | 動詞   | ensure       | 存在/真であることを保証する            | ensureDir()                 | ない場合は作成する                                  |
| Comparison    | 動詞   | compare      | 2つの値を比較する                      | compare(a, b)"              | 典型的には -1, 0, 1 を返す                          |
| Comparison    | 動詞   | equals       | 等価性をチェックする                   | equals(other)               | ディープ（深い）またはシャロー（浅い）比較          |
| Comparison    | 動詞   | match        | パターン/正規表現マッチング            | match(pattern)              | マッチ結果を返す                                    |
| Data Access   | 動詞   | get          | 軽量なメモリアクセス                   | getName(), getIndex()       | 高コストな処理には使わない(fetch参照)               |
| Data Access   | 動詞   | set          | 単純な代入                             | setName('Alice')            |                                                     |
| Data Access   | 動詞   | read         | 低レベルIO/ストリーム読み込み          | readBytes()                 |                                                     |
| Data Access   | 動詞   | write        | 低レベルIO/ストリーム書き込み          | writeBuffer()               |                                                     |
| Data Access   | 動詞   | load         | メモリへの読み込み/準備                | loadConfig()                |                                                     |
| Data Access   | 動詞   | save         | ストレージへ永続化する                 | saveChanges()               |                                                     |
| Data Access   | 動詞   | find         | 条件検索（nullの可能性あり）           | findUser('id')              | 見つからない場合はOptional/Nullを返す               |
| Data Access   | 動詞   | search       | 複雑なクエリ/スキャン                  | searchProducts(query)       |                                                     |
| Data Access   | 動詞   | query        | 複雑なデータ取得                       | queryDatabase(sql)          | データベースまたは複雑な検索                        |
| Data Access   | 動詞   | fetch        | リモート/高コストな取得                | fetchUserData()             | しばしばasync/waitを伴う                            |
| Collection    | 動詞   | add          | リスト/セットに追加する                | addTag('urgent')            | removeの対義語                                      |
| Collection    | 動詞   | remove       | リスト/セットから取り除く              | removeItem(item)            | addの対義語                                         |
| Collection    | 動詞   | insert       | 特定のインデックスに入れる             | insertAt(0, item)           |                                                     |
| Collection    | 動詞   | clear        | 全項目を削除する                       | clearCache()                | コレクションを空にする                              |
| Collection    | 動詞   | push         | 末尾に追加する（スタック）             | push(item)                  | スタック操作                                        |
| Collection    | 動詞   | pop          | 最後を除去して返す                     | pop()                       | スタック操作                                        |
| Collection    | 動詞   | shift        | 先頭を除去して返す                     | shift()                     | キュー操作                                          |
| Collection    | 動詞   | unshift      | 先頭に追加する                         | unshift(item)               | キュー操作                                          |
| Collection    | 動詞   | append       | 末尾に追加する（順序付き）             | appendLine()                |                                                     |
| Collection    | 動詞   | concat       | コレクションを結合する                 | concat(arr1, arr2)          | 新しいコレクションを返す                            |
| Collection    | 動詞   | slice        | 一部分を抽出する                       | slice(start, end)           | 非破壊的                                            |
| Collection    | 動詞   | splice       | インデックス指定で挿入/削除            | splice(index, count, items) | 破壊的                                              |
| Collection    | 動詞   | count        | 総数を取得する                         | countItems()                |                                                     |
| String        | 動詞   | uppercase    | 大文字に変換する                       | uppercase(str)              |                                                     |
| String        | 動詞   | lowercase    | 小文字に変換する                       | lowercase(str)              |                                                     |
| String        | 動詞   | capitalize   | 先頭文字を大文字にする                 | capitalize(str)             |                                                     |
| String        | 動詞   | trim         | 空白を除去する                         | trim(str)                   | 先頭および末尾                                      |
| String        | 動詞   | pad          | パディング文字を追加する               | padStart(str, 10)           |                                                     |
| String        | 動詞   | concat       | 文字列を結合する                       | concat(str1, str2)          |                                                     |
| String        | 動詞   | join         | 区切り文字で結合する                   | join(arr, ',')              |                                                     |
| String        | 動詞   | format       | フォーマットを適用する                 | format(template, args)      | テンプレート置換                                    |
| String        | 動詞   | substring    | 文字列の一部を抽出する                 | substring(start, end)       |                                                     |
| String        | 動詞   | replace      | テキストを置換する                     | replace(old, new)           |                                                     |
| Conversion    | 動詞   | convert      | データ型を変換する                     | convertToInt(str)           |                                                     |
| Conversion    | 動詞   | cast         | 型変換（キャスト）                     | cast(value)                 | 型アサーション                                      |
| Conversion    | 動詞   | parse        | 文字列を構造化データへ                 | parse(jsonString)           | Generalにもあるが、ここでは文脈的                   |
| Conversion    | 動詞   | stringify    | オブジェクトを文字列へ                 | stringify(obj)              | JSONシリアライズなど                                |
| Conversion    | 動詞   | toString     | 文字列に変換する                       | toString(obj)               |                                                     |
| Conversion    | 動詞   | toArray      | 配列に変換する                         | toArray(iterable)           |                                                     |
| Conversion    | 動詞   | toBoolean    | ブール値に変換する                     | toBoolean(value)            |                                                     |
| Conversion    | 動詞   | toNumber     | 数値に変換する                         | toNumber(str)               |                                                     |
| Lifecycle     | 動詞   | create       | 新しいインスタンス/レコード作成        | createUser()                |                                                     |
| Lifecycle     | 動詞   | delete       | レコード/ファイルを削除                | deleteFile()                | 破壊的                                              |
| Lifecycle     | 動詞   | init         | 初期化する（セットアップ）             | initDatabase()              | 一度だけ呼ばれることが多い                          |
| Lifecycle     | 動詞   | initialize   | initの正式形                           | initialize()                | initよりフォーマル                                  |
| Lifecycle     | 動詞   | finalize     | 破棄前のクリーンアップ                 | finalize()                  | GC（ガベージコレクタ）関連用語                      |
| Lifecycle     | 動詞   | start        | プロセス/サービスを開始                | startServer()               | ステートフル                                        |
| Lifecycle     | 動詞   | stop         | プロセスを停止                         | stopServer()                | ステートフル                                        |
| Lifecycle     | 動詞   | run          | メインロジックを実行                   | app.run()                   |                                                     |
| Lifecycle     | 動詞   | update       | 既存データを更新                       | updateProfile()             |                                                     |
| Lifecycle     | 動詞   | teardown     | 使用後のクリーンアップ                 | teardown()                  | テスト/リソースのクリーンアップ                     |
| Logic         | 動詞   | calc         | 値を計算する                           | calcTotal()                 | calculateの略                                       |
| Logic         | 動詞   | calculate    | 値を計算する                           | calculateTotal()            | calcの正式形                                        |
| Logic         | 動詞   | compute      | 複雑な計算を行う                       | computeHash()               | CPUコストがかかることを示唆                         |
| Logic         | 動詞   | execute      | コマンド/アクションを実行              | executeCommand()            | runのフォーマル版                                   |
| Logic         | 動詞   | process      | データ系列/ワークフローを処理          | processPayment()            |                                                     |
| Logic         | 動詞   | filter       | 条件で項目を選別する                   | filter(predicate)           | 部分集合を返す                                      |
| Logic         | 動詞   | map          | 各項目を変換する                       | map(fn)                     | 新しいコレクションを返す                            |
| Logic         | 動詞   | reduce       | 単一の値へ集約する                     | reduce(fn, initial)         | 畳み込み操作 (Fold)                                 |
| Logic         | 動詞   | sort         | 項目を並べ替える                       | sort(comparator)            |                                                     |
| Pattern       | 名詞   | adapter      | インターフェース変換                   | LegacyApiAdapter            | 構造パターン                                        |
| Pattern       | 名詞   | bridge       | 抽象と実装を分離                       | ViewBridge                  | 構造パターン                                        |
| Pattern       | 名詞   | builder      | 段階的な構築                           | QueryBuilder                | 複雑なオブジェクト生成                              |
| Pattern       | 名詞   | chain        | リクエストを連鎖的に渡す               | AuthChain                   | 責任の連鎖 (Chain of Responsibility)                |
| Pattern       | 名詞   | command      | オブジェクトとしての操作               | SaveCommand                 | Undo/Redoのサポート                                 |
| Pattern       | 名詞   | composite    | オブジェクトのツリー構造               | UIComponent                 | 単体とグループを同一視する                          |
| Pattern       | 名詞   | decorator    | 動的に振る舞いを追加                   | StreamDecorator             | ラッパー (Wrapper)                                  |
| Pattern       | 名詞   | facade       | 複雑なシステムの簡易IF                 | ApiFacade                   | 複雑さを隠蔽する                                    |
| Pattern       | 名詞   | factory      | オブジェクトを生成する                 | UserFactory                 | 生成パターン                                        |
| Pattern       | 名詞   | flyweight    | 共通状態を共有する                     | FontFlyweight               | メモリ最適化                                        |
| Pattern       | 名詞   | mediator     | 通信を集中管理する                     | ChatMediator                | 結合度を下げる                                      |
| Pattern       | 名詞   | memento      | 復元用に状態を保存                     | GameMemento                 | スナップショット                                    |
| Pattern       | 名詞   | observer     | 変更時に通知を受ける                   | EventObserver               | Pub/Sub（出版/購読）                                |
| Pattern       | 名詞   | prototype    | インスタンスを複製する                 | EnemyPrototype              | コピー作成                                          |
| Pattern       | 名詞   | proxy        | 代理/アクセス制御                      | ImageProxy                  | 遅延読み込み/認証                                   |
| Pattern       | 名詞   | singleton    | 唯一のインスタンス                     | AppConfig                   | 使用は控えめに                                      |
| Pattern       | 名詞   | state        | 状態依存の振る舞い                     | ConnectionState             | 有限オートマトン (FSM)                              |
| Pattern       | 名詞   | strategy     | 交換可能なアルゴリズム                 | SortStrategy                | 振る舞いパターン                                    |
| Pattern       | 名詞   | template     | アルゴリズムの骨格                     | ReportTemplate              | サブクラスが手順を埋める                            |
| Pattern       | 名詞   | visitor      | オブジェクト構造に対する操作           | NodeVisitor                 | 構造からアルゴリズムを分離                          |
| Role          | 名詞   | user         | システムユーザー                       | currentUser                 | システムを使う人                                    |
| Role          | 名詞   | admin        | 管理者ロール                           | adminUser                   | 最高レベルの権限                                    |
| Role          | 名詞   | member       | グループの参加者                       | teamMember                  | コレクションに属する                                |
| Role          | 名詞   | manager      | ロジック/リソースを管理                | SessionManager              | 警告: 曖昧になりがち                                |
| Role          | 名詞   | controller   | アプリの流れを制御                     | AuthController              | MVCのコントローラー                                 |
| Role          | 名詞   | service      | ビジネスロジック保持者                 | UserService                 | ドメインロジック                                    |
| Role          | 名詞   | repository   | データアクセスの抽象化                 | UserRepository              | DBの詳細を隠蔽する                                  |
| Role          | 名詞   | provider     | データ/依存を供給する                  | AuthProvider                | DI（依存性注入）パターン                            |
| Role          | 名詞   | helper       | 補助的な関数                           | ViewHelper                  | 警告: しばしばコードスメル                          |
| Role          | 名詞   | util         | 静的なユーティリティ関数               | DateUtil                    | 純粋関数に保つこと                                  |
| Role          | 名詞   | wrapper      | 他のオブジェクトを包む                 | ApiWrapper                  | 単純化                                              |
| Role          | 名詞   | middleware   | 処理パイプラインの構成要素             | AuthMiddleware              | インターセプター                                    |
| Role          | 名詞   | registry     | グローバル検索サービス                 | ServiceRegistry             | 中央リスト                                          |
| Network       | 動詞   | connect      | リンクを確立する                       | connectToDB()               |                                                     |
| Network       | 動詞   | disconnect   | リンクを切断する                       | disconnect()                |                                                     |
| Network       | 動詞   | send         | データを送信する                       | sendEmail()                 |                                                     |
| Network       | 動詞   | receive      | ストリームからデータを得る             | receiveMessage()            |                                                     |
| Network       | 動詞   | ack          | 受信成功の確認応答。                   | ackMessage(id)              | 正常に受け取ったことを相手に通知する。              |
| Network       | 動詞   | nack         | 受信失敗の確認応答。                   | nackMessage(id)             | 再送要求や失敗通知として使う。                      |
| Network       | 動詞   | upload       | リモートへ送信する                     | uploadFile()                |                                                     |
| Network       | 動詞   | download     | リモートから取得する                   | downloadFile()              |                                                     |
| Network       | 動詞   | push         | 即時通知を送る                         | pushNotification()          | Array.pushとの混同を避ける                          |
| Network       | 動詞   | ping         | 接続性をテストする                     | ping(host)                  |                                                     |
| Network       | 動詞   | poll         | 繰り返しチェックする                   | pollStatus()                |                                                     |
| File          | 名詞   | file         | ファイルシステムオブジェクト           | fileHandle                  | 個別のファイル                                      |
| File          | 名詞   | directory    | ファイルを含むフォルダ                 | directoryPath               | ファイルのコンテナ                                  |
| File          | 名詞   | path         | ファイルシステム内の場所               | filePath                    | ファイル/ディレクトリのアドレス                     |
| File          | 動詞   | exists       | 存在を確認する                         | exists(path)                | 真偽値（Boolean）を返す                             |
| File          | 動詞   | mkdir        | 新しいディレクトリを作成               | mkdir(path)                 | ディレクトリを作る                                  |
| File          | 動詞   | rmdir        | 空のディレクトリを削除                 | rmdir(path)                 | ディレクトリを消す                                  |
| File          | 動詞   | copy         | 新しい場所に複製する                   | copyFile(src, dest)         | 非破壊的な複製                                      |
| File          | 動詞   | move         | 新しい場所に再配置する                 | moveFile(src, dest)         | 場所を変更する                                      |
| File          | 動詞   | rename       | ファイル/ディレクトリ名変更            | rename(oldName, newName)    | 識別子を更新する                                    |
| File          | 動詞   | unlink       | システムからファイル削除               | unlink(path)                | 低レベルなファイル削除                              |
| File          | 動詞   | watch        | 変更を監視する                         | watch(path, callback)       | ファイルシステムイベント                            |
| Database      | 名詞   | table        | データベースのテーブル                 | tableName                   | 行のコレクション                                    |
| Database      | 名詞   | column       | データベースの列                       | columnName                  | 垂直方向のデータフィールド                          |
| Database      | 名詞   | row          | データベースの行                       | rowData                     | 水平方向のデータレコード                            |
| Database      | 名詞   | cell         | 行と列の交点                           | cellValue                   | 最小のデータ単位（実務では value と呼ぶことが多い） |
| Database      | 名詞   | field        | column の別名                          | fieldName                   | ORMやフォーム文脈でよく使う                         |
| Database      | 名詞   | record       | row の別名                             | recordData                  | テーブル内の論理的なデータ単位                      |
| Database      | 名詞   | tuple        | row の理論用語                         | tupleData                   | リレーショナルモデルでの呼称                        |
| Database      | 名詞   | value        | 行と列の交点にある値                   | columnValue                 | 理論上は attribute value と呼ぶ                     |
| Database      | 名詞   | attribute    | column の理論用語                      | attributeName               | ERモデリングで使用                                  |
| Database      | 名詞   | entity       | テーブルで表現される論理的な対象       | entityModel                 | ER図で使用                                          |
| Database      | 名詞   | relationship | テーブル間の関連                       | relationshipMap             | テーブル同士のつながりを定義                        |
| Database      | 名詞   | Primary      | 主キーを示す語                         | primaryKey                  | 行を一意に識別する                                  |
| Database      | 名詞   | Foreign      | 外部キーを示す語                       | foreignKey                  | 他テーブルの主キーを参照                            |
| Database      | 名詞   | Candidate    | 候補キーを示す語                       | candidateKey                | 一意識別が可能なキー候補                            |
| Database      | 名詞   | Alternate    | 代替キーを示す語                       | alternateKey                | 主キーに選ばれなかった候補キー                      |
| Database      | 名詞   | Composite    | 複合キーを示す語                       | compositeKey                | 複数列の組み合わせによるキー                        |
| Database      | 名詞   | Unique       | ユニークキーを示す語                   | uniqueKey                   | 重複を許さない制約キー                              |
| Database      | 名詞   | Surrogate    | 代理キーを示す語                       | surrogateKey                | 人工的に生成されるID                                |
| Database      | 名詞   | Natural      | 自然キーを示す語                       | naturalKey                  | 実データに基づく意味のあるキー                      |
| Database      | 名詞   | schema       | データベース構造定義                   | schemaDefinition            | テーブルとリレーションシップ                        |
| Database      | 名詞   | migration    | スキーマ変更スクリプト                 | migrationFile               | スキーマのバージョン管理                            |
| Database      | 名詞   | index        | データベースインデックス               | indexName                   | クエリパフォーマンスを向上                          |
| Database      | 動詞   | migrate      | スキーマ変更を適用する                 | migrate()                   | データベース構造を更新する                          |
| Database      | 動詞   | rollback     | トランザクション/移行を戻す            | rollback()                  | 変更を取り消す                                      |
| Database      | 動詞   | seed         | 初期データを投入する                   | seed()                      | デフォルト/テストデータを挿入                       |
| Database      | 動詞   | truncate     | 全行を削除する                         | truncate(table)             | テーブル構造は維持する                              |
| Testing       | 名詞   | suite        | 関連テストの集合                       | testSuite                   | グループ化されたテストケース                        |
| Testing       | 名詞   | fixture      | 定義済みのテストデータ/設定            | userFixture                 | 一貫したテスト状態                                  |
| Testing       | 名詞   | mock         | 偽の実装オブジェクト                   | serviceMock                 | 実際の依存を置き換える                              |
| Testing       | 名詞   | stub         | 定義済み応答オブジェクト               | apiStub                     | 缶詰（固定）の応答を返す                            |
| Testing       | 名詞   | spy          | 関数呼び出しトラッカー                 | functionSpy                 | 呼び出しを記録する                                  |
| Testing       | 動詞   | describe     | テストケースをグループ化               | describe('User', ...)       | BDDスタイルのグループ化                             |
| Testing       | 動詞   | it           | 単一テストケースを定義                 | it('should work', ...)      | BDDスタイルのテスト                                 |
| Testing       | 動詞   | test         | 単一テストケースを定義                 | test('works', ...)          | it' の代替                                          |
| Testing       | 動詞   | expect       | アサーションを行う                     | expect(value).toBe(...)     | アサーション関数                                    |
| Async         | 名詞   | promise      | 非同期操作の結果                       | userPromise                 | 将来の値のコンテナ                                  |
| Async         | 動詞   | resolve      | プロミスを値で解決する                 | resolve(value)              | プロミスを成功としてマーク                          |
| Async         | 動詞   | reject       | プロミスをエラーで失敗させる           | reject(error)               | プロミスを失敗としてマーク                          |
| Async         | 動詞   | await        | 非同期完了を待つ                       | await promise               | 解決されるまで実行を一時停止                        |
| Async         | 動詞   | then         | 非同期操作を繋げる                     | then(callback)              | 解決後の次のステップ                                |
| Async         | 動詞   | catch        | 非同期エラーを処理する                 | catch(err)                  | プロミスチェーンのエラーハンドラ                    |
| Async         | 動詞   | finally      | 非同期完了後に実行する                 | finally()                   | プロミス後に常に実行される                          |
| Async         | 動詞   | race         | 最初に完了したものを返す               | race(promises)              | 最初に確定したものが勝つ                            |
| Security      | 動詞   | login        | 認証しセッション作成                   | login(credentials)          | 認証済みセッションを開始                            |
| Security      | 動詞   | logout       | 認証済みセッション終了                 | logout()                    | セッションを破棄する                                |
| Security      | 動詞   | register     | 新規アカウントを作成                   | register(userInfo)          | サインアップ                                        |
| Security      | 動詞   | encrypt      | 暗号でデータを保護する                 | encrypt(data, key)          | 機密性を保護する                                    |
| Security      | 動詞   | decrypt      | 暗号化を逆変換する                     | decrypt(data, key)          | 元のデータを復元する                                |
| Security      | 動詞   | hash         | 一方向のエンコード                     | hash(password)              | 逆変換はできない                                    |
| Security      | 動詞   | sanitize     | 信頼できない入力を浄化                 | sanitize(userInput)         | インジェクション攻撃を防ぐ                          |
| UI            | 形容詞 | enabled      | 対話可能                               | isEnabled                   | ユーザーが有効化できる                              |
| UI            | 形容詞 | disabled     | 対話不可                               | isDisabled                  | ユーザーは有効化できない                            |
| UI            | 形容詞 | visible      | 画面に表示されている                   | isVisible                   | ユーザーが見ることができる                          |
| UI            | 動詞   | show         | 要素を表示する                         | show()                      | 表示に追加する                                      |
| UI            | 動詞   | hide         | 要素を不可視にする                     | hide()                      | 表示から削除する                                    |
| UI            | 動詞   | toggle       | 状態を切り替える                       | toggle()                    | 真偽状態を反転させる                                |
| UI            | 動詞   | focus        | 要素にフォーカスを当てる               | focus()                     | 入力をアクティブにする                              |
| UI            | 動詞   | blur         | 要素からフォーカスを外す               | blur()                      | 入力を非アクティブにする                            |
| UI            | 動詞   | render       | 画面に描画する                         | render()                    | ビューポートに描画する                              |
| UI            | 動詞   | click        | クリックをシミュレート                 | click()                     | クリックイベントをトリガー                          |
| Time          | 名詞   | timestamp    | 特定の時点                             | createdTimestamp            | 記録された瞬間の時間                                |
| Time          | 名詞   | duration     | 時間の長さ/期間                        | animationDuration           | 何かがかかる時間                                    |
| Time          | 名詞   | interval     | イベント間の間隔                       | pollingInterval             | 発生ごとのギャップ                                  |
| Time          | 名詞   | timeout      | 操作の制限時間                         | connectionTimeout           | 最大の待ち時間                                      |
| Time          | 動詞   | wait         | 条件まで一時停止する                   | wait(condition)             | 準備ができるまでブロック                            |
| Time          | 動詞   | delay        | 一定時間実行を一時停止                 | delay(500)                  | 指定期間待つ                                        |
| Time          | 動詞   | sleep        | 一定時間実行を一時停止                 | sleep(1000)                 | delayと同様                                         |
| Time          | 動詞   | schedule     | 将来の実行を計画する                   | scheduleTask()              | 将来のアクションを手配する                          |
| Error         | 名詞   | error        | 一般的な失敗                           | AuthError                   |                                                     |
| Error         | 名詞   | exception    | 言語構造としての例外                   | RuntimeException            | キャッチ可能                                        |
| Error         | 動詞   | throw        | 例外を発生させる                       | throw new Error()           |                                                     |
| Error         | 動詞   | fail         | 成功しなかった                         | fail()                      |                                                     |
| Error         | 動詞   | crash        | 予期しない停止                         | onCrash()                   |                                                     |
| Error         | 動詞   | panic        | 回復不能なエラー                       | panic()                     | システムレベルの失敗                                |
| Configuration | 名詞   | config       | 構成設定                               | appConfig                   | システム設定                                        |
| Configuration | 名詞   | option       | 単一の構成の選択肢                     | sortOption                  | 個別の設定                                          |
| Configuration | 名詞   | parameter    | 入力/構成パラメータ                    | functionParameter           | 渡された値                                          |
| Configuration | 名詞   | variable     | 設定値のホルダー                       | configVariable              | 変更可能な設定                                      |
| Configuration | 名詞   | environment  | ランタイム環境設定                     | environmentVariables        | デプロイメントコンテキスト                          |

(c) 2026 GoodRelax. MIT License.



