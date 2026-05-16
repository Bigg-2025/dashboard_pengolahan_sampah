# =========================================================
# TEMA WARNA HIJAU
# =========================================================

HIJAU_TUA   = "#1B5E20"
HIJAU       = "#2E7D32"
HIJAU_MED   = "#388E3C"
HIJAU_MUDA  = "#4CAF50"
HIJAU_CERAH = "#81C784"
HIJAU_PALE  = "#C8E6C9"
KUNING      = "#FDD835"
MERAH       = "#C62828"
MERAH_PALE  = "#FFCDD2"
KUNING_PALE = "#FFF9C4"
ABU         = "#ECEFF1"

# Palette urutan untuk bar/pie
HIJAU_PALET = [HIJAU_TUA, HIJAU_MED, HIJAU_MUDA, HIJAU_CERAH, HIJAU_PALE, "#A5D6A7", "#69F0AE"]

CSS = f"""
<style>
    .stApp {{
        background-color: #F1F8E9;
    }}
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {HIJAU_TUA} 0%, {HIJAU_MED} 100%);
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label {{
        color: {HIJAU_PALE} !important;
        font-weight: 600;
    }}
    .dashboard-header {{
        background: linear-gradient(135deg, {HIJAU_TUA} 0%, {HIJAU_MED} 60%, {HIJAU_MUDA} 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(27,94,32,0.25);
    }}
    .dashboard-header h1 {{
        color: white;
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 0.5px;
    }}
    .dashboard-header p {{
        color: {HIJAU_PALE};
        margin: 0.4rem 0 0 0;
        font-size: 1rem;
    }}
    .metric-card {{
        background: white;
        border-left: 5px solid {HIJAU_MUDA};
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
        height: 100%;
    }}
    .metric-card .label {{
        color: #555;
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.3rem;
    }}
    .metric-card .value {{
        color: {HIJAU_TUA};
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.1;
    }}
    .metric-card .sub {{
        color: #888;
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }}
    .section-title {{
        color: {HIJAU_TUA};
        font-size: 1.15rem;
        font-weight: 700;
        border-bottom: 3px solid {HIJAU_MUDA};
        padding-bottom: 0.4rem;
        margin-bottom: 1rem;
    }}
    h1, h2, h3 {{
        color: {HIJAU_TUA};
    }}
</style>
"""
