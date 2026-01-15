import requests
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

FIREBASE_URL = "https://gbmd5-4a69a-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions.json"

# =========================================================
# 🔢 100 THUẬT TOÁN TÀI – XỈU – KHÔNG DÙNG PHIÊN TRƯỚC
# =========================================================
def predict_00(h): return 'T' if np.percentile(h, 55) > 11.1 else 'X'
def predict_01(h): return 'T' if np.mean(h[-30:]) > np.mean(h) + 0.1 else 'X'
def predict_02(h): return 'T' if len([x for x in h if x in {11,12,13,14,15}])/len(h) > 0.5 else 'X'
def predict_03(h): return 'T' if np.median(h[-20:]) > 11.0 else 'X'
def predict_04(h): return 'T' if np.percentile(h[-50:], 65) > 11.3 else 'X'
def predict_05(h): return 'T' if np.mean([x for x in h[-40:] if x >= 11]) > 12.0 else 'X'
def predict_06(h): return 'T' if len([x for x in h[-25:] if x >= 12])/25 > 0.45 else 'X'
def predict_07(h): return 'T' if np.percentile(h[-15:], 70) > 11.4 else 'X'
def predict_08(h): return 'T' if np.mean(h[-12:]) > np.percentile(h, 60) else 'X'
def predict_09(h): return 'T' if len([x for x in h[-60:] if x >= 11])/60 > 0.53 else 'X'

def predict_10(h): return 'T' if np.percentile(h, 58) > 11.15 else 'X'
def predict_11(h): return 'T' if np.mean(h[-35:]) > np.mean(h) + 0.12 else 'X'
def predict_12(h): return 'T' if len([x for x in h if x in {12,13,14,15,16}])/len(h) > 0.45 else 'X'
def predict_13(h): return 'T' if np.median(h[-25:]) > 11.05 else 'X'
def predict_14(h): return 'T' if np.percentile(h[-45:], 68) > 11.35 else 'X'
def predict_15(h): return 'T' if np.mean([x for x in h[-35:] if x >= 11]) > 11.9 else 'X'
def predict_16(h): return 'T' if len([x for x in h[-30:] if x >= 12])/30 > 0.43 else 'X'
def predict_17(h): return 'T' if np.percentile(h[-18:], 72) > 11.45 else 'X'
def predict_18(h): return 'T' if np.mean(h[-14:]) > np.percentile(h, 62) else 'X'
def predict_19(h): return 'T' if len([x for x in h[-55:] if x >= 11])/55 > 0.52 else 'X'

def predict_20(h): return 'T' if np.percentile(h, 60) > 11.2 else 'X'
def predict_21(h): return 'T' if np.mean(h[-40:]) > np.mean(h) + 0.15 else 'X'
def predict_22(h): return 'T' if len([x for x in h if x in {13,14,15,16,17}])/len(h) > 0.4 else 'X'
def predict_23(h): return 'T' if np.median(h[-30:]) > 11.1 else 'X'
def predict_24(h): return 'T' if np.percentile(h[-40:], 70) > 11.4 else 'X'
def predict_25(h): return 'T' if np.mean([x for x in h[-30:] if x >= 11]) > 11.8 else 'X'
def predict_26(h): return 'T' if len([x for x in h[-35:] if x >= 12])/35 > 0.41 else 'X'
def predict_27(h): return 'T' if np.percentile(h[-20:], 75) > 11.5 else 'X'
def predict_28(h): return 'T' if np.mean(h[-16:]) > np.percentile(h, 65) else 'X'
def predict_29(h): return 'T' if len([x for x in h[-50:] if x >= 11])/50 > 0.51 else 'X'

def predict_30(h): return 'T' if np.percentile(h, 62) > 11.25 else 'X'
def predict_31(h): return 'T' if np.mean(h[-45:]) > np.mean(h) + 0.18 else 'X'
def predict_32(h): return 'T' if len([x for x in h if x in {14,15,16,17,18}])/len(h) > 0.35 else 'X'
def predict_33(h): return 'T' if np.median(h[-35:]) > 11.15 else 'X'
def predict_34(h): return 'T' if np.percentile(h[-35:], 72) > 11.45 else 'X'
def predict_35(h): return 'T' if np.mean([x for x in h[-25:] if x >= 11]) > 11.7 else 'X'
def predict_36(h): return 'T' if len([x for x in h[-40:] if x >= 12])/40 > 0.4 else 'X'
def predict_37(h): return 'T' if np.percentile(h[-22:], 77) > 11.55 else 'X'
def predict_38(h): return 'T' if np.mean(h[-18:]) > np.percentile(h, 68) else 'X'
def predict_39(h): return 'T' if len([x for x in h[-45:] if x >= 11])/45 > 0.5 else 'X'

