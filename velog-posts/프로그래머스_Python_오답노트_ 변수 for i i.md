<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 1. 나누어 떨어지는 숫자 배열</p>
</blockquote>
<p>array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.</p>
<blockquote>
<h3 id="오답-확인">오답 확인</h3>
<ol>
<li><code>return [ i for i in arr if i % divisor == 0 else -1 ]</code> </li>
</ol>
</blockquote>
<ul>
<li><code>if</code>와 <code>else</code>의 위치가 잘못됨.
<code>리스트 컴프리헨션</code>으로 if조건 뒤 else가 오려면, <code>[값1 if 조건 else 값2 for i in 리스트]</code>의 삼항자 연산식이어야함. 즉 <code>else</code>가 빠지거나/ 삼항자연산식을 써야함.<blockquote>
<ol start="2">
<li><code>return [ i if i % divisor == 0 for i in arr]</code> </li>
</ol>
</blockquote>
</li>
<li>if 뒤에 바로 for가 올 수 없음! <code>else</code>가 빠짐! <code>리스트 컴프리헨션</code>에서 if 썼으면 else를 써서 삼항자 연산식으로 써야함. <code>[값1 if 조건 else 값2 for i in 리스트]</code>여야함.<blockquote>
<ol start="3">
<li><code>return [ i if i % divisor == 0 else -1 for i in arr]</code> 
Q. 리스트 컴프리헨션으로 쓰려면 문법을 맞추라고 해서 맞췄는데도 틀림. 
A. 이건 모든 값을 리스트로 만든것. 문제는 딱 떨어지는것만 [ ] 리스트하고, 나누어 떨어지는게 없으면 [-1] 단독으로 리스트해야함.
그런데 이건 결과값이 섞여서 나옴. [5,10,-1,20,-1] 이런식으로 나와버림. 따라서 else를 분리해줘야함.</li>
</ol>
</blockquote>
</li>
</ul>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** [i for i in 리스트 if 조건] ** </p>
<pre><code class="language-python">def solution(arr, divisor):
    A = sorted([i for i in arr if i % divisor == 0])
    return A if A else [-1]</code></pre>
<ul>
<li><code>sorted(리스트)</code> : 리스트 오름차순 정렬</li>
<li><code>for</code>를 <code>리스트 []</code>안에 넣을때는 반드시 <code>for</code>앞에 <code>넣을값</code> 즉 <code>i</code>와 같은 변수가 있어야함. '무엇을 넣을지'말하지 않으면 혼란스러움.</li>
<li>else를 따로 빼서, 다음줄에 <code>값1 if 조건 else 값2</code>로 표현. <code>if조건</code>으로 값을 뜻하는 변수가 온 경우, 값이 있으면 True, 값이 없으면 False라서, 만족하는 값이 없는 경우, else [-1]이 됨.</li>
<li>문제에서 요구하는게 <code>[]리스트</code> 형식이기 때문에 -1이 아닌, [-1]로 작성.<blockquote>
<h3 id="삼항자-조건-연산자와-리스트-컴프리헨션-비교">삼항자 조건 연산자와 리스트 컴프리헨션 비교</h3>
</blockquote>
</li>
</ul>
<ol>
<li><code>삼항자 조건 연산자</code> : <code>값1 if 조건 else 값2</code> 이며, 단순 조건따라 둘 중 하나값을 정하는것.  <code>[]</code>사용 의미 없음. 가능은 하지만, 1개짜리 리스트를 만드는것과 같음.<pre><code class="language-python">x = 5
result = &quot;짝수&quot; if x % 2 == 0 else &quot;홀수&quot;
print(result) 
</code></pre>
</li>
</ol>
<p>```
2. <code>리스트 컴프리헨션</code> : <code>[값1 if 조건 else 값2 for i in 리스트]</code> 반드시 for가 뒤에 나와야함.</p>