<p>계속 계속 틀리는 나의 리스트 컴프리헨션....</p>
<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 1. x만큼 간격이 있는 n개의 숫자</p>
</blockquote>
<p>함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.</p>
<blockquote>
<h3 id="오답-확인">오답 확인</h3>
<ol>
<li><code>return [ i for i in range(1, n+1) if x*i]</code> </li>
</ol>
</blockquote>
<ul>
<li><code>if x* i</code> 조건절이 항상 참이 됨. (값이 있으면 참, 값이 0이면 거짓). 항상 참이 되면, 모든 i가 다 리스트 되는데 문제는, x*i의 형태로 리스트되는게 아니라 그냥 i가 리스트됨. (1,2,3,...)</li>
</ul>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** [i for i in range()] ** </p>
<pre><code class="language-python">def solution(x, n):
    return [x*i for i in range(1, n+1)]</code></pre>
<ul>
<li><code>x*i</code>의 형태로 리스트됨. range 범위가 1 ~ n+1 까지 다 i에 넣고 계산하여 return 결과는 x*i로 되는것.</li>
</ul>