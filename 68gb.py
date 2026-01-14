import requests
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

FIREBASE_URL = "https://gbmd5-4a69a-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions.json"

# ========== 100 THUẬT TOÁN THẬT MỚI – KHÔNG DÙNG PHIÊN TRƯỚC ==========
def predict_00(h):
    return 'T' if np.mean(h) > 10.9 else 'X'

def predict_01(h):
    return 'T' if np.percentile(h, 60) > 11.2 else 'X'

def predict_02(h):
    return 'T' if np.std(h) < 3.2 else 'X'

def predict_03(h):
    return 'T' if (np.max(h) - np.min(h)) > 9 else 'X'

def predict_04(h):
    return 'T' if np.median(h) > 10.8 else 'X'

def predict_05(h):
    return 'T' if np.percentile(h, 70) > 11.5 else 'X'

def predict_06(h):
    return 'T' if np.percentile(h, 30) > 9.5 else 'X'

def predict_07(h):
    return 'T' if np.mean([x for x in h if x >= 11]) > 12.5 else 'X'

def predict_08(h):
    return 'T' if np.mean([x for x in h if x <= 10]) < 8.5 else 'X'

def predict_09(h):
    return 'T' if len([x for x in h if x >= 11]) / len(h) > 0.52 else 'X'

def predict_10(h):
    return 'T' if len([x for x in h if x <= 10]) / len(h) < 0.48 else 'X'

def predict_11(h):
    return 'T' if np.percentile(h, 80) > 12.5 else 'X'

def predict_12(h):
    return 'T' if np.percentile(h, 20) > 8.5 else 'X'

def predict_13(h):
    return 'T' if np.var([x for x in h if x >= 11]) < 2.5 else 'X'

def predict_14(h):
    return 'T' if np.var([x for x in h if x <= 10]) < 2.2 else 'X'

def predict_15(h):
    return 'T' if np.max(h) > 15 else 'X'

def predict_16(h):
    return 'T' if np.min(h) < 6 else 'X'

def predict_17(h):
    return 'T' if np.percentile(h, 90) > 13.5 else 'X'

def predict_18(h):
    return 'T' if np.percentile(h, 10) > 7.5 else 'X'

def predict_19(h):
    return 'T' if np.mean(h[-50:]) > np.mean(h[:-50]) else 'X'

def predict_20(h):
    return 'T' if np.mean(h[-30:]) > 11.0 else 'X'

def predict_21(h):
    return 'T' if np.mean(h[-20:]) > 11.1 else 'X'

def predict_22(h):
    return 'T' if np.mean(h[-10:]) > 11.2 else 'X'

def predict_23(h):
    return 'T' if np.percentile(h[-30:], 75) > 11.5 else 'X'

def predict_24(h):
    return 'T' if np.percentile(h[-20:], 80) > 12.0 else 'X'

def predict_25(h):
    return 'T' if np.percentile(h[-10:], 85) > 12.5 else 'X'

def predict_26(h):
    return 'T' if np.var(h[-30:]) < 3.0 else 'X'

def predict_27(h):
    return 'T' if np.var(h[-20:]) < 2.8 else 'X'

def predict_28(h):
    return 'T' if np.var(h[-10:]) < 2.5 else 'X'

def predict_29(h):
    return 'T' if len([x for x in h[-30:] if x >= 11]) / 30 > 0.55 else 'X'

def predict_30(h):
    return 'T' if len([x for x in h[-20:] if x >= 11]) / 20 > 0.56 else 'X'

def predict_31(h):
    return 'T' if len([x for x in h[-10:] if x >= 11]) / 10 > 0.57 else 'X'

def predict_32(h):
    return 'T' if np.max(h[-30:]) > 15 else 'X'

def predict_33(h):
    return 'T' if np.max(h[-20:]) > 14 else 'X'

def predict_34(h):
    return 'T' if np.max(h[-10:]) > 13 else 'X'

def predict_35(h):
    return 'T' if np.min(h[-30:]) < 6 else 'X'

def predict_36(h):
    return 'T' if np.min(h[-20:]) < 7 else 'X'

def predict_37(h):
    return 'T' if np.min(h[-10:]) < 8 else 'X'

def predict_38(h):
    return 'T' if np.percentile(h[-30:], 90) > 13 else 'X'

