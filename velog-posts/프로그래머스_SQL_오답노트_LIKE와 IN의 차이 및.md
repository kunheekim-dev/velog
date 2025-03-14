<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-is-null-문제">프로그래머스 SQL 고득점 KIT 내 IS NULL 문제</h3>
<p>Level 1. 경기도에 위치한 식품창고 목록 출력하기.</p>
</blockquote>
<p>FOOD_WAREHOUSE 테이블에서 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문을 작성해주세요. 이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 결과는 창고 ID를 기준으로 오름차순 정렬해주세요.</p>
<blockquote>
<h3 id="문제-끊어-읽기">문제 끊어 읽기</h3>
</blockquote>
<p><code>FROM</code>  FOOD_WAREHOUSE 테이블에서 /
<code>WHERE</code> <strong>(LIKE, IN)</strong>  경기도에 위치한 /
<code>SELECT</code>  창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문/
<code>NVL</code>  이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 /
<code>ORDER BY</code> 결과는 창고 ID를 기준으로 오름차순 정렬해주세요./</p>
<blockquote>
<h3 id="정답-확인-오라클">정답 확인 [오라클]</h3>
</blockquote>
<pre><code class="language-sql">SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
       NVL(FREEZER_YN,'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC; </code></pre>
<blockquote>
<h3 id="정답-확인-my-sql">정답 확인 [MY SQL]</h3>
</blockquote>
<pre><code class="language-sql">SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
       IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;</code></pre>
<p><strong>NVL은 오라클에서만 사용하는 함수!
MY SQL에서는 NVL 대신 IFNULL 을 사용!
NVL 자리에 IFNULL 그대로 써줌.</strong></p>
<blockquote>
<h3 id="어려웠던-부분">어려웠던 부분</h3>
</blockquote>
<ul>
<li>경기도에 위치한~ <code>LIKE</code> <code>IN</code> 의 용법 차이</li>
</ul>
<p>나는 LIKE와 IN의 용법 차이를 정확하게 알고 있지 않았기 때문에 헷갈렸다.</p>
<p><code>LIKE</code> </p>
<ul>
<li>부분 문자열 검색 가능 
EX. '경기도%'</li>
</ul>
<p><code>IN</code></p>
<ul>
<li>정확히 일치하는 값들을 리스트에서 찾을때 사용
EX. 경기도 - 정확히 경기도만 포함된 주소를 찾게됨 
(경기도 안산시 - 검색 불가)</li>
</ul>
<blockquote>
<h3 id="null-관련-함수-정리-오라클-유선배-파랭이-p99">NULL 관련 함수 정리 [오라클] (유선배 파랭이 p99)</h3>
</blockquote>
<p>추가로 NULL 관련 함수 정리하고 간다.</p>
<ol>
<li><p><code>NVL(인수1,인수2)</code>
인수1 = NOT NULL -&gt; 인수1
인수1 = NULL -&gt; 인수2</p>
</li>
<li><p><code>NVL2(인수1, 인수2, 인수3)</code> - ONLY 오라클 / MY SQL 지원X
인수1 = NOT NULL -&gt; 인수2
인수1 = NULL -&gt; 인수3
EX. NVL2(REVIEW, '리뷰있음', '리뷰없음')</p>
</li>
<li><p><code>NULLIF(인수1, 인수2)'</code>
인수1 = 인수2 -&gt; NULL
인수1 =/= 인수2 -&gt; 인수1</p>
</li>
<li><p><code>COALESCE(인수1, 인수2, 인수3, ....)</code>
NULL이 아닌 최초의 인수를 반환
CASE1. 
인수1 = NOT NULL -&gt; 인수1
CASE2.
인수1 = NULL -&gt;
인수2 =/= NULL -&gt; 인수2
CASE3.
인수1 = NULL, 인수2 = NULL, -&gt; 인수3.....</p>
</li>
</ol>