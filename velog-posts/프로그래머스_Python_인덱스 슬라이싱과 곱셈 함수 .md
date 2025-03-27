<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 원소들의 곱과 합</p>
</blockquote>
<p>정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 1. 인덱스 슬라이싱 ** </p>
<pre><code class="language-python">def solution(num_list):
    import math
    return 1 if math.prod(num_list[::]) &lt; (sum(num_list[::])**2) else 0</code></pre>
<ul>
<li><code>math.prod()</code> : 곱셈 함수</li>
<li>사실 인덱스 슬라이싱을 쓸 필요가 없음.</li>
<li><strong><code>[123456789]</code> : <code>인덱스 슬라이싱</code> 만 사용 가능. 1개의 문자열이기 때문.</strong> </li>
<li>*<em><code>[1,2,3,4,5,6,7]</code> : <code>인덱스 슬라이싱</code> 과 <code>직접 (리스트)</code> 둘 다 사용 가능. *</em></li>
</ul>
<p>** 2. 간단한 풀이**</p>
<pre><code class="language-python">def solution(num_list):
    import math
    return 1 if math.prod(num_list) &lt; (sum(num_list)**2) else 0</code></pre>
<p><strong>- 어차피 전체 다 계산하는거라서 그냥 범위 지정 없이 (리스트)를 넣어줌.</strong></p>