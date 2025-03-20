<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-summaxmin">프로그래머스 SQL 고득점 KIT 내 SUM,MAX,MIN</h3>
<p>Level 1. 최댓값 구하기</p>
</blockquote>
<p>가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<pre><code class="language-sql">SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS</code></pre>
<blockquote>
<h3 id="정답-해설">정답 해설</h3>
</blockquote>
<ol>
<li><p>복잡하게 생각할 거 없이 최근값은 바로 <code>MAX</code>구하기.</p>
</li>
<li><p><strong>[나의 오답] 랭크로 줄세워서 1개 선택하려고 했으나 - 서브쿼리 사용 비효율적 복잡.</strong></p>
</li>
</ol>
<blockquote>
<h3 id="서브쿼리와-별칭-as-사용">서브쿼리와 별칭 AS 사용</h3>
</blockquote>
<ul>
<li><code>FROM</code>은 <code>AS</code> 반드시 필요함.</li>
<li><code>SELECT</code> <code>WHER</code>은 없어도 됨.</li>
</ul>
<ol>
<li><code>SELECT</code> </li>
</ol>
<p><strong>EX</strong></p>
<pre><code class="language-sql">`SELECT (SELECT MAX(DATETIME) FROM ANIMAL_INS) AS 시간`</code></pre>
<ul>
<li><code>SELECT</code>절 <code>서브쿼리</code>는 단일값 반환 (스칼라 서브쿼리)임.</li>
<li><code>AS</code>별칭 사용 필수 아님.</li>
</ul>
<ol start="2">
<li><code>FROM</code></li>
</ol>
<p><strong>EX</strong></p>
<pre><code class="language-sql">SELECT DATETIME
FROM (SELECT DATETIME, RANK() OVER (ORDER BY DATETIME DESC) AS 시간
    FROM ANIMAL_INS) A
WHERE RANKING = 1;</code></pre>
<ul>
<li><code>FROM(서브쿼리)</code> 를 테이블처럼 인식해야해서 <code>AS</code>별칭 필요.</li>
<li><code>AS</code> <strong>별칭 없으면 인식 불가.</strong></li>
</ul>
<ol start="3">
<li><code>WHERE</code></li>
</ol>
<p><strong>EX</strong></p>
<pre><code class="language-sql">SELECT PRODUCT_ID, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);</code></pre>
<ul>
<li><code>WHERE</code>절 서브쿼리는 하나의 값을 반환하는 조건식, </li>
<li><code>AS</code>없어도 가능.</li>
<li><code>서브쿼리</code> 결과가 다중값 반환이면 <code>=</code>이 아닌 <code>IN</code> 사용.</li>
</ul>