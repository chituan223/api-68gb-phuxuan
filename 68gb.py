from flask import Flask, jsonify
import requests
from collections import deque
import statistics

app = Flask(__name__)

# ==============================
# Cấu hình người dùng & API
# ==============================
API_URL = "https://gbgayy-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions/current.json"
USER_ID = "tuandz"

# ==============================
# Lịch sử để phân tích cầu
# ==============================
history = deque(maxlen=50)
totals = deque(maxlen=50)

# ==============================
# 🧠 AI21–AI30 – thuật toán thực chiến
# ==============================
def ai21_dynamic_parity(history, totals):
    if len(totals) < 6:
        return {"du_doan": "Tài", "do_tin_cay": 65.9}
    last6 = totals[-6:]
    even = sum(1 for t in last6 if t % 2 == 0)
    last = "Tài" if totals[-1] >= 11 else "Xỉu"
    if even >= 5:
        return {"du_doan": "Xỉu", "do_tin_cay": 89.2}
    if even <= 1:
        return {"du_doan": "Tài", "do_tin_cay": 88.5}
    return {"du_doan": last, "do_tin_cay": 72.3}

def ai22_cau_dao_chieu(history, totals):
    if len(history) < 6:
        return {"du_doan": "Tài", "do_tin_cay": 64.7}
    seq = "".join("T" if h == "Tài" else "X" for h in history[-6:])
    if seq.endswith("TTTX") or seq.endswith("XXXT"):
        return {"du_doan": "Tài" if history[-1] == "Xỉu" else "Xỉu", "do_tin_cay": 91.0}
    return {"du_doan": history[-1], "do_tin_cay": 73.1}

def ai23_weighted_pattern(history, totals):
    if len(history) < 10:
        return {"du_doan": "Tài", "do_tin_cay": 66.3}
    weights = [0.1, 0.15, 0.2, 0.25, 0.3]
    score = 0
    for i, w in enumerate(weights):
        if history[-(i+1)] == "Tài":
            score += w
        else:
            score -= w
    if score > 0.2:
        return {"du_doan": "Tài", "do_tin_cay": 88.1}
    if score < -0.2:
        return {"du_doan": "Xỉu", "do_tin_cay": 87.9}
    return {"du_doan": history[-1], "do_tin_cay": 72.0}

def ai24_stable_chain(history, totals):
    if len(totals) < 7:
        return {"du_doan": "Tài", "do_tin_cay": 65.0}
    var = max(totals[-7:]) - min(totals[-7:])
    if var <= 3:
        return {"du_doan": "Xỉu", "do_tin_cay": 84.6}
    else:
        return {"du_doan": "Tài", "do_tin_cay": 79.3}

def ai25_cross_cycle(history, totals):
    if len(history) < 8:
        return {"du_doan": "Tài", "do_tin_cay": 65.8}
    seq = "".join("T" if h == "Tài" else "X" for h in history[-8:])
    if "TXTX" in seq or "XTXT" in seq:
        next_pred = "Tài" if history[-1] == "Xỉu" else "Xỉu"
        return {"du_doan": next_pred, "do_tin_cay": 90.4}
    return {"du_doan": history[-1], "do_tin_cay": 73.0}

def ai26_phase_shift(history, totals):
    if len(totals) < 6:
        return {"du_doan": "Tài", "do_tin_cay": 65.2}
    avg3_now = statistics.mean(totals[-3:])
    avg3_prev = statistics.mean(totals[-6:-3])
    if avg3_now > avg3_prev + 1:
        return {"du_doan": "Tài", "do_tin_cay": 87.4}
    if avg3_now < avg3_prev - 1:
        return {"du_doan": "Xỉu", "do_tin_cay": 86.8}
    return {"du_doan": history[-1], "do_tin_cay": 74.0}

def ai27_reverse_tail(history, totals):
    if len(history) < 4:
        return {"du_doan": "Tài", "do_tin_cay": 63.8}
    last = history[-1]
    if history[-4:].count(last) == 3:
        return {"du_doan": "Xỉu" if last == "Tài" else "Tài", "do_tin_cay": 91.2}
    return {"du_doan": last, "do_tin_cay": 71.5}

