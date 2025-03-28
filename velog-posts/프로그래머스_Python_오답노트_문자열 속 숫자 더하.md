<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트-입문">1. 프로그래머스 python 코딩테스트 입문</h3>
<p>Level 0. 숨어있는 숫자의 덧셈(2)</p>
</blockquote>
<p>문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.</p>
<blockquote>
<h3 id="정답-확인">정답 확인</h3>
</blockquote>
<p>** 1. <code>i.isdigit()</code>을 사용하여 풀어쓰기 ** </p>
<pre><code class="language-python">def solution(my_string):
    num = ''
    nums = []
    for i in my_string:
        if i.isdigit():
            num += i
        else :
            if num:
                nums.append(int(num))
                num = ''
    if num:
        nums.append(int(num))
    return sum(nums)</code></pre>
<blockquote>
<p><strong><code>+=연산자</code> 활용</strong></p>
</blockquote>
<ul>
<li><p><code>str</code>+=<code>str</code> 문자 붙이기 '1' + '23' = '123'</p>
</li>
<li><p><code>list</code> += <code>list</code> 리스트 확장 [1,2] += [3,4] = [1,2,3,4]</p>
</li>
<li><p>`list += [int(i)]는 타입이 달라서 안됨.</p>
</li>
<li><p>숫자 += 숫자  a = 5, a += 3 , 5+3 = 8</p>
</li>
<li><p><strong><code>if - else</code> 구문에서 <code>else</code> 굳이 안써도 됨. 
<code>else</code>가 없으면 그냥 아무일 없이 넘어감.</strong></p>
</li>
<li><p><code>map(int, nums)</code> : 각 문자열을 int로 바꿔줌.
['1', '34'] -&gt; [1, 34]</p>
</li>
<li><p><code>sum(map(int,리스트))</code> : 나중에 한번에 숫자로 바꾸고 싶다.</p>
</li>
<li><p><code>append(int(num))</code> : 한개씩 바로 바로 바꾸고 싶다.</p>
</li>
<li><p><code>num += i</code> 로 숫자를 하나씩 모아, [123] 이런식으로 모아서 뭉쳐짐.</p>
</li>
<li><p>(알파벳이 나오지 않아) 뭉쳐놓은 숫자를 nums = [] 리스트에 하나씩 넣어줌.</p>
</li>
<li><p>넣어줄때 매번 <code>int()</code>하나씩 해서 넣어주어야함.</p>
</li>
<li><p><strong><code>int()</code>는 리스트 전체에 적용을 못하기 때문.</strong>
(전체 적용을 위해서는 <code>map함수</code>를 써야함.)</p>
</li>
</ul>
<blockquote>
<p><strong><code>.append()</code> vs <code>add()</code> 차이!</strong>
<img alt="" src="https://velog.velcdn.com/images/kunhee/post/2dfa733e-2202-43f3-8477-748d3c758413/image.png" /></p>
</blockquote>
<hr />
<p>*<em>2. <code>map 함수</code> 사용하기 *</em></p>
<pre><code class="language-python">def solution(my_string):
    num = ''
    nums = []
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            if num:
                nums.append(num)  # ❗여기선 문자열로 저장!
                num = ''
    if num:
        nums.append(num)
    return sum(map(int, nums)) </code></pre>
<blockquote>
<p><strong>map함수</strong></p>
</blockquote>
<ul>
<li><code>map(int, nums)</code> : 각 문자열을 int로 바꿔줌.
['1', '34'] -&gt; [1, 34]</li>
<li><code>sum(map(int,리스트))</code> : 나중에 한번에 숫자로 바꾸고 싶다.</li>
<li><code>append(int(num))</code> : 한개씩 바로 바로 바꾸고 싶다.</li>
</ul>
<hr />
<p>*<em>3. 발상의 전환!!! *</em></p>
<pre><code class="language-python">def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())</code></pre>
<blockquote>
<p><strong><code>''.join()</code>함수와 <code>.split()</code>함수 사용</strong></p>
</blockquote>
<ul>
<li><code>''.join()</code> 숫자는 join함수를 쓸 수 없음. '문자'만 사용 가능!
(join할때, int(i)를 사용하지 못한 이유.)</li>
<li><code>문자열.split()</code> : 문자열을 특정 문자로 잘라서, 결과로 리스트를 만들어냄. 따라서 <code>리스트.split()</code>라는건 없음.</li>
<li><code>.split()</code>인 경우 : ()공백이라 공백 기준으로 자르는것.</li>
</ul>
<ol>
<li>[ab1CD22E4g2] 인 경우, 숫자는 리스트에 담고, 영어문자들을 ''공백으로 담아서 새로운 []리스트를 만들기로함.</li>
<li>[    3   4  2345 9]와 같은 리스트를 만들었으면, 공백을 기준으로 숫자를 나눔. [3,4,2345,9] 같이 만든 후</li>
<li>자연수로 변경해서 모두 더해줌.</li>
</ol>