<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 중앙값 구하기</p>
</blockquote>
<p>중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 인덱스 활용 ** </p>
<pre><code class="language-python">def solution(array):
    array.sort()
    return array[len(array)//2]</code></pre>
<pre><code class="language-python">def solution(array):
    return sorted(array)[len(array)//2]</code></pre>
<ul>
<li>sorted(array)로 리스트 반환 + 바로 갖고올 위치 [len(array)//2] 를 써준것.</li>
</ul>
<blockquote>
<p><strong><code>sort()</code> 와 <code>sorted()</code>의 차이 (오름차순 정렬 공통)</strong></p>
</blockquote>
<ul>
<li><code>리스트.sort()</code> : 리스트를 제자리에서 변경 (원본리스트 변경)</li>
<li><code>sorted(리스트)</code> : 새로운 정렬 리스트 반환 (원본리스트 유지)</li>
<li><code>array.sort()</code> : 원본 array가 새롭게 오름차순 정렬됨.</li>
<li><code>리스트.sort(reverse=True)</code> :  내림차순 정렬</li>
<li><code>리스트.sort(key = len)</code> : 문자순 정렬. key = 조건</li>
<li><code>sorted(리스트, reverse=True)</code> : 내림차순 정렬</li>
</ul>
<p><strong>인덱스 함수 사용 설명</strong></p>
<ul>
<li>리스트에 <code>[ ]</code>를 붙이면 특정 위치(인텍스)값을 가져올 수 있음.</li>
<li><code>리스트[ ]</code> 하면 [ ] 번째 값을 가지고옴.</li>
<li>리스트 위치 숫자는 1부터가 아닌, 0부터 시작됨.
ex. <code>return array[len(array)//2]</code> 는 array 길이숫자 // 2인것인데, 0부터 시작하니까 중앙값이 구해짐.</li>
</ul>