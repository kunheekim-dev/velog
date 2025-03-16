<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-summaxmin">프로그래머스 SQL 고득점 KIT 내 SUM,MAX,MIN</h3>
<p>Level 3. 물고기 종류 별 대어 찾기</p>
</blockquote>
<p>물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력하는 SQL 문을 작성해주세요.</p>
<blockquote>
<h3 id="문제-요구사항-분석">문제 요구사항 분석</h3>
</blockquote>
<ol>
<li>물고기 종류별로</li>
<li>가장 큰 물고기</li>
<li>ID, 물고기 이름, 길이 출력</li>
</ol>
<blockquote>
<h3 id="정답-해설">정답 해설</h3>
</blockquote>
<ol>
<li>일반적인 <code>WHEN + 서브쿼리</code><pre><code class="language-sql">SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I 
INNER JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
WHERE I.LEGTH = 
   (SELECT MAX(FI.LENGTH)
    FROM FISH_NAME FI
    WHERE FI.FISH_TYPE = I.FISH_TYPE)
ORDER BY ID;</code></pre>
</li>
<li><code>PARTITION BY</code> 사용<pre><code class="language-sql">SELECT ID, FISH_NAME, LENGTH
FROM (
SELECT I.ID, N.FISH_NAME, I.LENGTH,
RANK() OVER (PARTITION BY I.FISH_TYPE ORDER BY I.LENGTH DESC) 
AS RANKING
FROM FISH_INFO I  
INNER JOIN FISH_NAME_INFO N 
ON I.FISH_TYPE = N.FISH_TYPE
) A
WHERE A.RANKING = 1
ORDER BY ID;</code></pre>
</li>
</ol>
<blockquote>
<h3 id="1-when--서브쿼리-구문-풀이">1. [WHEN + 서브쿼리] 구문 풀이</h3>
</blockquote>
<ol>
<li><code>FROM FISH_INFO FI</code>
FISH_INFO 테이블을 가져온다.</li>
<li><code>WHERE FI.FISH_TYPE = I.FISH_TYPE</code> 
2-1) 현재 메인 쿼리에서 보고 있는 <code>I.FISH_TYPE</code>과 같은 <code>FI.FISH_TYPE</code>만 필터링한다.
2-2) 즉 메인 쿼리 <code>FISH-TYPE = 0</code> 이면, 서브쿼리 <code>WHERE FISH_TYPE = 0</code> 인 데이터만 가져온다.</li>
</ol>
<p><strong>2-3) 자연스럽게 <code>GROUP</code>역할을 해주는 것!</strong>
3. <code>SELECT MAX(FI.LENGTH)</code>
각 필터링 된 데이터 중 가장 큰 <code>LENGTH</code>값을 찾는다.</p>
<ol>
<li>메인쿼리 : 
<code>INNER JOIN</code>으로 연결 <code>ON</code>으로 공통 컬럼 조인 조건 작성.</li>
<li>서브쿼리 :
<code>FISH_NAME</code> 테이블만 있어도 됨. (JOIN 안함)
메인 쿼리에서 사용한 AS를 쓸 수 없어서 서브쿼리에서 다시 <code>AS</code> 지정해줌.
메인쿼리 <code>FISH_NAME</code> 테이블과 서브쿼리 <code>FISH_NAME</code>테이블을 따로 작성.</li>
<li><code>WHERE FI.FISH_TYPE = I.FISH_TYPE</code> 의미
물고기 타입별로 묶는 <code>GROUP BY</code>의 역할을 해줌.</li>
</ol>
<blockquote>
<h3 id="group-by-와-having-이-안되는-이유">GROUP BY 와 HAVING 이 안되는 이유</h3>
</blockquote>
<ol>
<li><code>GROUP BY</code> </li>
</ol>
<ul>
<li>단독 사용시, 그룹별 하나의 행만 남아서 ID, LENGTH가 무작위인 행이 남게됨. 
(<code>PARTITION BY</code>는 그룹을 유지하며 모든 행을 남김.)</li>
<li>서브쿼리에 사용시, 메인쿼리와 연결이 안됨.</li>
</ul>
<ol start="2">
<li><code>HAVING</code></li>
</ol>
<ul>
<li>해석 순서상 너무 뒤에와서 <code>HAVING</code>조건이 의미 없음.</li>
<li><code>HAVING MAX(LENGTH)</code> 와 같은 단순함수는 불완전 조건이라서 안됨.
<code>HAVING MAX(LENGTH) &gt;50</code> 이와 같이 <code>=</code> <code>&gt;</code> 등의 비교연산자가 반드시 필요함.</li>
</ul>
<blockquote>
<p><code>WHEN+서브쿼리</code> 방식보다 <code>PATITOIN BY</code> 방식이 대량의 데이터 처리에 더 좋음. </p>
</blockquote>
<ul>
<li><code>RANK</code>외 <code>DENSE_RANK</code> 혹은 <code>ROW_NUMBER</code>로 변경해서 2, 3순위 구하기도 쉬움.</li>
</ul>