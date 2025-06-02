# smapill-bulb

### 스마트 전구 색상 변경 API
WiZ 스마트 전구를 제어하는 Flask API 서버입니다. \n
복약 확인 완료 시 전구의 색상을 변경하여 시각적 알림을 제공합니다.


### 설치 및 설정
#### 필요한 패키지 설치
# bash pip install flask pywizlight

전구 IP 주소 설정
코드의 BULB_IP 변수를 실제 WiZ 전구의 IP 주소로 변경하세요:

python
BULB_IP = "192.168.1.100"  # 실제 전구 IP로 변경
API 엔드포인트
POST /on
전구를 켜고 설정을 적용합니다.

요청 본문 (JSON):

json
{
    "brightness": 255,    // 밝기 (0-255, 기본값: 255)
    "colortemp": 4000,    // 색온도 (2000-6500, 기본값: 4000)
    "rgb": [255, 0, 0]    // RGB 색상 [R, G, B] (선택사항)
}
응답 예시:

json
{
    "status": "on",
    "brightness": 255,
    "colortemp": 4000,
    "rgb": [255, 0, 0]
}



사용 예시
복약 확인 완료 시 녹색으로 변경
bash
curl -X POST http://localhost:5000/on \
  -H "Content-Type: application/json" \
  -d '{"rgb": [0, 255, 0], "brightness": 200}'
  
복약 시간 알림 시 주황색으로 변경
bash
curl -X POST http://localhost:5000/on \
  -H "Content-Type: application/json" \
  -d '{"rgb": [255, 165, 0], "brightness": 255}'


실행 방법
bash
python app.py
서버는 http://0.0.0.0:5000에서 실행됩니다.

시스템 통합
이 API는 복약 관리 시스템과 연동되어 다음과 같은 시나리오에서 사용됩니다:

처방전 인식: OCR로 처방전을 인식하여 복약 정보를 등록

음성 확인: AI 스피커를 통해 복약 여부를 음성으로 확인

시각적 피드백: 복약 확인 완료 시 스마트 전구 색상 변경으로 시각적 알림 제공

참고 사항
네트워크에서 WiZ 전구를 찾으려면 전구와 같은 Wi-Fi 네트워크에 연결되어 있어야 합니다

전구 IP 주소는 라우터 관리 페이지나 WiZ 앱에서 확인할 수 있습니다

run_async 함수는 비동기 pywizlight 라이브러리를 동기 Flask 환경에서 사용하기 위한 헬퍼 함수입니다