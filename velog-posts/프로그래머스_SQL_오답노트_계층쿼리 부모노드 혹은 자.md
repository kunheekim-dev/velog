<blockquote>
<h3 id="프로그래머스-sql-고득점-kit-내-is-null-문제">프로그래머스 SQL 고득점 KIT 내 IS NULL 문제</h3>
<p>Level 3. 업그레이드 할 수 없는 아이템 구하기.</p>
</blockquote>
<p>더 이상 업그레이드할 수 없는 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬해 주세요.</p>
<blockquote>
<h3 id="문제-속-뜻-풀이">문제 속 뜻 풀이</h3>
</blockquote>
<p>부모아이템을 찾으라는 뜻이다. 
단순하게 생각하면 ITEM_C, ITEM_D, ITEM_E를 찾으면 되는데, 
그렇게 쿼리문을 만들어버리면 나중에 아이템을 추가했을때 쿼리문 전체를 수정해야하며 더 이상 쓸 수 없게 된다. <strong>(내가 이렇게 만들어버림...그럼 안돼...)</strong></p>
<p>따라서 쿼리 자체로 더 이상 업그레이드 할 수 없는 아이템을 찾아야한다.</p>
<ul>
<li>업그레이드 가능한 아이템 - <code>PARENT_ITEM_ID</code>에 등장하는 <code>ITEM_ID</code> = 0,1 (ITEM_A, ITEM_B)</li>
<li>더이상 업그레이드 할 수 없는 아이템 - <code>PARENT_ITEM_ID</code>에 없는 <code>ITEM_ID</code> 인 것 
= <code>ITEM_TREE.ITEM_ID</code>에는 있지만, <code>ITEM_TREE.PARENT_ITEM_ID</code>에 없는 값 
= 2,3,4, ...... (ITEM_C, ITEM_D, ITEM_E ....)</li>
</ul>
<blockquote>
<h3 id="my-sql">MY SQL</h3>
</blockquote>
<pre><code class="language-sql">SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I 
WHERE I.ITEM_ID NOT IN (SELECT PARENT_ITEM_ID
                       FROM ITEM_TREE
                       WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY I.ITEM_ID DESC;</code></pre>
<blockquote>
<h3 id="그럼-null-값은-어떻게-되나">그럼 NULL 값은 어떻게 되나?</h3>
</blockquote>
<pre><code class="language-sql">WHERE I.ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IS NOT NULL)</code></pre>
<p><code>PARENT_ITEM_ID</code> 값 중 NULL 아닌 값, 즉 0,1만 가져옴. (업그레이드 가능한 아이템)
거기서 <code>I.ITEM_ID</code> 에서 <code>NOT IN</code>을 사용했으니, 0,1 제외하고 2,3,4 만 선택함.</p>
<p><strong>NULL 값은...?</strong>
<code>PARNET_ITEM_ID</code>에 NULL값이 있으나, <code>WHERE PARENT_ITEM_ID IS NOT NULL</code>에서 NULL값을 제외시켰기 때문에, 아예 NULL값을 빼고 가져옴.
즉 NULL 은 <code>NOT IN</code> 대상이 아님. (<code>NOT IN</code> 사용때 <code>NULL</code>값이 있으면 비교가 불가능해짐)</p>
<hr />
<blockquote>
<p>유선배 파랭이 p278 계층쿼리 참고</p>
</blockquote>