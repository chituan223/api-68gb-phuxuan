import requests
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

FIREBASE_URL = "https://gbmd5-4a69a-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions.json"

# ========== 100 THUẬT TOÁN THẬT – KHÔNG RANDOM ==========
def predict_00(h):
    return 'T' if h[-1] >= 11 else 'X'

def predict_01(h):
    return 'T' if sum(h[-3:]) >= 33 else 'X'

def predict_02(h):
    return 'T' if h[-1] > np.mean(h[-5:]) else 'X'

def predict_03(h):
    return 'T' if len(h) >= 5 and h[-1] > h[-5] else 'X'

def predict_04(h):
    return 'T' if sum(1 for x in h[-5:] if x >= 11) >= 3 else 'X'

def predict_05(h):
    return 'T' if np.std(h[-5:]) < 2 else 'X'

def predict_06(h):
    return 'T' if h[-1] + h[-2] >= 22 else 'X'

def predict_07(h):
    return 'T' if np.median(h[-5:]) >= 11 else 'X'

def predict_08(h):
    return 'T' if h[-1] == max(h[-5:]) else 'X'

def predict_09(h):
    return 'T' if h[-1] - h[-2] >= 3 else 'X'

def predict_10(h):
    return 'T' if sum(h[-2:]) >= 22 else 'X'

def predict_11(h):
    return 'T' if min(h[-5:]) >= 9 else 'X'

def predict_12(h):
    return 'T' if max(h[-5:]) >= 14 else 'X'

def predict_13(h):
    return 'T' if h[-1] > 10 and h[-2] > 10 else 'X'

def predict_14(h):
    return 'T' if len(h) >= 6 and h[-1] > h[-6] else 'X'

def predict_15(h):
    return 'T' if sum(h[-4:]) >= 44 else 'X'

def predict_16(h):
    return 'T' if np.diff(h[-3:]).mean() > 0 else 'X'

def predict_17(h):
    return 'T' if h[-1] >= 12 and h[-2] >= 12 else 'X'

def predict_18(h):
    return 'T' if sum(1 for x in h[-7:] if x >= 11) >= 4 else 'X'

def predict_19(h):
    return 'T' if h[-1] > np.percentile(h[-10:], 70) else 'X'

def predict_20(h):
    return 'T' if h[-1] + h[-3] >= 22 else 'X'

def predict_21(h):
    return 'T' if h[-1] - h[-3] >= 4 else 'X'

def predict_22(h):
    return 'T' if np.mean(h[-7:]) >= 11 else 'X'

def predict_23(h):
    return 'T' if h[-1] >= 11 and h[-2] >= 11 else 'X'

def predict_24(h):
    return 'T' if sum(h[-5:]) >= 55 else 'X'

def predict_25(h):
    return 'T' if h[-1] > h[-2] > h[-3] else 'X'

def predict_26(h):
    return 'T' if len(h) >= 8 and h[-1] > h[-8] else 'X'

def predict_27(h):
    return 'T' if np.var(h[-5:]) < 1.5 else 'X'

def predict_28(h):
    return 'T' if h[-1] + h[-2] + h[-3] >= 33 else 'X'

def predict_29(h):
    return 'T' if h[-1] >= 13 or h[-2] >= 13 else 'X'

def predict_30(h):
    return 'T' if sum(1 for x in h[-6:] if x >= 11) >= 4 else 'X'

def predict_31(h):
    return 'T' if h[-1] > np.max(h[-10:-1]) else 'X'

def predict_32(h):
    return 'T' if h[-1] >= 11 and h[-2] < 11 else 'X'

def predict_33(h):
    return 'T' if np.percentile(h[-5:], 80) >= 12 else 'X'

def predict_34(h):
    return 'T' if h[-1] - h[-5] >= 3 else 'X'

def predict_35(h):
    return 'T' if sum(h[-2:]) >= 23 else 'X'

def predict_36(h):
    return 'T' if h[-1] <= 9 and h[-2] <= 9 else 'X'

def predict_37(h):
    return 'T' if np.mean(h[-9:]) >= 11 else 'X'

def predict_38(h):
    return 'T' if h[-1] + h[-2] + h[-4] >= 33 else 'X'

def predict_39(h):
    return 'T' if len(h) >= 10 and h[-1] > h[-10] else 'X'

def predict_40(h):
    return 'T' if sum(1 for x in h[-8:] if x >= 11) >= 5 else 'X'

def predict_41(h):
    return 'T' if h[-1] >= 11 and h[-3] >= 11 else 'X'

def predict_42(h):
    return 'T' if np.min(h[-5:]) >= 10 else 'X'

def predict_43(h):
    return 'T' if h[-1] - h[-2] >= 2 and h[-2] - h[-3] >= 2 else 'X'

def predict_44(h):
    return 'T' if np.percentile(h[-7:], 90) >= 13 else 'X'

def predict_45(h):
    return 'T' if h[-1] + h[-2] >= 24 else 'X'

def predict_46(h):
    return 'T' if sum(h[-3:]) >= 34 else 'X'

def predict_47(h):
    return 'T' if h[-1] > np.median(h[-9:]) else 'X'

def predict_48(h):
    return 'T' if len(h) >= 12 and h[-1] > h[-12] else 'X'

def predict_49(h):
    return 'T' if np.std(h[-7:]) < 1.8 else 'X'