def predict_39(h):
    return 'T' if np.percentile(h[-20:], 90) > 12.5 else 'X'

def predict_40(h):
    return 'T' if np.percentile(h[-10:], 90) > 12 else 'X'

def predict_41(h):
    return 'T' if np.percentile(h[-30:], 10) < 8 else 'X'

def predict_42(h):
    return 'T' if np.percentile(h[-20:], 10) < 8.5 else 'X'

def predict_43(h):
    return 'T' if np.percentile(h[-10:], 10) < 9 else 'X'

def predict_44(h):
    return 'T' if np.mean([x for x in h[-30:] if x >= 11]) > 12.3 else 'X'

def predict_45(h):
    return 'T' if np.mean([x for x in h[-20:] if x >= 11]) > 12.2 else 'X'

def predict_46(h):
    return 'T' if np.mean([x for x in h[-10:] if x >= 11]) > 12.1 else 'X'

def predict_47(h):
    return 'T' if np.mean([x for x in h[-30:] if x <= 10]) < 8.7 else 'X'

def predict_48(h):
    return 'T' if np.mean([x for x in h[-20:] if x <= 10]) < 8.8 else 'X'

def predict_49(h):
    return 'T' if np.mean([x for x in h[-10:] if x <= 10]) < 8.9 else 'X'

def predict_50(h):
    return 'T' if len([x for x in h if x in {11, 12, 13}]) / len(h) > 0.35 else 'X'

def predict_51(h):
    return 'T' if len([x for x in h if x in {8, 9, 10}]) / len(h) < 0.32 else 'X'

def predict_52(h):
    return 'T' if len([x for x in h if x >= 14]) / len(h) > 0.12 else 'X'

def predict_53(h):
    return 'T' if len([x for x in h if x <= 7]) / len(h) < 0.1 else 'X'

def predict_54(h):
    return 'T' if len([x for x in h if x == 11]) / len(h) > 0.12 else 'X'

def predict_55(h):
    return 'T' if len([x for x in h if x == 10]) / len(h) < 0.12 else 'X'

def predict_56(h):
    return 'T' if len([x for x in h if x == 12]) / len(h) > 0.11 else 'X'

def predict_57(h):
    return 'T' if len([x for x in h if x == 9]) / len(h) < 0.11 else 'X'

def predict_58(h):
    return 'T' if len([x for x in h if x == 13]) / len(h) > 0.1 else 'X'

def predict_59(h):
    return 'T' if len([x for x in h if x == 8]) / len(h) < 0.1 else 'X'

def predict_60(h):
    return 'T' if len([x for x in h if x == 14]) / len(h) > 0.08 else 'X'

def predict_61(h):
    return 'T' if len([x for x in h if x == 7]) / len(h) < 0.08 else 'X'

def predict_62(h):
    return 'T' if len([x for x in h if x == 15]) / len(h) > 0.06 else 'X'

def predict_63(h):
    return 'T' if len([x for x in h if x == 6]) / len(h) < 0.06 else 'X'

def predict_64(h):
    return 'T' if len([x for x in h if x == 16]) / len(h) > 0.04 else 'X'

def predict_65(h):
    return 'T' if len([x for x in h if x == 5]) / len(h) < 0.04 else 'X'

def predict_66(h):
    return 'T' if len([x for x in h if x == 17]) / len(h) > 0.02 else 'X'

def predict_67(h):
    return 'T' if len([x for x in h if x == 4]) / len(h) < 0.02 else 'X'

def predict_68(h):
    return 'T' if len([x for x in h if x == 18]) / len(h) > 0.01 else 'X'

def predict_69(h):
    return 'T' if len([x for x in h if x == 3]) / len(h) < 0.01 else 'X'

def predict_70(h):
    return 'T' if np.std(h) > 2.8 and np.mean(h) > 10.9 else 'X'

def predict_71(h):
    return 'T' if np.std(h) < 3.1 and np.mean(h) > 11.0 else 'X'

def predict_72(h):
    return 'T' if np.percentile(h, 75) - np.percentile(h, 25) > 3 else 'X'

def predict_73(h):
    return 'T' if np.percentile(h, 85) - np.percentile(h, 15) > 5 else 'X'

