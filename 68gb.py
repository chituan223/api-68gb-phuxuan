import requests
from flask import Flask, jsonify

app = Flask(__name__)

FIREBASE_URL = "https://gbmd5-4a69a-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions.json"

# =========================================================
# 🧠 SMART BET PATTERNS – GIỮ NGUYÊN LOGIC BẠN ĐƯA
# =========================================================

def cau_11_01(h):
    if len(h)<6: return None,0
    if all(h[-i]!=h[-i-1] for i in range(1,5)):
        return h[-1],65
    return None,0

def cau_11_02(h):
    if len(h)<7: return None,0
    if h[-6:]==["Tài","Xỉu"]*3 or h[-6:]==["Xỉu","Tài"]*3:
        return h[-1],70
    return None,0

def cau_22_01(h):
    if len(h)<8: return None,0
    if h[-8:]==["Tài","Tài","Xỉu","Xỉu"]*2:
        return h[-1],68
    if h[-8:]==["Xỉu","Xỉu","Tài","Tài"]*2:
        return h[-1],68
    return None,0

def cau_22_02(h):
    if len(h)<6: return None,0
    if h[-4]==h[-3] and h[-2]==h[-1] and h[-3]!=h[-2]:
        return h[-1],64
    return None,0

def cau_1212_01(h):
    if len(h)<6: return None,0
    if h[-6:]==["Tài","Xỉu"]*3:
        return "Tài",72
    if h[-6:]==["Xỉu","Tài"]*3:
        return "Xỉu",72
    return None,0

def cau_2211_01(h):
    if len(h)<8: return None,0
    if h[-8:]==["Tài","Tài","Xỉu","Xỉu","Tài","Xỉu","Tài","Xỉu"]:
        return h[-1],70
    return None,0

def bet_break_01(h):
    if len(h)<6: return None,0
    if h[-2]==h[-3]==h[-4] and h[-1]!=h[-2]:
        return h[-1],66
    return None,0

def bet_break_02(h):
    if len(h)<7: return None,0
    if h[-3]==h[-4]==h[-5]==h[-6] and h[-1]!=h[-2]:
        return h[-1],70
    return None,0

def bet_follow_01(h):
    if len(h)<5: return None,0
    if h[-1]==h[-2]==h[-3]:
        return h[-1],60
    return None,0

def bet_follow_02(h):
    if len(h)<6: return None,0
    if h[-1]==h[-2]==h[-3]==h[-4]:
        return h[-1],65
    return None,0

def nhip_31(h):
    if len(h)<6: return None,0
    if h[-4]==h[-3]==h[-2] and h[-1]!=h[-2]:
        return h[-1],67
    return None,0

def nhip_41(h):
    if len(h)<7: return None,0
    if h[-5]==h[-4]==h[-3]==h[-2] and h[-1]!=h[-2]:
        return h[-1],72
    return None,0

def momentum_flip(h):
    if len(h)<20: return None,0
    if h[-10:].count("Tài")>=7: return "Xỉu",75
    if h[-10:].count("Xỉu")>=7: return "Tài",75
    return None,0

SMART_VOTERS = [
    cau_11_01, cau_11_02,
    cau_22_01, cau_22_02,
    cau_1212_01, cau_2211_01,
    bet_break_01, bet_break_02,
    bet_follow_01, bet_follow_02,
    nhip_31, nhip_41,
    momentum_flip
]

def smart_vote_engine(history):
    score={"Tài":0,"Xỉu":0}
    total=0
    for f in SMART_VOTERS:
        r,c=f(history)
        if r:
            score[r]+=c
            total+=c
    if total==0:
        return None,0
    if score["Tài"]>score["Xỉu"]:
        return "Tài", int(score["Tài"]/total*100)
    if score["Xỉu"]>score["Tài"]:
        return "Xỉu", int(score["Xỉu"]/total*100)
    return None,0

# =========================================================
# 🌐 API – DỮ LIỆU THẬT + DỰ ĐOÁN PHIÊN KẾ TIẾP
# =========================================================
@app.route("/api/taixiumd5", methods=["GET"])
def taixiumd5():
    try:
        res = requests.get(FIREBASE_URL, timeout=10)
        res.raise_for_status()
        data = res.json()

        sessions = sorted(data.values(), key=lambda x: int(x["phien"]))

        history=[]
        for s in sessions:
            t = int(s["xuc_xac_1"]) + int(s["xuc_xac_2"]) + int(s["xuc_xac_3"])
            history.append("Tài" if t>=11 else "Xỉu")

        du_doan, conf = smart_vote_engine(history)

        latest = sessions[-1]
        x1,x2,x3 = int(latest["xuc_xac_1"]),int(latest["xuc_xac_2"]),int(latest["xuc_xac_3"])
        tong = x1+x2+x3
        ketqua = "Tài" if tong>=11 else "Xỉu"

        return jsonify({
            "status":"success",
            "phien_hien_tai": latest["phien"],
            "xuc_xac_1": x1,
            "xuc_xac_2": x2,
            "xuc_xac_3": x3,
            "tong": tong,
            "ketqua": ketqua,
            "du_doan_phien_tiep_theo": du_doan,
            "confidence": conf
        })

    except Exception as e:
        return jsonify({"status":"error","message":str(e)}),500

# =========================================================
# 🚀 RUN
# =========================================================
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
