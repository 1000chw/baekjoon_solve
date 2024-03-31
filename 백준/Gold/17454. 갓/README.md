# [Gold II] 갓 - 17454 

[문제 링크](https://www.acmicpc.net/problem/17454) 

### 성능 요약

메모리: 31120 KB, 시간: 308 ms

### 분류

수학

### 제출 일자

2024년 3월 31일 20:46:00

### 문제 설명

<p>동현이와 현수와 승원이는 오랫동안 문제 풀이 갓(god)의 칭호를 달기 위해 실력을 쌓아 왔다. 어느덧 세 명 모두 갓이라고 불리기에 손색없는 실력이 되었으나, 하늘 아래 갓이 세 명일 수는 없는 법. 단 한 명의 <span style="font-style: italic;">진정한 갓</span>을 어떻게 가릴지 논의하던 세 사람은 결국 이름에 <span style="font-style: italic;">갓</span>을 붙였을 때 가장 잘 어울리는 사람을 진정한 갓으로 삼기로 결정했다.</p>

<p>그러나 어울린다는 것은 주관적이라서 여러 사람의 의견이 필요하다. 따라서 세 사람은 각자 자신의 친구들을 모아 투표를 진행하기로 했다. 이때 자기 자신이 후보에 들어 있으면 불공정한 투표가 될 수 있으므로, 각자 자기 자신은 후보에서 제외하고 투표를 진행했다. 투표가 끝나고 나면 각 사람은 다른 두 사람이 진행한 투표에서 자신이 받은 표를 가져가고, 이렇게 가져간 표가 가장 많은 사람이 진정한 갓이 된다. 만약 가장 많은 표를 받은 사람이 여러 명이라면 투표는 무효가 된다. 세 사람 모두 친구가 많기 때문에 각 투표에는 한 명 이상이 참가했음이 보장된다.</p>

<p style="margin-top: 15px;"><img alt="alt text" src="https://upload.acmicpc.net/6bd3f0f1-4b42-4e31-8239-d426071a7a51/-/preview/" style="display: block; margin-left: auto; margin-right: auto; width: 100%; max-width: 500px;"></p>

<p style="margin-bottom: 15px; text-align: center;">투표의 예시</p>

<p>오늘은 투표 결과가 공개되는 날이다. 그런데 세 사람은 서로를 견제하기 위해 전체 투표 결과를 내놓지 않고, 각자가 진행한 투표에서 두 후보가 받은 표의 비율만을 공개했다! 공개된 결과만 볼 때 동현이가 진정한 갓이 될 수 있을지 판단해 보자.</p>

### 입력 

 <p>첫 줄에 투표를 진행한 횟수를 의미하는 정수 <span style="font-style: italic;">T</span>(1 ≤ <span style="font-style: italic;">T</span> ≤ 100,000)가 주어진다.</p>

<p>다음 <span style="font-style: italic;">T</span>개의 줄에 걸쳐 각 줄에 투표의 결과를 의미하는 6개의 정수 <span style="font-style: italic;">DH</span>, <span style="font-style: italic;">DS</span>, <span style="font-style: italic;">HD</span>, <span style="font-style: italic;">HS</span>, <span style="font-style: italic;">SD</span>, <span style="font-style: italic;">SH</span>(1 ≤ <span style="font-style: italic;">DH</span>, <span style="font-style: italic;">DS</span>, <span style="font-style: italic;">HD</span>, <span style="font-style: italic;">HS</span>, <span style="font-style: italic;">SD</span>, <span style="font-style: italic;">SH</span> ≤ 1,000)가 공백을 사이에 두고 주어진다.</p>

<ul>
	<li><span style="font-style: italic;">DH</span>, <span style="font-style: italic;">DS</span>는 동현이가 진행한 투표에서 <span style="font-style: italic;">갓현수</span>와 <span style="font-style: italic;">갓승원</span>이 받은 표의 비율을 의미한다. 두 수는 서로소임이 보장된다.</li>
	<li><span style="font-style: italic;">HD</span>, <span style="font-style: italic;">HS</span>는 현수가 진행한 투표에서 <span style="font-style: italic;">갓동현</span>과 <span style="font-style: italic;">갓승원</span>이 받은 표의 비율을 의미한다. 두 수는 서로소임이 보장된다.</li>
	<li><span style="font-style: italic;">SD</span>, <span style="font-style: italic;">SH</span>는 승원이가 진행한 투표에서 <span style="font-style: italic;">갓동현</span>과 <span style="font-style: italic;">갓현수</span>가 받은 표의 비율을 의미한다. 두 수는 서로소임이 보장된다.</li>
</ul>

### 출력 

 <p><span style="font-style: italic;">T</span>개의 줄에 걸쳐 각 줄에 각 투표에서 동현이가 진정한 갓이 될 수 있다면 <code>GOD</code>을, 불가능하다면 <code>KDH</code>를 출력한다.</p>

