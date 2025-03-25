<p>리스트 컴프리헨션 응용.
두가지 논리적인 풀이.
풀어놓은 논리 구조 익히기!</p>
<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 1. 나머지가 1이 되는 수 찾기</p>
</blockquote>
<p>자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 풀어서 [논리 순서대로] 작성 ** </p>
<pre><code class="language-python">def solution(n):
    for x in range(1,n):
        if n % x == 1:
            return x</code></pre>
<ul>
<li>반복 범위 지정 + 반복문 공식 + x 출력</li>
<li>1부터 범위가 지정되어있기 때문에, 나누다가 제일 처음 나오는 x 나오면 종료됨. (x 1개 나오면 종료. 그리고 그 값이 가장 최소값)</li>
</ul>
<p><strong>한줄로 <code>리스트 컴프리헨션</code>사용한 문제 풀이</strong></p>
<pre><code class="language-python">def solution(n):
    return min([x for x in range(1, n) if n%x == 1])</code></pre>
<ul>
<li><code>[]</code>리스트를 만들고 <code>min()</code> 값을 추출함.</li>
<li>메모리를 좀 더 씀.</li>
</ul>
<p><strong>한줄로 <code>제너레이션 표현식</code>사용한 문제 풀이</strong></p>
<pre><code class="language-python">def solution(n):
    return min(x for x in range(1, n) if n%x == 1)</code></pre>
<ul>
<li><code>[]</code>리스트 안만들고 <code>min()</code> 값만 추출함.</li>
<li>메모리를 안씀. 더 효율적이고 빠름</li>
</ul>