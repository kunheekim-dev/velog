<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 0. 외계행성 나이</p>
</blockquote>
<p>우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<blockquote>
<ol>
<li><code>딕셔너리 사용</code> </li>
</ol>
</blockquote>
<pre><code class="language-python">def solution(age):
    d = {
        0:'a',
        1:'b',
        2:'c',
        3:'d',
        4:'e',
        5:'f',
        6:'g',
        7:'h',
        8:'i',
        9:'j'
    }
    return ''.join(d[int(i)] for i in str(age))</code></pre>
<ul>
<li><code>딕셔너리</code></li>
<li><code>return</code>은 결과를 반환하는 키워드.</li>
<li><code>result =</code> 변수 할당하고 사용함. </li>
<li><code>d[i] for i in str(age)</code>는 str(age)에서 하나씩 뽑는 i가 문   자열이라 딕셔너리 key (숫자)랑 매치를 못함.</li>
<li><code>d[i]</code>를 숫자로 변경해서, 딕셔너리 key랑 매치함.</li>
<li></li>
</ul>
<blockquote>
<p>2.<code>인덱스 사용</code> </p>
</blockquote>
<pre><code class="language-python">def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer += alpha[int(i)]
    return answer</code></pre>
<ul>
<li><code>인덱스</code>는 <code>정수</code>여야하기 때문에 <code>alpha[int(i)]</code> 라고 <code>정수</code> 처리함.</li>
</ul>
<hr />
<blockquote>
<h3 id="인덱스-정리">인덱스 정리</h3>
</blockquote>
<ol>
<li><p>값을 가져오기.
<code>리스트[인덱스]</code>  or <code>문자열[인덱스]</code>
ex. a[1] -&gt; 'b'</p>
</li>
<li><p>위치 찾기.
<code>리스트.인덱스(값)</code> or <code>문자열.index(값)</code>
ex. a.index('b') -&gt; 1</p>
</li>
<li><p>안되는 경우!!</p>
<pre><code class="language-python">d = {'a': 1, 'b': 2}
d.index('a')     # ❌ AttributeError 발생
</code></pre>
</li>
</ol>
<p>d['a']   # -&gt; 1 딕셔너리는 key 기반.</p>
<pre><code>- 리스트, 문자열이 아닌 자료형 (딕셔너리)는 index() 안됨!!
- 딕셔너리는 key 기반. `딕셔너리.[]` 사용해야함.

4. 딕셔너리에서 `n번째 항목`을 찾을때
``` python
list(d.items())[1]    # ('b', 20) → 두 번째 항목
list(d.keys())[1]     # 'b' → 두 번째 키
list(d.values())[1]   # 20 → 두 번째 값</code></pre><ol start="5">
<li>정리
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/b1f48c0e-4747-4e0e-b1ea-bf5cab564cb3/image.png" /></li>
</ol>