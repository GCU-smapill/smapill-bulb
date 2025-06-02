from flask import Flask, request, jsonify
from pywizlight import wizlight, PilotBuilder
import asyncio

app = Flask(__name__)

# 전구 IP 주소
BULB_IP = "192.168.1.100"

# asyncio 이벤트 루프 실행 헬퍼
def run_async(coro):
    return asyncio.get_event_loop().run_until_complete(coro)

@app.route('/on', methods=['POST'])
def turn_on():
    brightness = request.json.get('brightness', 255)  # 0~255, 기본 255
    colortemp = request.json.get('colortemp', 4000)  # 2000~6500, 기본 4000
    rgb = request.json.get('rgb', None)               # [r, g, b] 리스트, 옵션

    bulb = wizlight(BULB_IP)

    if rgb:
        pilot = PilotBuilder(rgb=tuple(rgb), brightness=brightness)
    else:
        pilot = PilotBuilder(brightness=brightness, colortemp=colortemp)

    run_async(bulb.turn_on(pilot))

    return jsonify({"status": "on", "brightness": brightness, "colortemp": colortemp, "rgb": rgb})

@app.route('/off', methods=['POST'])
def turn_off():
    bulb = wizlight(BULB_IP)
    run_async(bulb.turn_off())
    return jsonify({"status": "off"})

@app.route('/status', methods=['GET'])
def status():
    # pywizlight는 상태 조회 기능 미지원 - 추후 직접 구현 가능
    return jsonify({"status": "status read not implemented"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
