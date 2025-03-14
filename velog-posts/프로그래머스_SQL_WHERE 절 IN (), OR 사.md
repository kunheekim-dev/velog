<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-sum-max-min">프로그래머스 SQL 고득점 KIT, SUM, MAX, MIN</h3>
<p>Level 1. 흉부외과 또는 일반외과 의사 목록 출력하기</p>
</blockquote>
<p>DOCTOR 테이블에서 진료과가 흉부외과(CS)이거나 일반외과(GS)인 의사의 이름, 의사ID, 진료과, 고용일자를 조회하는 SQL문을 작성해주세요. 이때 결과는 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 이름을 기준으로 오름차순 정렬해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<ol>
<li>MY SQL<pre><code class="language-sql">SELECT DR_NAME, DR_ID, MCDP_CD, 
 DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;</code></pre>
</li>
</ol>
<p>*<em><code>WHERE MCDP_CD IN ('CS','GS')</code>
= <code>WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'</code>
*</em></p>
<blockquote>
<h3 id="어려웠던-부분">어려웠던 부분</h3>
<p><code>WHERE 컬럼명 IN (   )</code></p>
</blockquote>
<ul>
<li><p><code>IN</code> 다음 <code>( , )</code>괄호를 빼먹음.</p>
</li>
<li><p><code>(   )</code> 괄호 안에는 <code>IN</code> <code>OR</code> 같은 연산자는 안씀.</p>
</li>
<li><p>굳이 굳이 <code>WHERE</code>절에 서브쿼리를 쓴다면, <code>WHERE 컬럼 연산자(IN, = 등등) 서브쿼리</code> 구조여야함.</p>
<pre><code class="language-sql">SELECT DR_NAME, DR_ID, MCDP_CD, 
  DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN (
    SELECT MCDP_CD 
    FROM DOCTOR
    WHERE MCDP_CD IN ('CS', 'GS')
    )
ORDER BY HIRE_YMD DESC, DR_NAME ASC;</code></pre>
</li>
<li><p><em>이 경우엔 서브쿼리를 쓸 필요가 전혀 없다! 비효율적임.
<code>WHERE</code> 절에 올 경우 어떻게 쓰나 보려고 작성해본것임.*</em></p>
</li>
</ul>