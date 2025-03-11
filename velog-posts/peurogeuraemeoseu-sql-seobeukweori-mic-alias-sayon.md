<p><strong>이 문제는 서브쿼리를 작성할 필요가 전혀 없는 문제이다.</strong> 
그런데 서브쿼리 사용시 오라클과 MY SQL이 다르길래, 기록 삼아 포스팅한다.</p>
<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-is-null-문제">프로그래머스 SQL 고득점 KIT 내 IS NULL 문제</h3>
<p>Level 1. 나이 정보가 없는 회원 수 구하기.</p>
</blockquote>
<p>USER_INFO 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 USERS로 지정해주세요.</p>
<blockquote>
<h3 id="모두-사용-가능-정답-확인">[모두 사용 가능] 정답 확인</h3>
</blockquote>
<pre><code class="language-sql">SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;</code></pre>
<blockquote>
<p><strong>간단한 코드 작성이 정답이다. 그런데 서브쿼리를 쓴 사람도 있어서 이게 되나 싶어 서브쿼리 작성 연습해볼 겸 작성해봤는데, 오라클과 MY SQL 정답이 달라서 놀랬다.</strong></p>
</blockquote>
<hr />
<blockquote>
<h3 id="오라클-정답-확인">[오라클] 정답 확인</h3>
</blockquote>
<pre><code class="language-sql">SELECT COUNT(USER_ID) AS USERS
FROM ( SELECT USER_ID
       FROM USER_INFO
       WHERE AGE IS NULL);</code></pre>
<p><strong>서브쿼리 작성시 AS를 붙이지 않음. 붙이면 오류남!</strong></p>
<blockquote>
<h3 id="my-sql-정답-확인">[MY SQL] 정답 확인</h3>
</blockquote>
<pre><code class="language-sql">SELECT COUNT(USER_ID) AS USERS
FROM ( SELECT USER_ID
       FROM USER_INFO
       WHERE AGE IS NULL) AS TEMP_TABLE;</code></pre>
<p><strong>서브쿼리 사용 시 () AS 000 별칭 작성해줘야함.
AS를 쓰지 않으면 오류남!</strong></p>
<blockquote>
<h3 id="서브쿼리">서브쿼리</h3>
</blockquote>
<p>이런 문제에서는 굳이 서브쿼리를 사용할 필요가 없다. 불필요하게 문장만 길고 복잡해지기 때문.</p>
<p><strong>서브쿼리</strong></p>
<ul>
<li>여러개의 조건을 추가적으로 적용해야할 때</li>
<li>조인을 사용해야할 때</li>
</ul>
<p><strong>+스칼라 서브쿼리</strong>
컬럼 대신 사용되므로 반드시 하나의 값만 반환.</p>
<p><strong>+인라인뷰</strong>
FROM절에 오는 서브쿼리.
FROM절 등 테이블명이 올 수 있는 위치에 사용 가능.</p>