def predict_40(h): return 'T' if np.percentile(h, 65) > 11.3 else 'X'
def predict_41(h): return 'T' if np.mean(h[-50:]) > np.mean(h) + 0.2 else 'X'
def predict_42(h): return 'T' if len([x for x in h if x in {15,16,17,18,19}])/len(h) > 0.3 else 'X'
def predict_43(h): return 'T' if np.median(h[-40:]) > 11.2 else 'X'
def predict_44(h): return 'T' if np.percentile(h[-30:], 75) > 11.5 else 'X'
def predict_45(h): return 'T' if np.mean([x for x in h[-20:] if x >= 11]) > 11.6 else 'X'
def predict_46(h): return 'T' if len([x for x in h[-45:] if x >= 12])/45 > 0.38 else 'X'
def predict_47(h): return 'T' if np.percentile(h[-25:], 80) > 11.6 else 'X'
def predict_48(h): return 'T' if np.mean(h[-20:]) > np.percentile(h, 70) else 'X'
def predict_49(h): return 'T' if len([x for x in h[-40:] if x >= 11])/40 > 0.49 else 'X'

def predict_50(h): return 'T' if np.percentile(h, 68) > 11.35 else 'X'
def predict_51(h): return 'T' if np.mean(h[-55:]) > np.mean(h) + 0.22 else 'X'
def predict_52(h): return 'T' if len([x for x in h if x >= 16])/len(h) > 0.25 else 'X'
def predict_53(h): return 'T' if np.median(h[-45:]) > 11.25 else 'X'
def predict_54(h): return 'T' if np.percentile(h[-25:], 78) > 11.6 else 'X'
def predict_55(h): return 'T' if np.mean([x for x in h[-15:] if x >= 11]) > 11.5 else 'X'
def predict_56(h): return 'T' if len([x for x in h[-50:] if x >= 12])/50 > 0.36 else 'X'
def predict_57(h): return 'T' if np.percentile(h[-28:], 82) > 11.7 else 'X'
def predict_58(h): return 'T' if np.mean(h[-22:]) > np.percentile(h, 72) else 'X'
def predict_59(h): return 'T' if len([x for x in h[-35:] if x >= 11])/35 > 0.48 else 'X'

def predict_60(h): return 'T' if np.percentile(h, 70) > 11.4 else 'X'
def predict_61(h): return 'T' if np.mean(h[-60:]) > np.mean(h) + 0.25 else 'X'
def predict_62(h): return 'T' if len([x for x in h if x >= 17])/len(h) > 0.2 else 'X'
def predict_63(h): return 'T' if np.median(h[-50:]) > 11.3 else 'X'
def predict_64(h): return 'T' if np.percentile(h[-20:], 80) > 11.7 else 'X'
def predict_65(h): return 'T' if np.mean([x for x in h[-10:] if x >= 11]) > 11.4 else 'X'
def predict_66(h): return 'T' if len([x for x in h[-55:] if x >= 12])/55 > 0.34 else 'X'
def predict_67(h): return 'T' if np.percentile(h[-30:], 85) > 11.8 else 'X'
def predict_68(h): return 'T' if np.mean(h[-24:]) > np.percentile(h, 75) else 'X'
def predict_69(h): return 'T' if len([x for x in h[-30:] if x >= 11])/30 > 0.47 else 'X'

def predict_70(h): return 'T' if np.percentile(h, 72) > 11.45 else 'X'
def predict_71(h): return 'T' if np.mean(h[-65:]) > np.mean(h) + 0.28 else 'X'
def predict_72(h): return 'T' if len([x for x in h if x >= 18])/len(h) > 0.15 else 'X'
def predict_73(h): return 'T' if np.median(h[-55:]) > 11.35 else 'X'
def predict_74(h): return 'T' if np.percentile(h[-15:], 82) > 11.8 else 'X'
def predict_75(h): return 'T' if np.mean([x for x in h[-8:] if x >= 11]) > 11.3 else 'X'
def predict_76(h): return 'T' if len([x for x in h[-60:] if x >= 12])/60 > 0.32 else 'X'
def predict_77(h): return 'T' if np.percentile(h[-32:], 87) > 11.9 else 'X'
def predict_78(h): return 'T' if np.mean(h[-26:]) > np.percentile(h, 77) else 'X'
def predict_79(h): return 'T' if len([x for x in h[-25:] if x >= 11])/25 > 0.46 else 'X'

