import requests
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

FIREBASE_URL = "https://gbmd5-4a69a-default-rtdb.asia-southeast1.firebasedatabase.app/taixiu_sessions.json"

# ========== 100 THUẬT TOÁN LOGIC THUẦN – KHÔNG ML, KHÔNG RANDOM ==========
def predict_00(h):  # Đảo chiều 3 phiên
    if len(h) < 4: return 'X'
    last3 = h[-3:]
    return 'T' if all(x >= 11 for x in last3) else ('X' if all(x <= 10 for x in last3) else ('T' if h[-1] <= 10 else 'X'))

def predict_01(h):  # Trung bình 5 phiên
    if len(h) < 5: return 'X'
    return 'T' if np.mean(h[-5:]) > 10.5 else 'X'

def predict_02(h):  # Trung bình 10 phiên
    if len(h) < 10: return 'X'
    return 'T' if np.mean(h[-10:]) > 10.5 else 'X'

def predict_03(h):  # Trung bình 20 phiên
    if len(h) < 20: return 'X'
    return 'T' if np.mean(h[-20:]) > 10.5 else 'X'

def predict_04(h):  # Trung bình 30 phiên
    if len(h) < 30: return 'X'
    return 'T' if np.mean(h[-30:]) > 10.5 else 'X'

def predict_05(h):  # Phân vị 75% 10 phiên
    if len(h) < 10: return 'X'
    return 'T' if np.percentile(h[-10:], 75) > 10.5 else 'X'

def predict_06(h):  # Phân vị 75% 20 phiên
    if len(h) < 20: return 'X'
    return 'T' if np.percentile(h[-20:], 75) > 10.5 else 'X'

def predict_07(h):  # Phân vị 90% 10 phiên
    if len(h) < 10: return 'X'
    return 'T' if np.percentile(h[-10:], 90) > 10.5 else 'X'

def predict_08(h):  # Độ lệch chuẩn thấp → Tài
    if len(h) < 10: return 'X'
    return 'T' if np.std(h[-10:]) < 2.5 else 'X'

def predict_09(h):  # Độ lệch chuẩn cao → Xỉu
    if len(h) < 10: return 'X'
    return 'T' if np.std(h[-10:]) > 3.5 else 'X'

def predict_10(h):  # Tăng 3 phiên liên tiếp
    if len(h) < 4: return 'X'
    return 'T' if h[-1] > h[-2] > h[-3] else 'X'

def predict_11(h):  # Giảm 3 phiên liên tiếp
    if len(h) < 4: return 'X'
    return 'T' if h[-1] < h[-2] < h[-3] else 'X'

def predict_12(h):  # Tăng mạnh 4 điểm
    if len(h) < 2: return 'X'
    return 'T' if h[-1] - h[-2] >= 4 else 'X'

def predict_13(h):  # Giảm mạnh 4 điểm
    if len(h) < 2: return 'X'
    return 'T' if h[-2] - h[-1] >= 4 else 'X'

def predict_14(h):  # Max 5 phiên >= 14
    if len(h) < 5: return 'X'
    return 'T' if max(h[-5:]) >= 14 else 'X'

def predict_15(h):  # Min 5 phiên <= 7
    if len(h) < 5: return 'X'
    return 'T' if min(h[-5:]) <= 7 else 'X'

def predict_16(h):  # Sóng ngắn 3 phiên
    if len(h) < 4: return 'X'
    a, b, c = h[-3:]
    return 'T' if (a < b > c and b > 11) else 'X'

def predict_17(h):  # Sóng dài 5 phiên
    if len(h) < 5: return 'X'
    return 'T' if (h[-3] > h[-2] < h[-1] and h[-1] > 11) else 'X'

def predict_18(h):  # Tần suất Tài 7/10
    if len(h) < 10: return 'X'
    return 'T' if sum(1 for x in h[-10:] if x > 10.5) >= 7 else 'X'

def predict_19(h):  # Tần suất Xỉu 7/10
    if len(h) < 10: return 'X'
    return 'T' if sum(1 for x in h[-10:] if x <= 10.5) >= 7 else 'X'

def predict_20(h):  # Tần suất Tài 4/5
    if len(h) < 5: return 'X'
    return 'T' if sum(1 for x in h[-5:] if x > 10.5) >= 4 else 'X'

def predict_21(h):  # Tần suất Xỉu 4/5
    if len(h) < 5: return 'X'
    return 'T' if sum(1 for x in h[-5:] if x <= 10.5) >= 4 else 'X'

def predict_22(h):  # Trung vị 7 phiên
    if len(h) < 7: return 'X'
    return 'T' if np.median(h[-7:]) > 10.5 else 'X'

def predict_23(h):  # Trung vị 15 phiên
    if len(h) < 15: return 'X'
    return 'T' if np.median(h[-15:]) > 10.5 else 'X'

def predict_24(h):  # Gradient tăng
    if len(h) < 5: return 'X'
    return 'T' if np.gradient(h[-5:])[-1] > 0 else 'X'

def predict_25(h):  # Gradient giảm
    if len(h) < 5: return 'X'
    return 'T' if np.gradient(h[-5:])[-1] < 0 else 'X'

def predict_26(h):  # Chu kỳ 6 phiên
    if len(h) < 6: return 'X'
    return 'T' if h[-1] > h[-6] else 'X'

