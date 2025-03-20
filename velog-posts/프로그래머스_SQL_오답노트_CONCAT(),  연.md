<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-summaxmin">프로그래머스 SQL 고득점 KIT 내 SUM,MAX,MIN</h3>
<p>Level 1. 잡은 물고기 중 가장 큰 물고기의 길이 구하기</p>
</blockquote>
<p>FISH_INFO 테이블에서 잡은 물고기 중 가장 큰 물고기의 길이를 'cm' 를 붙여 출력하는 SQL 문을 작성해주세요.</p>
<p>이 때 컬럼명은 'MAX_LENGTH' 로 지정해주세요.</p>
<blockquote>
<h3 id="오라클-및-my-sql-공통-정답">오라클 및 MY SQL 공통 정답</h3>
<p><code>CONCAT()</code> 함수 사용</p>
</blockquote>
<pre><code class="language-sql">SELECT CONCAT(MAX(LENGTH),'cm') AS MAX_LENGTH
FROM FISH_INFO</code></pre>
<ul>
<li><code>||</code> 연산자는 오라클에서만 사용 가능!</li>
</ul>
<pre><code class="language-sql">SELECT MAX(LENGTH)||'cm' AS MAX_LENGTH
FROM FISH_INFO</code></pre>
<p>연산자 사용했다가 틀림! (MY SQL이라서!)
함수도 함께 알아두자!</p>
<p>추가로, 
<strong><code>WHERE</code>에서는 <code>집계함수</code> 사용 불가!</strong></p>
<ol>
<li><code>WHERE</code>는 행을 비교하는데, <code>집계함수</code>는 전체 데이터를 계산하는 함수이기 때문!</li>
<li>굳이 쓰고 싶다면, <code>HAVING</code>에서 가능하나, <code>HAVING</code>절에서는 단순 <code>MAX()</code>가 아닌, <code>MAX(LENGTH) &gt; 100</code>과 같은 비교연산자를 사용한 구체적인 비교가 이루어져야함.</li>
</ol>