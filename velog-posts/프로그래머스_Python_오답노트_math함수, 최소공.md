<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 피자 나눠 먹기 (2)</p>
</blockquote>
<p>정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 1. 차근차근 ** </p>
<pre><code class="language-python">def solution(n):
    return min((i for i in range(1, 101) if (6*i)%n == 0))</code></pre>
<ul>
<li>range 범위는 n을 기준으로 잡음</li>
<li><code>min()</code>을 붙이지 않으면, n식을 만족하는 모든 i가 구해짐.</li>
<li>()<code>제너레이터 표현식</code> 도 가능하고, []<code>리스트 컴프리헨션</code> 도 가능함. </li>
</ul>
<p>** 2. 수학적 풀이 [최소공배수] **</p>
<pre><code class="language-python">import math
def solution(n):
    lcm = (6 * n) // math.gcd(6, n)
    return lcm // 6</code></pre>
<p>-** <code>GCD</code> : 최대공약수 / GCD(6,8) = 2**
-** <code>LCM</code> : 최소공배수 / LCM(6,8) = 24**
-** <code>LCM = (a * b)) // GCD(a,b)</code>   :  (6<em>8) // 2 = 24*</em></p>