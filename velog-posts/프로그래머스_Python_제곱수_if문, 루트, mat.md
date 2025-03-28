<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 0. 제곱수 판별하기</p>
</blockquote>
<p>어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인-replace-안씀">정답 확인 (replace 안씀)</h3>
</blockquote>
<blockquote>
<ol>
<li><code>for 반복문 + if문</code> </li>
</ol>
</blockquote>
<pre><code class="language-python">def solution(n):
    for i in range(1,1001):
        if i**2 == n:
            return 1
    return 2</code></pre>
<ul>
<li><code>return</code>의 위치를 자꾸 잘못 넣음.
만일 <code>if</code>문 아래에 위치한다면, <code>i=1</code>만 검사하고 바로 return 해버림. 더 검사하고 싶으면, return을 <code>if</code>문 밖으로 빼야함.</li>
</ul>
<h2 id="while-vs-if-차이">**[while vs if 차이!]</h2>
<p><code>while</code>은 조건이 맞는 동안 계속 반복함.
<code>if</code>는 조건이 한번 맞는지 확인해서 실행함.</p>
<blockquote>
<p>2.<code>수학적 풀이_루트 사용</code> </p>
</blockquote>
<pre><code class="language-python">def solution(n):
    return 1 if int(n**0.5)**2 == n else 2</code></pre>
<ul>
<li><code>n**0.5</code> : 루트n, 즉 n의 제곱근.
n = 6, <code>16 ** 0.5 = 4</code>
n = 18, <code>18 ** 0.5 = 4.24</code></li>
<li><code>int(n**0.5)</code> : 제곱근을 정수로 자른것. 
int(4) = 4
int(4.25) = 4</li>
<li><code>int(n**0.5) ** 2</code> : 정수로 자른 값에 다시 제곱.
n = 16 - <code>int(16**0.5)=4</code> - <code>4**2=16</code></li>
<li>전체 조건 : <code>int(n**0.5)**2==n</code>
n의 제곱근을 정수로 자른 다음 다시 2(제곱)할때, 원래의 수 n과 같으면 n은 제곱수.</li>
</ul>
<blockquote>
<p>3.<code>math 라이브러리</code> </p>
</blockquote>
<pre><code class="language-python">import math
def solution(n):
    return 1 if math.isqrt(n)**2 == n else 2</code></pre>
<ul>
<li><code>math.isqrt()</code> : 루트n, 즉 n의 제곱근.</li>
</ul>