def predict_50(h):
    return 'T' if h[-1] >= 11 and h[-2] >= 11 and h[-3] >= 11 else 'X'

def predict_51(h):
    return 'T' if max(h[-3:]) >= 15 else 'X'

def predict_52(h):
    return 'T' if sum(1 for x in h[-9:] if x >= 11) >= 6 else 'X'

def predict_53(h):
    return 'T' if h[-1] - h[-6] >= 4 else 'X'

def predict_54(h):
    return 'T' if np.mean(h[-11:]) >= 11 else 'X'

def predict_55(h):
    return 'T' if h[-1] + h[-5] >= 22 else 'X'

def predict_56(h):
    return 'T' if h[-1] >= 12 and h[-2] < 10 else 'X'

def predict_57(h):
    return 'T' if len(h) >= 15 and h[-1] > h[-15] else 'X'

def predict_58(h):
    return 'T' if sum(h[-4:]) >= 45 else 'X'

def predict_59(h):
    return 'T' if np.percentile(h[-6:], 75) >= 12 else 'X'

def predict_60(h):
    return 'T' if h[-1] >= 11 and h[-4] >= 11 else 'X'

def predict_61(h):
    return 'T' if np.var(h[-9:]) < 2.5 else 'X'

def predict_62(h):
    return 'T' if h[-1] > np.mean(h[-13:]) else 'X'

def predict_63(h):
    return 'T' if sum(1 for x in h[-10:] if x >= 11) >= 7 else 'X'

def predict_64(h):
    return 'T' if h[-1] + h[-2] + h[-5] >= 33 else 'X'

def predict_65(h):
    return 'T' if h[-1] - h[-7] >= 3 else 'X'

def predict_66(h):
    return 'T' if np.min(h[-7:]) >= 10 else 'X'

def predict_67(h):
    return 'T' if h[-1] >= 14 or h[-2] >= 14 else 'X'

def predict_68(h):
    return 'T' if np.mean(h[-15:]) >= 11 else 'X'

def predict_69(h):
    return 'T' if h[-1] + h[-2] + h[-6] >= 33 else 'X'

def predict_70(h):
    return 'T' if len(h) >= 20 and h[-1] > h[-20] else 'X'

def predict_71(h):
    return 'T' if sum(h[-5:]) >= 56 else 'X'

def predict_72(h):
    return 'T' if np.percentile(h[-8:], 80) >= 12 else 'X'

def predict_73(h):
    return 'T' if h[-1] >= 11 and h[-5] >= 11 else 'X'

def predict_74(h):
    return 'T' if np.std(h[-11:]) < 2.2 else 'X'

def predict_75(h):
    return 'T' if h[-1] > np.percentile(h[-12:], 70) else 'X'

def predict_76(h):
    return 'T' if sum(1 for x in h[-11:] if x >= 11) >= 7 else 'X'

def predict_77(h):
    return 'T' if h[-1] + h[-3] + h[-5] >= 33 else 'X'

def predict_78(h):
    return 'T' if h[-1] - h[-8] >= 4 else 'X'

def predict_79(h):
    return 'T' if np.mean(h[-17:]) >= 11 else 'X'

def predict_80(h):
    return 'T' if max(h[-5:]) >= 15 else 'X'

def predict_81(h):
    return 'T' if h[-1] >= 11 and h[-6] >= 11 else 'X'

def predict_82(h):
    return 'T' if sum(h[-6:]) >= 66 else 'X'

def predict_83(h):
    return 'T' if np.var(h[-13:]) < 3 else 'X'

def predict_84(h):
    return 'T' if h[-1] > np.mean(h[-19:]) else 'X'

def predict_85(h):
    return 'T' if sum(1 for x in h[-12:] if x >= 11) >= 8 else 'X'

def predict_86(h):
    return 'T' if h[-1] + h[-4] + h[-7] >= 33 else 'X'

def predict_87(h):
    return 'T' if len(h) >= 25 and h[-1] > h[-25] else 'X'

def predict_88(h):
    return 'T' if np.percentile(h[-9:], 85) >= 13 else 'X'

def predict_89(h):
    return 'T' if h[-1] - h[-9] >= 3 else 'X'

def predict_90(h):
    return 'T' if np.min(h[-9:]) >= 9 else 'X'

def predict_91(h):
    return 'T' if h[-1] >= 13 and h[-2] >= 13 else 'X'

def predict_92(h):
    return 'T' if sum(h[-7:]) >= 77 else 'X'

def predict_93(h):
    return 'T' if np.mean(h[-21:]) >= 11 else 'X'

def predict_94(h):
    return 'T' if h[-1] > np.max(h[-7:-1]) else 'X'

def predict_95(h):
    return 'T' if sum(1 for x in h[-13:] if x >= 11) >= 8 else 'X'

def predict_96(h):
    return 'T' if h[-1] + h[-5] + h[-9] >= 33 else 'X'

def predict_97(h):
    return 'T' if np.std(h[-15:]) < 2.8 else 'X'

def predict_98(h):
    return 'T' if h[-1] - h[-10] >= 4 else 'X'

def predict_99(h):
    return 'T' if np.percentile(h[-10:], 90) >= 14 else 'X'

# ========== ENSEMBLE ==========
def ensemble_predict(h):
    votes = [globals()[f'predict_{i:02d}'](h) for i in range(100)]
    t = votes.count('T')
    return 'T' if t > 50 else 'X', round(t / 100, 2)

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
