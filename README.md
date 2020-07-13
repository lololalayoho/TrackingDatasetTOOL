# Tracking Object and Make Dataset(csv파일)

## 개발 환경
* Python 3.7.4
* Opencv 3.4.2
* keyboard 0.13.5

## 실행방법
<pre>
<code>
git clone https://github.com/lololalayoho/trackingDatasetTOOL.git
5번 줄 편집 : 경로 바꾸기
python tracking_KCF.py
</code>
</pre>

## 뽑히는 Feature
* 박스 중점 x좌표
* 박스 중점 y좌표
* 박스 중점 x좌표 변화량
* 박스 중점 y좌표 변화량

## 작동 방법
### 1. 키보드 i를 누른다 (Label 0)
* 선택할 Object에 사각형을 그린다.
<img src = "/image/1.jpg" width = "350" height = "200">

### 2. 키보드 u를 누른다 (Label 1)
* 선택할 Object에 사각형을 그린다.
<img src = "/image/2.jpg" width = "350" height = "200">

### 3. 키보드 o를 누른다.
* o를 누르기 전까지 Tracking 하면서 Feature를 저장한다.
* 더이상 데이터를 넣고 싶지 않을때 <사고가 발생 하는 순간>
<img src = "/image/3.jpg" width = "350" height = "200">

### 4. 키보드 p를 누른다.
* label1.csv , label2.csv 파일에 각각 Label 0, Label 1의 데이터가 떨어진다.

<img src = "/image/label0.jpg" width = "350" height = "200">     <img src = "/image/label1.jpg" width = "350" height = "200">

### 5. 키보드 a 또는 s를 누른다.
* 키보드 a : 비디오 다시 재생
* 키보드 s : 다음 비디오로 진행