def predict_74(h):
    return 'T' if np.percentile(h, 95) - np.percentile(h, 5) > 7 else 'X'

def predict_75(h):
    return 'T' if len([x for x in h if x >= 11]) > len([x for x in h if x <= 10]) else 'X'

def predict_76(h):
    return 'T' if np.mean(h[-100:]) > np.mean(h[:-100]) if len(h) > 200 else 'X'

def predict_77(h):
    return 'T' if np.mean(h[-50:]) > 11.05 else 'X'

def predict_78(h):
    return 'T' if np.mean(h[-25:]) > 11.1 else 'X'

def predict_79(h):
    return 'T' if np.mean(h[-15:]) > 11.15 else 'X'

def predict_80(h):
    return 'T' if np.mean(h[-5:]) > 11.2 else 'X'

def predict_81(h):
    return 'T' if len([x for x in h[-50:] if x >= 11]) / 50 > 0.53 else 'X'

def predict_82(h):
    return 'T' if len([x for x in h[-30:] if x >= 11]) / 30 > 0.54 else 'X'

def predict_83(h):
    return 'T' if len([x for x in h[-10:] if x >= 11]) / 10 > 0.55 else 'X'

def predict_84(h):
    return 'T' if np.percentile(h, 65) > 11.3 else 'X'

def predict_85(h):
    return 'T' if np.percentile(h, 35) > 9.8 else 'X'

def predict_86(h):
    return 'T' if np.mean(h[-200:]) > 10.95 else 'X'

def predict_87(h):
    return 'T' if np.mean(h[-150:]) > 10.98 else 'X'

def predict_88(h):
    return 'T' if np.mean(h[-80:]) > 11.0 else 'X'

def predict_89(h):
    return 'T' if np.mean(h[-40:]) > 11.05 else 'X'

def predict_90(h):
    return 'T' if np.mean(h[-20:]) > 11.1 else 'X'

def predict_91(h):
    return 'T' if np.mean(h[-12:]) > 11.12 else 'X'

def predict_92(h):
    return 'T' if np.mean(h[-8:]) > 11.15 else 'X'

def predict_93(h):
    return 'T' if np.mean(h[-6:]) > 11.18 else 'X'

def predict_94(h):
    return 'T' if np.mean(h[-4:]) > 11.2 else 'X'

def predict_95(h):
    return 'T' if np.mean(h[-2:]) > 11.25 else 'X'

def predict_96(h):
    return 'T' if len([x for x in h if x in {11, 12, 13, 14}]) / len(h) > 0.4 else 'X'

def predict_97(h):
    return 'T' if len([x for x in h if x in {8, 9, 10, 11}]) / len(h) < 0.45 else 'X'

def predict_98(h):
    return 'T' if len([x for x in h if x >= 15]) / len(h) > 0.08 else 'X'

def predict_99(h):
    return 'T' if len([x for x in h if x <= 6]) / len(h) < 0.07 else 'X'

# ========== ENSEMBLE ==========
def ensemble_predict(h):
    if len(h) < 10:
        return 'X', 0.0
    votes = [globals()[f'predict_{i:02d}'](h) for i in range(100)]
    t = votes.count('T')
    conf = round(t / 100, 2)
    return ('T' if t > 50 else 'X'), conf

# ========== API ==========
@app.route("/api/taixiumd5", methods=["GET"])
def taixiumd5():
    try:
        res = requests.get(FIREBASE_URL, timeout=10)
        data = res.json()
        if not data:
            return jsonify({"error": "No data"}), 404

        sessions = sorted(data.values(), key=lambda x: int(x["phien"]))
        totals = [int(s["xuc_xac_1"]) + int(s["xuc_xac_2"]) + int(s["xuc_xac_3"]) for s in sessions]

        prediction, confidence = ensemble_predict(totals)

        latest = sessions[-1]
        xx1 = int(latest["xuc_xac_1"])
        xx2 = int(latest["xuc_xac_2"])
        xx3 = int(latest["xuc_xac_3"])
        tong = xx1 + xx2 + xx3

        return jsonify({
            "phien": latest["phien"],
            "xuc_xac_1": xx1,
            "xuc_xac_2": xx2,
            "xuc_xac_3": xx3,
            "tong": tong,
            "du_doan": prediction,
            "confidence": confidence,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
