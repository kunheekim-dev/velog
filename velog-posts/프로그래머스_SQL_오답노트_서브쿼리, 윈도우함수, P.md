<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-summaxmin">프로그래머스 SQL 고득점 KIT 내 SUM,MAX,MIN</h3>
<p>Level 2. 연도별 대장균 크기의 편차 구하기</p>
</blockquote>
<p>분화된 연도(YEAR), 분화된 연도별 대장균 크기의 편차(YEAR_DEV), 대장균 개체의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 분화된 연도별 대장균 크기의 편차는 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기로 구하며 결과는 연도에 대해 오름차순으로 정렬하고 같은 연도에 대해서는 대장균 크기의 편차에 대해 오름차순으로 정렬해주세요.</p>
<blockquote>
<h3 id="문제-끊어-읽기">문제 끊어 읽기</h3>
</blockquote>
<p><code>SELECT</code> 
분화된 연도 YEAR, 
분화된 연도별 대장균 크기의 편차 YEAR_DEV, 
ID 출력
<code>FROM</code>
ECOLI_DATA
<code>ORDER BY</code>
YEAR, YEAR_DEV</p>
<p>조건</p>
<ol>
<li>분화된 연도 YEAR
DIFFERENTIATION_DATA 에서 연도 추출</li>
<li>분화된 연도별 대장균 크기의 편차 AS YEAR_DEV
DIFFERENTIATION_DATA 연도 추출 - 연도별
MAX 가장 큰 SIZE_OF_COLONY
각 대장균의 크기 SIZE_OF_COLONY</li>
</ol>
<p><code>WHEN</code>절 사용? 
<code>GORUP BY</code> 사용? 
<code>서브쿼리</code> 사용? 
<code>윈도우함수</code>사용?</p>
<blockquote>
<h3 id="어떤-함수를-써야하는지-판단하는-요령">어떤 함수를 써야하는지 판단하는 요령</h3>
</blockquote>
<p><strong>1. 내가 원하는 데이터는 개별행인가? 그룹데이터인가?</strong></p>
<ul>
<li><p>개별행 데이터 = <code>윈도우함수 (OVER())</code></p>
</li>
<li><p>그룹별로만 요약된 한줄 데이터 = <code>GROUP BY</code></p>
</li>
<li><p>다른 테이블 OR 같은 테이블의 특정값 갖고오기 = <code>JOIN</code> <code>WHERE</code></p>
</li>
</ul>
<hr />
<p><strong>2. 어떤 계산이 필요한가?</strong></p>
<ul>
<li><p>같은 그룹 내 각 행마다 비교 또는 계산
<code>윈도우함수 (OVER())</code> : 개별행이 유지된 채, 같은 그룹의 다른 값과 비교한다.
EX. 각 행마다 연도별 최대값과 비교</p>
</li>
<li><p>단순 그룹별 요약값이 필요
<code>GROUP BY</code> : <code>SUM()</code> <code>COUNT()</code> <code>AVG()</code> <code>MAX()</code> 등 집계함수로 집계하고, 개별행이 필요 없는 경우.
EX. 연도별 대장균의 평균 크기</p>
</li>
<li><p>어떤 값을 찾기 위해 테이블을 한번 더 조회하는 경우.
<code>서브쿼리 (JOIN OR WHERE)</code>
EX. 이 개체의 부모 크기 갖고오기</p>
</li>
</ul>
<hr />
<p><strong>3. 문제에서 핵심적으로 비교하는 값은?</strong></p>
<p>3-1. 같은 그룹 내의 값과 비교하는가? = <code>OVER(PATITION BY())</code></p>
<ul>
<li>각 행마다 같은 연도의 최대값과 비교해야한다.
(연도별 최대 크기 / 개별 크기)</li>
</ul>
<p>3-2. 특정한 그룹끼리 합산 = <code>GROUP BY</code></p>
<ul>
<li>연도별 개체수를 세어라. -&gt; <code>COUNT(*) GROUP BY YEAR</code></li>
</ul>
<p>3-3. 다른 행에서 특정 값을 가져옴 = <code>서브쿼리 - JOIN</code></p>
<ul>
<li>이 개체의 부모 개체의 크기를 찾아라. -&gt; <code>JOIN</code> 또는 <code>WHERE(SELECT...)서브쿼리</code></li>
</ul>
<hr />
<p><strong>4. 조건이 <code>WHERE</code>에 들어가나, <code>HAVING</code>에 들어가나?</strong></p>
<ul>
<li><p>각 행을 기준으로 조건을 건다 - <code>WHERE</code>
EX. SIZE_OF_COLONY가 50 이상인 개체만 출력해라.</p>
</li>
<li><p>집계된 값(그룹별 최댓값, 합계 등)에 조건을 건다 - <code>HAVING</code>
EX. 연도별 개체수가 10개 이상인 연도만 출력해라.</p>
</li>
</ul>
<hr />
<blockquote>
<h3 id="다시-문제-함수-선택하기">다시 문제 함수 선택하기.</h3>
<p>[각 행마다 연도별 최대값과 비교해야함]</p>
</blockquote>
<p><code>SELECT</code> 
분화된 연도 YEAR, 
분화된 연도별 대장균 크기의 편차 YEAR_DEV, 
ID 출력
<code>FROM</code>
ECOLI_DATA
<code>ORDER BY</code>
YEAR, YEAR_DEV</p>
<p><strong>적용</strong></p>
<ol>
<li>연도별 가장 큰 대장균 크기 - 개별 대장균 크기 구하기</li>
</ol>
<ul>
<li>개별행 유지  = <code>윈도우 함수 OVER</code></li>
<li>각 연도별 최대 크기 비교 = <code>OVER(PARTITION BY())</code></li>
<li>연도별 최대 크기 = <code>MAX(SIZE_OF_COLONY) OVER(PARTITON BY)</code></li>
</ul>
<blockquote>
<h3 id="정답">정답</h3>
</blockquote>
<pre><code class="language-sql">SELECT 
    EXTRACT(YEAR FROM DIFFERENTIATION_DATE) AS YEAR, 
    (MAX(SIZE_OF_COLONY) 
     OVER(PARTITION BY EXTRACT(YEAR FROM DIFFERENTIATION_DATE)) 
        - SIZE_OF_COLONY) AS YEAR_DEV,
    ID
