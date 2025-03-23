<p>4가지 수식을 비교할 예정.</p>
<blockquote>
<h3 id="프로그래머스-python-코딩테스트-입문">프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 짝수의 합.</p>
</blockquote>
<p>정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p><strong>1. for문 + if 조건문 (기본)</strong></p>
<pre><code class="language-python">def solution(n):
    answer = 0
    for i in range(1, n + 1):  # 1부터 n까지 반복
        if i % 2 == 0:  # 짝수인지 확인
            answer += i  # 짝수라면 더하기
    return answer
# 테스트
print(solution(10))  # 30
print(solution(4))   # 6</code></pre>
<ul>
<li>코드길이 : 길다</li>
<li>속도 : 느림</li>
<li>가독성 : 직관적</li>
</ul>
<p><strong>2. for문에서 바로 짝수 반복 (더 효율)</strong></p>
<pre><code class="language-python">def solution(n):
    answer = 0
    for i in range(2, n + 1, 2):  # 2부터 n까지 2씩 증가
        answer += i
    return answer
# 테스트
print(solution(10))  # 30
print(solution(4))   # 6</code></pre>
<ul>
<li>코드길이 : 짧다</li>
<li>속도 : 중간</li>
<li>가독성 : 좋음</li>
</ul>
<p><strong>3. 리스트 컴프리헨션 + sum() (깔끔. python 방식)</strong></p>
<pre><code class="language-python">def solution(n):
    answer = sum (i for i in range(2, n + 1, 2))
    return answer</code></pre>
<ul>
<li>코드 길이 : 매우 짧음.</li>
<li>속도 : 중간</li>
<li>가독성 : pythonic 직관적</li>
</ul>
<p><strong>4. 등차수열 공식 (수학적 방식, 가장 빠름)</strong></p>
<pre><code class="language-python">def solution(n):
    return (n // 2) * (2 + n) // 2
# 테스트
print(solution(10))  # 30
print(solution(4))   # 6</code></pre>
<ul>
<li>코드 길이 : 짧다</li>
<li>속도 : 가장 빠름</li>
<li>가독성 : 수학적 사고 필요</li>
</ul>
<hr />
<blockquote>
<h3 id="함수-정리">함수 정리</h3>
</blockquote>
<ol>
<li><code>range(start, stop, step)</code></li>
</ol>
<ul>
<li><code>start</code> : 시작 숫자 (포함)</li>
<li><code>stop</code> : <strong>종료 숫자 (포함 안됨)</strong></li>
<li><code>step</code> : 증가값
종료값 즉 <code>stop</code>값이 포함되려면, <code>n+1</code>을 해줘야 <code>n</code>값이 포함.</li>
</ul>
<p>예를 들면, 2부터, n까지, 2씩 증가.
= range (2, n+1, 2)</p>
<ol start="2">
<li><code>i for i in range()</code>
제너레이터 표현식으로 리스트 없이 값 생성 가능.</li>
</ol>
<ul>
<li><strong>추가 예제</strong> 
짝수 중에서도 4보다 큰 값만 더하기.<pre><code class="language-python">sum(i for i in range(2, n+1, 2) if i &gt; 4)</code></pre>
</li>
<li><code>if</code>조건 추가 가능 -&gt; SQL의 <code>WHERE</code>처럼 사용 가능!</li>
</ul>
<hr />
<blockquote>
<h3 id="등차수열-공식">등차수열 공식</h3>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/kunhee/post/3391d06a-3f62-4c56-ad6f-b333246708d2/image.png" /></p>