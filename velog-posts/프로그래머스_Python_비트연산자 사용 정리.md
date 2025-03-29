<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 세균 증식</p>
</blockquote>
<p>어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인-수학적--비트연산자">정답 확인 (수학적 / 비트연산자)</h3>
</blockquote>
<p><strong>1. 수학 풀이</strong></p>
<pre><code class="language-python">def solution(n, t):
    return n*(2**t)</code></pre>
<p><strong>2. 비트연산자 사용</strong></p>
<pre><code class="language-python">def solution(n, t):
    return n&lt;&lt;t</code></pre>
<p><code>n&lt;&lt;t</code>는 n * (2**t) 뜻임.</p>
<hr />
<blockquote>
<h3 id="비트연산자-정리">비트연산자 정리</h3>
</blockquote>
<p><code>비트연산자</code>란 숫자를 2진수(0과 1)로 표현해서 그 비트(자리)들을 직접 비교하거나 조작하는것.</p>
<ol>
<li>비트연산자의 종류
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/18ae2a9c-b9cf-4bde-abf0-1faac3feb498/image.png" /></li>
</ol>
<ul>
<li><code>n&lt;&lt;t</code>는 n * (2**t) 뜻임.</li>
<li><code>n&gt;&gt;t</code>는 n // (2**t) 뜻임. (정수 나눗셈 // 과 동일)</li>
</ul>