<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-sum-max-min">프로그래머스 SQL 고득점 KIT, SUM, MAX, MIN</h3>
<p>Level 2. 가격이 제일 비싼 식품의 정보 출력하기</p>
</blockquote>
<p>FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<pre><code class="language-sql">SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)</code></pre>
<blockquote>
<h3 id="어려웠던-부분">어려웠던 부분</h3>
</blockquote>
<ul>
<li><code>WHERE</code>절에서 <code>집계함수</code> <code>서브쿼리</code> 의 사용 주의!</li>
</ul>
<ol>
<li><code>SELECT</code>절에서 <code>집계함수</code> 사용 <pre><code class="language-sql">SELECT PRODUCT_ID, MAX(PRICE)
FROM FOOD_PRODUCT;</code></pre>
</li>
</ol>
<ul>
<li>틀린 이유
<code>MAX(PRICE)</code> 
: 집계함수
: 단일값을 반환하지만, <strong>테이블 전체에서 계산됨</strong></li>
<li><em>PRODUCT_ID 와 같은것들은 개별 행 데이터*</em>
개별행 데이터와 MAX(PRICE)
SQL이 어떤 <code>PRODUCT_ID</code> (EX. A,B,C,D,..) 와 <code>MAX(PRICE)</code>를 비교해야할지 모름.</li>
</ul>
<ol start="2">
<li><code>WHERE</code>절에서 <code>집계함수</code> 사용<pre><code class="language-sql">SELECT PRODUCT_ID, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = MAX(PRICE);</code></pre>
</li>
</ol>
<ul>
<li>틀린 이유
<code>WHERE</code>절에서는 각 행단위 조건 비교해야함.
<code>PRICE</code> (개별행)과 <code>MAX(PRICE)</code> (테이블 전체 값)을 비교할 수 없음.</li>
</ul>
<blockquote>
<p><strong>무엇보다 <code>WHERE</code>절에서 <code>서브쿼리</code>없이 <code>집계함수</code> 사용 불가!!</strong></p>
</blockquote>
<blockquote>
<h3 id="그럼-정답은-왜-정답인가">그럼 정답은 왜 정답인가</h3>
</blockquote>
<pre><code class="language-sql">SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);</code></pre>
<ol>
<li><code>SELECT MAX(PRICE) FROM FOOD_PRODUCT</code> 최대 가격 단일값 반환 EX. 1,000원.</li>
<li><code>WHERE PRICE = 1000</code> 각 행의 <code>PRICE</code>와 비교 가능.</li>
<li><code>WHERE</code> 개별행과 단일값을 비교 가능! 오류 없음.</li>
</ol>