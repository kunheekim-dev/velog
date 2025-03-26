<blockquote>
<h3 id="1-프로그래머스-python-코딩테스트">1. 프로그래머스 python 코딩테스트</h3>
<p>Level 0. 가위 바위 보</p>
</blockquote>
<p>가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.</p>
<blockquote>
<h3 id="정답-확인-replace-안씀">정답 확인 (replace 안씀)</h3>
</blockquote>
<blockquote>
<ol>
<li><code>for 반복문 + if - elif</code> </li>
</ol>
</blockquote>
<pre><code class="language-python">def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
    return ''.join([answer])</code></pre>
<ul>
<li><code>answer = ''</code>이 핵심. 변수는 반드시 사용 전에, 정의(초기화)를 해야함. 식 중간에 <code>answer</code>가 나올예정이니, 꼭 미리 정의해야함.</li>
<li><code>[]</code>는 사용 안해도 됨. 어차피 문자열 하나만 return 될거니까.</li>
</ul>
<blockquote>
<p>2.<code>딕셔너리 사용</code> </p>
</blockquote>
<pre><code class="language-python">def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)</code></pre>
<ul>
<li>가위 바위 보 규칙을 딕셔너리를 사용해 저장한것.</li>
<li>가장 잘 푼 정답임.</li>
</ul>