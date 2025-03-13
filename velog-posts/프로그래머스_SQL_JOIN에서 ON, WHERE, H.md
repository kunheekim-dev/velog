<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-is-null-문제">프로그래머스 SQL 고득점 KIT 내 IS NULL 문제</h3>
<p>Level 2. ROOT 아이템 구하기.</p>
</blockquote>
<p>ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.</p>
<blockquote>
<h3 id="my-sql">MY SQL</h3>
</blockquote>
<pre><code class="language-sql">SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO I
INNER JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID ASC;</code></pre>
<blockquote>
<h3 id="join에서-on-의-사용">JOIN에서 ON 의 사용</h3>
</blockquote>
<p>*<em><code>JOIN</code>에서 <code>ON</code>은 두 테이블간의 관계를 나타내야한다.
*</em>
다른 JOIN 조건들은 <code>WHERE</code>절에서 필터링해야함.</p>
<blockquote>
<h3 id="join에서-where과-having의-차이">JOIN에서 WHERE과 HAVING의 차이</h3>
</blockquote>
<ol>
<li><code>WHERE</code> </li>
</ol>
<ul>
<li>개별행 필터링. (개별 행에 대한 조건을 평가)</li>
<li><code>GROUP BY</code> 전에 실행.</li>
<li><code>GROUP BY</code> 없이 사용 가능.</li>
<li>서브쿼리 없이 <code>WHERE</code>절 집계함수 (<code>SUM</code> <code>AVG</code> <code>MAX</code> 등) 사용 못함 - 그룹 내 데이터를 하나의 결과로 축약하는 것이기 때문에! </li>
<li>JOIN이 없어도 <code>WHERE</code>절에서는 집계함수 사용 못함.</li>
</ul>
<blockquote>
<p>오류.</p>
</blockquote>
<pre><code class="language-sql">SELECT * 
FROM employees 
WHERE salary = MAX(salary);</code></pre>
<ol>
<li><code>서브쿼리</code> 사용하기.<pre><code class="language-sql">SELECT * 
FROM employees 
WHERE salary = (SELECT MAX(salary) FROM employees);</code></pre>
</li>
<li><code>HAVING</code>절 사용하기.<pre><code class="language-sql">SELECT department, MAX(salary) 
FROM employees 
GROUP BY department 
HAVING MAX(salary) &gt; 5000;</code></pre>
</li>
</ol>
<ul>
<li><code>WHERE</code> + 단순조건 [= &gt; &lt;] 가능</li>
<li><code>WHERE</code> + 단일행 서브쿼리 [집계함수 = &gt; &lt;] 가능 </li>
</ul>
<hr />
<ul>
<li><code>WHERE</code> + 다중행 서브쿼리 [집계함수 = &gt; &lt;] 오류 <pre><code class="language-sql">SELECT * FROM products WHERE price = (SELECT price FROM products WHERE category = 'Electronics');</code></pre>
오류 - <code>price = (SELECT ~)</code> 구문이 다중행 반환할 가능성이 있는데 <code>=</code>를 사용함.</li>
</ul>
<hr />
<ul>
<li><code>WHERE</code> + 다중행 서브쿼리 <code>IN</code> 사용시 [집계함수 = &gt; &lt;] 가능<pre><code class="language-sql">SELECT * FROM products WHERE price IN (SELECT price FROM products WHERE category = 'Electronics');</code></pre>
가능 - <code>IN</code> 연산자는 <code>=</code> 와 같은 단일행 연산자가 아니라 다중값을 비교 가능한 연산자라서 다중행 서브쿼리와 사용 가능.</li>
</ul>
<hr />
<ol start="2">
<li><code>HAVING</code></li>
</ol>
<ul>
<li>그룹 필터링.</li>
<li><code>GROUP BY</code> 이후 실행.</li>
<li><code>GROUP BY</code> 가 꼭 필요함.</li>
<li>집계함수 (<code>AVG</code> <code>SUM</code> <code>MAX</code> 등) 사용 가능.</li>
<li>단일행 연산자 (<code>=</code> <code>&lt;</code> <code>&gt;</code> 등) 사용 가능.</li>
</ul>
<hr />
<blockquote>
<p>단일행 필터링 - <code>WHERE</code>
그룹별 필터링 - <code>HAVING</code></p>
</blockquote>