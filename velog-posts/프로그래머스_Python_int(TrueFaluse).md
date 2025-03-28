<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. n의 배수</p>
</blockquote>
<p>정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 1. 익숙한 방식 : 삼항 연산자 ** </p>
<pre><code class="language-python">def solution(num, n):
    return 1 if num%n == 0 else 0</code></pre>
<blockquote>
<h3 id="정답-확인-1">정답 확인</h3>
</blockquote>
<p>** 2. <code>int()</code> 응용하기 ** </p>
<pre><code class="language-python">def solution(num, n):
    return int(num%n == 0)</code></pre>
<blockquote>
<p><strong><code>int()</code>에서 True / Faluse 에 따른 값 반환</strong></p>
</blockquote>
<ul>
<li><code>int(True)</code> : 1 을 반환</li>
<li><code>int(Faluse)</code> : 2 를 반환</li>
</ul>