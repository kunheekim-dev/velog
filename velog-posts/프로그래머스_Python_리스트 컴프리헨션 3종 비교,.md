<h2 id="리스트-컴프리헨션-문제-종합-비교-정리"><strong>리스트 컴프리헨션 문제 종합 비교 정리</strong></h2>
<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 대문자와 소문자</p>
</blockquote>
<p>문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="1-정답-확인">1. 정답 확인</h3>
</blockquote>
<p>** 1. '구분자'.JOIN(리스트) 구문 ** </p>
<pre><code class="language-python">def solution(my_string):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in my_string])</code></pre>
<ul>
<li><p><code>isupper()</code> : 대문자인지 확인 (True/False)</p>
</li>
<li><p><code>islower()</code> : 소문자인지 확인 (T/F)</p>
</li>
<li><p><code>''.JOIN(리스트)</code> : 따로 구분자 없이 ''이렇게 바로 리스트한걸 JOIN한다는 의미. 리스트를 하나의 문자열로!</p>
</li>
<li><p>(리스트) 안에 <code>[리스트 컴프리헨션]</code>을 넣은 구조</p>
</li>
<li><p><code>[값1 if 조건 else 값2 for i in 리스트]</code> :  [ i.lower() if i.isupper() else i.upper() for i in my_string ] </p>
</li>
</ul>
<p><strong>2. 사실 이 경우는 <code>swapcase()</code>함수를 쓰면 더 편함.</strong></p>
<pre><code class="language-python">def solution(my_string):
    return my_string.swapcase()</code></pre>
<hr />
<blockquote>
<h3 id="2-프로그래머스-python-코딩테스트-입문">2. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 짝수 홀수 개수</p>
</blockquote>
<p>정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>
<blockquote>
<h3 id="2-정답-확인">2. 정답 확인</h3>
<p>count()함수는 쓸 수 없음.</p>
</blockquote>
<p>** <code>i for i in 리스트 if 조건</code> 구문 ** </p>
<pre><code class="language-python">def solution(num_list):
    return[sum(1 for i in num_list if i % 2 == 0), sum(1 for i in num_list if i % 2 == 1)]</code></pre>
<ul>
<li><code>count()</code> : 리스트 안에서 특정값이 몇번 나오는지 확인하는 함수. 
ex) 2가 몇번 들어가있나.</li>
</ul>
<hr />
<blockquote>
<h3 id="리스트-컴프리헨션-정리-반드시-for-문이-있어야함">리스트 컴프리헨션 정리 (반드시 for 문이 있어야함.)</h3>
</blockquote>
<ol>
<li><code>값 for 변수 in 리스트</code> <strong>기본 형식</strong></li>
</ol>
<ul>
<li><code>i for i in 리스트</code> : 리스트에서 뽑은 i 를 i 그대로 추가.</li>
<li><code>i</code> : 변경 가능, 리스트에 i를 어떻게 추가할지 정하는 변수.
<code>i *2 for i in 리스트</code> : 뽑은 i에 *2를 해서 추가.</li>
</ul>
<ol start="2">
<li><p><code>값 for 변수 in 리스트 if 조건</code> <strong>특정값만 필터링</strong></p>
</li>
<li><p><code>참일때 값1 if 조건 else 거짓일때 값2 for 변수 in 리스트</code></p>
</li>
</ol>
<p>** 모든값 필터링**</p>
<ol start="4">
<li><p>** if 조건문 뒤에 또 다시 for 가 오면 틀림**</p>
</li>
<li><p>리스트 컴프리헨션 <code>[ 리스트 ]</code> 대괄호를 사용.
리스트 생성 , 메모리에 모든 값 저장, 즉시 사용 가능.
cf) 제너레이터 컴프리헨션 <code>(리스트)</code> 소괄호 사용.
메모리 절약 (모든 값을 저장하지 않고, 필요할때 계산)
값이 바로 보이지 앟아서 list(), for문, next()를 사용해야함.</p>
</li>
</ol>