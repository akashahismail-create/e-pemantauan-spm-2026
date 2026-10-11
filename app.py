import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os, json
from datetime import datetime, date, time
from io import BytesIO

st.set_page_config(page_title="e-Pemantauan Sektor Pentaksiran dan Peperiksaan JPN Selangor Tahun 2026", layout="wide", page_icon="📋")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stDecoration"], div[data-testid="stStatusWidget"], .stAppToolbar {visibility: hidden !important; display: none !important;}
.stApp { background: linear-gradient(180deg, #F8FAFF 0%, #EEF2FF 60%, #F5F7FF 100%) !important; }
div[data-testid="stRadio"] label {
    font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 14.5px !important; font-weight: 700 !important;
    color: #334155 !important; padding: 8px 16px !important; border-radius: 100px !important;
    border: 1.5px solid #E2E8F0 !important; background: white !important;
    transition: all 0.25s ease !important; box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}
div[data-testid="stRadio"] label:hover { color: #0D47A1 !important; background: #EFF6FF !important; border-color: #93C5FD !important; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(13,71,161,0.12) !important; }
div[data-testid="stRadio"] div[role="radiogroup"] { gap: 10px !important; padding: 8px 0 !important; }
div[data-testid="stRadio"] div[data-testid="stWidgetLabel"] + div div[aria-checked="true"] label {
    background: linear-gradient(135deg, #0D47A1 0%, #1976D2 100%) !important; color: white !important; border-color: #0D47A1 !important;
    padding: 9px 18px !important; border-radius: 100px !important; box-shadow: 0 6px 20px rgba(13,71,161,0.35) !important;
}
div[data-testid="stRadio"] div[data-testid="stWidgetLabel"] + div div[aria-checked="true"] label p { color: white !important; }
div[data-testid="stNumberInput"] input, div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {
    border-radius: 12px !important; border: 1.5px solid #E2E8F0 !important; padding: 10px 14px !important;
    font-weight: 600 !important; font-size: 14px !important; background: white !important; box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
div[data-testid="stNumberInput"] input:focus, div[data-testid="stTextInput"] input:focus, div[data-testid="stTextArea"] textarea:focus {
    border-color: #0D47A1 !important; box-shadow: 0 0 0 4px rgba(13,71,161,0.1), 0 4px 12px rgba(13,71,161,0.12) !important;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius: 12px !important; border: 1.5px solid #E2E8F0 !important; background: white !important; }
div[data-testid="stButton"] button { border-radius: 12px !important; font-weight: 700 !important; letter-spacing: 0.3px !important; padding: 10px 20px !important; box-shadow: 0 4px 14px rgba(0,0,0,0.08) !important; transition: all 0.2s ease !important; border: none !important; }
div[data-testid="stButton"] button[kind="primary"] { background: linear-gradient(135deg, #0D47A1 0%, #1976D2 100%) !important; color: white !important; }
div[data-testid="stButton"] button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 24px rgba(13,71,161,0.25) !important; }
div[data-testid="stMetric"] { background: white !important; border-radius: 16px !important; padding: 16px !important; border: 1px solid #EEF2FF !important; box-shadow: 0 4px 20px rgba(13,71,161,0.06) !important; }
.borang-card { background: white; border-radius: 20px; padding: 22px; border: 1px solid #EEF2FF; box-shadow: 0 8px 32px rgba(13,71,161,0.08), 0 1px 3px rgba(0,0,0,0.04); margin: 18px 0; position: relative; overflow: hidden; }
.borang-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #0D47A1 0%, #42A5F5 50%, #FFC107 100%); }
.borang-header { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; padding-bottom: 14px; border-bottom: 2px solid #F1F5F9; }
.borang-header-icon { width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; background: linear-gradient(135deg, #0D47A1 0%, #1976D2 100%); color: white; box-shadow: 0 4px 12px rgba(13,71,161,0.25); }
.borang-header-title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 17px; font-weight: 800; color: #0F172A; letter-spacing: -0.3px; }
.borang-header-subtitle { font-size: 11.5px; color: #64748B; font-weight: 600; margin-top: 2px; }
hr { border: none !important; height: 2px !important; background: linear-gradient(90deg, transparent 0%, #E2E8F0 20%, #CBD5E1 50%, #E2E8F0 80%, transparent 100%) !important; margin: 22px 0 !important; }
.header-biru {
    background: linear-gradient(135deg, #0A1931 0%, #0D2A54 20%, #0D47A1 60%, #1565C0 100%);
    padding: 30px 28px; border-radius: 24px; margin-bottom: 26px;
    box-shadow: 0 20px 60px rgba(13,71,161,0.30); border: 1px solid rgba(255,255,255,0.1); text-align: center; position: relative; overflow: hidden;
}
.header-biru::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #FFC107 0%, #FFD54F 30%, #FFC107 60%, #FFB300 100%); }
.header-biru h1 { color: white; margin: 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; text-shadow: 0 2px 12px rgba(0,0,0,0.3); }
.header-biru h3 { color: #FFECB3; margin: 10px 0 0 0; font-size: 13px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; }
.header-biru h2 { color: white; margin: 16px 0 0 0; font-size: 18px; font-weight: 800; background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); display: inline-block; padding: 9px 22px; border-radius: 100px; border: 1px solid rgba(255,255,255,0.15); }
.header-biru p { color: #BBDEFB; margin: 12px 0 0 0; font-size: 12.5px; font-weight: 500; }
.login-card { background: white; padding: 30px; border-radius: 24px; border: 1px solid #EEF2FF; box-shadow: 0 20px 60px rgba(13,71,161,0.12); position: relative; overflow: hidden; }
.login-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #0D47A1 0%, #42A5F5 50%, #FFC107 100%); }
.login-container { max-width: 520px; margin: 0 auto; }
.login-title { text-align: center; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 22px; }
</style>
""", unsafe_allow_html=True)

st.markdown('''
<div class="header-biru">
    <h1>🏛️ JABATAN PENDIDIKAN NEGERI SELANGOR</h1>
    <h3>SEKTOR PENTAKSIRAN DAN PEPERIKSAAN</h3>
    <h2>📋 e-Pemantauan Sektor Pentaksiran dan Peperiksaan JPN Selangor Tahun 2026</h2>
    <p>🎓 SPM • Amali Sains • Ujian Bertutur BM/BI • STAM • MUET | 10 Daerah Selangor</p>
    <p style="margin-top:10px; font-size:11px; background: rgba(255,255,255,0.12); display:inline-block; padding:6px 14px; border-radius:100px; border:1px solid rgba(255,255,255,0.15);">✨ Created by Akashah Ismail | JPN Selangor 2026 | Versi Cantik & Kemas Ultimate</p>
</div>
''', unsafe_allow_html=True)


all_files = os.listdir('.')
FILE_SPM = FILE_AMALI = None
for f in all_files:
    if f.lower().endswith('.xlsx') and 'v1.1' in f.lower(): FILE_SPM = f
    if f.lower().endswith('.xlsx') and 'amali' in f.lower(): FILE_AMALI = f
if not FILE_SPM:
    for f in all_files:
        if f.lower().endswith('.xlsx') and 'data_v1' in f.lower(): FILE_SPM = f; break

@st.cache_data
def load_spm():
    xl = pd.ExcelFile(FILE_SPM)
    return xl.parse("selenggara_pusat", dtype=str), xl.parse("Jadual_Rasmi_SPM2026", dtype=str)

@st.cache_data
def load_amali():
    xl = pd.ExcelFile(FILE_AMALI)
    df_r = xl.parse("Ringkasan_Makmal", dtype=str)
    df_j = xl.parse("jadual_amali", dtype=str) if "jadual_amali" in xl.sheet_names else pd.DataFrame()
    return df_r, df_j

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = ""
    st.session_state.user_name = ""
    st.session_state.is_admin = False
    st.session_state.is_kppk = False

ADMIN_PASSWORD = "JPN2026"

def login_screen():
    # Muka depan cantik - tanpa peraturan serabut
    _, col_center, _ = st.columns([1,2,1])
    with col_center:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">🔐 e-Pemantauan Sektor Pentaksiran dan Peperiksaan<br>JPN Selangor Tahun 2026</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        role_pilih = st.radio("Log masuk sebagai:", ["👤 Pemantau (PPD/JPN)", "🔑 Admin JPN", "👔 KPPK/Pengarah"], horizontal=True)
        st.divider()
        
        if "Pemantau" in role_pilih:
            nama_login = st.text_input("Nama Pemantau (penuh)", placeholder="Contoh: Akashah Bin Ismail")
            st.caption("Gunakan nama penuh yang sama setiap kali login | Sistem menyokong 600 orang pemantau")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➡️ Masuk sebagai Pemantau", type="primary", use_container_width=True):
                if nama_login.strip() == "":
                    st.error("Sila isi nama pemantau!")
                else:
                    st.session_state.logged_in = True
                    st.session_state.role = "pemantau"
                    st.session_state.user_name = nama_login.strip()
                    st.session_state.is_admin = False
                    st.session_state.is_kppk = False
                    st.success(f"Selamat datang, {nama_login}!")
                    st.rerun()
        elif "Admin" in role_pilih:
            pwd = st.text_input("Kata Laluan Admin", type="password", placeholder="Masukkan password admin")
            st.caption("Hubungi Urus Setia JPN untuk kata laluan")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🔓 Masuk sebagai Admin", type="primary", use_container_width=True):
                if pwd == ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.session_state.role = "admin"
                    st.session_state.user_name = "ADMIN JPN"
                    st.session_state.is_admin = True
                    st.session_state.is_kppk = False
                    st.success("Login Admin berjaya!")
                    st.rerun()
                else:
                    st.error("❌ Password salah!")
        else:  # KPPK/Pengarah
            pwd_kppk = st.text_input("Kata Laluan KPPK/Pengarah", type="password", placeholder="Masukkan password KPPK/Pengarah")
            st.caption("Password sama: JPN2026 | Hanya lihat semua laporan, tidak boleh padam")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("👔 Masuk sebagai KPPK/Pengarah", type="primary", use_container_width=True):
                if pwd_kppk == ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.session_state.role = "kppk"
                    st.session_state.user_name = "KPPK/PENGARAH"
                    st.session_state.is_admin = False
                    st.session_state.is_kppk = True
                    st.success("Login KPPK/Pengarah berjaya! (Lihat semua, tak boleh padam)")
                    st.rerun()
                else:
                    st.error("❌ Password salah!")
        
        st.markdown('<div style="text-align:center; margin-top:20px; padding:12px; background:#F8FAFC; border-radius:10px; border:1px solid #E8EEF6;">', unsafe_allow_html=True)
        st.markdown('<span style="color:#64748B; font-size:11px;">✨ Created by <b style="color:#0D47A1;">Akashah Ismail</b> | JPN Selangor 2026</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    return False


if not st.session_state.logged_in:
    login_screen()
    st.stop()

c_user, c_logout = st.columns([4,1])
with c_user:
    if st.session_state.is_admin:
        st.markdown(f"✅ Login sebagai: **🔑 ADMIN** | **{st.session_state.user_name}** | Boleh PADAM & PADAM SEMUA", unsafe_allow_html=True)
    elif st.session_state.get('is_kppk', False):
        st.markdown(f"✅ Login sebagai: **👔 KPPK/PENGARAH** | **{st.session_state.user_name}** | Lihat SEMUA laporan (Tak boleh padam)", unsafe_allow_html=True)
    else:
        st.markdown(f"✅ Login sebagai: **👤 PEMANTAU** | **{st.session_state.user_name}** | Hanya laporan anda", unsafe_allow_html=True)
with c_logout:
    if st.button("🚪 Log Keluar", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.role = ""
        st.session_state.user_name = ""
        st.session_state.is_admin = False
        st.session_state.is_kppk = False
        st.rerun()

st.markdown("""
<div style="background: linear-gradient(135deg, #0A1931 0%, #0D47A1 50%, #1565C0 100%); padding:18px 24px; border-radius:14px; margin:10px 0; box-shadow: 0 8px 24px rgba(13,71,161,0.25);">
    <div style="display:flex; align-items:center; gap:12px;">
        <div style="background: rgba(255,193,7,0.2); border:1px solid rgba(255,193,7,0.4); color:#FFECB3; font-size:11px; font-weight:800; letter-spacing:1.5px; padding:4px 12px; border-radius:20px;">🏛️ JPN SELANGOR 2026</div>
        <div style="color:#FFC107; font-size:10px; font-weight:700;">● SISTEM RASMI</div>
        <div style="background: rgba(255,255,255,0.15); color:#FFECB3; font-size:9px; font-weight:700; padding:3px 10px; border-radius:20px; border:1px solid rgba(255,193,7,0.3); margin-left:8px;">✨ Created by Akashah Ismail</div>
    </div>
    <div style="color:white; font-size:22px; font-weight:900; margin-top:8px; letter-spacing:0.5px; text-shadow:0 2px 8px rgba(0,0,0,0.3);">e-Pemantauan Sektor Pentaksiran dan Peperiksaan</div>
    <div style="color:#90CAF9; font-size:13px; font-weight:600; margin-top:4px; letter-spacing:0.3px;">Jabatan Pendidikan Negeri Selangor Tahun 2026 | SPM • Amali Sains • Ujian Bertutur BM/BI • STAM • MUET</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ===== KPPK/PENGARAH - TANPA BORANG, HANYA PILIH PEPERIKSAAN & TARIKH - LAPORAN SAMA FORMAT 100% DENGAN ADMIN/PEMANTAU (FIX FINAL KASHAH) =====
if st.session_state.get('is_kppk', False):
    st.markdown("<div style='background: linear-gradient(135deg, #4A148C 0%, #7B1FA2 100%); padding:18px 22px; border-radius:14px; margin-bottom:16px;'><div style='display:flex; align-items:center; gap:10px;'><div style='background: rgba(255,255,255,0.2); padding:8px 14px; border-radius:20px; font-size:12px; font-weight:800; color:white;'>KPPK / PENGARAH</div><div style='color:#E1BEE7; font-size:11px; font-weight:700;'>MOD LIHAT SAHAJA - Tiada Borang</div></div><div style='color:white; font-size:18px; font-weight:800; margin-top:10px;'>Papan Pemuka Laporan - Pilih Peperiksaan</div><div style='color:#CE93D8; font-size:12px; margin-top:4px;'>Pilih peperiksaan - Pilih tarikh - Format sama 100% dengan Admin & Pemantau</div></div>", unsafe_allow_html=True)
    
    jenis_kppk = st.radio("Pilih Peperiksaan untuk Lihat Laporan:", ["1. Pemantauan SPM", "2. Pemantauan Amali Sains", "3. Ujian Bertutur BM", "4. Ujian Bertutur BI", "5. STAM", "6. MUET"], horizontal=True)
    
    if "1. Pemantauan SPM" in jenis_kppk:
        FILE_LAP_KPPK = "laporan_spm_504.json"
        MODE_KPPK = "SPM"
    elif "2. Pemantauan Amali" in jenis_kppk:
        FILE_LAP_KPPK = "laporan_amali_473.json"
        MODE_KPPK = "AMALI"
    elif "3. Ujian Bertutur BM" in jenis_kppk:
        FILE_LAP_KPPK = "laporan_ubbm.json"
        MODE_KPPK = "UBBM"
    elif "4. Ujian Bertutur BI" in jenis_kppk:
        FILE_LAP_KPPK = "laporan_ubbi.json"
        MODE_KPPK = "UBBI"
    elif "5. STAM" in jenis_kppk:
        FILE_LAP_KPPK = "laporan_stam.json"
        MODE_KPPK = "STAM"
    else:
        FILE_LAP_KPPK = "laporan_muet.json"
        MODE_KPPK = "MUET"
    
    def load_laporan_kppk():
        if os.path.exists(FILE_LAP_KPPK):
            try:
                with open(FILE_LAP_KPPK, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []
    
    lap_list_kppk = load_laporan_kppk()
    st.divider()
    st.markdown(f"#### Laporan {MODE_KPPK} - KPPK/Pengarah (Format Sama 100% Admin)")
    
    if not lap_list_kppk:
        st.info(f"Belum ada laporan {MODE_KPPK} dalam sistem.")
        st.stop()
    
    c1,c2,c3 = st.columns(3)
    with c1: st.metric(f"Jumlah Laporan {MODE_KPPK}", len(lap_list_kppk))
    with c2: 
        tarikh_unique = len(set([l.get('tarikh_lawatan','') for l in lap_list_kppk]))
        st.metric("Bilangan Tarikh", tarikh_unique)
    with c3:
        pemantau_unique = len(set([l.get('nama_pemantau','') for l in lap_list_kppk]))
        st.metric("Bilangan Pemantau", pemantau_unique)
    
    from collections import Counter
    tarikh_all = [l.get('tarikh_lawatan','') for l in lap_list_kppk]
    counter_tarikh = Counter(tarikh_all)
    unique_tarikh = sorted(set(tarikh_all), reverse=True)
    tarikh_options = ["Semua Tarikh"] + [f"{t} ({counter_tarikh[t]} laporan)" for t in unique_tarikh if t]
    pilih_tarikh_raw = st.selectbox(f"Pilih Tarikh Pemantauan {MODE_KPPK} ({len(unique_tarikh)} tarikh, {len(lap_list_kppk)} laporan):", tarikh_options)
    
    if pilih_tarikh_raw == "Semua Tarikh":
        filtered_kppk = lap_list_kppk
    else:
        tarikh_selected = pilih_tarikh_raw.split(" (")[0]
        filtered_kppk = [l for l in lap_list_kppk if l.get('tarikh_lawatan','') == tarikh_selected]
    
    filtered_kppk = sorted(filtered_kppk, key=lambda x: (x.get('tarikh_lawatan',''), x.get('masa_lawatan',''), x.get('no_pusat','')))
    st.write(f"Menunjukkan {len(filtered_kppk)} laporan untuk {pilih_tarikh_raw}")
    
    if len(filtered_kppk) > 1:
        pilihan_labels = []
        for l in filtered_kppk:
            mp_short = l.get('mata_pelajaran','')[:35]
            pilihan_labels.append(f"{l.get('no_pusat','')} | {l.get('nama_sekolah','')[:25]} | {l.get('masa_lawatan','')} | {mp_short} | {l.get('nama_pemantau','')[:15]}")
        idx_pilih = st.selectbox(f"Pilih Laporan {MODE_KPPK} - {pilih_tarikh_raw}:", range(len(filtered_kppk)), format_func=lambda i: pilihan_labels[i])
        sel = filtered_kppk[idx_pilih]
    else:
        sel = filtered_kppk[0]
        st.success(f"{sel['no_pusat']} | {sel['nama_sekolah']} | {sel['tarikh_lawatan']} {sel.get('masa_lawatan','')} | {sel['mata_pelajaran'][:40]}")
    
    MODE = MODE_KPPK
    
    def badge(text, bg="#E3F2FD", color="#0D47A1"):
        return f'<span style="display:inline-block; background:{bg}; color:{color}; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; margin:1px;">{text}</span>'

    b_kebal = sel.get('bilik_kebal_penyelia','')
    if b_kebal and "Penyelia Kawasan" in str(sel.get('jawatan_pemantau','')):
        pemantau_html = f" {sel['nama_pemantau']} | {badge(sel['jawatan_pemantau'], '#0D47A1', 'white')} {badge(sel['daerah_pemantau'], '#E0E7FF', '#4338CA')} {badge(f'Bilik Kebal: {b_kebal}', '#FFF3E0', '#EF6C00')}"
    else:
        pemantau_html = f" {sel.get('nama_pemantau','')} | {badge(sel.get('jawatan_pemantau',''), '#0D47A1', 'white')} {badge(sel.get('daerah_pemantau',''), '#E0E7FF', '#4338CA')}"

    b_pep = sel.get('bilik_peperiksaan',0)
    b_kuar = sel.get('bilik_kuarantin',0)
    b_sakit = sel.get('bilik_sakit',0)
    b_dewan = sel.get('dewan',0)
    b_total = sel.get('total_bilik',0)
    b_makmal = sel.get('bilik_makmal',0)
    b_makmal_ujian = sel.get('bilik_makmal_ujian', sel.get('bilik_peperiksaan',0))
    b_persediaan = sel.get('bilik_persediaan',0)
    b_sidang = sel.get('sidang_no','')
    b_ujian = sel.get('bilik_ujian',0)
    b_menunggu = sel.get('bilik_menunggu', sel.get('bilik_lapor',0))
    b_petugas = sel.get('petugas',0)
    b_kelas = sel.get('bilik_kelas',0)
    c_berdaftar = sel.get('calon_berdaftar',0)
    c_hadir = sel.get('calon_hadir',0)
    c_th = sel.get('calon_tidak_hadir',0)
    c_cicir = sel.get('calon_cicir',0)
    c_bantah = sel.get('calon_bantah',0)
    c_menumpang = sel.get('calon_menumpang',0)
    c_keseluruhan = sel.get('calon_keseluruhan',0)
    c_hari = sel.get('hari','')

    if MODE in ["SPM"]:
        bilik_html = f"{badge(f'Pep: {b_pep}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Sakit: {b_sakit}', '#FCE4EC', '#C2185B')} {badge(f'Dewan: {b_dewan}', '#E3F2FD', '#1565C0')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
        calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Cicir: {c_cicir}', '#FFF3E0', '#EF6C00')} {badge(f'Bantah: {c_bantah}', '#F3E5F5', '#6A1B9A')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
        petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"
    elif MODE=="AMALI":
        b_kuar_amali = sel.get('bilik_kuarantin', 0)
        b_bilangan_sidang = sel.get('bilangan_sidang', sel.get('total_bilik', 0))
        b_sidang_lawatan = sel.get('sidang_lawatan', sel.get('sidang_no',''))
        bilik_html = f"{badge(f'Makmal: {b_makmal}', '#E8F5E9', '#2E7D32')} {badge(f'Bilik Ujian: {b_makmal_ujian}', '#E3F2FD', '#1565C0')} {badge(f'Persediaan: {b_persediaan}', '#FFF3E0', '#EF6C00')} {badge(f'Kuarantin: {b_kuar_amali}', '#FFEBEE', '#C62828')} {badge(f'Bil Sidang: {b_bilangan_sidang}', '#E0F7FA', '#006064')} {badge(f'Lawatan Sidang: {b_sidang_lawatan}', '#F3E5F5', '#6A1B9A')} {badge(f'Total Bilik: {b_total}', '#0D47A1', 'white')}"
        calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
        petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Petugas Makmal Amali', '#E0F7FA', '#006064')}"
    elif MODE in ["UBBM","UBBI"]:
        bilik_html = f"{badge(f'Bilik Menunggu: {b_menunggu}', '#E3F2FD', '#1565C0')} {badge(f'Bilik Ujian: {b_ujian}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Sidang Dipantau: {b_sidang}', '#E0F2F1', '#00695C')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
        petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"
        calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Hari: {c_hari}', '#FFF8E1', '#F57F17')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
    else:
        bilik_html = f"{badge(f'Kelas/Dewan: {b_kelas}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
        calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Menumpang: {c_menumpang}', '#E0F7FA', '#006064')} {badge(f'Cicir: {c_cicir}', '#FFF3E0', '#EF6C00')} {badge(f'Bantah: {c_bantah}', '#F3E5F5', '#6A1B9A')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
        petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"

    jenis_label = sel.get('jenis','SPM')
    if jenis_label=="UBBM":
        jenis_label_full = "UJIAN BERTUTUR BAHASA MELAYU"
        jenis_icon = "BM"
    elif jenis_label=="UBBI":
        jenis_label_full = "UJIAN BERTUTUR BAHASA INGGERIS"
        jenis_icon = "BI"
    elif jenis_label=="STAM":
        jenis_label_full = "STAM"
        jenis_icon = "STAM"
    elif jenis_label=="MUET":
        jenis_label_full = "MUET"
        jenis_icon = "MUET"
    elif jenis_label=="AMALI":
        jenis_label_full = "AMALI SAINS SPM 2026"
        jenis_icon = "AMALI"
    else:
        jenis_label_full = "SPM 2026"
        jenis_icon = "SPM"

    IMG_D = IMG_DEWAN_B64 if 'IMG_DEWAN_B64' in globals() else ""
    IMG_S = IMG_SEKOLAH_B64 if 'IMG_SEKOLAH_B64' in globals() else ""

    def buat_carta_pai_html_kppk(sel_data):
        try:
            hadir = int(sel_data.get('calon_hadir',0) or 0)
            th = int(sel_data.get('calon_tidak_hadir',0) or 0)
            total = hadir + th
            if total == 0: total = 1
            pct_hadir = int(hadir/total*100) if total else 0
            pct_th = 100 - pct_hadir
            return f'<div style="text-align:center;"><div style="width:90px; height:90px; border-radius:50%; background: conic-gradient(#4CAF50 0% {pct_hadir}%, #EF5350 {pct_hadir}% 100%); margin:0 auto;"></div><div style="font-size:10px; margin-top:8px;"><span style="color:#4CAF50;">Hadir {pct_hadir}%</span> <span style="color:#EF5350; margin-left:8px;">TH {pct_th}%</span></div></div>'
        except:
            return '<div style="text-align:center; font-size:10px; color:#999;">Carta</div>'
    
    CHART_PAI_HTML = buat_carta_pai_html_kppk(sel)

    if MODE=="SPM":
        table_rows = f"<tr style='background:#F8FAFC; border-bottom:2px solid #E8EEF6;'><td style='padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;'>NAMA PUSAT / SEKOLAH (SPM)</td><td style='padding:11px 14px; font-weight:700; font-size:13px;'>{sel['nama_sekolah']}</td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;'>NO PUSAT / DAERAH</td><td style='padding:10px 14px;'><b style='color:#0D47A1;'>{sel['no_pusat']}</b> <span style='margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;'>{sel.get('kod_ppd','')}</span></td></tr><tr style='background:#FAFBFC; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;'>TARIKH, HARI & MP</td><td style='padding:10px 14px;'><span style='background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;'>{sel['tarikh_lawatan']}</span> <span style='background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;'>{sel['masa_lawatan']}</span> <b style='color:#0D47A1; margin-left:8px;'>{sel['mata_pelajaran']}</b></td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;'>BILIK PEPERIKSAAN SPM</td><td style='padding:10px 14px;'>{bilik_html}</td></tr><tr style='background:#FFF3E0; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;'>KEHADIRAN PETUGAS SPM</td><td style='padding:10px 14px;'>{petugas_html}</td></tr><tr style='background:#FAFBFC; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;'>KEHADIRAN CALON SPM</td><td style='padding:10px 14px;'>{calon_html}</td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;'>ULASAN PEMANTAUAN SPM</td><td style='padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;'>{sel['ulasan'] or 'Tiada ulasan'}</td></tr><tr style='background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);'><td style='padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;'>PEMANTAU SPM</td><td style='padding:11px 14px; font-weight:600;'>{pemantau_html}</td></tr>"
    else:
        table_rows = f"<tr style='background:#F8FAFC; border-bottom:2px solid #E8EEF6;'><td style='padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px;'>NAMA PUSAT / SEKOLAH ({MODE})</td><td style='padding:11px 14px; font-weight:700;'>{sel['nama_sekolah']}</td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; background:#FAFBFC;'>NO PUSAT / DAERAH</td><td style='padding:10px 14px;'><b>{sel['no_pusat']}</b> {sel.get('kod_ppd','')}</td></tr><tr style='background:#FAFBFC; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569;'>TARIKH, HARI & MP</td><td style='padding:10px 14px;'>{sel['tarikh_lawatan']} {sel['masa_lawatan']} {sel['mata_pelajaran']}</td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; background:#FAFBFC;'>BILIK ({MODE})</td><td style='padding:10px 14px;'>{bilik_html}</td></tr><tr style='background:#FFF3E0; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:800; color:#EF6C00;'>KEHADIRAN PETUGAS {MODE}</td><td style='padding:10px 14px;'>{petugas_html}</td></tr><tr style='background:#FAFBFC; border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569;'>KEHADIRAN CALON UNTUK SIDANG DIPANTAU</td><td style='padding:10px 14px;'>{calon_html}</td></tr><tr style='border-bottom:1px solid #F1F5F9;'><td style='padding:11px 14px; font-weight:700; color:#475569; background:#FAFBFC;'>ULASAN</td><td style='padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;'>{sel['ulasan'] or 'Tiada ulasan'}</td></tr><tr style='background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);'><td style='padding:11px 14px; font-weight:800; color:#0D47A1;'>PEMANTAU</td><td style='padding:11px 14px; font-weight:600;'>{pemantau_html}</td></tr>"

    html_one = f"""
<div style="width:100%; display:flex; justify-content:center; padding:12px 8px; background: linear-gradient(135deg, #EEF2F7 0%, #E3EAF3 100%);">
    <div style="width:100%; max-width:860px; background:white; border-radius:20px; overflow:hidden; box-shadow: 0 20px 60px rgba(13,71,161,0.18); border:1px solid white; position:relative;">
        <div style="height:5px; background: linear-gradient(90deg, #FFC107 0%, #FFD54F 50%, #FFC107 100%);"></div>
        <div style="background: linear-gradient(135deg, #0A1931 0%, #0D47A1 45%, #1565C0 100%); padding:22px 26px; display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1;">
                <div style="background: rgba(255,193,7,0.2); color:#FFECB3; font-size:10px; font-weight:800; padding:3px 10px; border-radius:20px; display:inline-block; margin-bottom:6px;">{jenis_icon} SEKTOR PENTAKSIRAN & PEPERIKSAAN - {MODE}</div>
                <div style="color:white; font-size:20px; font-weight:900;">JABATAN PENDIDIKAN NEGERI SELANGOR</div>
                <div style="color:#90CAF9; font-size:11px; font-weight:700; margin-top:6px;">LAPORAN PEMANTAUAN {jenis_label_full} - {sel['tarikh_lawatan']} - {sel['masa_lawatan']}</div>
            </div>
            <div style="text-align:right; margin-left:20px;">
                <div style="background:white; color:#0D2A54; font-size:20px; font-weight:900; padding:10px 18px; border-radius:12px;">{sel['no_pusat']}</div>
                <div style="color:#FFECB3; font-size:9px; font-weight:700; margin-top:7px; text-align:center;">NO. PUSAT {MODE}</div>
            </div>
        </div>
        <div style="padding:18px; background:#F8FAFC;">
            <div style="display:flex; gap:14px;">
                <div style="flex:1.25; position:relative; border-radius:14px; overflow:hidden; height:195px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border:2px solid white;">
                    <img src="data:image/jpeg;base64,{IMG_D}" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:0; left:0; right:0; padding:12px; background: linear-gradient(transparent, rgba(0,0,0,0.7));">
                        <div style="color:white; font-size:11px; font-weight:800;">DEWAN / BILIK {MODE}</div>
                    </div>
                </div>
                <div style="flex:1.25; position:relative; border-radius:14px; overflow:hidden; height:195px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border:2px solid white;">
                    <img src="data:image/jpeg;base64,{IMG_S}" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:0; left:0; right:0; padding:12px; background: linear-gradient(transparent, rgba(0,0,0,0.7));">
                        <div style="color:white; font-size:11px; font-weight:800;">BANGUNAN {MODE}</div>
                    </div>
                </div>
                <div style="flex:0.95; background:white; border-radius:14px; padding:14px 12px; box-shadow: 0 8px 24px rgba(13,71,161,0.1); border:1px solid #E8EEF6; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    {CHART_PAI_HTML}
                </div>
            </div>
        </div>
        <div style="padding:0 18px 18px;">
            <div style="background:white; border-radius:14px; overflow:hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border:1px solid #E8EEF6;">
                <table style="width:100%; border-collapse:collapse; font-size:12.5px;">
                    {table_rows}
                </table>
            </div>
        </div>
        <div style="padding:20px 26px; background:#F1F5F9; border-top:1px solid #E2E8F0; display:flex; justify-content:space-between; gap:24px;">
            <div style="text-align:center; flex:1; border-top:2px solid #0D47A1; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#0D47A1;">PEMANTAU</div>
                <div style="font-size:12px; font-weight:700; margin-top:4px;">{sel['nama_pemantau']}</div>
                <div style="font-size:9px; color:#64748B;">{sel['tarikh_submit']}</div>
            </div>
            <div style="text-align:center; flex:1; border-top:2px dashed #94A3B8; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#475569;">COP SEKOLAH / PUSAT</div>
                <div style="font-size:12px; font-weight:700; margin-top:4px;">{sel['no_pusat']}</div>
            </div>
            <div style="text-align:center; flex:1; border-top:2px solid #0D47A1; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#0D47A1;">PENGESAHAN JPN / PPD</div>
                <div style="font-size:9px; color:#64748B; margin-top:12px;">Tandatangan & Cop Rasmi</div>
            </div>
        </div>
        <div style="background: linear-gradient(90deg, #0D47A1 0%, #1565C0 100%); padding:10px 26px; display:flex; justify-content:space-between;">
            <div style="color:rgba(255,255,255,0.8); font-size:9px;">2026 JPN Selangor | e-Pemantauan - SPM, Amali, Ujian Bertutur, STAM & MUET | Created by Akashah Ismail</div>
            <div style="color:#A5D6A7; font-size:9px;">SAH & DIREKODKAN | KPPK VIEW - SAMA FORMAT ADMIN 100%</div>
        </div>
        <div style="height:5px; background: linear-gradient(90deg, #FFC107 0%, #FFD54F 50%, #FFC107 100%);"></div>
        <div style="background:#0A1931; padding:8px; text-align:center;">
            <span style="color:#FFECB3; font-size:10px; letter-spacing:0.5px;">Created by <b style="color:white;">Akashah Ismail</b> | Sektor Pentaksiran & Peperiksaan JPN Selangor | 2026</span>
        </div>
    </div>
</div>
"""

    components.html(html_one, height=740, scrolling=True)
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        full_html = f"<html><head><meta charset='utf-8'></head><body>{html_one}</body></html>"
        st.download_button("Cetak PDF / Cetak (KPPK - Sama Format Admin)", full_html, file_name=f"Laporan_{MODE}_{sel['no_pusat']}_{sel['tarikh_lawatan']}_KPPK_SAMA_ADMIN.html", mime="text/html", use_container_width=True, type="primary")
    with c2:
        df_one = pd.DataFrame([sel])
        out = BytesIO()
        with pd.ExcelWriter(out, engine='openpyxl') as writer: df_one.to_excel(writer, index=False)
        st.download_button("Download Excel (KPPK)", out.getvalue(), file_name=f"{MODE}_{sel['no_pusat']}_KPPK.xlsx", use_container_width=True)
    st.success("Format laporan KPPK/Pengarah SAMA 100% dengan format Admin & Pemantau!")
    st.info("KPPK/Pengarah - Mod Lihat Sahaja - Tiada borang Maklumat Pusat, tiada akses padam - Hanya pilih peperiksaan & tarikh - Format SAMA 100%")
    st.stop()

jenis = st.radio("", ["1. Pemantauan SPM", "2. Pemantauan Amali Sains", "3. Ujian Bertutur BM", "4. Ujian Bertutur BI", "5. STAM", "6. MUET"], horizontal=True, label_visibility="collapsed")


if "1. Pemantauan SPM" in jenis:
    df_pusat, df_jadual = load_spm()
    df_jadual["TARIKH_CLEAN"] = df_jadual["TARIKH"].astype(str).str.extract(r"(\d{4}-\d{2}-\d{2})")
    df_jadual["MP_CLEAN"] = df_jadual["MATA PELAJARAN"].astype(str).str.replace("\n", " ").str.strip()
    SENARAI_TARIKH = sorted(df_jadual["TARIKH_CLEAN"].dropna().unique().tolist())
    MODE = "SPM"
    df_ringkas = df_pusat
elif "2. Pemantauan Amali" in jenis:
    df_ringkas, df_jadual_amali = load_amali()
    df_jadual_amali["tarikh_clean"] = df_jadual_amali["tarikh"].astype(str).str.replace(",", ".").str.strip()
    def parse_t(t):
        try:
            if "." in t:
                d,m,y = t.split(".")
                return f"{y}-{m.zfill(2)}-{d.zfill(2)}"
            return t
        except:
            return t
    df_jadual_amali["tarikh_iso"] = df_jadual_amali["tarikh_clean"].apply(parse_t)
    df_jadual_amali["mp_clean"] = df_jadual_amali["mata_pelajaran"].astype(str).str.title() + " (" + df_jadual_amali["kod_mata_pelajaran"].astype(str) + "/" + df_jadual_amali["kertas"].astype(str) + ")"
    SENARAI_TARIKH = sorted(df_jadual_amali["tarikh_iso"].dropna().unique().tolist())
    MODE = "AMALI"
    df_pusat, _ = load_spm()
elif "3. Ujian Bertutur BM" in jenis:
    df_pusat, _ = load_spm()
    # UBBM - Oktober, November, Disember 2026 (ikut arahan Kashah)
    SENARAI_TARIKH = ['2026-10-01', '2026-10-02', '2026-10-05', '2026-10-06', '2026-10-07', '2026-10-08', '2026-10-09', '2026-10-12', '2026-10-13', '2026-10-14', '2026-10-15', '2026-10-16', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23', '2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-16', '2026-11-17', '2026-11-18', '2026-11-19', '2026-11-20', '2026-11-23', '2026-11-24', '2026-11-25', '2026-11-26', '2026-11-27', '2026-11-30', '2026-12-01', '2026-12-02', '2026-12-03', '2026-12-04', '2026-12-07', '2026-12-08', '2026-12-09', '2026-12-10', '2026-12-11', '2026-12-14', '2026-12-15', '2026-12-16', '2026-12-17', '2026-12-18']
    MODE = "UBBM"
    df_ringkas = df_pusat
    df_jadual_amali = pd.DataFrame()
elif "4. Ujian Bertutur BI" in jenis:
    df_pusat, _ = load_spm()
    # UBBI - Oktober, November, Disember 2026 (ikut arahan Kashah)
    SENARAI_TARIKH = ['2026-10-01', '2026-10-02', '2026-10-05', '2026-10-06', '2026-10-07', '2026-10-08', '2026-10-09', '2026-10-12', '2026-10-13', '2026-10-14', '2026-10-15', '2026-10-16', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23', '2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-16', '2026-11-17', '2026-11-18', '2026-11-19', '2026-11-20', '2026-11-23', '2026-11-24', '2026-11-25', '2026-11-26', '2026-11-27', '2026-11-30', '2026-12-01', '2026-12-02', '2026-12-03', '2026-12-04', '2026-12-07', '2026-12-08', '2026-12-09', '2026-12-10', '2026-12-11', '2026-12-14', '2026-12-15', '2026-12-16', '2026-12-17', '2026-12-18']
    MODE = "UBBI"
    df_ringkas = df_pusat
    df_jadual_amali = pd.DataFrame()
elif "5. STAM" in jenis:
    df_pusat, _ = load_spm()
    # STAM - 1 OKTOBER HINGGA 31 OKTOBER 2026 SAHAJA (ikut arahan terbaru Kashah - bukan November)
    SENARAI_TARIKH = ["2026-10-01","2026-10-02","2026-10-03","2026-10-04","2026-10-05","2026-10-06","2026-10-07","2026-10-08","2026-10-09","2026-10-10","2026-10-11","2026-10-12","2026-10-13","2026-10-14","2026-10-15","2026-10-16","2026-10-17","2026-10-18","2026-10-19","2026-10-20","2026-10-21","2026-10-22","2026-10-23","2026-10-24","2026-10-25","2026-10-26","2026-10-27","2026-10-28","2026-10-29","2026-10-30","2026-10-31"]
    MODE = "STAM"
    df_ringkas = df_pusat
    df_jadual_amali = pd.DataFrame()
else:  # MUET - SEMUA BULAN
    df_pusat, _ = load_spm()
    SENARAI_TARIKH = [
        "2026-01-10","2026-01-11","2026-01-17","2026-01-18",
        "2026-02-07","2026-02-08","2026-02-14","2026-02-15",
        "2026-03-08","2026-03-09","2026-03-14","2026-03-15","2026-03-16",
        "2026-04-11","2026-04-12","2026-04-18","2026-04-19",
        "2026-05-09","2026-05-10","2026-05-16","2026-05-17",
        "2026-06-06","2026-06-07","2026-06-13","2026-06-14",
        "2026-07-11","2026-07-12","2026-07-13","2026-07-18","2026-07-19",
        "2026-08-08","2026-08-09","2026-08-15","2026-08-16",
        "2026-09-12","2026-09-13","2026-09-19","2026-09-20",
        "2026-10-10","2026-10-11","2026-10-17","2026-10-18",
        "2026-11-07","2026-11-08","2026-11-09","2026-11-14","2026-11-15","2026-11-16",
        "2026-12-05","2026-12-06","2026-12-12","2026-12-13"
    ]
    MODE = "MUET"
    df_ringkas = df_pusat
    df_jadual_amali = pd.DataFrame()

if MODE=="SPM":
    FILE_LAP = "laporan_spm_504.json"
elif MODE=="AMALI":
    FILE_LAP = "laporan_amali_473.json"
elif MODE=="UBBM":
    FILE_LAP = "laporan_ubbm.json"
elif MODE=="UBBI":
    FILE_LAP = "laporan_ubbi.json"
elif MODE=="STAM":
    FILE_LAP = "laporan_stam.json"
else:
    FILE_LAP = "laporan_muet.json"

def load_laporan():
    if os.path.exists(FILE_LAP):
        try:
            with open(FILE_LAP, "r", encoding="utf-8") as f: return json.load(f)
        except: return []
    return []

def save_all_laporan(list_data):
    with open(FILE_LAP, "w", encoding="utf-8") as f: json.dump(list_data, f, ensure_ascii=False, indent=2)

def save_laporan(data):
    ex = load_laporan(); ex.append(data); save_all_laporan(ex)

# KOD DAERAH RASMI - BA hingga BK (10 daerah utama Selangor)
KOD_DAERAH_MAP = {
    "BA": "KLANG",
    "BB": "KUALA LANGAT",
    "BC": "KUALA SELANGOR",
    "BD": "HULU LANGAT",
    "BE": "HULU SELANGOR",
    "BF": "SABAK BERNAM",
    "BG": "GOMBAK",
    "BH": "PETALING PERDANA",
    "BJ": "SEPANG",
    "BK": "PETALING UTAMA",
    # Kod tambahan / alias (untuk filter data lama)
    "BL": "PETALING UTAMA",
    "BM": "KLANG",
    "BN": "GOMBAK",
    "A": "KLANG",
    "J": "SEPANG",
}

# Reverse map: Nama Daerah -> List Kod (untuk filter tepat)
NAMA_KE_KOD_MAP = {
    "KLANG": ["BA", "BM", "A"],
    "KUALA LANGAT": ["BB"],
    "KUALA SELANGOR": ["BC"],
    "HULU LANGAT": ["BD"],
    "HULU SELANGOR": ["BE"],
    "SABAK BERNAM": ["BF"],
    "GOMBAK": ["BG", "BN"],
    "PETALING PERDANA": ["BH"],
    "SEPANG": ["BJ", "J"],
    "PETALING UTAMA": ["BK", "BL"],
}

# Senarai 10 daerah sahaja - papar nama sahaja, tak payah kod (BA, BJ etc)
DAERAH_LIST = ["KLANG", "KUALA LANGAT", "KUALA SELANGOR", "HULU LANGAT", "HULU SELANGOR", "SABAK BERNAM", "GOMBAK", "PETALING PERDANA", "SEPANG", "PETALING UTAMA"]
def kod_to_daerah(kod):
    if not kod:
        return ""
    kod = str(kod).strip().upper()
    # Kod penuh (BA, BB etc)
    if kod in KOD_DAERAH_MAP:
        return KOD_DAERAH_MAP[kod]
    # Ambil 2 huruf pertama
    k2 = kod[:2]
    if k2 in KOD_DAERAH_MAP:
        return KOD_DAERAH_MAP[k2]
    # Jika dah nama daerah terus
    if kod in DAERAH_LIST:
        return kod
    return kod

def get_nama_daerah_from_pusat(no_pusat, kod_ppd=""):
    if kod_ppd:
        nama = kod_to_daerah(kod_ppd)
        if nama != kod_ppd:
            return nama
        # Jika kod_ppd sudah nama daerah
        if kod_ppd.upper() in DAERAH_LIST:
            return kod_ppd.upper()
    if no_pusat:
        k = str(no_pusat).strip().upper()
        huruf = "".join([c for c in k if c.isalpha()])[:2]
        if huruf:
            nama = kod_to_daerah(huruf)
            if nama in DAERAH_LIST:
                return nama
            return nama
    return kod_ppd or ""

def daerah_to_kod_list(nama_daerah):
    nama_daerah = str(nama_daerah).strip().upper()
    return NAMA_KE_KOD_MAP.get(nama_daerah, [])

DAERAH_LIST = ["Petaling Perdana","Petaling Utama","Hulu Langat","Gombak","Klang","Kuala Langat","Kuala Selangor","Hulu Selangor","Sabak Bernam","Sepang"]

st.markdown('<div class="borang-card"><div class="borang-header"><div class="borang-header-icon">🏫</div><div><div class="borang-header-title">Maklumat Pusat Peperiksaan</div><div class="borang-header-subtitle">Pilih Daerah → Sekolah → No Pusat</div></div></div>', unsafe_allow_html=True)
if MODE in ["STAM","MUET"]:
    st.caption(f"📌 {MODE} - Pusat Tak Sama SPM - Isi Sendiri | Daerah/PPD Tetap Pilih")
else:
    st.caption("1️⃣ Pilih Daerah/PPD → 2️⃣ Pilih Sekolah (auto filter) → 3️⃣ Pilih No Pusat")

# Pilihan Daerah - hanya 10 nama daerah, tak payah kod (BA, BJ etc) - ikut arahan Kashah
daerah_options = ["-- Pilih Daerah --"] + DAERAH_LIST

col_d, col_s, col_p = st.columns([1,2,1])
pilih_daerah = col_d.selectbox("1️⃣ Daerah / PPD", daerah_options)

# ===== UNTUK STAM - ISI SENDIRI, TAK PERLU PILIHAN =====
if MODE in ["STAM","MUET"]:
    pilih_nama = col_s.text_input(f"2️⃣ Nama Pusat {MODE} (Isi Sendiri)", placeholder="Contoh: SMKA ... / Pusat STAM ...")
    pilih_no = col_p.text_input(f"3️⃣ No Pusat {MODE} (Isi Sendiri)", placeholder="Contoh: BC001 / ST001")
    # Kod PPD ambil dari pilihan daerah - map nama ke kod pertama (case-insensitive)
    daerah_upper = pilih_daerah.strip().upper() if pilih_daerah != "-- Pilih Daerah --" else ""
    if daerah_upper and daerah_upper in NAMA_KE_KOD_MAP:
        kod_ppd = NAMA_KE_KOD_MAP[daerah_upper][0]
    else:
        kod_ppd = pilih_daerah if pilih_daerah!="-- Pilih Daerah --" else ""
    bil_calon = ""
    df_by_daerah = df_pusat
    nama_list = []
    no_opts = []
    st.info(f"📝 {MODE} - Pusat & No Pusat diisi manual oleh pemantau (tak sama dengan SPM)")
else:
    # SPM, AMALI, UBBM, UBBI - pakai dropdown dengan filter TEPAT ikut daerah sahaja (FIX case-insensitive)
    if pilih_daerah != "-- Pilih Daerah --":
        df_by_daerah = pd.DataFrame()
        # Lookup case-insensitive - kunci dalam map adalah UPPER
        daerah_upper = pilih_daerah.strip().upper()
        kod_list = NAMA_KE_KOD_MAP.get(daerah_upper, [pilih_daerah])
        
        # 1. Cuba filter ikut Kod_PPD = kod (BA, BE etc)
        if "Kod_PPD" in df_pusat.columns:
            mask_kod = df_pusat["Kod_PPD"].astype(str).str.strip().str.upper().isin([k.upper() for k in kod_list])
            df_by_daerah = df_pusat[mask_kod]
            
            # 2. Jika tak jumpa, cuba filter Kod_PPD = nama daerah terus (HULU SELANGOR)
            if df_by_daerah.empty:
                mask_nama = df_pusat["Kod_PPD"].astype(str).str.strip().str.upper() == daerah_upper
                df_by_daerah = df_pusat[mask_nama]
        
        # 3. Jika masih kosong, cuba filter ikut No_Pusat (kod dari No Pusat - BEA... -> HULU SELANGOR)
        if df_by_daerah.empty and "No_Pusat" in df_pusat.columns:
            try:
                def match_daerah(no_pusat):
                    try:
                        return kod_to_daerah(str(no_pusat)).upper() == daerah_upper
                    except:
                        return False
                mask_no = df_pusat["No_Pusat"].apply(match_daerah)
                df_by_daerah = df_pusat[mask_no]
            except:
                pass
        
        # 4. Jika masih kosong, cuba cari column Daerah / PPD / Nama_PPD jika ada
        if df_by_daerah.empty:
            for col in ["Daerah", "PPD", "Nama_PPD", "Daerah_PPD", "Nama_Daerah"]:
                if col in df_pusat.columns:
                    mask_col = df_pusat[col].astype(str).str.strip().str.upper().str.contains(daerah_upper, na=False)
                    if mask_col.any():
                        df_by_daerah = df_pusat[mask_col]
                        break
        
        # 5. Jika masih kosong juga, baru papar amaran dan kosongkan list
        if df_by_daerah.empty:
            st.error(f"⚠️ Tiada sekolah ditemui untuk {pilih_daerah} (Kod: {', '.join(kod_list)}). Semak fail Excel selenggara_pusat. Kod_PPD dalam Excel: {df_pusat['Kod_PPD'].dropna().unique()[:10].tolist() if 'Kod_PPD' in df_pusat.columns else 'tiada'}")
            df_by_daerah = pd.DataFrame(columns=df_pusat.columns)
            nama_list = ["-- Tiada Sekolah Dalam Daerah Ini --"]
        else:
            nama_list = ["-- Pilih Sekolah --"] + sorted(df_by_daerah["Nama_Pusat"].dropna().unique().tolist()) + ["LAIN-LAIN (Taip Sendiri) ✍️"]
            kod_display = ", ".join(kod_list)
            st.success(f"✅ {len(nama_list)-2} sekolah dalam {pilih_daerah} (Kod: {kod_display}) - Filter Tepat! + Lain-lain")
    else:
        df_by_daerah = df_pusat
        nama_list = ["-- Pilih Daerah Dulu --"]

    pilih_nama = col_s.selectbox("2️⃣ Nama Sekolah / Pusat", nama_list)

    # Jika pilih LAIN-LAIN, keluar column isi manual untuk SPM, AMALI, UBBM, UBBI
    if pilih_nama == "LAIN-LAIN (Taip Sendiri) ✍️":
        st.warning("⚠️ Sekolah tiada dalam senarai? Sila taip manual di bawah (SPM / Amali / UBBM / UBBI)")
        lain_c1, lain_c2 = st.columns(2)
        manual_nama_lain = lain_c1.text_input("✍️ Nama Sekolah/Pusat (Lain-lain) - Taip Sendiri", placeholder="Contoh: SMK CONTOH BARU / PUSAT BARU", key="manual_nama_lain")
        manual_no_lain = lain_c2.text_input("✍️ No Pusat (Lain-lain) - Taip Sendiri", placeholder="Contoh: BA999 / BH001 / BK999", key="manual_no_lain")
        no_opts = [manual_no_lain] if manual_no_lain else ["-- Taip No Pusat Dulu --"]
        kod_ppd = pilih_daerah if pilih_daerah!="-- Pilih Daerah --" else ""
        bil_calon = ""
        pilih_no = col_p.selectbox("3️⃣ No Pusat (Lain-lain)", no_opts)
        # Simpan untuk final - auto uppercase seperti STAM/MUET juga
        st.info(f"📝 Manual: {manual_nama_lain} | No: {manual_no_lain}")
    elif pilih_nama not in ["-- Pilih Sekolah --", "-- Pilih Daerah Dulu --"] and pilih_nama != "-- Pilih --":
        df_f = df_by_daerah[df_by_daerah["Nama_Pusat"]==pilih_nama]
        no_opts = df_f["No_Pusat"].tolist()
        kod_ppd = df_f.iloc[0]["Kod_PPD"] if not df_f.empty and "Kod_PPD" in df_f.columns else pilih_daerah
        bil_calon = df_f.iloc[0]["Bil_Calon_Pusat"] if not df_f.empty and "Bil_Calon_Pusat" in df_f.columns else ""
        manual_nama_lain = ""
        manual_no_lain = ""
        pilih_no = col_p.selectbox("3️⃣ No Pusat", no_opts)
    else:
        no_opts = ["-- Pilih Sekolah Dulu --"]
        kod_ppd = pilih_daerah if pilih_daerah!="-- Pilih Daerah --" else ""
        bil_calon = ""
        manual_nama_lain = ""
        manual_no_lain = ""
        pilih_no = col_p.selectbox("3️⃣ No Pusat", no_opts)

if MODE=="AMALI":
    # NAMA MAKMAL - ISI SENDIRI, BUKAN PILIHAN
    pilih_makmal = st.text_input("4️⃣ Nama Makmal (AMALI) - Isi Sendiri ✍️", placeholder="Contoh: Makmal Sains 1 / Makmal Kimia / Makmal Fizik / Makmal Biologi")
    nama_makmal_final = pilih_makmal.strip() if pilih_makmal else ""
    # Papar hint makmal yang ada dalam data (jika ada) sebagai rujukan sahaja
    try:
        df_ringkas_amali, _ = load_amali()
        if pilih_nama not in ["-- Pilih Sekolah --", "-- Pilih Daerah Dulu --"] and not df_ringkas_amali.empty:
            df_mak = df_ringkas_amali[df_ringkas_amali["Nama_Pusat"]==pilih_nama] if "Nama_Pusat" in df_ringkas_amali.columns else pd.DataFrame()
            if not df_mak.empty and "Nama_Makmal" in df_mak.columns:
                hint_makmal = df_mak["Nama_Makmal"].dropna().unique().tolist()[:5]
                if hint_makmal:
                    st.caption(f"💡 Rujukan makmal di pusat ini: {', '.join(hint_makmal)} (boleh taip sendiri)")
    except:
        pass
    if not nama_makmal_final:
        st.info("📝 Nama Makmal diisi manual oleh pemantau - Contoh: Makmal Sains 1")
else:
    nama_makmal_final = ""
    pilih_makmal = ""

if MODE in ["STAM","MUET"]:
    if pilih_nama and pilih_no:
        st.success(f"✅ {MODE} | {pilih_nama} | No: {pilih_no} | PPD: {kod_ppd} | {pilih_daerah}")
else:
    if pilih_nama == "LAIN-LAIN (Taip Sendiri) ✍️" and manual_nama_lain and manual_no_lain:
        st.success(f"✅ {manual_nama_lain.upper()} | No: {manual_no_lain.upper()} | PPD: {kod_ppd} | Calon: {bil_calon} (Lain-lain)")
    elif pilih_nama not in ["-- Pilih Sekolah --", "-- Pilih Daerah Dulu --"] and pilih_no not in ["-- Pilih Sekolah Dulu --"]:
        st.success(f"✅ {pilih_nama} | No: {pilih_no} | PPD: {kod_ppd} | Calon: {bil_calon}")

if MODE in ["STAM","MUET"]:
    # AUTO TUKAR KE HURUF BESAR untuk No Pusat dan Nama Sekolah/Pusat - STAM & MUET sahaja (ulasan kekal)
    pilih_nama_final = pilih_nama.strip().upper() if pilih_nama and pilih_nama.strip()!="" else ""
    pilih_no_final = pilih_no.strip().upper() if pilih_no and pilih_no.strip()!="" else ""
else:
    # Jika LAIN-LAIN dipilih untuk SPM, AMALI, UBBM, UBBI - auto uppercase sama seperti STAM/MUET
    if pilih_nama == "LAIN-LAIN (Taip Sendiri) ✍️":
        pilih_nama_final = manual_nama_lain.strip().upper() if manual_nama_lain and manual_nama_lain.strip()!="" else ""
        pilih_no_final = manual_no_lain.strip().upper() if manual_no_lain and manual_no_lain.strip()!="" else ""
    else:
        pilih_nama_final = pilih_nama if pilih_nama not in ["-- Pilih Sekolah --", "-- Pilih Daerah Dulu --", "-- Pilih --", "LAIN-LAIN (Taip Sendiri) ✍️"] else ""
        pilih_no_final = pilih_no if pilih_no not in ["-- Pilih Sekolah Dulu --", "-- Pilih --"] else ""

st.divider()
st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #7B1FA2 0%, #AB47BC 100%);">📅</div><div><div class="borang-header-title">Tarikh & Masa Lawatan</div><div class="borang-header-subtitle">Tahun → Bulan → Tarikh → Masa (6 pagi - 12 malam)</div></div></div>', unsafe_allow_html=True)
st.caption("✅ Boleh pilih Tahun & Bulan terus")

from datetime import datetime as dt_parse
try:
    available_dates_sorted = sorted(SENARAI_TARIKH)
    tahun_unik = sorted(set([d.split("-")[0] for d in available_dates_sorted if "-" in d]))
    if not tahun_unik:
        tahun_unik = ["2026"]
except:
    tahun_unik = ["2026"]
    available_dates_sorted = SENARAI_TARIKH

BULAN_NAMA = {"01":"Januari","02":"Februari","03":"Mac","04":"April","05":"Mei","06":"Jun","07":"Julai","08":"Ogos","09":"September","10":"Oktober","11":"November","12":"Disember"}

c_y, c_m, c_d, c_t = st.columns([1,1,1.2,1.2])
tahun_pilih = c_y.selectbox("📅 Tahun", tahun_unik, index=tahun_unik.index("2026") if "2026" in tahun_unik else 0)
try:
    bulan_unik = sorted(set([d.split("-")[1] for d in available_dates_sorted if d.startswith(tahun_pilih)]))
    if not bulan_unik:
        bulan_unik = ["02","10","11"]
except:
    bulan_unik = ["11","12"]
default_bulan_idx = 0
if MODE in ["UBBM","UBBI"] and "10" in bulan_unik:
    default_bulan_idx = bulan_unik.index("10")
elif MODE in ["UBBM","UBBI"] and "11" in bulan_unik:
    default_bulan_idx = bulan_unik.index("11")
elif MODE in ["UBBM","UBBI"] and "12" in bulan_unik:
    default_bulan_idx = bulan_unik.index("12")
elif "02" in bulan_unik and MODE in ["UBBM","UBBI"]:
    default_bulan_idx = bulan_unik.index("02")
elif "10" in bulan_unik:
    default_bulan_idx = bulan_unik.index("10")
elif "11" in bulan_unik:
    default_bulan_idx = bulan_unik.index("11")

bulan_pilih = c_m.selectbox("📅 Bulan", bulan_unik, index=default_bulan_idx, format_func=lambda m: f"{BULAN_NAMA.get(m,m)} ({m})")
tarikh_list_bulan = [d for d in available_dates_sorted if d.startswith(f"{tahun_pilih}-{bulan_pilih}")]
if not tarikh_list_bulan:
    tarikh_list_bulan = available_dates_sorted
tarikh_str = c_d.selectbox("📅 Tarikh (Hari)", tarikh_list_bulan, format_func=lambda d: dt_parse.strptime(d, "%Y-%m-%d").strftime("%d %b %Y - %A") if "-" in d else d)
try:
    tarikh = dt_parse.strptime(tarikh_str, "%Y-%m-%d").date()
except:
    tarikh = date(2026,11,23)

hari_minggu = tarikh.strftime("%A")
hari_melayu = {"Monday":"Isnin","Tuesday":"Selasa","Wednesday":"Rabu","Thursday":"Khamis","Friday":"Jumaat","Saturday":"Sabtu","Sunday":"Ahad"}.get(hari_minggu, hari_minggu)
st.caption(f"🗓️ Hari: {hari_melayu} ({hari_minggu})")

jam_pilihan = []
for h in range(6, 24):
    for m in [0, 15, 30, 45]:
        jam_pilihan.append(f"{h:02d}:{m:02d}")
jam_pilihan.extend(["00:00", "00:15", "00:30"])
masa_str = c_t.selectbox("⏰ Masa (6 Pagi - 12 Malam)", jam_pilihan, index=jam_pilihan.index("09:00") if "09:00" in jam_pilihan else 0)
try:
    hh, mm = masa_str.split(":")[:2]
    masa = time(int(hh), int(mm))
except:
    masa = time(9, 0)

st.divider()
if MODE=="SPM":
    df_mp = df_jadual[df_jadual["TARIKH_CLEAN"]==tarikh_str]
    mp_options = df_mp["MP_CLEAN"].tolist() if not df_mp.empty else ["Tiada MP - Pilih Tarikh Lain"]
    pilih_mp = st.selectbox("📚 Mata Pelajaran SPM", mp_options)
elif MODE=="AMALI":
    df_mp = df_jadual_amali[df_jadual_amali["tarikh_iso"]==tarikh_str] if not df_jadual_amali.empty else pd.DataFrame()
    mp_options = df_mp["mp_clean"].tolist() if not df_mp.empty else ["Tiada MP - Pilih Tarikh Lain"]
    pilih_mp = st.selectbox("🔬 Mata Pelajaran Amali Sains", mp_options)
elif MODE=="UBBM":
    pilih_mp = st.selectbox("🗣️ Mata Pelajaran", ["Bahasa Melayu - Ujian Bertutur (1103/3)", "Bahasa Melayu - Ujian Bertutur - Menumpang"])
elif MODE=="UBBI":
    pilih_mp = st.selectbox("🗣️ Mata Pelajaran", ["Bahasa Inggeris - Ujian Bertutur (1119/3)", "Bahasa Inggeris - Ujian Bertutur - Menumpang"])
elif MODE=="STAM":
    stam_options = ["Hifz Al-Quran (9301)", "Hadith & Mustolah (9302)", "Tauhid & Mantiq (9303)", "Fiqh & Usul Fiqh (9304)", "Tafsir (9305)", "Nahu & Sorof (9306)", "Insya & Mutolaah (9307)", "Arudh & Qafiyah (9308)", "Balaghah (9309)", "Adab & Nusus (9310)", "Semua Kertas STAM"]
    pilih_mp = st.selectbox("📖 Kertas Peperiksaan STAM", stam_options)
else: # MUET
    muet_options = ["Listening (800/1)", "Speaking (800/2)", "Reading (800/3)", "Writing (800/4)", "Semua Kertas MUET (800)"]
    pilih_mp = st.selectbox("📝 Kertas Peperiksaan MUET", muet_options)

st.divider()

if MODE=="SPM":
    st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);">🚪</div><div><div class="borang-header-title">Bilangan Bilik SPM</div><div class="borang-header-subtitle">Peperiksaan + Kuarantin + Sakit + Dewan</div></div></div>', unsafe_allow_html=True)
    b1,b2,b3,b4 = st.columns(4)
    bilik_pep = b1.number_input("Bilik Peperiksaan", 0,50,5)
    bilik_kuar = b2.number_input("Bilik Kuarantin", 0,10,1)
    bilik_sakit = b3.number_input("Bilik Sakit", 0,10,1)
    bilik_dewan = b4.number_input("Dewan", 0,10,0)
    b5,b6 = st.columns(2)
    petugas = b5.number_input("👮 Bilangan Petugas SPM", 0,50,5, help="Bil petugas termasuk Ketua Pengawas")
    bilik_makmal=""; sidang_no=""; bilik_lapor=0; bilik_ujian=0; station=0; bilik_kelas=0
    total_bilik = bilik_pep+bilik_kuar+bilik_sakit+bilik_dewan
elif MODE=="AMALI":
    st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #EF6C00 0%, #FFA726 100%);">🧪</div><div><div class="borang-header-title">Bilik Amali Sains</div><div class="borang-header-subtitle">Makmal + Ujian + Persediaan + Kuarantin + Sidang</div></div></div>', unsafe_allow_html=True)
    m1,m2,m3,m4 = st.columns(4)
    bilik_makmal = m1.number_input("Bil Makmal", 0,10,2)
    bilik_makmal_ujian = m2.number_input("Bilik Ujian", 0,10,1)
    bilik_persediaan = m3.number_input("Bilik Persediaan", 0,10,1)
    bilik_kuar = m4.number_input("Bilik Kuarantin", 0,10,1)
    m5,m6,m7 = st.columns(3)
    bilangan_sidang = m5.number_input("📊 Bilangan Sidang (Total Sidang Makmal)", 0,10,4, help="Berapa banyak sidang keseluruhan di makmal ini, contoh 4 sidang")
    sidang_lawatan = m6.selectbox("⏰ Sidang Lawatan (Semasa Pemantau Hadir)", ["1","2","3","4","Semua"], help="Sidang ke berapa semasa pemantau buat lawatan, contoh Sidang 2")
    petugas = m7.number_input("👮 Bil Petugas Amali", 0,30,5, help="Bil petugas makmal Amali")
    sidang_no = sidang_lawatan  # untuk compatibility lama
    bilik_pep = bilik_makmal_ujian
    bilik_sakit=bilik_dewan=bilik_lapor=bilik_ujian=station=bilik_kelas=0
    total_bilik = bilik_makmal+bilik_makmal_ujian+bilik_persediaan+bilik_kuar
elif MODE in ["UBBM","UBBI"]:
    st.markdown(f"#### 🗣️ Bilangan Bilik & Sesi (Ujian Bertutur {MODE})")
    u1,u2,u3 = st.columns(3)
    bilik_menunggu = u1.number_input("Bilik Menunggu", 0,20,2)
    bilik_ujian = u2.number_input("Bilik Ujian", 0,20,3)
    bilik_kuar = u3.number_input("Bilik Kuarantin", 0,10,1)
    s1,s2,s3 = st.columns(3)
    sidang_no = s1.selectbox("Sidang Dipantau", ["1","2","3","4","Semua"])
    petugas = s2.number_input("Bilangan Petugas", 0,30,5)
    hari_text = s3.text_input("Hari", value=hari_melayu)
    bilik_pep=bilik_ujian; bilik_sakit=0; bilik_dewan=0; bilik_makmal=""; bilik_kelas=0
    # Total bilik = Menunggu + Ujian + Kuarantin (Station dan Lapor Diri dibuang)
    total_bilik = bilik_menunggu+bilik_ujian+bilik_kuar
    bilik_lapor = bilik_menunggu  # Backward compat - simpan sebagai menunggu juga
    station = 0  # Station dibuang
elif MODE=="STAM":
    st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #4A148C 0%, #7B1FA2 100%);">🕌</div><div><div class="borang-header-title">Bilik & Kelas STAM</div><div class="borang-header-subtitle">Kelas/Dewan + Kuarantin + Petugas</div></div></div>', unsafe_allow_html=True)
    st1,st2,st3 = st.columns(3)
    bilik_kelas = st1.number_input("Bil Kelas / Dewan", 0,30,5)
    bilik_kuar = st2.number_input("Bilik Kuarantin", 0,10,1)
    petugas = st3.number_input("Bil Petugas (termasuk Ketua Pengawas)", 0,30,5)
    bilik_pep=bilik_kelas; bilik_ujian=0; bilik_lapor=0; station=0; bilik_sakit=0; bilik_dewan=0; bilik_makmal=""; sidang_no=""; hari_text=""
    total_bilik = bilik_kelas+bilik_kuar
else: # MUET
    st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #0D47A1 0%, #42A5F5 100%);">🎓</div><div><div class="borang-header-title">Bilik & Kelas MUET</div><div class="borang-header-subtitle">Kelas/Dewan + Kuarantin + Petugas (Jan-Dis)</div></div></div>', unsafe_allow_html=True)
    st1,st2,st3 = st.columns(3)
    bilik_kelas = st1.number_input("Bil Kelas / Dewan", 0,30,5)
    bilik_kuar = st2.number_input("Bilik Kuarantin", 0,10,1)
    petugas = st3.number_input("Bil Petugas (termasuk Ketua Pengawas)", 0,30,5)
    bilik_pep=bilik_kelas; bilik_ujian=0; bilik_lapor=0; station=0; bilik_sakit=0; bilik_dewan=0; bilik_makmal=""; sidang_no=""; hari_text=""
    total_bilik = bilik_kelas+bilik_kuar

st.divider()
if MODE in ["SPM","AMALI"]:
    st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #C2185B 0%, #EC407A 100%);">👥</div><div><div class="borang-header-title">Bilangan Calon SPM/Amali</div><div class="borang-header-subtitle">Hadir + Berdaftar + Cicir + Bantah</div></div></div>', unsafe_allow_html=True)
    ca1,ca2,ca3,ca4 = st.columns(4)
    calon_hadir = ca1.number_input("Calon Hadir", 0,500, int(bil_calon) if str(bil_calon).isdigit() else 20)
    calon_berdaftar = ca2.number_input("Calon Berdaftar", 0,500, int(bil_calon) if str(bil_calon).isdigit() else 22)
    calon_cicir = ca3.number_input("Calon Cicir", 0,50,0)
    calon_bantah = ca4.number_input("Calon Bantah", 0,50,0)
    calon_menumpang=0
    tidak_hadir = calon_berdaftar - calon_hadir
    keseluruhan = calon_berdaftar + calon_cicir + calon_bantah
    st.caption(f"Tidak Hadir: {tidak_hadir} | Keseluruhan: {keseluruhan}")
elif MODE in ["UBBM","UBBI"]:
    st.markdown("#### 👥 Bilangan Calon Untuk Sidang yang Dipantau (Ujian Bertutur)")
    ub1,ub2,ub3 = st.columns(3)
    calon_berdaftar = ub1.number_input("Calon Berdaftar Untuk Sidang yang Dipantau", 0,500, 30)
    calon_hadir = ub2.number_input("Calon Hadir Untuk Sidang yang Dipantau", 0,500, 28)
    calon_tidak_hadir = ub3.number_input("Calon Tidak Hadir", 0,100, 2)
    calon_cicir=0; calon_bantah=0; calon_menumpang=0
    tidak_hadir = calon_tidak_hadir
    keseluruhan = calon_berdaftar
    st.caption(f"Sidang Dipantau: {sidang_no} | Petugas: {petugas} | Bilik: Menunggu={bilik_menunggu}, Ujian={bilik_ujian}, Kuarantin={bilik_kuar}")
elif MODE=="STAM":
    st.markdown("#### 👥 Bilangan Calon (STAM) - WAJIB ISI HADIR")
    st1,st2,st3,st4,st5 = st.columns(5)
    calon_berdaftar = st1.number_input("Calon Berdaftar (STAM)", 0,500, 30, key=f"stam_berdaftar_{MODE}")
    calon_hadir = st2.number_input("✅ Calon Hadir (STAM) - WAJIB ISI", 0,500, 28, key=f"stam_hadir_{MODE}", help="Pemantau WAJIB isi bilangan calon yang hadir peperiksaan STAM")
    calon_menumpang = st3.number_input("Calon Menumpang", 0,100, 0, key=f"stam_menumpang_{MODE}")
    calon_cicir = st4.number_input("Calon Cicir", 0,50,0, key=f"stam_cicir_{MODE}")
    calon_bantah = st5.number_input("Calon Bantah", 0,50,0, key=f"stam_bantah_{MODE}")
    tidak_hadir = calon_berdaftar - calon_hadir
    if tidak_hadir < 0:
        tidak_hadir = 0
    keseluruhan = calon_berdaftar + calon_menumpang + calon_cicir + calon_bantah
    st.caption(f"STAM | Berdaftar: {calon_berdaftar} | Hadir: {calon_hadir} | TH: {tidak_hadir} | Menumpang: {calon_menumpang} | Cicir: {calon_cicir} | Bantah: {calon_bantah} | Keseluruhan: {keseluruhan} | Petugas: {petugas}")
    if calon_hadir == 0:
        st.warning("⚠️ Sila isi Calon Hadir STAM (wajib)")

else: # MUET
    st.markdown("#### 👥 Bilangan Calon (MUET)")
    st1,st2,st3,st4 = st.columns(4)
    calon_berdaftar = st1.number_input("Calon Berdaftar", 0,500, 30)
    calon_menumpang = st2.number_input("Calon Menumpang", 0,100, 0)
    calon_cicir = st3.number_input("Calon Cicir", 0,50,0)
    calon_bantah = st4.number_input("Calon Bantah", 0,50,0)
    calon_hadir = calon_berdaftar
    tidak_hadir = 0
    keseluruhan = calon_berdaftar + calon_menumpang
    st.caption(f"Berdaftar: {calon_berdaftar} + Menumpang: {calon_menumpang} = Keseluruhan: {keseluruhan} | Petugas: {petugas}")

ulasan = st.text_area("📝 Ulasan Pemantau (WAJIB - min 5 huruf)", height=100, placeholder="Tulis ulasan...")

st.divider()
st.markdown('<div class="borang-header"><div class="borang-header-icon" style="background: linear-gradient(135deg, #37474F 0%, #78909C 100%);">👮</div><div><div class="borang-header-title">Maklumat Pemantau & Ulasan</div><div class="borang-header-subtitle">Nama + Jawatan + Daerah + Ulasan Wajib</div></div></div>', unsafe_allow_html=True)
p1,p2,p3 = st.columns(3)
if st.session_state.is_admin:
    nama_pemantau = p1.text_input("Nama Pemantau", value=st.session_state.user_name)
    jawatan_pemantau = p2.selectbox("Jawatan", ["-- Pilih --", "Penolong Pengarah SPP", "Penolong PPD SPP", "Penyelia Kawasan"])
else:
    nama_pemantau = p1.text_input("Nama Pemantau", value=st.session_state.user_name, disabled=True)
    jawatan_pemantau = p2.selectbox("Jawatan", ["-- Pilih --", "Penolong Pengarah SPP", "Penolong PPD SPP", "Penyelia Kawasan"])

# Jika Penyelia Kawasan - Daerah auto ikut pilihan daerah sebelum pilihan sekolah (tak boleh keluar daerah)
if "Penyelia Kawasan" in jawatan_pemantau:
    if pilih_daerah and pilih_daerah != "-- Pilih Daerah --" and pilih_daerah != "-- Pilih Daerah Dulu --":
        daerah_pemantau = pilih_daerah
        p3.text_input("Daerah (Auto - Penyelia Kawasan ikut daerah atas)", value=daerah_pemantau, disabled=True)
        st.caption(f"🔒 Penyelia Kawasan terkunci di daerah: {daerah_pemantau} - tak boleh keluar daerah yang dipilih di atas ({pilih_daerah})")
    else:
        # Jika belum pilih daerah di atas, suruh pilih dulu
        daerah_pemantau = p3.selectbox("Daerah (Penyelia Kawasan - Wajib pilih daerah atas dulu)", ["-- Pilih Daerah --", "Petaling Perdana","Petaling Utama","Hulu Langat","Gombak","Klang","Kuala Langat","Kuala Selangor","Hulu Selangor","Sabak Bernam","Sepang"])
        if daerah_pemantau == "-- Pilih Daerah --":
            st.warning("⚠️ Sila pilih Daerah di bahagian atas (1️⃣ Daerah / PPD) dulu - Penyelia Kawasan tak boleh keluar dari daerah yang dipilih")
        else:
            st.info(f"✅ Penyelia Kawasan akan terkunci di daerah: {daerah_pemantau}")
    bilik_kebal_penyelia = st.text_input("🏦 Nama Bilik Kebal Penyelia Kawasan (Wajib untuk Penyelia Kawasan)", placeholder="Contoh: Bilik Kebal PPD Klang / Bilik Kebal PPD Petaling Perdana / Bilik Kebal SMK Meru")
elif "PPD SPP" in jawatan_pemantau and "Penolong PPD" in jawatan_pemantau:
    daerah_pemantau = p3.selectbox("Daerah", ["Petaling Perdana","Petaling Utama","Hulu Langat","Gombak","Klang","Kuala Langat","Kuala Selangor","Hulu Selangor","Sabak Bernam","Sepang"])
    bilik_kebal_penyelia = ""
elif "Penolong Pengarah SPP" in jawatan_pemantau:
    daerah_pemantau = p3.selectbox("JPN", ["Sektor Pentaksiran & Peperiksaan","Sektor Pengurusan Sekolah","Lain-lain"])
    bilik_kebal_penyelia = ""
else:
    daerah_pemantau = p3.text_input("Daerah / JPN")
    bilik_kebal_penyelia = ""

if st.button(f"💾 SIMPAN LAPORAN {MODE}", type="primary", use_container_width=True):
    errors = []
    if pilih_daerah in ["-- Pilih Daerah --", "-- Pilih Daerah Dulu --", "", None]:
        errors.append("❌ Sila pilih Daerah / PPD")
    if not pilih_nama_final or pilih_nama_final in ["-- Pilih Sekolah --", "-- Pilih Daerah Dulu --", "-- Pilih --", ""]:
        errors.append("❌ Sila pilih Nama Sekolah / Pusat")
    if not pilih_no_final or pilih_no_final in ["-- Pilih Sekolah Dulu --", "-- Pilih --", ""]:
        errors.append("❌ Sila pilih No Pusat")
    if MODE=="AMALI" and (not nama_makmal_final or nama_makmal_final in ["-- Pilih Makmal --", "-- Pilih Sekolah Dulu --", "-- Tiada Makmal --"]):
        errors.append("❌ Sila pilih Nama Makmal (AMALI)")
    if not tarikh_str:
        errors.append("❌ Sila pilih Tarikh Lawatan")
    if not pilih_mp or pilih_mp in ["Tiada MP", "Tiada MP - Pilih Tarikh Lain", "", "-- Pilih --"]:
        errors.append("❌ Sila pilih Mata Pelajaran / Kertas")
    if total_bilik == 0:
        errors.append("❌ Sila isi Bilangan Bilik (Total tidak boleh 0)")
    if MODE in ["SPM","AMALI","UBBM","UBBI"] and calon_berdaftar == 0:
        errors.append("❌ Sila isi Calon Berdaftar (tidak boleh 0)")
    if MODE in ["STAM","MUET"] and calon_berdaftar==0 and calon_menumpang==0:
        errors.append(f"❌ Sila isi Calon Berdaftar atau Menumpang ({MODE})")
    # Station dibuang untuk UBBM/UBBI - tak perlu validation lagi
    if MODE in ["SPM","AMALI","UBBM","UBBI","STAM","MUET"] and petugas==0:
        errors.append("❌ Sila isi Bilangan Petugas")
    if not ulasan or ulasan.strip() == "" or len(ulasan.strip()) < 5:
        errors.append("❌ Sila isi Ulasan Pemantau (min 5 huruf) - WAJIB")
    if not nama_pemantau or nama_pemantau.strip() == "":
        errors.append("❌ Sila isi Nama Pemantau")
    if not jawatan_pemantau or jawatan_pemantau in ["-- Pilih --", ""]:
        errors.append("❌ Sila pilih Jawatan Pemantau")
    if "Penyelia Kawasan" in jawatan_pemantau and (not bilik_kebal_penyelia or bilik_kebal_penyelia.strip()==""):
        errors.append("❌ Sila isi Nama Bilik Kebal Penyelia Kawasan (wajib untuk Penyelia Kawasan)")
    if not daerah_pemantau or str(daerah_pemantau).strip() == "":
        errors.append("❌ Sila isi / pilih Daerah / JPN Pemantau")
    
    if errors:
        st.error("⚠️ **SEMUA MAKLUMAT WAJIB DILENGKAPKAN!**")
        for err in errors:
            st.markdown(f"- {err}")
        st.warning(f"🔴 {len(errors)} maklumat belum lengkap.")
        st.stop()
    
    data = {
        "jenis": MODE, "tarikh_submit": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nama_sekolah": pilih_nama_final, "no_pusat": pilih_no_final, "nama_makmal": nama_makmal_final,
        "kod_ppd": kod_ppd, "tarikh_lawatan": str(tarikh), "masa_lawatan": str(masa),
        "mata_pelajaran": pilih_mp,
        "bilik_kebal_penyelia": bilik_kebal_penyelia if 'bilik_kebal_penyelia' in locals() else "", 
        "bilik_peperiksaan": bilik_pep if 'bilik_pep' in locals() else 0, 
        "bilik_kuarantin": bilik_kuar if 'bilik_kuar' in locals() else 0,
        "bilik_sakit": bilik_sakit if 'bilik_sakit' in locals() else 0, 
        "dewan": bilik_dewan if 'bilik_dewan' in locals() else 0, 
        "bilik_makmal": bilik_makmal if 'bilik_makmal' in locals() else "",
        "bilik_makmal_ujian": bilik_makmal_ujian if 'bilik_makmal_ujian' in locals() else 0,
        "bilik_persediaan": bilik_persediaan if 'bilik_persediaan' in locals() else 0,
        "bilangan_sidang": bilangan_sidang if 'bilangan_sidang' in locals() else 0,
        "sidang_lawatan": sidang_lawatan if 'sidang_lawatan' in locals() else "",
        "sidang_no": sidang_no if 'sidang_no' in locals() else "",
        "total_bilik": total_bilik,
        "bilik_menunggu": bilik_menunggu if 'bilik_menunggu' in locals() else 0,
        "bilik_ujian": bilik_ujian if 'bilik_ujian' in locals() else 0,
        "bilik_lapor": bilik_lapor if 'bilik_lapor' in locals() else 0,
        "station": station if 'station' in locals() else 0,
        "petugas": petugas if 'petugas' in locals() else 0,
        "bilik_kelas": bilik_kelas if 'bilik_kelas' in locals() else 0,
        "hari": hari_text if 'hari_text' in locals() else hari_melayu,
        "calon_hadir": calon_hadir, "calon_berdaftar": calon_berdaftar,
        "calon_tidak_hadir": tidak_hadir, "calon_cicir": calon_cicir if 'calon_cicir' in locals() else 0, 
        "calon_bantah": calon_bantah if 'calon_bantah' in locals() else 0,
        "calon_menumpang": calon_menumpang if 'calon_menumpang' in locals() else 0,
        "calon_keseluruhan": keseluruhan,
        "ulasan": ulasan, "nama_pemantau": nama_pemantau,
        "jawatan_pemantau": jawatan_pemantau, "daerah_pemantau": daerah_pemantau
    }
    save_laporan(data)
    st.session_state["last"] = data
    st.success(f"✅ Berjaya SIMPAN {MODE}! Semua maklumat lengkap.")
    st.balloons()

st.divider()
if st.session_state.is_admin:
    st.markdown(f"#### 📊 Laporan {MODE} - ADMIN (Semua + Boleh Padam + Padam Semua)")
elif st.session_state.get('is_kppk', False):
    st.markdown(f"#### 📊 Laporan {MODE} - KPPK/PENGARAH (Semua - Lihat Sahaja)")
else:
    st.markdown(f"#### 📊 Laporan {MODE} - Saya ({st.session_state.user_name})")

lap_list = load_laporan()

if st.session_state.is_admin or st.session_state.get('is_kppk', False):
    filtered_list = lap_list
else:
    filtered_list = [l for l in lap_list if l.get("nama_pemantau","").lower().strip() == st.session_state.user_name.lower().strip()]
    if "last" in st.session_state and st.session_state["last"].get("jenis")==MODE:
        if st.session_state["last"].get("nama_pemantau","").lower().strip() == st.session_state.user_name.lower().strip():
            if st.session_state["last"] not in filtered_list:
                filtered_list = [st.session_state["last"]] + filtered_list

if not filtered_list:
    if st.session_state.is_admin or st.session_state.get('is_kppk', False):
        st.info(f"Belum ada laporan {MODE} dalam sistem.")
    else:
        st.info(f"Belum ada laporan anda untuk {MODE}. Laporan orang lain tidak dipaparkan.")
    st.stop()

st.write(f"Jumlah: {len(filtered_list)} laporan")

if st.session_state.is_admin:
    st.warning("⚠️ Anda Admin - Boleh padam laporan & padam SEMUA laporan. Pemantau biasa TIDAK ada butang padam.")
    # Admin - Padam Semua Report function
    with st.expander("🗑️ FUNGSI ADMIN - Padam Semua Laporan", expanded=False):
        st.error("⚠️ AMARAN: Ini akan padam SEMUA laporan dalam sistem! Tindakan tidak boleh undur!")
        col_del1, col_del2 = st.columns(2)
        confirm_text = col_del1.text_input("Taip PADAM SEMUA untuk sahkan", placeholder="PADAM SEMUA")
        if col_del2.button("🗑️ PADAM SEMUA LAPORAN", type="primary", use_container_width=True):
            if confirm_text == "PADAM SEMUA":
                save_all_laporan([])
                st.success("✅ SEMUA laporan telah dipadam oleh ADMIN!")
                st.balloons()
                st.rerun()
            else:
                st.error("❌ Sila taip tepat: PADAM SEMUA")
elif st.session_state.get('is_kppk', False):
    st.info("👔 Anda KPPK/Pengarah - Boleh lihat SEMUA laporan, TIDAK boleh padam laporan.")

from collections import Counter
tarikh_all = [l.get('tarikh_lawatan','') for l in filtered_list]
counter_tarikh = Counter(tarikh_all)
unique_tarikh = sorted(set(tarikh_all), reverse=True)

tarikh_options = ["📅 Semua Tarikh"] + [f"{t} ({counter_tarikh[t]} laporan)" for t in unique_tarikh]
pilih_tarikh_raw = st.selectbox(f"📅 Pilih Tarikh Laporan ({len(unique_tarikh)} tarikh, {len(filtered_list)} laporan):", tarikh_options)

if pilih_tarikh_raw == "📅 Semua Tarikh":
    filtered_by_tarikh = filtered_list
else:
    tarikh_selected = pilih_tarikh_raw.split(" (")[0]
    filtered_by_tarikh = [l for l in filtered_list if l.get('tarikh_lawatan','') == tarikh_selected]

filtered_by_tarikh = sorted(filtered_by_tarikh, key=lambda x: (x.get('tarikh_lawatan',''), x.get('masa_lawatan',''), x.get('no_pusat','')))

if len(filtered_by_tarikh) > 1:
    pilihan_labels = []
    for l in filtered_by_tarikh:
        mp_short = l.get('mata_pelajaran','')[:35]
        calon_info = f" H:{l.get('calon_hadir',0)}"
        pilihan_labels.append(f"{l.get('no_pusat','')} | {l.get('nama_sekolah','')[:22]} | {l.get('masa_lawatan','')} | {mp_short}{calon_info}")
    idx_pilih = st.selectbox(f"📑 Pilih Laporan {MODE} - {pilih_tarikh_raw}:", range(len(filtered_by_tarikh)), format_func=lambda i: pilihan_labels[i])
    sel = filtered_by_tarikh[idx_pilih]
else:
    sel = filtered_by_tarikh[0]
    st.success(f"📌 {sel['no_pusat']} | {sel['nama_sekolah']} | {sel['tarikh_lawatan']} {sel.get('masa_lawatan','')} | {sel['mata_pelajaran'][:40]}")

for i, orig in enumerate(lap_list):
    if orig == sel:
        idx_in_main = i
        break
else:
    idx_in_main = -1

with st.container(border=True):
    colA, colB, colC = st.columns([3,2,1])
    with colA:
        st.caption(f"📄 {sel['no_pusat']} | {sel['nama_sekolah'][:30]} | {sel['tarikh_lawatan']}")
    with colB:
        st.caption(f"👤 {sel['nama_pemantau']} | {sel['tarikh_submit']}")
    with colC:
        if st.session_state.is_admin and idx_in_main != -1:
            if st.button("🗑️ Padam", key=f"del_{MODE}_{idx_in_main}", type="secondary", use_container_width=True):
                new_list = [l for j,l in enumerate(lap_list) if j != idx_in_main]
                save_all_laporan(new_list)
                st.success(f"Laporan {sel['no_pusat']} dipadam!")
                st.rerun()
        else:
            st.caption("🔒 Tiada akses padam")

IMG_D = IMG_DEWAN_B64
IMG_S = IMG_SEKOLAH_B64

def buat_carta_pai_html(sel_data):
    try:
        hadir = int(sel_data.get('calon_hadir',0) or 0)
        th = int(sel_data.get('calon_tidak_hadir',0) or 0)
        cicir = int(sel_data.get('calon_cicir',0) or 0)
        bantah = int(sel_data.get('calon_bantah',0) or 0)
        menumpang = int(sel_data.get('calon_menumpang',0) or 0)
        berdaftar = int(sel_data.get('calon_berdaftar',0) or 0)
        total = hadir + th + cicir + bantah + menumpang
        if total == 0:
            total = berdaftar if berdaftar>0 else 1
            hadir = total
        segments = []
        if hadir > 0: segments.append((hadir, '#4CAF50', 'Hadir'))
        if th > 0: segments.append((th, '#EF5350', 'TH'))
        if menumpang > 0: segments.append((menumpang, '#42A5F5', 'Menumpang'))
        if cicir > 0: segments.append((cicir, '#FFA726', 'Cicir'))
        if bantah > 0: segments.append((bantah, '#AB47BC', 'Bantah'))
        if not segments:
            segments = [(berdaftar if berdaftar>0 else 1, '#42A5F5', 'Berdaftar')]
            total = berdaftar if berdaftar>0 else 1
        gradient_parts = []
        legend_html = ""
        curr_pct = 0
        for val, col2, label in segments:
            pct = (val / total) * 100 if total>0 else 0
            next_pct = curr_pct + pct
            gradient_parts.append(f"{col2} {curr_pct:.1f}% {next_pct:.1f}%")
            legend_html += f'<div style="display:flex; align-items:center; gap:5px; font-size:9px; margin:2px 0;"><div style="width:10px; height:10px; background:{col2}; border-radius:50%;"></div><span style="font-weight:600;">{label}</span> <span style="color:#666;">{val} ({pct:.0f}%)</span></div>'
            curr_pct = next_pct
        gradient_str = ", ".join(gradient_parts)
        chart_html = f"""
        <div style="display:flex; flex-direction:column; align-items:center; width:100%;">
            <div style="font-size:10px; font-weight:800; color:#0D47A1; margin-bottom:8px; background:#E3F2FD; padding:4px 10px; border-radius:20px;">📊 STATUS CALON</div>
            <div style="position:relative; width:120px; height:120px;">
                <div style="width:120px; height:120px; border-radius:50%; background: conic-gradient({gradient_str}); box-shadow: 0 4px 15px rgba(0,0,0,0.15);"></div>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:58px; height:58px; background:white; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="font-size:18px; font-weight:900; color:#0D47A1;">{berdaftar}</div>
                    <div style="font-size:7px; font-weight:700; color:#78909C;">BERDAFTAR</div>
                </div>
            </div>
            <div style="margin-top:10px; width:100%; background:#F8FAFC; border-radius:8px; padding:6px 8px; border:1px solid #F1F5F9;">{legend_html}</div>
        </div>
        """
        return chart_html
    except Exception as e:
        return f"<div>Error: {e}</div>"

CHART_PAI_HTML = buat_carta_pai_html(sel)

def badge(text, bg="#E3F2FD", color="#0D47A1"):
    return f'<span style="display:inline-block; background:{bg}; color:{color}; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; margin:1px;">{text}</span>'

# Pemantau html - tambah bilik kebal jika Penyelia Kawasan (FIX NameError)
b_kebal = sel.get('bilik_kebal_penyelia','')
if b_kebal and "Penyelia Kawasan" in str(sel.get('jawatan_pemantau','')):
    pemantau_html = f"👤 {sel['nama_pemantau']} | {badge(sel['jawatan_pemantau'], '#0D47A1', 'white')} {badge(sel['daerah_pemantau'], '#E0E7FF', '#4338CA')} {badge(f'🏦 Bilik Kebal: {b_kebal}', '#FFF3E0', '#EF6C00')}"
else:
    pemantau_html = f"👤 {sel['nama_pemantau']} | {badge(sel['jawatan_pemantau'], '#0D47A1', 'white')} {badge(sel['daerah_pemantau'], '#E0E7FF', '#4338CA')}"

# Prepare values for html to avoid nested f-string issue
b_pep = sel.get('bilik_peperiksaan',0)
b_kuar = sel.get('bilik_kuarantin',0)
b_sakit = sel.get('bilik_sakit',0)
b_dewan = sel.get('dewan',0)
b_total = sel.get('total_bilik',0)
b_makmal = sel.get('bilik_makmal',0)
b_makmal_ujian = sel.get('bilik_makmal_ujian', sel.get('bilik_peperiksaan',0))
b_persediaan = sel.get('bilik_persediaan',0)
b_sidang = sel.get('sidang_no','')
b_ujian = sel.get('bilik_ujian',0)
b_menunggu = sel.get('bilik_menunggu', sel.get('bilik_lapor',0))
b_lapor = sel.get('bilik_lapor',0)
b_station = sel.get('station',0)
b_petugas = sel.get('petugas',0)
b_kelas = sel.get('bilik_kelas',0)
c_berdaftar = sel.get('calon_berdaftar',0)
c_hadir = sel.get('calon_hadir',0)
c_th = sel.get('calon_tidak_hadir',0)
c_cicir = sel.get('calon_cicir',0)
c_bantah = sel.get('calon_bantah',0)
c_menumpang = sel.get('calon_menumpang',0)
c_keseluruhan = sel.get('calon_keseluruhan',0)
c_hari = sel.get('hari','')

if MODE in ["SPM"]:
    bilik_html = f"{badge(f'Pep: {b_pep}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Sakit: {b_sakit}', '#FCE4EC', '#C2185B')} {badge(f'Dewan: {b_dewan}', '#E3F2FD', '#1565C0')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
    calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Cicir: {c_cicir}', '#FFF3E0', '#EF6C00')} {badge(f'Bantah: {c_bantah}', '#F3E5F5', '#6A1B9A')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
    petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"
elif MODE=="AMALI":
    b_makmal_ujian = sel.get('bilik_makmal_ujian', sel.get('bilik_peperiksaan', 0))
    b_persediaan = sel.get('bilik_persediaan', 0)
    b_kuar_amali = sel.get('bilik_kuarantin', 0)
    b_bilangan_sidang = sel.get('bilangan_sidang', sel.get('total_bilik', 0))
    b_sidang_lawatan = sel.get('sidang_lawatan', sel.get('sidang_no',''))
    bilik_html = f"{badge(f'Makmal: {b_makmal}', '#E8F5E9', '#2E7D32')} {badge(f'Bilik Ujian: {b_makmal_ujian}', '#E3F2FD', '#1565C0')} {badge(f'Persediaan: {b_persediaan}', '#FFF3E0', '#EF6C00')} {badge(f'Kuarantin: {b_kuar_amali}', '#FFEBEE', '#C62828')} {badge(f'Bil Sidang: {b_bilangan_sidang}', '#E0F7FA', '#006064')} {badge(f'Lawatan Sidang: {b_sidang_lawatan}', '#F3E5F5', '#6A1B9A')} {badge(f'Total Bilik: {b_total}', '#0D47A1', 'white')}"
    calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
    petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Petugas Makmal Amali', '#E0F7FA', '#006064')}"
elif MODE in ["UBBM","UBBI"]:
    # FIX UBBM/UBBI BARU: Bilik Menunggu, Bilik Ujian, Bilik Kuarantin, Sidang Dipantau - Buang Station & Lapor Diri
    bilik_html = f"{badge(f'Bilik Menunggu: {b_menunggu}', '#E3F2FD', '#1565C0')} {badge(f'Bilik Ujian: {b_ujian}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Sidang Dipantau: {b_sidang}', '#E0F2F1', '#00695C')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
    petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"
    calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Hadir: {c_hadir}', '#E8F5E9', '#2E7D32')} {badge(f'TH: {c_th}', '#FFEBEE', '#C62828')} {badge(f'Hari: {c_hari}', '#FFF8E1', '#F57F17')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
else:
    # FIX: Petugas jangan dalam bilik untuk STAM/MUET juga - letak atas Kehadiran Calon
    bilik_html = f"{badge(f'Kelas/Dewan: {b_kelas}', '#E8F5E9', '#2E7D32')} {badge(f'Kuarantin: {b_kuar}', '#FFF3E0', '#EF6C00')} {badge(f'Total: {b_total}', '#0D47A1', 'white')}"
    calon_html = f"{badge(f'Berdaftar: {c_berdaftar}', '#E3F2FD', '#0D47A1')} {badge(f'Menumpang: {c_menumpang}', '#E0F7FA', '#006064')} {badge(f'Cicir: {c_cicir}', '#FFF3E0', '#EF6C00')} {badge(f'Bantah: {c_bantah}', '#F3E5F5', '#6A1B9A')} {badge(f'Keseluruhan: {c_keseluruhan}', '#0D47A1', 'white')}"
    petugas_html = f"{badge(f'Bil Petugas: {b_petugas}', '#0D47A1', 'white')} {badge(f'Ketua Pengawas + Pengawas', '#E0F7FA', '#006064')}"

jenis_label = sel.get('jenis','SPM')
if jenis_label=="UBBM":
    jenis_label_full = "UJIAN BERTUTUR BAHASA MELAYU"
    jenis_icon = "🗣️"
elif jenis_label=="UBBI":
    jenis_label_full = "UJIAN BERTUTUR BAHASA INGGERIS"
    jenis_icon = "🗣️"
elif jenis_label=="STAM":
    jenis_label_full = "SIJIL TINGGI AGAMA MALAYSIA (STAM)"
    jenis_icon = "🕌"
elif jenis_label=="MUET":
    jenis_label_full = "MALAYSIAN UNIVERSITY ENGLISH TEST (MUET)"
    jenis_icon = "🎓"
elif jenis_label=="AMALI":
    jenis_label_full = "AMALI SAINS SPM 2026"
    jenis_icon = "🧪"
else:
    jenis_label_full = "SPM 2026"
    jenis_icon = "📝"

# ===== TEMPLATE MENGIKUT PEPERIKSAAN - ASING SETIAP JENIS =====
# SPM - Template khas
if MODE=="SPM":
    table_rows = f'''
                    <tr style="background:#F8FAFC; border-bottom:2px solid #E8EEF6;">
                        <td style="padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🏫 NAMA PUSAT / SEKOLAH (SPM)</td>
                        <td style="padding:11px 14px; font-weight:700; font-size:13px;">{sel['nama_sekolah']}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📍 NO PUSAT / DAERAH</td>
                        <td style="padding:10px 14px;"><b style="color:#0D47A1;">{sel['no_pusat']}</b> <span style="margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;">📍 {get_nama_daerah_from_pusat(sel['no_pusat'], sel.get('kod_ppd',''))} ({sel.get('kod_ppd','')})</span></td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">📅 TARIKH, HARI & MP</td>
                        <td style="padding:10px 14px;"><span style="background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;">{sel['tarikh_lawatan']}</span> <span style="background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">🕒 {sel['masa_lawatan']}</span> <span style="background:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">📅 {sel.get('hari','')}</span> <b style="color:#0D47A1; margin-left:8px;">{sel['mata_pelajaran']}</b></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">🚪 BILIK PEPERIKSAAN SPM</td>
                        <td style="padding:10px 14px;">{bilik_html}</td>
                    </tr>
                    <tr style="background:#FFF3E0; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;">👮 KEHADIRAN PETUGAS SPM</td>
                        <td style="padding:10px 14px;">{petugas_html}</td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">👥 KEHADIRAN CALON SPM</td>
                        <td style="padding:10px 14px;">{calon_html}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📝 ULASAN PEMANTAUAN SPM</td>
                        <td style="padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;">❝ {sel['ulasan'] or 'Tiada ulasan'} ❞</td>
                    </tr>
                    <tr style="background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;">👮 PEMANTAU SPM</td>
                        <td style="padding:11px 14px; font-weight:600;">{pemantau_html}</td>
                    </tr>
    '''
# AMALI - Template khas dengan Nama Makmal, Bilangan Sidang, Sidang Lawatan
elif MODE=="AMALI":
    table_rows = f'''
                    <tr style="background:#F8FAFC; border-bottom:2px solid #E8EEF6;">
                        <td style="padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🏫 NAMA PUSAT / SEKOLAH (AMALI)</td>
                        <td style="padding:11px 14px; font-weight:700; font-size:13px;">{sel['nama_sekolah']}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📍 NO PUSAT / DAERAH</td>
                        <td style="padding:10px 14px;"><b style="color:#0D47A1;">{sel['no_pusat']}</b> <span style="margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;">📍 {get_nama_daerah_from_pusat(sel['no_pusat'], sel.get('kod_ppd',''))} ({sel.get('kod_ppd','')})</span></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9; background:#FFFEF7;">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🧪 NAMA MAKMAL</td>
                        <td style="padding:10px 14px;"><b style="color:#2E7D32; background:#E8F5E9; padding:4px 12px; border-radius:20px; font-size:12px;">🔬 {sel.get('nama_makmal','-') or '-'}</b></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9; background:#E0F7FA;">
                        <td style="padding:11px 14px; font-weight:800; color:#006064; font-size:11px; border-right:1px solid #B2EBF2;">📊 BILANGAN SIDANG</td>
                        <td style="padding:10px 14px;"><b style="color:white; background:#006064; padding:4px 14px; border-radius:20px; font-size:12px;">{sel.get('bilangan_sidang', sel.get('total_bilik', '-'))} Sidang</b></td>
                    </tr>
                    <tr style="background:#F3E5F5; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#6A1B9A; font-size:11px; border-right:1px solid #E1BEE7;">⏰ SIDANG LAWATAN</td>
                        <td style="padding:10px 14px;"><b style="color:white; background:#6A1B9A; padding:4px 14px; border-radius:20px; font-size:12px;">Sidang {sel.get('sidang_lawatan', sel.get('sidang_no','-')) or '-'}</b></td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">📅 TARIKH, HARI & MP AMALI</td>
                        <td style="padding:10px 14px;"><span style="background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;">{sel['tarikh_lawatan']}</span> <span style="background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">🕒 {sel['masa_lawatan']}</span> <span style="background:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">📅 {sel.get('hari','')}</span> <b style="color:#0D47A1; margin-left:8px;">{sel['mata_pelajaran']}</b></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">🔬 BILIK AMALI SAINS</td>
                        <td style="padding:10px 14px;">{bilik_html}</td>
                    </tr>
                    <tr style="background:#FFF3E0; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;">👮 KEHADIRAN PETUGAS AMALI</td>
                        <td style="padding:10px 14px;">{petugas_html}</td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">👥 KEHADIRAN CALON AMALI</td>
                        <td style="padding:10px 14px;">{calon_html}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📝 ULASAN AMALI</td>
                        <td style="padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;">❝ {sel['ulasan'] or 'Tiada ulasan'} ❞</td>
                    </tr>
                    <tr style="background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;">👮 PEMANTAU AMALI</td>
                        <td style="padding:11px 14px; font-weight:600;">{pemantau_html}</td>
                    </tr>
    '''
# UBBM / UBBI - Template Ujian Bertutur ada Station & Sidang
elif MODE in ["UBBM","UBBI"]:
    table_rows = f'''
                    <tr style="background:#F8FAFC; border-bottom:2px solid #E8EEF6;">
                        <td style="padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🏫 NAMA PUSAT / SEKOLAH ({MODE})</td>
                        <td style="padding:11px 14px; font-weight:700; font-size:13px;">{sel['nama_sekolah']}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📍 NO PUSAT / DAERAH</td>
                        <td style="padding:10px 14px;"><b style="color:#0D47A1;">{sel['no_pusat']}</b> <span style="margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;">📍 {get_nama_daerah_from_pusat(sel['no_pusat'], sel.get('kod_ppd',''))} ({sel.get('kod_ppd','')})</span></td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">📅 TARIKH, HARI, SIDANG & MP</td>
                        <td style="padding:10px 14px;"><span style="background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;">{sel['tarikh_lawatan']}</span> <span style="background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">🕒 {sel['masa_lawatan']}</span> <span style="background:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">📅 {sel.get('hari','')}</span> <b style="color:#0D47A1; margin-left:8px;">{sel['mata_pelajaran']}</b> <span style="margin-left:8px; background:#00695C; color:white; padding:3px 10px; border-radius:20px; font-size:10px;">Sidang {sel.get('sidang_no','-')}</span></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">🗣️ BILIK UJIAN BERTUTUR {MODE} (Ada Station & Sidang)</td>
                        <td style="padding:10px 14px;">{bilik_html}</td>
                    </tr>
                    <tr style="background:#FFF3E0; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;">👮 KEHADIRAN PETUGAS {MODE}</td>
                        <td style="padding:10px 14px;">{petugas_html}</td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">👥 KEHADIRAN CALON {MODE}</td>
                        <td style="padding:10px 14px;">{calon_html}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📝 ULASAN {MODE}</td>
                        <td style="padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;">❝ {sel['ulasan'] or 'Tiada ulasan'} ❞</td>
                    </tr>
                    <tr style="background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;">👮 PEMANTAU {MODE}</td>
                        <td style="padding:11px 14px; font-weight:600;">{pemantau_html}</td>
                    </tr>
    '''
# STAM - Template tiada Makmal, tiada Sidang, tiada Station
elif MODE=="STAM":
    table_rows = f'''
                    <tr style="background:#F8FAFC; border-bottom:2px solid #E8EEF6;">
                        <td style="padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🕌 NAMA PUSAT STAM (Isi Sendiri)</td>
                        <td style="padding:11px 14px; font-weight:700; font-size:13px;">{sel['nama_sekolah']}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📍 NO PUSAT STAM / DAERAH</td>
                        <td style="padding:10px 14px;"><b style="color:#0D47A1;">{sel['no_pusat']}</b> <span style="margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;">📍 {get_nama_daerah_from_pusat(sel['no_pusat'], sel.get('kod_ppd',''))} ({sel.get('kod_ppd','')})</span> <span style="margin-left:6px; background:#FFF3E0; color:#EF6C00; padding:2px 8px; border-radius:10px; font-size:9px;">Isi Sendiri - Pusat Tak Sama SPM</span></td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">📅 TARIKH & MASA LAWATAN STAM</td>
                        <td style="padding:10px 14px;"><span style="background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;">{sel['tarikh_lawatan']}</span> <span style="background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">🕒 {sel['masa_lawatan']}</span> <span style="background:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">📅 {sel.get('hari','')}</span> <b style="color:#0D47A1; margin-left:8px;">{sel['mata_pelajaran']}</b></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">🕌 BILIK STAM (Tiada Sidang, Tiada Station)</td>
                        <td style="padding:10px 14px;">{bilik_html}</td>
                    </tr>
                    <tr style="background:#FFF3E0; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;">👮 KEHADIRAN PETUGAS STAM</td>
                        <td style="padding:10px 14px;">{petugas_html}</td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">👥 KEHADIRAN CALON STAM</td>
                        <td style="padding:10px 14px;">{calon_html}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📝 ULASAN STAM</td>
                        <td style="padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;">❝ {sel['ulasan'] or 'Tiada ulasan'} ❞</td>
                    </tr>
                    <tr style="background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;">👮 PEMANTAU STAM</td>
                        <td style="padding:11px 14px; font-weight:600;">{pemantau_html}</td>
                    </tr>
    '''
# MUET - Template tiada Sidang, tiada Station
else:  # MUET
    table_rows = f'''
                    <tr style="background:#F8FAFC; border-bottom:2px solid #E8EEF6;">
                        <td style="padding:11px 14px; width:26%; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #EEF2F7;">🎓 NAMA PUSAT MUET (Isi Sendiri - Semua Bulan)</td>
                        <td style="padding:11px 14px; font-weight:700; font-size:13px;">{sel['nama_sekolah']}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📍 NO PUSAT MUET / DAERAH</td>
                        <td style="padding:10px 14px;"><b style="color:#0D47A1;">{sel['no_pusat']}</b> <span style="margin-left:8px; background:#0D47A1; color:white; padding:4px 12px; border-radius:20px; font-weight:700; font-size:11px;">📍 {get_nama_daerah_from_pusat(sel['no_pusat'], sel.get('kod_ppd',''))} ({sel.get('kod_ppd','')})</span> <span style="margin-left:6px; background:#E0F7FA; color:#006064; padding:2px 8px; border-radius:10px; font-size:9px;">Jan-Dis 2026</span></td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">📅 TARIKH & MASA LAWATAN MUET</td>
                        <td style="padding:10px 14px;"><span style="background:#0D47A1; color:white; padding:3px 8px; border-radius:6px; font-size:11px;">{sel['tarikh_lawatan']}</span> <span style="background:#FFF8E1; color:#F57F17; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">🕒 {sel['masa_lawatan']}</span> <span style="background:#E8F5E9; color:#2E7D32; padding:3px 8px; border-radius:6px; font-size:11px; margin-left:4px;">📅 {sel.get('hari','')}</span> <b style="color:#0D47A1; margin-left:8px;">{sel['mata_pelajaran']}</b></td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">🎓 BILIK MUET (Tiada Sidang, Tiada Station)</td>
                        <td style="padding:10px 14px;">{bilik_html}</td>
                    </tr>
                    <tr style="background:#FFF3E0; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:800; color:#EF6C00; font-size:11px; border-right:1px solid #FFE0B2;">👮 KEHADIRAN PETUGAS MUET</td>
                        <td style="padding:10px 14px;">{petugas_html}</td>
                    </tr>
                    <tr style="background:#FAFBFC; border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; border-right:1px solid #EEF2F7;">👥 KEHADIRAN CALON MUET</td>
                        <td style="padding:10px 14px;">{calon_html}</td>
                    </tr>
                    <tr style="border-bottom:1px solid #F1F5F9;">
                        <td style="padding:11px 14px; font-weight:700; color:#475569; font-size:11px; background:#FAFBFC; border-right:1px solid #EEF2F7;">📝 ULASAN MUET</td>
                        <td style="padding:11px 14px; font-style:italic; background:#FFFEF7; border-left:3px solid #FFC107;">❝ {sel['ulasan'] or 'Tiada ulasan'} ❞</td>
                    </tr>
                    <tr style="background: linear-gradient(90deg, #EEF2FF 0%, #E0E7FF 100%);">
                        <td style="padding:11px 14px; font-weight:800; color:#0D47A1; font-size:11px; border-right:1px solid #C7D2FE;">👮 PEMANTAU MUET</td>
                        <td style="padding:11px 14px; font-weight:600;">{pemantau_html}</td>
                    </tr>
    '''

html_one = f"""
<div style="width:100%; display:flex; justify-content:center; padding:12px 8px; background: linear-gradient(135deg, #EEF2F7 0%, #E3EAF3 100%);">
    <div style="width:100%; max-width:860px; background:white; border-radius:20px; overflow:hidden; box-shadow: 0 20px 60px rgba(13,71,161,0.18); border:1px solid white; position:relative;">
        <div style="height:5px; background: linear-gradient(90deg, #FFC107 0%, #FFD54F 50%, #FFC107 100%);"></div>
        <div style="background: linear-gradient(135deg, #0A1931 0%, #0D47A1 45%, #1565C0 100%); padding:22px 26px; display:flex; justify-content:space-between; align-items:center;">
            <div style="flex:1;">
                <div style="background: rgba(255,193,7,0.2); color:#FFECB3; font-size:10px; font-weight:800; padding:3px 10px; border-radius:20px; display:inline-block; margin-bottom:6px;">{jenis_icon} SEKTOR PENTAKSIRAN & PEPERIKSAAN - {MODE}</div>
                <div style="color:white; font-size:20px; font-weight:900;">JABATAN PENDIDIKAN NEGERI SELANGOR</div>
                <div style="color:#90CAF9; font-size:11px; font-weight:700; margin-top:6px;">LAPORAN PEMANTAUAN {jenis_label_full} • {sel['tarikh_lawatan']} • {sel['masa_lawatan']}</div>
            </div>
            <div style="text-align:right; margin-left:20px;">
                <div style="background:white; color:#0D2A54; font-size:20px; font-weight:900; padding:10px 18px; border-radius:12px;">{sel['no_pusat']}</div>
                <div style="color:#FFECB3; font-size:9px; font-weight:700; margin-top:7px; text-align:center;">NO. PUSAT {MODE}</div>
            </div>
        </div>
        <div style="padding:18px; background:#F8FAFC;">
            <div style="display:flex; gap:14px;">
                <div style="flex:1.25; position:relative; border-radius:14px; overflow:hidden; height:195px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border:2px solid white;">
                    <img src="data:image/jpeg;base64,{IMG_D}" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:0; left:0; right:0; padding:12px; background: linear-gradient(transparent, rgba(0,0,0,0.7));">
                        <div style="color:white; font-size:11px; font-weight:800;">📸 DEWAN / BILIK {MODE}</div>
                    </div>
                </div>
                <div style="flex:1.25; position:relative; border-radius:14px; overflow:hidden; height:195px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border:2px solid white;">
                    <img src="data:image/jpeg;base64,{IMG_S}" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:0; left:0; right:0; padding:12px; background: linear-gradient(transparent, rgba(0,0,0,0.7));">
                        <div style="color:white; font-size:11px; font-weight:800;">🏫 BANGUNAN {MODE}</div>
                    </div>
                </div>
                <div style="flex:0.95; background:white; border-radius:14px; padding:14px 12px; box-shadow: 0 8px 24px rgba(13,71,161,0.1); border:1px solid #E8EEF6; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    {CHART_PAI_HTML}
                </div>
            </div>
        </div>
        <div style="padding:0 18px 18px;">
            <div style="background:white; border-radius:14px; overflow:hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border:1px solid #E8EEF6;">
                <table style="width:100%; border-collapse:collapse; font-size:12.5px;">
                    {table_rows}
                </table>
            </div>
        </div>
        <div style="padding:20px 26px; background:#F1F5F9; border-top:1px solid #E2E8F0; display:flex; justify-content:space-between; gap:24px;">
            <div style="text-align:center; flex:1; border-top:2px solid #0D47A1; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#0D47A1;">PEMANTAU</div>
                <div style="font-size:12px; font-weight:700; margin-top:4px;">{sel['nama_pemantau']}</div>
                <div style="font-size:9px; color:#64748B;">{sel['tarikh_submit']}</div>
            </div>
            <div style="text-align:center; flex:1; border-top:2px dashed #94A3B8; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#475569;">COP SEKOLAH / PUSAT</div>
                <div style="font-size:12px; font-weight:700; margin-top:4px;">{sel['no_pusat']}</div>
            </div>
            <div style="text-align:center; flex:1; border-top:2px solid #0D47A1; padding-top:10px; margin-top:30px;">
                <div style="font-size:11px; font-weight:800; color:#0D47A1;">PENGESAHAN JPN / PPD</div>
                <div style="font-size:9px; color:#64748B; margin-top:12px;">Tandatangan & Cop Rasmi</div>
            </div>
        </div>
        <div style="background: linear-gradient(90deg, #0D47A1 0%, #1565C0 100%); padding:10px 26px; display:flex; justify-content:space-between;">
            <div style="color:rgba(255,255,255,0.8); font-size:9px;">© 2026 JPN Selangor | e-Pemantauan • SPM, Amali, Ujian Bertutur, STAM & MUET | ✨ Created by Akashah Ismail</div>
            <div style="color:#A5D6A7; font-size:9px;">● SAH & DIREKODKAN</div>
        </div>
        <div style="height:5px; background: linear-gradient(90deg, #FFC107 0%, #FFD54F 50%, #FFC107 100%);"></div>
        <div style="background:#0A1931; padding:8px; text-align:center;">
            <span style="color:#FFECB3; font-size:10px; letter-spacing:0.5px;">✨ Created by <b style="color:white;">Akashah Ismail</b> | Sektor Pentaksiran & Peperiksaan JPN Selangor | 2026</span>
        </div>
    </div>
</div>
"""

components.html(html_one, height=740, scrolling=True)

st.divider()
c1, c2 = st.columns(2)
with c1:
    full_html = f"<html><head><meta charset='utf-8'></head><body>{html_one}</body></html>"
    st.download_button("🖨️ Cetak PDF / Cetak", full_html, file_name=f"Laporan_{MODE}_{sel['no_pusat']}_{sel['tarikh_lawatan']}.html", mime="text/html", use_container_width=True, type="primary")
with c2:
    df_one = pd.DataFrame([sel])
    out = BytesIO()
    with pd.ExcelWriter(out, engine='openpyxl') as writer: df_one.to_excel(writer, index=False)
    st.download_button("📊 Download Excel", out.getvalue(), file_name=f"{MODE}_{sel['no_pusat']}.xlsx", use_container_width=True)

if st.session_state.is_admin and filtered_list:
    df_all = pd.DataFrame(filtered_list)
    out_all = BytesIO()
    with pd.ExcelWriter(out_all, engine='openpyxl') as writer: df_all.to_excel(writer, index=False)
    st.download_button(f"📊 Download SEMUA ({len(filtered_list)} laporan) - Admin", out_all.getvalue(), file_name=f"SEMUA_{MODE}_ADMIN.xlsx", use_container_width=True)