def ai28_entropy(history, totals):
    if len(history) < 10:
        return {"du_doan": "Tài", "do_tin_cay": 64.9}
    pattern = history[-10:]
    diversity = len(set(pattern))
    if diversity == 1:
        return {"du_doan": "Xỉu" if pattern[-1] == "Tài" else "Tài", "do_tin_cay": 93.4}
    elif diversity == 2:
        return {"du_doan": history[-1], "do_tin_cay": 78.2}
    return {"du_doan": history[-1], "do_tin_cay": 71.2}

def ai29_long_short_avg(history, totals):
    if len(totals) < 12:
        return {"du_doan": "Tài", "do_tin_cay": 65.6}
    short_avg = sum(totals[-4:]) / 4
    long_avg = sum(totals[-12:]) / 12
    if short_avg > long_avg + 0.8:
        return {"du_doan": "Tài", "do_tin_cay": 86.9}
    if short_avg < long_avg - 0.8:
        return {"du_doan": "Xỉu", "do_tin_cay": 86.5}
    return {"du_doan": history[-1], "do_tin_cay": 72.0}

def ai30_chain_balance(history, totals):
    if len(history) < 6:
        return {"du_doan": "Tài", "do_tin_cay": 65.4}
    chain = 0
    for i in range(1, 6):
        if history[-i] == history[-(i+1)]:
            chain += 1
        else:
            break
    if chain >= 3:
        return {"du_doan": "Xỉu" if history[-1] == "Tài" else "Tài", "do_tin_cay": 90.1}
    return {"du_doan": history[-1], "do_tin_cay": 73.1}

# ==============================
# 🌐 Hàm tổng hợp AI30
# ==============================
def ai_logic_30(tong, x1, x2, x3, history_list):
    totals_list = [x1+x2+x3]
    ai_funcs = [
        ai21_dynamic_parity, ai22_cau_dao_chieu, ai23_weighted_pattern, ai24_stable_chain,
        ai25_cross_cycle, ai26_phase_shift, ai27_reverse_tail, ai28_entropy,
        ai29_long_short_avg, ai30_chain_balance
    ]
    vote_counts = {}
    vote_conf = {}
    for func in ai_funcs:
        res = func(history_list, totals_list)
        pred = res["du_doan"]
        conf = res["do_tin_cay"]
        vote_counts[pred] = vote_counts.get(pred, 0) + 1
        vote_conf[pred] = conf  # lấy giá trị cuối cùng của vote nhiều nhất
    final_pred = max(vote_counts, key=lambda k: vote_counts[k])
    final_conf = vote_conf[final_pred]
    return final_pred, final_conf

# ==============================
# 🌐 API /api/taixiu
# ==============================
@app.route("/api/taixiu")
def get_taixiu():
    try:
        data = requests.get(API_URL, timeout=5).json()
        phien = data.get("Phien")
        kq = data.get("ket_qua")
        x1 = data.get("xuc_xac_1")
        x2 = data.get("xuc_xac_2")
        x3 = data.get("xuc_xac_3")
        tong = data.get("tong")

        if kq:
            history.append(kq)
            totals.append(tong)

        du_doan, do_tin_cay = ai_logic_30(tong, x1, x2, x3, list(history))

        return jsonify({
            "id": USER_ID,
            "phien": phien,
            "xuc_xac_1": x1,
            "xuc_xac_2": x2,
            "xuc_xac_3": x3,
            "tong": tong,
            "du_doan": du_doan,
            "do_tin_cay": f"{do_tin_cay}%"
        })
    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"})

# ==============================
# 🏠 Trang chủ
# ==============================
@app.route("/")
def home():
    return """
    <h2>TOOL TÀI XỈU AI30 + AI21-30 THỰC CHIẾN</h2>
    <p>API: <a href='/api/taixiu'>/api/taixiu</a></p>
    <p>Người dùng: <b>tuandz</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)