def predict_27(h):  # Chu kỳ 12 phiên
    if len(h) < 12: return 'X'
    return 'T' if h[-1] > h[-12] else 'X'

def predict_28(h):  # Chu kỳ 24 phiên
    if len(h) < 24: return 'X'
    return 'T' if h[-1] > h[-24] else 'X'

def predict_29(h):  # Đảo chiều sau 5 Tài
    if len(h) < 6: return 'X'
    return 'T' if all(x > 10.5 for x in h[-6:-1]) and h[-1] <= 10.5 else 'X'

def predict_30(h):  # Đảo chiều sau 5 Xỉu
    if len(h) < 6: return 'X'
    return 'T' if all(x <= 10.5 for x in h[-6:-1]) and h[-1] > 10.5 else 'X'

def predict_31(h):  # Độ dốc tuyến tính 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0 else 'X'

def predict_32(h):  # Độ dốc tuyến tính 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0 else 'X'

def predict_33(h):  # Độ dốc tuyến tính 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0 else 'X'

def predict_34(h):  # Độ dốc âm 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0 else 'X'

def predict_35(h):  # Độ dốc âm 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0 else 'X'

def predict_36(h):  # Độ dốc âm 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0 else 'X'

def predict_37(h):  # Độ dốc mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.5 else 'X'

def predict_38(h):  # Độ dốc yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0.2 else 'X'

def predict_39(h):  # Độ dốc mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.3 else 'X'

def predict_40(h):  # Độ dốc yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0.1 else 'X'

def predict_41(h):  # Độ dốc mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.2 else 'X'

def predict_42(h):  # Độ dốc yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < 0.05 else 'X'

def predict_43(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1 else 'X'

def predict_44(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1 else 'X'

def predict_45(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.8 else 'X'

def predict_46(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.8 else 'X'

def predict_47(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.4 else 'X'

def predict_48(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.4 else 'X'

def predict_49(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.25 else 'X'

def predict_50(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.25 else 'X'

def predict_51(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 2 else 'X'

def predict_52(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -2 else 'X'

def predict_53(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1.5 else 'X'

def predict_54(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1.5 else 'X'

def predict_55(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.6 else 'X'

def predict_56(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.6 else 'X'

def predict_57(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.3 else 'X'

def predict_58(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.3 else 'X'

def predict_59(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 3 else 'X'

def predict_60(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -3 else 'X'

def predict_61(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 2 else 'X'

def predict_62(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -2 else 'X'

def predict_63(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.8 else 'X'

def predict_64(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.8 else 'X'

def predict_65(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.4 else 'X'

def predict_66(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.4 else 'X'

def predict_67(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 4 else 'X'

def predict_68(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -4 else 'X'

def predict_69(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 2.5 else 'X'

def predict_70(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -2.5 else 'X'

def predict_71(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1 else 'X'

def predict_72(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1 else 'X'

def predict_73(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.5 else 'X'

def predict_74(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.5 else 'X'

def predict_75(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 5 else 'X'

def predict_76(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -5 else 'X'

def predict_77(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 3 else 'X'

def predict_78(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -3 else 'X'

def predict_79(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1.2 else 'X'

def predict_80(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1.2 else 'X'

def predict_81(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.6 else 'X'

def predict_82(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.6 else 'X'

def predict_83(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 6 else 'X'

def predict_84(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -6 else 'X'

def predict_85(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 3.5 else 'X'

def predict_86(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -3.5 else 'X'

def predict_87(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1.5 else 'X'

def predict_88(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1.5 else 'X'

def predict_89(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.7 else 'X'

def predict_90(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.7 else 'X'

def predict_91(h):  # Độ dốc cực mạnh 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 7 else 'X'

def predict_92(h):  # Độ dốc cực yếu 5 phiên
    if len(h) < 5: return 'X'
    x = np.arange(5)
    y = h[-5:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -7 else 'X'

def predict_93(h):  # Độ dốc cực mạnh 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 4 else 'X'

def predict_94(h):  # Độ dốc cực yếu 10 phiên
    if len(h) < 10: return 'X'
    x = np.arange(10)
    y = h[-10:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -4 else 'X'

def predict_95(h):  # Độ dốc cực mạnh 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 1.8 else 'X'

def predict_96(h):  # Độ dốc cực yếu 20 phiên
    if len(h) < 20: return 'X'
    x = np.arange(20)
    y = h[-20:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -1.8 else 'X'

def predict_97(h):  # Độ dốc cực mạnh 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m > 0.8 else 'X'

def predict_98(h):  # Độ dốc cực yếu 30 phiên
    if len(h) < 30: return 'X'
    x = np.arange(30)
    y = h[-30:]
    m, _ = np.polyfit(x, y, 1)
    return 'T' if m < -0.8 else 'X'

def predict_99(h):  # Ensemble cuối: đa số 100 logic
    if len(h) < 30: return 'X'
    votes = [globals()[f'predict_{i:02d}'](h) for i in range(99)]
    t = votes.count('T')
    return 'T' if t >= 50 else 'X'

# ========== ENSEMBLE ==========
def ensemble_predict(h):
    votes = [globals()[f'predict_{i:02d}'](h) for i in range(100)]
    t = votes.count('T')
    return ('T' if t > 50 else 'X'), round(t / 100, 2)

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
