<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 약수 구하기</p>
</blockquote>
<p>정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 1. 차근차근 ** </p>
<pre><code class="language-python">def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer += [i]
    return sorted(answer)</code></pre>
<ul>
<li><code>answer = ''</code>는 문자열 선언! 
+= [리스트] 는 타입이 달라서 안됨 - <code>answer = [ ]</code> 리스트 선언</li>
<li><code>.sort()</code> : 제자리에서 오름차순 - return 값 none
 리스트에서만 사용 가능. <code>'내 리스트 그냥 지금 정렬해!'</code></li>
<li><code>sorted(리스트)</code> : 새 리스트 반환 - return 값 <code>정렬된 리스트</code>  리스트, 집합, 문자열 모두 사용 가능. <code>'정렬된 결과 따로 저장해서 쓸거야!</code></li>
</ul>
<p>** 2. 중복 제거 <code>set()</code> 사용 **</p>
<pre><code class="language-python">def solution(n):
    answer = set()
    for i in range(1, n+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)
    return sorted(answer)</code></pre>
<ul>
<li><code>set.sort()</code> 불가능. <code>answer.sort()</code>도 정렬만 하고 return 값 none이라 안됨. 따라서 <code>sorted(answer)</code> 이 되어야함.</li>
</ul>
<blockquote>
<h3 id="set-정리"><code>set()</code> 정리</h3>
</blockquote>
<ul>
<li><code>set()</code> : 중복 제거 함수</li>
<li><code>set()</code> : <strong>순서 없는 집합 자료형. 즉, 순서가 없고, 정렬도 없고, 인덱스도 사용 불가능. <code>set() 결과는 set 자료형</code>임.</strong></li>
<li><code>set()</code> 함수와 <code>+=</code> 연산자는 함께 사용 불가. 
 (<code>+=</code> : 리스트에서만 사용 가능.)</li>
<li><code>set()</code>과 <code>append()</code>도 사용 불가. 대신 <code>add()</code> 사용.</li>
<li><code>set([1,2,3,3,])</code> -&gt; {1,2,3} 리스트, 문자열, 튜플 등을 집합으로 변환.</li>
<li><code>set('banana')</code> -&gt; {'a''b''n'} 중복 제거, 순서보장 안됨.
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/d0a18ea5-364c-4100-81a9-2b5cf78f8157/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/9283a007-5949-4608-a0b3-65aa228f6092/image.png" /></li>
</ul>
<blockquote>
<h3 id="append-와-add-정리"><code>append()</code> 와 <code>add()</code> 정리</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kunhee/post/33c077ab-fc6d-4bf4-a88a-4f6d0588a6fc/image.png" /></p>
</blockquote>