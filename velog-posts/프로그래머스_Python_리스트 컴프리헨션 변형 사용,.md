<p>리스트 컴프리헨션의 다양한 사용
여태 <code>[i for i in range()]</code>뿐이었던 나에게
<code>range()</code> 말고 다른것도 사용 가능하단걸 보여준 예.</p>
<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 1. 자리수 더하기</p>
</blockquote>
<p>자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** [int(i) for i in str(n)] ** </p>
<pre><code class="language-python">def solution(n):
    return sum([int(i) for i in str(n)])</code></pre>
<ul>
<li><code>sum</code>은 <code>sum()</code>이거니까, list만드는건 <code>[]</code>.</li>
<li><code>i</code> 대신 리스트에 들어갈 건 문자 아닌 숫자 <code>int(i)</code>여야 <code>sum</code>이 가능함.</li>
<li><code>range()</code>만 올 수 있는 줄 알았으나, <code>str(n)</code> 도 가능함.</li>
<li><code>for c in 'hello'</code> 뭐 이런것도 됨. <code>c</code>는 <code>i</code>대신 들어간 변형자. 쓰기 나름이니, <code>for</code>를 잘 활용하자.</li>
</ul>