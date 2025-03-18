<blockquote>
<h3 id="프로그래머스-sql-고득점-select">프로그래머스 SQL 고득점 SELECT</h3>
<p>Level 2. 3월에 태어난 여성 회원 목록 출력하기</p>
</blockquote>
<p>MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<ol>
<li><p>MY SQL</p>
<pre><code class="language-sql">SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
 DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE EXTRACT(MONTH FROM DATE_OF_BIRTH) = 03
 AND TLNO IS NOT NULL
 AND GENDER = 'W'
ORDER BY MEMBER_ID ASC;</code></pre>
</li>
<li><p>오라클</p>
<pre><code class="language-sql">SELECT MEMBER_ID, MEMBER_NAME, GENDER,
    TO_CHAR(DATE_OF_BIRTH,'YYYY-MM-DD')
FROM MEMBER_PROFILE
WHERE EXTRACT(MONTH FROM DATE_OF_BIRTH) = 03
 AND TLNO IS NOT NULL
 AND GENDER = 'W'
ORDER BY MEMBER_ID ASC;</code></pre>
</li>
</ol>
<p>*<em>오라클 - <code>TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD)</code>
MY SQL - <code>DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d')</code>
*</em></p>
<blockquote>
<h3 id="어려웠던-부분">어려웠던 부분</h3>
</blockquote>
<ul>
<li><p><code>DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d')</code> 
%Y-%M-%D 의 값 변화</p>
</li>
<li><p><code>%Y-%M-%D</code>
%Y - 2025
%y - 25
%M - March
%m - 03
%D - 10th
%d - 10</p>
</li>
</ul>