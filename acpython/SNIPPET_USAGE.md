# スニペット使い方集

`acpython/.vscode/*.code-snippets` の各スニペットの使い方と例をまとめた資料。
見出しは VS Code で入力する `prefix`。

- 「API」はクラス直下の説明コメント（クラスがない場合は関数のシグネチャ）を抜き出したもの。
- 「例」は `prefix` で展開したコードの後に書けばそのまま動く呼び出し例。`N`・`edges` などは問題の入力に合わせて置き換える。
- 他スニペットへの依存（例: `treedp` は `tree` が必要）は各説明文に記載している。

## 目次

- [00 入力](#00-入力)：[input](#input) / [inint](#inint) / [inints](#inints) / [inarr](#inarr) / [inarr1d](#inarr1d) / [inarr2d](#inarr2d) / [instr](#instr) / [instrs](#instrs) / [ingrid](#ingrid) / [inpair](#inpair)
- [01 基本](#01-基本)：[heapq](#heapq) / [zaatsu](#zaatsu) / [queue](#queue) / [sort](#sort) / [abc](#abc) / [reclimit](#reclimit) / [itertools](#itertools) / [query](#query)
- [02 データ構造](#02-データ構造)：[avl](#avl) / [bit](#bit) / [lazyseg](#lazyseg) / [union](#union) / [seg](#seg) / [wavelet](#wavelet) / [multiset](#multiset) / [linkedlist](#linkedlist) / [trie](#trie) / [map](#map) / [union_potential](#union_potential) / [BinaryTrie](#binarytrie) / [cartesianTree](#cartesiantree) / [sortedSet](#sortedset) / [rangeList](#rangelist) / [union_persist](#union_persist) / [dynamic_segtree](#dynamic_segtree) / [packed2dlist](#packed2dlist)
- [03 グラフ・木](#03-グラフ木)：[dijkstra](#dijkstra) / [kruskal](#kruskal) / [maxflow](#maxflow) / [mincost](#mincost) / [scc](#scc) / [tree](#tree) / [treepath](#treepath) / [treedp](#treedp) / [auxtree](#auxtree) / [warflo](#warflo) / [tree64](#tree64) / [graph](#graph) / [bfs](#bfs) / [dag](#dag) / [matching](#matching) / [particalgraph](#particalgraph) / [twosat](#twosat) / [ushi](#ushi) / [grid](#grid)
- [04 文字列](#04-文字列)：[rori](#rori) / [string](#string) / [eertree](#eertree) / [hensyukyori](#hensyukyori) / [suffixarray](#suffixarray) / [zalg](#zalg)
- [05 数学](#05-数学)：[adm](#adm) / [comb](#comb) / [convmod](#convmod) / [convolvell](#convolvell) / [divhoujo](#divhoujo) / [divisor](#divisor) / [gyoretu](#gyoretu) / [hakidasi](#hakidasi) / [inv](#inv) / [kika](#kika) / [kyori](#kyori) / [math](#math) / [period](#period) / [prime](#prime) / [totu](#totu) / [touhi](#touhi) / [tousa](#tousa) / [convolution](#convolution) / [gensikon](#gensikon) / [Packer](#packer) / [radix_convert](#radix_convert) / [hakidasi2](#hakidasi2) / [way12](#way12) / [bunkatu](#bunkatu) / [ragu](#ragu) / [argsort](#argsort)
- [06 DP](#06-dp)：[dfa](#dfa) / [nfa](#nfa) / [slopetrick](#slopetrick) / [LIS](#lis) / [cht](#cht)
- [07 区間・クエリ](#07-区間クエリ)：[mo](#mo) / [rangeaffine](#rangeaffine) / [imos2d](#imos2d) / [squaresplit](#squaresplit)
- [08 その他アルゴリズム](#08-その他アルゴリズム)：[bitall](#bitall) / [nibutan](#nibutan) / [tentou](#tentou) / [prevgreater](#prevgreater) / [grundy](#grundy)
- [09 アーカイブ（旧版）](#09-アーカイブ旧版)：[olddeque](#olddeque) / [oldlazyseg](#oldlazyseg) / [oldtree](#oldtree) / [oldtreedp](#oldtreedp)

## 00 入力

ファイル: [`00-input.code-snippets`](.vscode/00-input.code-snippets)

### input

入力高速化 (input = sys.stdin.readline)

展開結果:

```python
import sys
input = sys.stdin.readline

```

### inint

1つの整数を読み込む (N = int(input()))

展開結果:

```python
N = int(input())
```

### inints

1行の複数整数を個別変数に読み込む (N, M = map(int, input().split()))

展開結果:

```python
N, M = map(int, input().split())
```

### inarr

1行を int の1次元リストに変換 (A = list(map(int, input().split())))

展開結果:

```python
A = list(map(int, input().split()))
```

### inarr1d

N 行を1つずつ int で読み込み1次元リストに (A = [int(input()) for _ in range(N)])

展開結果:

```python
A = [int(input()) for _ in range(N)]
```

### inarr2d

N 行を int の2次元リストに変換 (A = [list(map(int, input().split())) for _ in range(N)])

展開結果:

```python
A = [list(map(int, input().split())) for _ in range(N)]
```

### instr

1行の文字列を読み込む (S = input().rstrip())

展開結果:

```python
S = input().rstrip()
```

### instrs

1行のスペース区切り文字列をリストに読み込む (S = input().rstrip().split())

展開結果:

```python
S = input().rstrip().split()
```

### ingrid

H 行の文字列グリッドを1次元リストとして読み込む (grid = [input().rstrip() for _ in range(H)])

展開結果:

```python
grid = [input().rstrip() for _ in range(H)]
```

### inpair

N 行の (a, b) ペアをタプルのリストで読み込む、辺の入力等に (edges = [tuple(...) for _ in range(N)])

展開結果:

```python
edges = [tuple(map(int, input().split())) for _ in range(N)]
```


## 01 基本

ファイル: [`01-basic.code-snippets`](.vscode/01-basic.code-snippets)

### heapq

ヒープキュー HeapQue (最大/最小切替・default 値・push/pop/top/pushpop)

API:

```python
class HeapQue
  # 注意: is_max=True は値を -1 倍して管理するため数値限定 (文字列・タプル等は不可)
  # pop(): 最小(is_max時は最大)値を取り出す
  # top(): 最小(is_max時は最大)値を覗き見る
  # push(x): 値を追加する
  # pushpop(x): x を追加してから最小(is_max時は最大)値を取り出す
  # is_empty(): 空かどうかを返す
  # reset(): 中身を空にする
```

例:

```python
q = HeapQue(is_max=True)
q.push(x)
q.pop()
```

### zaatsu

座標圧縮 Zaatsu (値→順位/順位→値、前処理 O(N log N)・rank/value は O(1))

API:

```python
class Zaatsu
  # compress(): 初期化時に渡した A を順位(0-indexed, 小さい順)のリストに変換したものを返す
  # rank(x): 値 x の順位(0-indexed)を返す (x は A に含まれる値限定)
  # value(i): 順位 i に対応する元の値を返す
```

例:

```python
z = Zaatsu(${1:A})
comp = z.compress()
v = z.value(2)$0
```

### queue

FIFO キュー (deque の薄いラッパ、put/get エイリアス)

例:

```python
put(x)
x = get()
while q:  # 空判定は q で行う
  x = get()
```

### sort

cmp_to_key で比較関数 sort (cmpstr の中身を書き換えて使う、対象リストを placeholder)

API:

```python
def cmpstr(a, b)
```

例:

```python
def cmpstr(a, b): return (a + b > b + a) - (a + b < b + a)  # 例: 連結して最小になる順
arr = sorted(arr, key=cmp_to_key(cmpstr))
```

### abc

アルファベット 26 文字定数 (ABC = 大文字、abc = 小文字)

展開結果:

```python
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc = "abcdefghijklmnopqrstuvwxyz"
```

例:

```python
i = ABC.index("C")  # 2
c = abc[(abc.index(ch) + k) % 26]  # 小文字 ch を k 文字ずらす
```

### reclimit

再帰上限の引き上げ (sys.setrecursionlimit)

例:

```python
sys.setrecursionlimit(10**6)  # 再帰関数(DFS 等)の前に。PyPy は深い再帰が遅くメモリを食うので非再帰化も検討
```

### itertools

itertools 系ユーティリティ (rle/rle_int/unrle/accumulate/pairwise/flatten/unflatten)

API:

```python
class itr
  # rle(S): ランレングス圧縮 [(値, 個数), ...] を返す
  # rle_int(S): 0~9の数字とみなしてランレングス圧縮する
  # unrle(pairs): rle/rle_int の結果から元の列を復元する
  # accumulate(A, initial=0): 累積和のリストを返す (先頭に initial を含む)
  # pairwise(A): 隣接する要素のペア (a[i], a[i+1]) のリストを返す
  # flatten(A): 2次元リストを1次元に平坦化する（(i, j) は i * W + j に移る。各行の長さ W のとき）
  # unflatten(F, w): flatten の逆。w が int なら幅 w ごと、list なら w[i] 個ずつ区切って2次元に戻す
```

例:

```python
itr.rle("aabbb") -> [("a", 2), ("b", 3)]
itr.rle_int("1100") -> [(1, 2), (0, 2)]
itr.unrle([("a", 2), ("b", 3)]) -> ["a", "a", "b", "b", "b"]
itr.accumulate([1, 2, 3]) -> [0, 1, 3, 6]
itr.pairwise([1, 2, 3]) -> [(1, 2), (2, 3)]
itr.flatten([[1, 2], [3, 4]]) -> [1, 2, 3, 4]
itr.unflatten([1, 2, 3, 4], 2) -> [[1, 2], [3, 4]]  # 幅で復元
itr.unflatten([1, 2, 3], [1, 2]) -> [[1], [2, 3]]  # 行ごとの長さで復元（長さは flatten 前に [len(r) for r in A] で取っておく）
```

### query

クエリ種別ディスパッチャ Query_solve (ops[i-ind](*que) で呼び分け)

API:

```python
class Query_solve
  # solve(Query): 各クエリの先頭要素(種別番号)に対応する ops の処理を呼び出す
```

例:

```python
solver = Query_solve([op_add, op_get])
queries = [list(map(int, input().split())) for _ in range(Q)]
solver.solve(queries)  # 各クエリは [種別, 引数...] (種別は ind 始まり)
```


## 02 データ構造

ファイル: [`02-data-structure.code-snippets`](.vscode/02-data-structure.code-snippets)

### avl

AVL 木 (平衡二分探索木、key/value 対応)

API:

```python
class AVL
  # insert(k, v): key=k, value=v の要素を追加する
  # delete(k): key=k の要素を削除する
  # check(k): key=k が存在するかを返す
  # getMax(): 最大キーの (key, value) を返す
  # getMin(): 最小キーの (key, value) を返す
  # print(): 木の中身を見やすく表示する (デバッグ用)
  # makeKeyList(L): L の値を順位(小さい順の番号)のリストに変換する
```

例:

```python
t = AVL()
t.insert(k, v)
ok = t.check(k)
t.delete(k)
```

### bit

BIT / フェニック木 (1点更新・区間和、全操作 O(log N))

API:

```python
class BIT
  # set(L): L の内容をまとめて反映する
  # update(x, n): 位置 x に n を加算する
  # getV(x): 先頭から x までの和(x を含む)を返す
  # print(): 各位置の値と全体の和を表示する (デバッグ用、O(N log N))
```

例:

```python
bit = BIT(N)
bit.update(i, x)
s = bit.getV(r)
bit.print()  # 例: [1, 2, 13, 4, 5] sum: 25
```

### lazyseg

遅延評価セグ木 (atcoder.lazysegtree ラッパ、用途別 factory)

API:

```python
class LSTFactory
  # 遅延セグ木 (ac-library-python の LazySegTree) の生成ファクトリ
  #   makeAddMinSegTree(v) / makeAddMaxSegTree(v): 区間加算・区間 min / max
  #   makeAddSumSegTree(v): 区間加算・区間和
  #   makeSetMinSegTree(v) / makeSetMaxSegTree(v): 区間代入・区間 min / max
  #   makeSetSumSegTree(v): 区間代入・区間和
  #   makeAffineSumSegTree(v): 区間アフィン変換 x -> a*x+b・区間和 (mod MOD)
  #   debug(seg): seg の各位置の値と全体の演算結果 all_prod を表示する (デバッグ用、O(N log N))
  # Sum 系は内部で要素を (値 << RNG) + 区間長 に詰めている (区間長 < 2^RNG)。
  #   get / prod / all_prod / max_right / min_left の値は自動で取り出されるので利用者は意識不要。
  #   値は負や 2^RNG 以上でも可 (Add/Set Sum)。
  # Affine 系は apply(l, r, a, b) で指定。a, b は内部で % MOD する (関数を (a << RNG) + b に詰めるため b は [0, MOD) 前提)。
```

例:

```python
t = LSTFactory.makeAddSumSegTree(v)
t.apply(l, r, f)
t.prod(l, r)
u = LSTFactory.makeAffineSumSegTree(v)
u.apply(l, r, a, b)  # [l, r) の各 x を a*x+b (mod MOD) に
u.prod(l, r)
LSTFactory.debug(t)  # 例: [6, 7, 3] all_prod: 16
```

### union

Union-Find (経路圧縮 + サイズマージ、ほぼ O(α(N)))

API:

```python
class Union
  # root(x): x の属する集合の代表元を返す
  # merge(x, y): x と y の集合を併合する
  # size(x): x の属する集合の要素数を返す
  # same(x, y): x と y が同じ集合かを返す
  # root_group(): グループごとに要素をまとめたリストを返す(各グループ先頭が根)
  # print(): 内部状態を表示する (デバッグ用)
```

例:

```python
u = Union(N)
u.merge(a, b)
r = u.root(x)
u.size(x)
```

### seg

セグメント木 (op / e を関数で渡す汎用版)

API:

```python
class segtree
  # set(p, x): 位置 p の値を x にする (1点更新)
  # get(p): 位置 p の値を取得する (1点取得)
  # prod(l, r): [l, r) の区間演算結果を返す
  # all_prod(): 全体の演算結果を返す
  # max_right(l, g): l を左端に固定したとき g を満たす最長区間の右端を返す
  # min_left(r, g): r を右端に固定したとき g を満たす最長区間の左端を返す
  # print(): 各位置の値と全体の演算結果 all_prod を表示する (デバッグ用)
class segtreeFactory
  makeMaxSegTree(N,  v = None)
  makeMinSegTree(N, v = None)
  makeSumSegTree(N, v = None)
  makeFuncSegTree(N, v = None)
  emax()
  opmax(a, b)
  emin()
  opmin(a, b)
  opsum(a, b)
  esum()
  efunc()
  opfunc(a, b)
```

例:

```python
t = segtreeFactory.makeSumSegTree(N)
t.set(i, x)
s = t.prod(l, r)
t.print()  # 値と全体の演算結果 all_prod を表示
```

### wavelet

ウェーブレット行列 (静的列の k-th / select / 区間内 quantile)

API:

```python
class wavelet
  __init__(T)
  access(n)
  rank(n, c)
  select(c, n)
  quantile(st, en, r)
  topk(st, en, k)
  sum(st, en)
```

例:

```python
w = wavelet(A)
w.access(i)
w.rank(i, c)
w.select(c, k)
w.quantile(l, r, k)
w.topk(l, r, k)
w.sum(l, r)
```

### multiset

マルチセット (ヒープ実装、追加/削除/min 全 O(log N))

API:

```python
class HeapQue
  __init__(is_max = False, default = None)
  pop()
  top()
  push(x)
  pushpop(x)
  is_empty()
  reset()
class multiset
  # insert(v): 値 v を追加する
  # delete(v): 値 v を1つ削除する
  # pop_max(): 最大値を取り出して削除する
  # pop_min(): 最小値を取り出して削除する
  # top_max(): 最大値を覗き見る
  # top_min(): 最小値を覗き見る
```

例:

```python
ms = multiset()
ms.insert(x)
ms.delete(x)
m = ms.top_min()
```

### linkedlist

双方向連結リスト (add / insert / remove 全 O(1))

API:

```python
class DoubleLinkedList()
  # data は一意であること (data をキーにノードを引く)
  # add(data): 末尾に要素を追加する
  # remove(data): 要素を削除する
  # insert(data_i, data): data_i の後ろに data を挿入する
  # getList(): 内容をリストで返す
  # pophead(): 先頭要素を取り出す
  # poptail(): 末尾要素を取り出す
```

例:

```python
ll = DoubleLinkedList()
ll.add(x)
ll.remove(x)
```

### trie

トライ木 (文字列集合の prefix 共有表現)

API:

```python
class Trie
  # insert(key, value): key(文字のリスト)に値を紐づけて登録する
  # find(key): keyを検索して値を返す(未登録ならNone)
```

例:

```python
t = Trie()
t.insert("abc", value)
v = t.find("abc")
```

### map

ハッシュ Map (衝突攻撃耐性のランダム化キー、HASH_NUM ビット)

API:

```python
class Map
  # set(key, value): key に value を設定する
  # get(key): key の値を返す (未設定なら init を返す)
```

例:

```python
m = Map()
m.set(k, v)
v = m.get(k)
```

### union_potential

ポテンシャル付き Union-Find (重み付き連結・差分検査)

API:

```python
class UnionPotential
  # root(x): x の属する集合の代表元を返す
  # merge(x, y, w): weight(y) - weight(x) = w となるように x, y を併合する
  # size(x): x の属する集合の要素数を返す
  # same(x, y): x と y が同じ集合かを返す
  # diff(x, y): weight(y) - weight(x) を返す
  # weight(x): x のポテンシャル(根からの相対値)を返す
  # print(): 内部状態を表示する (デバッグ用)
```

例:

```python
u = UnionPotential(N)
u.merge(a, b, w)
d = u.diff(a, b)
```

### BinaryTrie

Binary Trie (xor 最小値検索・整数集合 [0, 2^BIT_SIZE))

API:

```python
class BinaryTrie
  # 非負整数の集合 (重複不可: 同じ値を複数回 insert しても1個扱い、remove で消える)
  # 値域: 0 <= key < 2 ** (BIT_SIZE + 1) (ビット BIT_SIZE..0 を見る)
  #   insert(key): key を追加する
  #   remove(key): key を削除する (無ければ何もしない)
  #   find(key): key が存在すれば True、無ければ False (空なら None)
  #   findXorMin(key): key ^ y が最小となる要素 y 自身を返す (xor 値ではない、空なら None)
  #   findXorMax(key): key ^ y が最大となる要素 y 自身を返す (xor 値ではない、空なら None)
```

例:

```python
t = BinaryTrie()
t.insert(x)
y = t.findXorMin(q)
```

### cartesianTree

カルテシアン木 (区間 min/max の階層構造、RMQ 前処理など)

API:

```python
class CartesianTree
  __init__(N: int, A: list[int], L: list[int], R: list[int], P: list[int], root: int)
  getParentList()
  getParent(x: int)
  getRoot()
  makeSizeOfPartTree()
  topDownDp(op : Callable[[int, int, int, Any], Any], dp: Any)
  bottomUpDp(op : Callable[[int, int, int, Any], Any], dp: Any)
  print()
class CartesianTreeFactory
  makeMinTree(A: list[int])
  makeMaxTree(A: list[int])
```

例:

```python
t = CartesianTreeFactory.makeMinTree(A)
root = t.getRoot()
```

### sortedSet

Sorted Set (tatyam 実装、平方分割で全操作 O(√N))

API:

```python
class SortedSet(Generic[T])
  __init__(a: Iterable[T] = [])
  add(x: T)
  discard(x: T)
  lt(x: T)
  le(x: T)
  gt(x: T)
  ge(x: T)
  pop(i: int = -1)
  index(x: T)
  index_right(x: T)
```

例:

```python
s = SortedSet([1, 2, 3])
s.add(x)
s.lt(x)
s.le(x)
s.gt(x)
```

### rangeList

区間リストの解析 (包含区間の削除・包含/非交差ペア検出・被覆に必要な区間列)

API:

```python
class RangeList
  __init__(v : list[int, int])
  remove_nest()
  find_nest_pair()
  find_overlapping_pair()
  find_cover_ranges(start, end)
```

例:

```python
rl = RangeList([(1, 3), (5, 7)])
pair = rl.find_nest_pair()
cover = rl.find_cover_ranges(l, r)
```

### union_persist

永続 Union-Find (過去の時刻状態にも問い合わせ可能)

API:

```python
class UnionPersistentPart
  __init__(N)
  find(t,x)
  merge(x,y)
  same(t,x,y)
  size(t,x)
  merge_timming(x, y)
```

例:

```python
u = UnionPersistentPart(N)
u.merge(x, y)
ok = u.same(u.now, x, y)
```

### dynamic_segtree

動的セグ木 (要素 index が大きくても座圧不要・遅延ノード生成)

API:

```python
class dinamic_segtree
  __init__(N, op, e)
  set(p, x)
  get(p)
  prod(l, r)
  all_prod()
  reset(l, r)
  max_right(l, g)
  min_left(r, g)
  print()  # 値を設定した位置 {index: value} と全体の演算結果 all_prod を表示する (デバッグ用)
class segtreeFactory
  makeMaxSegTree(N)
  makeMinSegTree(N)
  makeSumSegTree(N)
  makeFuncSegTree(N)
  emax()
  opmax(a, b)
  emin()
  opmin(a, b)
  opsum(a, b)
  esum()
  efunc()
  opfunc(a, b)
```

例:

```python
t = segtreeFactory.makeSumSegTree(N)
t.set(i, x)
s = t.prod(l, r)
t.print()  # 値と全体の演算結果 all_prod を表示
```

### packed2dlist

2D 座標 (a, b) を 1 整数にパックして保持するリスト (高速化用)

API:

```python
class Packed2DList(list)
  __init__(N: int = 10**6, size: int = 0)
  append(a: int, b: int)
  pop()
  extend(iterable)
  index(element)
  count(element)
```

例:

```python
p = Packed2DList(N=10**6)
p.append(a, b)
a, b = p[0]
```


## 03 グラフ・木

ファイル: [`03-graph.code-snippets`](.vscode/03-graph.code-snippets)

### dijkstra

ダイクストラ法 (重み付きグラフの単一始点最短距離 O((N+M) log N))

API:

```python
class Graph
  __init__(N: int, directed: bool = False, weighted: bool = False)
  add_edge(a: int, b: int, weight: int = 1)
  add_edges(edges: list)
  get_edges()
  get_rvs_list()
  getDrectedGraphMinimum()
  getDfsTreeNodes(root = 0)
class Dijkstra
  __init__(graph : Graph)
  dist(start, L = None)
  dist_need_path(start, L = None)
  get_bridge(start, goal, nodes)
  get_shortest_path_graph(start, goal)
```

例:

```python
g = Graph(N, directed=True, weighted=True)
g.add_edge(a, b, w)
d = Dijkstra(g).dist(s)
```

### kruskal

クラスカル法 (最小全域木 MST、辺ソート + Union-Find)

API:

```python
class Union
  # root(x): x の属する集合の(代表元, サイズ)を返す
  # merge(x, y): x と y の集合を併合する
  # size(x): x の属する集合の要素数を返す
  # same(x, y): x と y が同じ集合かを返す
class Kruskal
  # add(a, b, x): 重み x の辺 (a, b) を候補に追加する
  # exe(): 最小全域木を構築し (総重み, 使用した辺のリスト) を返す
```

例:

```python
k = Kruskal(N)
k.add(a, b, w)
total, mst_edges = k.exe()
```

### maxflow

最大流 maxFlow (Dinic 系の自前実装、整数容量)

API:

```python
class maxFlow
  __init__(n)
  add_edge(frm, to, cap)
  get_edge(i)
  edges()
  change_edge(i, new_cap, new_flow)
  flow(s, t, flow_limit = NUMERIC_LIMITS)
  min_cut(s)
```

例:

```python
mf = maxFlow(N)
mf.add_edge(a, b, cap)
f = mf.flow(s, t)
```

### mincost

最小費用流 MinCostFlow (Dijkstra + ポテンシャル法、負コスト辺は初回 Bellman-Ford で対応・負閉路不可) O(F (N+M) log M)

API:

```python
class mcf_graph
  add_edge(frm, to, cap, cost)
  get_edge(i)
  edges()
  flow(s, t, flow_limit = NUMERIC_LIMITS)
  dual_ref(s, t)
  slope(s, t, flow_limit = NUMERIC_LIMITS)
```

例:

```python
mcf = mcf_graph(N)
mcf.add_edge(a, b, cap, cost)
flow, cost = mcf.flow(s, t, limit)
```

### scc

強連結成分分解 SCC (有向グラフを縮約して DAG 化)

API:

```python
class scc_graph
  groups(N, adj)
  compress(graph)
```

例:

```python
groups = scc_graph.groups(N, adj)  # adj[v] = vから出る辺の行き先リスト
compressed, ids = scc_graph.compress(graph)  # graph: GraphData(N, True)
```

### tree

木の前処理 Tree (LCA / k 個上の祖先 / 距離 / パス / 部分木区間 / 直径 / 子・葉リスト / 重心 / HLD 区間分解、重み対応、構築 O(N)・クエリ O(log N))

API:

```python
class Tree
  # 木の前処理（非再帰 DFS 1 回 + HLD）。頂点は内部で 0-indexed（index=1 で 1-indexed 入力を変換）
  #   Tree(N, edges, root=None, index=0, weighted=False): edges = [(u, v)] or [(u, v, w)]
  #     root は edges と同じ番号付け（省略時は内部番号 0 の頂点）
  #   lca(u, v): 最小共通祖先 O(log N)
  #   kth_ancestor(v, k): v から k 個上の祖先（無ければ -1）O(log N)
  #   jump(u, v, k): u から v へ向かって k 歩進んだ頂点（無ければ -1）O(log N)
  #   dist(u, v): u-v 間の距離（weighted=False なら辺数）O(log N)
  #   path(u, v): u から v へのパス上の頂点リスト O(パス長)
  #   subtree(v): v の部分木が占める pos の半開区間 (l, r)
  #   path_ranges(u, v, edge=False): u→v パスを pos の区間 (l, r, rev) 列に分解（rev=True は r-1→l の向き）
  #   edge_vertex(a, b): 辺 (a, b) の子側の頂点（辺の値を載せる位置）
  #   diameter(): (直径, 端点 a, 端点 b)
  #   is_ancestor(u, v): u が v の祖先（u == v を含む）か O(1)
  #   centroid(): 重心のリスト（1 個か 2 個）O(N)
  #   debug(): 各配列を print する
  # 属性: par[v] 親(根は -1), depth[v] 辺数の深さ, wdepth[v] 重み付き深さ, pw[v] 親への辺の重み,
  #   size[v] 部分木サイズ, order 先行順の頂点列, adj[v] = [(to, w)], pos[v] HLD 順の位置, at[p] 位置 p の頂点,
  #   ch[v] 子のリスト, leaves 葉のリスト（子がない頂点。N=1 なら根も含む）, height[v] v から部分木内の最深の葉までの辺数
```

例:

```python
tr = Tree(N, edges, index=1)  # edges が 1-indexed なら index=1（root も同じ番号付け、以降のメソッドは 0-indexed で呼ぶ）
tr = Tree(N, edges, weighted=True)     # 重み付き edges = [(u, v, w), ...]
c = tr.lca(u, v)
d = tr.dist(u, v)
x = tr.jump(u, v, k)
d, a, b = tr.diameter()
p = tr.path(a, b)
l, r = tr.subtree(v)  # v の部分木の頂点 = tr.at[l:r]
for c in tr.ch[v]: ...  # v の子
for v in tr.leaves: ...  # 葉
for v in reversed(tr.order): ...  # 葉から根の順（子を処理してから親）
tr.is_ancestor(u, v)
g = tr.centroid()
tr.debug()
```

### treepath

木のパス・部分木クエリ TreePath (HLD + セグ木、頂点/辺の値、非可換対応、tree と seg スニペットが必要、O(log^2 N))

API:

```python
class TreePath
  # 木のパス・部分木クエリ（HLD + セグ木）。tree スニペットの Tree と seg スニペットの segtree が必要
  #   TreePath(tr, val, op, e, edge=False, commutative=True)
  #     val[v]: 頂点 v の値。edge=True なら辺 (par[v], v) の値を v に置く（根の値は無視）
  #     commutative=False なら向きを考慮する（逆向きのセグ木も持つ）
  #   set(v, x): 頂点 v（edge=True なら辺 (par[v], v)）の値を x にする O(log N)
  #   get(v): 頂点 v の値 O(1)
  #   path(u, v): u→v パス上の値を u 側から順に op した結果 O(log^2 N)
  #   subtree(v): v の部分木の総積（edge=True なら部分木内の辺のみ）O(log N)
```

例:

```python
tr = Tree(N, edges)
tp = TreePath(tr, A, lambda a, b: a + b, lambda: 0)  # 頂点 v の値 A[v]、パス和
tp.set(v, x)
s = tp.path(u, v)
s = tp.subtree(v)
B = [0] * N
for u, v, w in wedges: B[tr.edge_vertex(u, v)] = w   # 辺の値は子側の頂点に置く
te = TreePath(tr, B, max, lambda: -10**18, edge=True)  # パス上の辺の最大値
m = te.path(u, v)
```

### treedp

木 DP TreeDP (葉→根の bottom_up / 全方位 solve、merge / add_root / add_edge を渡すだけ、tree スニペットが必要、O(N))

API:

```python
class TreeDP
  # 木 DP（葉→根の 1 方向）と全方位木 DP。tree スニペットの Tree が必要。頂点番号は Tree と同じ 0-indexed
  # 【考え方】v を根とする部分木の値 dp[v] を次の式で計算する
  #   dp[v] = add_root(merge(e, add_edge(dp[c1], c1, v, w1), add_edge(dp[c2], c2, v, w2), ...), v)
  #   1. add_edge: 子 c の値 dp[c] を「親 v から見た寄与」に変換する（辺の重みを足す等）
  #   2. merge: 子の寄与を e から順にまとめる（葉は子がないので e のまま）
  #   3. add_root: まとめた寄与に頂点 v 自身の分を加えて dp[v] にする
  # 【引数】TreeDP(tr, e, merge, add_root, add_edge=None)
  #   e: merge の単位元（merge(e, x) == x となる値）
  #   merge(a, b): 寄与どうしをまとめる。solve では結合的・可換が必要。bottom_up のみなら adj の順に左から畳み込む
  #   add_root(x, v): まとめた寄与 x に頂点 v 自身を加えて dp[v] にする
  #   add_edge(x, c, v, w): 子 c の値 x を辺 c-v（重み w。重みなし Tree なら w=1）越しの寄与にする。省略時は x のまま
  # 【メソッド】
  #   bottom_up(): tr.root を根とした dp を葉から順に計算してリストで返す O(N)（普通の木 DP はこれだけ）
  #   solve(): 全頂点それぞれを根にしたときの dp[根] のリストを返す O(N)（全方位木 DP）
  #   sub[v]: tr.root を根としたときの dp[v]（bottom_up / solve の後に参照可）
```

例:

```python
tr = Tree(N, edges)  # edges が 1-indexed なら index=1（以降の頂点番号は 0-indexed）
# --- 葉→根の木 DP（bottom_up）---
# 部分木のサイズ: 子の合計 + 自分 1
size = TreeDP(tr, 0, lambda a, b: a + b, lambda x, v: x + 1).bottom_up()
# 最大独立集合: dp[v] = (v を選ばない最大, v を選ぶ最大)
#   子 c の寄与 = (max(dp[c]), dp[c][0])  ← v を選ばないなら c は自由、選ぶなら c は選べない
mis = TreeDP(tr, (0, 0), lambda a, b: (a[0] + b[0], a[1] + b[1]), lambda x, v: (x[0], x[1] + 1), lambda x, c, v, w: (max(x), x[0])).bottom_up()
print(max(mis[tr.root]))
# --- 全方位木 DP（solve）---
tr = Tree(N, edges, weighted=True)
# 各頂点から最も遠い頂点までの距離
far = TreeDP(tr, 0, max, lambda x, v: x, lambda x, c, v, w: x + w).solve()
# 各頂点から全頂点への距離の総和（値 = (距離和, 頂点数)）
rr = TreeDP(tr, (0, 0), lambda a, b: (a[0] + b[0], a[1] + b[1]), lambda x, v: (x[0], x[1] + 1), lambda x, c, v, w: (x[0] + x[1] * w, x[1]))
tot = [s for s, _ in rr.solve()]
```

### auxtree

圧縮木 Auxiliary Tree (頂点集合と LCA だけ残した木、tree スニペットが必要、O(K log N))

API:

```python
def auxtree(tr, vs)
```

例:

```python
tr = Tree(N, edges)
nodes, par = auxtree(tr, vs)
for i in range(1, len(nodes)):
  length = tr.dist(nodes[i], nodes[par[i]])
```

### warflo

ワーシャル・フロイド法 (全点対最短距離 O(N^3))

API:

```python
class warflo
  # add(a, b, c): a から b へ c の辺を張る (負の辺は不可)
  # exe(): 各点間の距離を求める (O(N^3))
  # route(a, b): a から b への経路を返す (先に exe() をすること)
```

例:

```python
wf = warflo(N, inf)
wf.add(a, b, w)
D = wf.exe()
```

### tree64

Tree64 (深さ × ビット幅で部分木列を 64bit 整数化、定数倍高速化)

API:

```python
class Tree64
  # 2 ** (HEIGHT * BIT_SIZE) - 1 まで可能
  # HEIGHT = 8, BIT_SIZE = 6の場合
  # 2 ** 48 - 1 >= 10 ** 14
```

例:

```python
t = Tree64()
t.add(n)
ok = t.find(n)
```

### graph

グラフ汎用クラス GraphData (有向/無向 + 重み 切替)

API:

```python
class GraphData
  __init__(N: int, directed: bool = False, weighted: bool = False)
  convert_indexed(data, indexed = 1)
  add_edge(a, b, weight = 1)
  add_edges(list)
  get_edges()
  getDrectedGraphMinimum()
  getDfsTreeNodes(root = 0)
```

例:

```python
g = GraphData(N, directed=True, weighted=False)
g.add_edge(a, b)
```

### bfs

01-BFS (辺重み 0/1 限定、deque で O(N+M))

API:

```python
class Graph
  __init__(N: int, directed: bool = False, weighted: bool = False)
  add_edge(a: int, b: int, weight: int = 1)
  add_edges(edges: list)
  get_edges()
  get_rvs_list()
  getDrectedGraphMinimum()
  getDfsTreeNodes(root = 0)
class BFS
  __init__(graph : Graph)
  dist_list(start)
  shortest_path(start, goal)
  shortest_tree(start)
  dists_remove_edge(start, goal)
  shortest_path_graph(start, goal)
  dirmeter()
  bfs2Goal(start, goal)
  bfs01(start)
  bfs(start)
```

例:

```python
g = Graph(N, weighted=True)
g.add_edge(a, b, w_0_or_1)
d = BFS(g).bfs01(s)
```

### dag

DAG (トポロジカル順序 + DP の土台)

API:

```python
class DAG
  __init__(N, AdjacencyList, ReverseList, inputCount)
  makeDag(gf : GraphData)
  toposo(C = 1)
  enumerateTriangles()
```

例:

```python
dag = DAG.makeDag(gf)
order = dag.toposo()
```

### matching

最大二部マッチング (atcoder.maxflow 経由)

API:

```python
class Matching
  # Matching(N, weight=1, R=None): 左側 N 頂点(0..N-1)、右側 R 頂点(0..R-1、省略時は N)
  #   weight: 各頂点が使える回数（s→左, 右→t の容量）
  # add_edge(a, b, weight=1): 左側の頂点 a と右側の頂点 b を辺で結ぶ
  # flow(M=None): 最大マッチング数(または最大 M まで)を返す
  # list_matching(L): 隣接リストから最大マッチングする Matching を作る (static)
```

例:

```python
m = Matching(N)
m.add_edge(l, r)
n = m.flow()
```

### particalgraph

部分グラフ ParticalGraph (元グラフからエッジ集合で誘導)

API:

```python
class ParticalGraph
  __init__(N)
  add_edge(a: int, b: int)
  add_edges(edges: list)
  partical_number_list()
  partical_number(S)
  connection_partical_number_list(g)
  reachable_number_list(i)
  entire_area_number(S, f, g)
```

例:

```python
pg = ParticalGraph(N)
pg.add_edges(edge_subset)
```

### twosat

2-SAT (含意グラフ + SCC、節集合を満たす変数割当を判定/構成)

API:

```python
class two_sat
  # add_clause(i, f, j, g): 節 (x_i == f) or (x_j == g) を追加する
  # satisfiable(): 全ての節を満たす割り当てが存在するか判定する O(n + m)
  # answer(): satisfiable() が True のときの割り当て (x_0, ..., x_{n-1}) を返す
```

例:

```python
ts = two_sat(N)
ts.add_clause(x, vx, y, vy)
ok = ts.satisfiable()
ans = ts.answer()
```

### ushi

牛ゲー (差分制約 a - b ≤ w を最短路に帰着して整合性判定 / 最適値)

API:

```python
class Ushi
  __init__(N)
  add_edge(a, b, v)
  add_edge_gt(a, b, v)
  add_edge_eq(a, b, v)
  ushi_maximam(st, en)
  ushi_minimam(st, en)
  bellman_ford(st, en)
```

例:

```python
u = Ushi(N)
u.add_edge(a, b, w)
ans = u.ushi_maximam(st, en)
```

### grid

グリッド管理 gridMan (壁付与 + 4方向 BFS 距離 / 最大値)

API:

```python
class gridMan
  # makeWall(x=-2): 四方を壁で囲む (範囲外アクセスを防ぐ)
  # dist(S): S=(行, 列) から上下左右に進んで何手かかるかのリスト（到達不能は-1）と最大値を返す
  #   makeWall の有無に関わらず元のグリッドの座標(0-indexed)で指定・返却する
```

例:

```python
g = gridMan(L)
g.makeWall()
D, mx = g.dist((sr, sc))
```


## 04 文字列

ファイル: [`04-string.code-snippets`](.vscode/04-string.code-snippets)

### rori

ローリングハッシュ Rori (二重 mod、文字列の部分一致を O(1) で比較)

API:

```python
class Rori
  # hashLR(l, r): [l, r) のハッシュ値(2つのmodの組)を返す
  # same(l1, r1, l2, r2): [l1, r1) と [l2, r2) が同じ文字列かを返す (長さ一致も確認)
  # 文字は ord(c) をそのまま値に使う (英小文字以外・大文字・数字も可)
```

例:

```python
rh = Rori(S)
h = rh.hashLR(l, r)  # S[l:r] のハッシュ
ok = rh.same(l1, r1, l2, r2)  # S[l1:r1] == S[l2:r2] か
```

### string

文字列アルゴリズム集 (suffix array / LCP / 文字列ソート関連まとめ)

API:

```python
# O(n) sが文字列の時
def suffix_array(s, upper = -1)
# O(n)
def lcp_array(s, sa)
# Longest Common Prefix
def z_algorithm(s)
# O(n + upper)
def sa_is(s, upper)
# O(n^2 log n)
def sa_naive(s)
#doubling
def sa_doubling(s)
# O(n)
def suffix_array_str(s)
```

例:

```python
sa = suffix_array(s)
lcp = lcp_array(s, sa)
z = z_algorithm(s)
```

### eertree

eertree / 回文木 (文字列内の全ての異なる回文部分文字列を管理)

API:

```python
class eertree
  # 回文木 (eertree): 文字列に含まれる回文部分文字列を管理する
  #   addChar(x): 末尾に 1 文字追加する
  #   addString(xs): 末尾に文字列を追加する
  #   getIndex(i): i 文字目(0-indexed)を末尾とする最長回文の node を返す
  #   getCount(): 回文部分文字列の総数(出現位置で区別)を返す
  #   getCountUnique(): 異なる回文部分文字列の種類数を返す
  #   getMaxSize(): 最長回文の長さを返す
  #   getMaxWord(): 最長回文を文字のリストで返す (文字列は ''.join で)
  #   getNodeList(): 作成順の node リストを返す
  #   node.getCount(): その node の回文を末尾とする回文の個数 / node.getLengthIndex(): その回文の長さ
```

例:

```python
et = eertree()
et.addChar(c)
cnt = et.getCount()
et.addString(S)
w = ''.join(et.getMaxWord())
```

### hensyukyori

編集距離 (Levenshtein 距離、hensyuKyori: 時間 O(|S| * |T|) / メモリ O(min(|S|, |T|))、hensyuKyoriK: 距離 K 以下限定の帯 DP O(|S| * K))

API:

```python
def chmin(data, i, x)
def hensyuKyori(S, T)
def hensyuKyoriK(S, T, K)
```

例:

```python
d = hensyuKyori(S, T)
dk = hensyuKyoriK(S, T, K)
ok = dk <= K  # 編集距離が K 以下か
```

### suffixarray

Suffix Array (ac-library-python 依存: atcoder.string ラッパ、部分文字列順序付け + LCP)

API:

```python
class SA
  __init__(S)
  restore_list(L)
  suffix_array(s, upper = None)
  lcp_array(s, sa)
  debug_suffix_str()
```

例:

```python
sa = SA(S)
positions = sa.sa
lcp = sa.lcp
```

### zalg

Z-algorithm (ac-library-python 依存: atcoder.string ラッパ、各位置からの最長一致長 O(N))

API:

```python
class Zalg
  __init__(S)
  z_algorithm(s)
```

例:

```python
z = Zalg(S)
arr = z.z
```


## 05 数学

ファイル: [`05-math.code-snippets`](.vscode/05-math.code-snippets)

### adm

アダマール変換 FWT (XOR 畳み込み、長さ 2^k)

API:

```python
# 0 <= x <= n 逆元リスト
def invL(n, MOD):
# アダマール変換
def fwt(f)
# 実行
def exe(L, MOD)
# ここに処理を書く
def proc(L)
```

例:

```python
exe(L, MOD)  # L が in-place で畳み込まれる
```

### comb

二項係数 comb (前計算 階乗+逆元、O(N) 前処理 / O(1) クエリ)

API:

```python
class comb()
  # com(n, k): n個からk個選ぶ組み合わせの数
  # com_multi(n, k): n個から重複を許してk個選ぶ組み合わせの数
  # per(n, k): n個からk個並べる順列の数
  # cataran(n): n番目のカタラン数
  # narayana(n, k): n, k番目のnarayana数
```

例:

```python
c = comb(N, MOD)
c.com(n, k)
c.com_multi(n, k)
```

### convmod

畳み込み MOD (NTT、特定 mod 用)

API:

```python
class Convolution
  __init__(MOD)
  convolution(a, b)
  butterfly(a)
  butterfly_inv(a)
  ceil_pow2(n)
  bsf(n)
  prime(x)
  primitive_root(x)
```

例:

```python
c = Convolution(MOD)
h = c.convolution(f, g)
```

### convolvell

畳み込み (numpy FFT、整数係数 / 高速だが MOD 不可。float64 精度のため結果の各係数の絶対値が 1e15 程度を超えると丸め誤差で不正確)

API:

```python
def convolve(f, g)
```

例:

```python
h = convolve(f, g)
```

### divhoujo

除数包除 (約数について閉じた昇順リスト D 上で「d の約数についての和」→「ちょうど d」を求めて総和、O(Σ d(x)) + 約数列挙)

API:

```python
#       グローバルの MOD を使う
def exe(x)
def divisor(n)
def divhoujo(D)
```

例:

```python
MOD = 998244353
D = divisor(N)
ans = divhoujo(D)
```

### divisor

約数列挙 (O(√N))

API:

```python
def divisor(n)
```

例:

```python
divs = divisor(n)
```

### gyoretu

行列累乗 mat_pow (ダブリング、MOD は冒頭で要定義)

API:

```python
def mat_mul(a, b)
def mat_pow(x, n)
```

例:

```python
A = mat_pow(M, k)  # M 正方、k 指数
```

### hakidasi

XOR 掃き出し (整数列を GF(2) 上で階段化、in-place)

API:

```python
def hakidasi(L)
```

例:

```python
B = hakidasi(L[:])
rank = sum(1 for v in B if v)
basis = B[:rank]
```

### inv

逆元 Inv クラス (modpow + 単発逆元 + 逆元リスト)

API:

```python
class Inv
  # invx(a): a の逆元 (a^-1 mod MOD) を返す
  # invL(n): 0 <= x <= n の逆元リストを返す
  # invpowL(a, n): a^-x (0 <= x <= n) のリストを返す
```

例:

```python
inv = Inv(MOD)
inv.invx(a)
inv.invL(n)
```

### kika

幾何ユーティリティ (2D 配列の 90° 回転 / 余白トリム)

API:

```python
def turn(D)
def trim(D)
```

例:

```python
D2 = turn(D)
D3 = trim(D)
```

### kyori

2D 距離関数 (Euclid edist / Manhattan mdist / Chebyshev cdist)

API:

```python
def edist(a, b)
def mdist(a, b)
def cdist(a, b)
```

例:

```python
d = mdist(a, b)  # a, b = (x, y)
```

### math

数学ユーティリティ集 (inv_mod 等の素朴関数)

API:

```python
# O(log m)
def inv_mod(x, m)
# O(n log lcm(m[i]))
def crt(r, m)
# O(log(n + m + a + b))
def floor_sum(n, m, a, b)
# gcdと逆元
def inv_gcd(a, b)
```

例:

```python
y = inv_mod(x, m)
r0, m0 = crt(r, m)
```

### period

周期検出 (関数グラフで x から K 項たどったときの各頂点の訪問回数、K が巨大でも O(N))

API:

```python
def period(L, K, x = 0)
```

例:

```python
D = period(L, K, x=0)  # D[v] = x から始めて K 項 (x を含む) の中で v を通る回数
```

### prime

素数列挙 + 素因数分解 Prime クラス (N<=5*10**6: 線形篩+lpf表 / それ以上: メモリ節約篩、素因数分解は N**2 まで素数リストで試し割り・それ超は O(√x) 試し割り、x>N の素数判定はミラーラビン)

API:

```python
class Prime
  # getPrimeList(): 素数リスト(Nまで)を返す
  # isPrime(x): 素数判定を行う (x<=N: 篩の結果 / x>N: ミラーラビン法)
  # primeFactorization(x): 素因数分解を行い {素数: 指数} を返す (x<=N: lpf表 / N<x<=N**2: 素数リストで試し割り / それ以上: O(√x) 試し割り)
  #   x >= 1 が前提 (x=1 は {}、x<=0 は ValueError)
  # factorize(x): primeFactorization のエイリアス
```

例:

```python
pr = Prime(N)
pr.getPrimeList()
pr.factorize(x)
```

### totu

凸包 (Andrew monotone chain、上下凸包の併合 O(N log N))

API:

```python
def det(p, q)
def sub(p, q)
def get_convex_hull(points)
# 多角形の面積 * 2 (2をかけると必ず整数になる)
def area(points)
# 多角形の線分上の格子点の数の和
def all_points_ontotu(points)
# 線分上の格子点の数
def points_online(x0, y0, x1, y1)
# 凸包に含まれる格子点の数
def inner_points(points)
```

例:

```python
hull = get_convex_hull(points)
```

### touhi

等比数列和 (1 + x + ... + x^t mod MOD、ダブリング O(log t))

API:

```python
# 1 + x + x^2 + ... + x^t (初項1 公比x 項数t+1) の和を mod で求め、[和, x^t] を返す
def nib(x, t, MOD)
```

例:

```python
s, last = nib(x, t, MOD)  # s = 1 + x + ... + x^t, last = x^t
```

### tousa

区間に等差数列を加算 (Imos の 2 階差分版)

API:

```python
class Imos
  __init__(N)
  add_line(l, r, a, d)
  get_array()
```

例:

```python
im = Imos(N)
im.add_line(l, r, init, diff)
A = im.get_array()
```

### convolution

その他の畳み込み集 (AND / OR / XOR 畳み込み (FWT、長さ 2^k、引数を破壊的に変換) / min-plus 畳み込み (a が下に凸))

API:

```python
class Convolution
  # ※ and/or/xorProductConv は引数 a, b を破壊的に変換する (元の値が必要なら a[:], b[:] を渡す)
class Hadamard
  opAndFwt(f : list[int], i: int, j: int)
  opAndIfwt(f : list[int], i: int, j: int)
  opOrFwt(f : list[int], i: int, j: int)
  opOrIfwt(f : list[int], i: int, j: int)
  opXorFwt(f : list[int], i: int, j: int)
  fwt(f, op)
```

例:

```python
h = Convolution.andProductConv(a[:], b[:], MOD)  # a, b は破壊されるのでコピーを渡す
```

### gensikon

原始根・離散対数 Gensikon (素数 p の最小原始根 / BSGS で X^K≡Y (mod p) の最小 K を O(√p))

API:

```python
class Gensikon
  # 原始根・離散対数 (インスタンス化せず Gensikon.xxx(...) で呼ぶ)
  #   primitive_root(x): 素数 x (x >= 3) の最小の原始根を返す O(√x + 試す候補数 × d(x-1) log x)
  #   prime(x): x の約数を昇順で返す O(√x)
  #   solve(X, Y, M): X^K ≡ Y (mod M) となる最小の K >= 0 を返す (なければ -1)。M は素数 O(√M)
```

例:

```python
g = Gensikon.primitive_root(p)
k = Gensikon.solve(g, y, p)  # g^k ≡ y (mod p) の最小 k (なければ -1)
```

### Packer

タプル↔整数パッカー (辞書 key 高速化、(a,b) を 1 整数に)

API:

```python
class Packer()
  __init__(N: int = 10**6, size = 2)
  pack(*data)
  unpack(packed)
```

例:

```python
p = Packer(N=10**6, size=2)
k = p.pack(a, b)
a, b = p.unpack(k)
```

### radix_convert

進数変換 Radix_Convert (任意基数 ↔ 10 進の相互変換)

API:

```python
class Radix_Convert
  toDec(x, n)
  fromDec(x, n)
  n2m(x, n, m)
```

例:

```python
dec = Radix_Convert.toDec(x, n)
x = Radix_Convert.fromDec(dec, n)
```

### hakidasi2

XOR 基底クラス XORBasis (掃き出し法のクラス版、追加/包含/次元)

API:

```python
class XORBasis
  __init__(x_list)
  represent(target)
  get_basis_list()
```

例:

```python
b = XORBasis([3, 5])
mask = b.represent(6)
basis = b.get_basis_list()
```

### way12

写像 12 相 (n 玉を k 箱に入れる、玉/箱/制約 の 12 通り)

API:

```python
class way12()
  # com(n, k): n個からk個選ぶ組み合わせの数
  # per(n, k): n個からk個並べる順列の数
  # sti(n, k): 第二種スターリング数
  # bel(n, k): ベル数
  # part(n, k): k を n 個以下に分割する方法の数
  # way(n, k, box, ball, limit): n箱/kボールの写像12相をまとめて呼び分ける
```

例:

```python
w = way12(N + K, MOD)
n = w.way(n=N, k=K, box=True, ball=True, limit=0)
```

### bunkatu

整数分割の列挙 (n を正整数の順不同和で表す全パターンを生成)

API:

```python
class Bunkatu
  bunkatu(N)
  bunkatu_map(N)
```

例:

```python
P = Bunkatu.bunkatu(N)
```

### ragu

ラグランジュ補間 (ragu1: N 点から f(T) を O(N^2 log MOD) / ragu2: 係数リストを O(N^2)、x は相異なる・MOD は素数)

API:

```python
class Inv
  __init__(mod)
  modpow(a, n)
  invx(a)
  invpowL(a, n)
  invL(n)
```

例:

```python
MOD = 998244353
xs = [0, 1, 2, 3]
ys = [1, 3, 5, 7]
v = ragu1(xs, ys, 10)  # f(10) = 21
coef = ragu2(xs, ys)   # [1, 2, 0, 0] (f(x) = 1 + 2x)
```

### argsort

偏角ソート (整数のまま外積で比較、atan2 順 (-π, π]、原点は偏角 0 扱い、添字返し切替 O(N log N))

API:

```python
# 偏角が等しい点同士は元の順を保つ (安定ソート)
def arg_sort(points, return_index=False)
```

例:

```python
points = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1)]
P = arg_sort(points)                       # [(0, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]
idx = arg_sort(points, return_index=True)  # [3, 0, 4, 1, 2]
```


## 06 DP

ファイル: [`06-dp.code-snippets`](.vscode/06-dp.code-snippets)

### dfa

オートマトン DP (桁 DP 含む、I-DFA を構築して状態遷移で集計)

API:

```python
class I_DFA
  __init__()
  init()
  next(state, alphabet: str, index: int)
  accept(state)
  successful(state)
  unsuccessful(state)
  stateList()
class DFA
  count(dfa: I_DFA, n, alphabet, mod = -1)
  count_sum(dfa: I_DFA, n, alphabet, mod = -1)
  count_list(dfa: I_DFA, n, alphabet, op, mod = -1)
```

例:

```python
dfa = DFA.And(DFA.Leq(N), DFA.DigitSumMultipleOF(k))
ans = DFA.count(dfa, len(str(N)), DFA.ALP_DIGIT)
```

### nfa

オートマトン DP NFA 有り版 (ε 遷移と非決定性を扱える)

API:

```python
class I_DFA
  __init__()
  init()
  next(state, alphabet: str, index: int)
  accept(state)
  successful(state)
  unsuccessful(state)
  stateList()
class DFA
  count(dfa: I_DFA, n, alphabet, mod = -1)
class DFAFactory
  make_dfa(state_size: int, transitions: dict[tuple[int, str], int], dfa_start_state: int, accept_states: list[int])
```

例:

```python
dfa = DFAFactory.make_dfa_by_nfa(state_size, alphabet, trans, [start], accept_states)
ans = DFA.count(dfa, n, alphabet)
```

### slopetrick

Slope Trick (区分線形凸関数を左右ヒープで管理、最小値追跡)

API:

```python
class HeapQue
  __init__(is_max = False, default = None)
  pop()
  top()
  push(x)
  pushpop(x)
  is_empty()
  reset()
class SlopeTrick
  # 区分線形凸関数 f(x) を管理する (初期値 f(x) = 0)
  #   get_min(): f の最小値
  #   get_min_range(): 最小値をとる区間 [l, r] (端がなければ default)
  #   add_constant(a): f(x) += a
  #   add_right(a): f(x) += max(0, x - a)
  #   add_left(a): f(x) += max(0, a - x)
  #   add_absolute(a): f(x) += |x - a|
  #   comulative_minimum(reverse): f(x) = min_{y<=x} f(y) (reverse=True なら min_{y>=x} f(y))
  #   slide(a, b): f(x) = min_{x-b<=y<=x-a} f(y) (a <= b、a = b なら平行移動)
```

例:

```python
st = SlopeTrick()
st.add_left(a)
st.add_right(a)
st.slide(a, b)
st.get_min()
l, r = st.get_min_range()
```

### LIS

最長増加部分列 LIS (bisect で O(N log N))

API:

```python
class LIS
  lis(A)
  lis_max(A)
  lis_min_ind(A)
  lis_length(A)
  lis_ext(A)
```

例:

```python
length = LIS.lis_length(A)
dp = LIS.lis(A)
```

### cht

Convex Hull Trick (傾き単調増加追加 + x単調増加クエリ、min/max 切替)

API:

```python
class CHT
  # 単調CHT
  # add: 傾き a を単調増加順 / query: x を単調増加順 (add と query は交互に呼んでもよい)
  # is_min=True なら min(a*x+b)、False なら max(a*x+b)
```

例:

```python
cht = CHT(is_min=True)
cht.add(a, b)
v = cht.query(x)
```


## 07 区間・クエリ

ファイル: [`07-range.code-snippets`](.vscode/07-range.code-snippets)

### mo

Mo's algorithm (区間クエリのオフライン処理、クエリは 1-indexed 半開区間 [l, r)、√N ブロック並べ替え O((N + Q)√N))

API:

```python
class Mo
  # Mo(N, Query): Query は (l, r) の列。1-indexed 半開区間 [l, r) = 要素 l..r-1 (1 <= l <= r <= N+1)
  #   区間は空 [1, 1) から始まり、l_plus/l_minus/r_plus/r_minus で 1 ずつ伸縮して各クエリ区間に合わせる
  # getAns(): 各クエリの答えのリストを返す (入力順)
  # 以下はサブクラスでオーバーライドして使う拡張点:
  # ini(): 初期化 / l_plus,l_minus,r_plus,r_minus(): 区間の伸縮時の処理 / anser(i): i番目の答えを確定させる
```

例:

```python
A = [0] + A  # 1-indexed にする
class MyMo(Mo):  # 例: 区間和
  def l_plus(self): self.ans -= A[self.l]; self.l += 1   # 要素 l を除く
  def l_minus(self): self.l -= 1; self.ans += A[self.l]  # 要素 l-1 を加える
  def r_plus(self): self.ans += A[self.r]; self.r += 1   # 要素 r を加える
  def r_minus(self): self.r -= 1; self.ans -= A[self.r]  # 要素 r-1 を除く
Query = [(l, r + 1) for l, r in LR]  # 閉区間 [l, r] (1-indexed) の入力なら r + 1 にする
ans = MyMo(N, Query).getAns()
```

### rangeaffine

区間 min/max の総和 RangeAffine (一列の N+1 点と辺重み L について、各点から他の全点へのパス上の min / max の総和を O(N) で全点分求める)

API:

```python
class RangeAffine
  # 区間 min/max の総和 (一列に並んだ N+1 点、点 i と i+1 の間の重みが L[i])
  #   range_min_sum_list(L): 各点 i について、全ての j != i への区間 L[min(i,j):max(i,j)] の最小値の和のリスト(長さ N+1)を返す O(N)
  #   range_max_sum_list(L): 同様に最大値の和のリストを返す O(N)
```

例:

```python
m = RangeAffine.range_min_sum_list(L)  # 長さ len(L) + 1
M = RangeAffine.range_max_sum_list(L)
total = sum(m) // 2  # 全区間 (i < j) の min の総和
```

### imos2d

2D いもす法 (矩形加算 + 累積和、計算 O(HW))

API:

```python
class Imos2D
  # add(h1, w1, h2, w2, value): 矩形範囲[h1,h2)x[w1,w2)に value を加算する (0-indexed 半開、範囲外は自動クランプ)
  # get_data(): 累積和を取って現在の2次元配列を返す
```

例:

```python
im = Imos2D(H, W)
im.add(r1, c1, r2, c2, v)
G = im.get_data()
```

### squaresplit

グラフの次数による平方分割 Square Split (クラス名は互換のため SquareSpilit、頂点更新を隣接頂点へ伝播、graph スニペットの GraphData(重みなし) 前提、1 クエリ O(√N + M/√N))

API:

```python
class SquareSpilit
  # 次数が √N 以上の頂点(重い頂点)は隣接頂点へ push せず、隣接頂点側がクエリ時に pull することで 1 クエリ O(√N + M/√N) にする
  #   SquareSpilit(gf, qs): gf は graph スニペットの GraphData (重みなし: adj_list[i] が頂点番号のリスト)、qs は Query_solve
  #   query(q): クエリ q を処理し、qs.solve_myself の戻り値を返す
  #   Query_solve: クエリ内容に応じて書き換える部分。デフォルトは「頂点 a の現在値を返し、a と隣接頂点を value にする」(初期値 1)
```

例:

```python
gf = GraphData(N)  # graph スニペットを先に展開しておく。重みなし前提 (weighted=True だと adj_list がタプルになり動かない)
gf.add_edges(edges)  # 0-indexed
qs = SquareSpilit.Query_solve(N)
sq = SquareSpilit(gf, qs)
ans = sq.query((x, y))  # q = (頂点, 値)
```


## 08 その他アルゴリズム

ファイル: [`08-misc-algo.code-snippets`](.vscode/08-misc-algo.code-snippets)

### bitall

ビット全探索 BitAll (M 桁の全ビット列を立っている数の少ない順に列挙・部分集合列挙・立っているビット位置、O(2^M))

API:

```python
class BitAll
  # ビット全探索ユーティリティ (Fenwick Tree の BIT ではない)
  #   bitall(M): 0 <= n < 2^M を立っているビット数の少ない順に返す
  #   bitall_index_list(M): bitall の順に立っているビット位置のリストを返す
  #   bitall_line(N, M): M 桁で N ビット立っているものを昇順に返す
  #   subset_of(n): n の部分集合を返す (順不同、0 を含む)
  #   bitall_with_subsets(M): (n, n の部分集合 s) を返す O(3^M)
  #   set_bit_indices(n): n で立っているビット位置のリストを返す
  #   debug_bit(n, M): n を M 桁の 2 進文字列にする
```

例:

```python
for s in BitAll.bitall(M): ...
idx = BitAll.set_bit_indices(s)
```

### nibutan

二分探索 (汎用 nibutan + 昇順リスト向け lt / le / gt / ge はインデックスを返す、O(log N))

API:

```python
class nibutan
  # nibutan(ok, ng, op): op(ok) が True / op(ng) が False の前提で、op が True となる ng 側ぎりぎりの値を返す
  # lt(L, n) / le(L, n): 昇順 L で n 未満 / n 以下の最大要素のインデックス (無ければ -1)
  # gt(L, n) / ge(L, n): 昇順 L で n 超過 / n 以上の最小要素のインデックス (無ければ len(L))
```

例:

```python
x = nibutan.nibutan(ok, ng, op)
i = nibutan.le(L, n)  # L[i] <= n となる最大の i (L は昇順)
```

### tentou

転倒数 (BIT で O(N log N))

API:

```python
class BIT
  __init__(num)
  set(L)
  update(x, n)
  getV(x)
```

例:

```python
cnt = tentou(A)
```

### prevgreater

各要素の左側で、それより大きい最も右の要素の番号 (単調スタック O(N))

API:

```python
def prev_greater(A)
```

例:

```python
res = prev_greater(A)  # res[i] = i より前で A[i] より大きい最も右の番号 / なければ -1
```

### grundy

組み合わせゲームの Grundy 数を総当たり計算 (遷移関数を渡す・ゲームの和は XOR・小さい状態の実験用)

API:

```python
class Grundy
  # 組み合わせゲームの Grundy 数を総当たりで求める（小さい状態で周期・規則性を探す実験用）
  #   g(s): 状態 s の Grundy 数を返す（0 なら手番側の負け）
  #   table(states): 各状態の Grundy 数を print する
  # moves(s): s から 1 手で移れる状態のリストを返す関数（利用者が定義）
  #   遷移先を list で返すと「独立な複数ゲームの和」とみなし、各 Grundy 数の XOR を取る
  # 状態は hashable（int / tuple / frozenset 等）であること。再帰なので深い状態は PyPy 推奨
```

例:

```python
def moves(n):  # 1〜3 個取れる石取り
  return [n - k for k in (1, 2, 3) if n - k >= 0]
gr = Grundy(moves)
gr.table(range(20))  # 0 1 2 3 0 1 2 3 ... の周期が見える
def moves2(n):  # 山を 2 つの空でない山に分ける
  return [[a, n - a] for a in range(1, n)]
Grundy(moves2).table(range(10))
```


## 09 アーカイブ（旧版）

ファイル: [`09-archive.code-snippets`](.vscode/09-archive.code-snippets)

### olddeque

両端キュー Deque (両端 O(1)・ランダムアクセス対応・二重スタック実装)

API:

```python
class Deque
  # add_r(n): 末尾に追加する
  # add_l(n): 先頭に追加する
  # pop_r(): 末尾から取り出す
  # pop_l(): 先頭から取り出す
  # size(): 要素数を返す
  # is_empty(): 空かどうかを返す
  # get(ind): 先頭から ind 番目の要素を返す
  # getList(): 中身をリストで返す (チェック用 O(N))
```

例:

```python
dq = Deque([1, 2, 3])
dq.add_r(4)
dq.pop_l()
```

### oldlazyseg

遅延評価セグ木 (自己完結版・ACL 不要・op/e/mapping/composition/id 渡し)

API:

```python
class lazySegTree
  #遅延評価セグメント木
```

例:

```python
t = lazySegTree(op, e, mapping, composition, id, v)
t.apply(l, r, f)
```

### oldtree

[旧] 木構造 TreeFactory (LCA / 距離 / 部分木サイズ / 全方位木 DP 等)（tree / treepath / treedp / auxtree に置き換え）

API:

```python
class TreeFactory
  __init__(num)
  setByAdjacencyList(list, index = 0)
  setByParentList(list, index = 0)
  set(a, b)
  makeTree()
  makeTreeDP(root)
  makeTour(root)
  makeLca(root)
  makeAuxiliaryTree(root, V)
  makeHld(root = 0)
  makesub(root)
```

例:

```python
t = TreeFactory(N)
t.setByAdjacencyList(edges)
lca = t.makeLca(root)
```

### oldtreedp

[旧] 木 DP (子の DFS 結果から親へ集約する典型木 DP テンプレ)（treedp に置き換え）

API:

```python
class Tree
  # setByAdjacencyList(list, index): 辺リスト list = [(u, v), ...] から木を作る
  # setByParentList(list, index): 親リスト list (list[i] = ノード i+1 の親) から木を作る
  # makeRank(root): root を根として各ノードの親/子/深さを計算する
  # allDP(): 全方位木DP(ボトムアップ+トップダウン)を実行し結果を返す
```

例:

```python
t = Tree(N)
t.setByAdjacencyList(edges)
t.makeRank(root)
ans = t.allDP()
```