FROM ECOLI_DATA
ORDER BY YEAR, YEAR_DEV ;</code></pre>
<hr />
<p><strong>추가로 GROUP BY, 서브쿼리 JOIN 비교</strong></p>
<ol>
<li><p>연도별로 개체의 평균 크기 구하기.</p>
<pre><code class="language-sql">SELECT EXTRACT(YEAR FROM DIFFERENTIATION_DATE) AS YEAR, 
    AVG(SIZE_OF_COLONY) AS AVG_SIZE
FROM ECOLI_DATA
GROUP BY EXTRACT(YEAR FROM DIFFERENTIATION_DATE);</code></pre>
<p>#그룹별 집계가 필요 = <code>GROUP BY</code></p>
</li>
<li><p>각 개체의 부모 개체의 크기와 비교해서 얼마나 큰지 작은지 비교해서 출력하기.</p>
<pre><code class="language-sql">SELECT 
 E1.ID,
 E1.SIZE_OF_COLONY,
 E2.SIZE_OF_COLONY AS PARENT_SIZE,
 CASE 
     WHEN E1.SIZE_OF_COLONY &gt; E2.SIZE_OF_COLONY THEN 'LARGER'
     ELSE 'SMALLER'
 END AS SIZE_COMPARE
FROM ECOLI_DATA E1
JOIN ECOLI_DATA E2
ON E1.PARENT_ID = E2.ID;</code></pre>
<p>#다른 행에서 데이터를 가져옴 = <code>JOIN</code></p>
</li>
</ol>