def predict_80(h): return 'T' if np.percentile(h, 75) > 11.5 else 'X'
def predict_81(h): return 'T' if np.mean(h[-70:]) > np.mean(h) + 0.3 else 'X'
def predict_82(h): return 'T' if len([x for x in h if x >= 19])/len(h) > 0.1 else 'X'
def predict_83(h): return 'T' if np.median(h[-60:]) > 11.4 else 'X'
def predict_84(h): return 'T' if np.percentile(h[-12:], 85) > 12.0 else 'X'
def predict_85(h): return 'T' if np.mean([x for x in h[-5:] if x >= 11]) > 11.2 else 'X'
def predict_86(h): return 'T' if len([x for x in h[-65:] if x >= 12])/65 > 0.3 else 'X'
def predict_87(h): return 'T' if np.percentile(h[-35:], 90) > 12.1 else 'X'
def predict_88(h): return 'T' if np.mean(h[-28:]) > np.percentile(h, 80) else 'X'
def predict_89(h): return 'T' if len([x for x in h[-20:] if x >= 11])/20 > 0.45 else 'X'

def predict_90(h): return 'T' if np.percentile(h, 77) > 11.55 else 'X'
def predict_91(h): return 'T' if np.mean(h[-75:]) > np.mean(h) + 0.32 else 'X'
def predict_92(h): return 'T' if len([x for x in h if x >= 20])/len(h) > 0.08 else 'X'
def predict_93(h): return 'T' if np.median(h[-65:]) > 11.45 else 'X'
def predict_94(h): return 'T' if np.percentile(h[-10:], 88) > 12.2 else 'X'
def predict_95(h): return 'T' if np.mean([x for x in h[-6:] if x >= 11]) > 11.1 else 'X'
def predict_96(h): return 'T' if len([x for x in h[-70:] if x >= 12])/70 > 0.28 else 'X'
def predict_97(h): return 'T' if np.percentile(h[-38:], 92) > 12.3 else 'X'
def predict_98(h): return 'T' if np.mean(h[-30:]) > np.percentile(h, 82) else 'X'
def predict_99(h): return 'T' if len([x for x in h[-15:] if x >= 11])/15 > 0.44 else 'X'

# =========================================================
# 🔍 ENSEMBLE – TỔNG HỢP 100 THUẬT TOÁN
# =========================================================
def ensemble_predict(h):
    if len(h) < 10:
        return 'X', 0.0
    votes = [globals()[f'predict_{i:02d}'](h) for i in range(100)]
    t = votes.count('T')
    conf = round(t / 100, 2)
    return ('T' if t > 50 else 'X'), conf

# =========================================================
# 🔻 API – TRẢ VỀ KẾT QUẢ THẬT + DỰ ĐOÁN + ĐỘ TIN CẬY
# =========================================================
@app.route("/api/taixiumd5", methods=["GET"])
def taixiumd5():
    try:
        res = requests.get(FIREBASE_URL, timeout=10)
        res.raise_for_status()
        data = res.json()

        if not data:
            return jsonify({"status": "error", "message": "No data"}), 404

        sessions = sorted(data.values(), key=lambda x: int(x["phien"]))
        totals = [int(s["xuc_xac_1"]) + int(s["xuc_xac_2"]) + int(s["xuc_xac_3"]) for s in sessions]

        prediction, confidence = ensemble_predict(totals)

        latest = sessions[-1]
        x1 = int(latest["xuc_xac_1"])
        x2 = int(latest["xuc_xac_2"])
        x3 = int(latest["xuc_xac_3"])
        tong = x1 + x2 + x3
        ketqua = "Tài" if tong >= 11 else "Xỉu"

        return jsonify({
            "status": "success",
            "phien": latest["phien"],
            "xuc_xac_1": x1,
            "xuc_xac_2": x2,
            "xuc_xac_3": x3,
            "tong": tong,
            "ketqua": ketqua,
            "du_doan": "Tài" if prediction == 'T' else "Xỉu",
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# =========================================================
# 🚀 RUN SERVER
# =========================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
