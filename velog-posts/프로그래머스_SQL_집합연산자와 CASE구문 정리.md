<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-is-null-문제">프로그래머스 SQL 고득점 KIT 내 IS NULL 문제</h3>
<p>Level 1. 잡은 물고기의 평균 길이 구하기.</p>
</blockquote>
<p>잡은 물고기의 평균 길이를 출력하는 SQL문을 작성해주세요.</p>
<p>평균 길이를 나타내는 컬럼 명은 AVERAGE_LENGTH로 해주세요.
평균 길이는 소수점 3째자리에서 반올림하며, 10cm 이하의 물고기들은 10cm 로 취급하여 평균 길이를 구해주세요.</p>
<blockquote>
<h3 id="사용할-함수-정하기">사용할 함수 정하기</h3>
</blockquote>
<ul>
<li>MY SQL이 주력이라면 <code>IF</code>와 <code>IFNULL</code>을 사용한다면 좀 더 간단하게 할 수 있을 것이다.</li>
<li>나는 오라클밖에 배운적이 없어서 MY SQL과 오라클 공통으로 사용 가능한 <code>CASE</code> 구문을 사용하겠다.</li>
</ul>
<blockquote>
<h3 id="my-sql--오라클---공통구문-case-사용">MY SQL &amp; 오라클 - 공통구문 CASE 사용</h3>
</blockquote>
<pre><code class="language-sql">SELECT ROUND(AVG
             (CASE
             WHEN LENGTH IS NULL 
             THEN 10 
             ELSE ROUND(LENGTH,2)
             END),2)
       AS AVERAGE_LENGTH
FROM FISH_INFO ;</code></pre>
<blockquote>
<h3 id="case-구문-정리-case-다음-무엇이-오는가">CASE 구문 정리 (CASE 다음 무엇이 오는가)</h3>
</blockquote>
<ul>
<li><code>CASE WHEN ---</code> </li>
<li><code>CASE 컬럼명 WHEN 값 THEN ---</code></li>
</ul>
<blockquote>
<p><strong>단순 CASE (CASE WHEN - 다양한 조건 가능)</strong></p>
</blockquote>
<pre><code class="language-sql">SELECT ITEM_NAME,
       CASE 
           WHEN PRICE &gt;= 10000 THEN 'Expensive'
           WHEN PRICE BETWEEN 5000 AND 9999 THEN 'Medium'
           ELSE 'Cheap'
       END AS PRICE_CATEGORY
FROM ITEM_INFO;</code></pre>
<ul>
<li>여러 조건을 비교할때 사용.</li>
<li>가장 유연하게 사용할 수 있음!</li>
</ul>
<blockquote>
<p><strong>CASE 컬럼명 WHEN 값 THEN - 특정값 비교</strong></p>
</blockquote>
<pre><code class="language-sql">SELECT ITEM_NAME,
       CASE PRICE
           WHEN 10000 THEN 'Expensive'
           WHEN 5000 THEN 'Medium'
           ELSE 'Cheap'
       END AS PRICE_CATEGORY
FROM ITEM_INFO;</code></pre>
<ul>
<li>특정 값과 일치하는지 체크!</li>
<li><code>BETWEEN</code> <code>&gt;</code> 비교연산자 불가.
(<code>WHEN PRICE &gt;= 1000</code> 같은 비교 불가능!)</li>
</ul>