from flask import Flask
import datetime

app = Flask(__name__)

def get_weather_data(province):
    sample_data = {
        "แหลมฉบัง": {
            "wind_speed": 35,
            "rainfall": 12.5,
            "pressure": 1002,
            "storm": True,
            "wave_height": 2.5
        },
        "ศรีราชา": {
            "wind_speed": 28,
            "rainfall": 5.0,
            "pressure": 1005,
            "storm": False,
            "wave_height": 1.8
        }
    }
    return sample_data.get(province, {})

def generate_alert(province):
    data = get_weather_data(province)
    if not data:
        return f"ไม่พบข้อมูลสภาพอากาศสำหรับจังหวัด {province}"

    alerts = []
    if data["wind_speed"] > 30:
        alerts.append(f"ลมแรง ({data['wind_speed']} km/h)")
    if data["rainfall"] > 10:
        alerts.append(f"ฝนตกหนัก ({data['rainfall']} mm)")
    if data["storm"]:
        alerts.append("มีพายุ")
    if data["wave_height"] > 2:
        alerts.append(f"คลื่นสูง ({data['wave_height']} เมตร)")
    if data["pressure"] < 1003:
        alerts.append(f"ความกดอากาศต่ำ ({data['pressure']} hPa)")

    if alerts:
        alert_message = f"แจ้งเตือนสภาพอากาศ {province} ณ {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}
- " + "
- ".join(alerts)
    else:
        alert_message = f"{province}: สภาพอากาศปกติ ไม่มีเหตุการณ์รุนแรง"

    return alert_message

@app.route('/')
def index():
    return "ระบบแจ้งเตือนสภาพอากาศพร้อมทำงาน"

@app.route('/alert/<province>')
def alert(province):
    return generate_alert(province)
