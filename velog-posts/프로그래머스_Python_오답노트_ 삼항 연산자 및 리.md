<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 0. 숫자 찾기</p>
</blockquote>
<p>정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.</p>
<blockquote>
<h3 id="나의-오답-확인">나의 오답 확인</h3>
</blockquote>
<blockquote>
<ol>
<li>문법 요류 있음. </li>
</ol>
</blockquote>
<pre><code class="language-python">def solution(num, k):
    str(num)
    return [n.index(i) if i == str(k) else -1 for i in n]</code></pre>
<p>1.<code>str(num)</code>으로만 쓰면 변경된 타입이 num에 저장되지 않음. 변수설정을 해줘야함. <code>n = str(num)</code> 이 옳음.
2. <code>.index</code>는 <code>숫자</code> 사용 불가. <code>문자</code> <code>리스트</code> 사용 가능함.
3. <code>[참값 if 조건 else 거짓값 for in 리스트]</code> 는 무조건 <code>[]</code> 괄호가 있어야함.</p>
<ul>
<li><strong>삼항자 연산식</strong> <code>[]</code>필요 없음.
<code>참값 if 조건 else 거짓값 for in 리스트</code></li>
<li><strong>리스트 컴프리헨션</strong> <code>[]</code> 필수
<code>[i for i in 리스트 if 조건]</code>
<code>[참값 if 조건 else 거짓 for i in 리스트]</code></li>
</ul>
<ol start="4">
<li><code>[]</code>대괄호를 친다고 해도, 문제가 '위치 하나만 반환' 하라고 했는데, [  ] 괄호를 치면, [ 2, 3, -1, -1, 1, ]이런식으로 모든 값에 대하여 반환하게됨.</li>
</ol>
<hr />
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<pre><code class="language-python">def solution(num, k):
    return str(num).index(str(k))+1 if str(k) in str(num) else -1</code></pre>
<ul>
<li>같은 문자 타입끼리 비교해야함. 문자와 숫자 비교 불가.</li>
<li><code>.index()</code>는 처음 나온 k값의 인덱스만 반환함. 중복값이있어도, 가장 먼저 나온 위치값을 반환하기 때문에 사용 가능.</li>
</ul>
<pre><code class="language-python">def solution(num, k):
    return str(num).find(str(k))+1 if str(k) in str(num) else -1</code></pre>
<ul>
<li><code>.index()</code> 대신 <code>.find()</code> 써도 됨.</li>
</ul>
<hr />
<blockquote>
<h3 id="-find-정리">. find() 정리</h3>
</blockquote>
<ol>
<li>처음 등장한 위치만 반환</li>
<li><code>문자열</code>에서만 사용 가능.
<code>리스트</code> 불가 - <code>.index()</code>사용
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/feff693b-0cd0-4165-9088-c833a6703afa/image.png" /></li>
</ol>