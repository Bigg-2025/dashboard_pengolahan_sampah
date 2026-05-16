import streamlit as st

# ── konfigurasi halaman (harus paling atas) ──────────────
st.set_page_config(
    page_title="Dashboard Pengelolaan Sampah",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── modul lokal ──────────────────────────────────────────
from theme       import CSS
from data_loader import load_data, load_geojson, apply_filters, agg_provinsi
from sidebar     import render_sidebar
from kpi         import render_kpi
from charts      import (
    chart_top10_kota, chart_jenis_tpa,
    chart_pengelolaan_provinsi, chart_scatter,
    chart_timbulan_provinsi, chart_boxplot_tpa,
    chart_map_timbulan, chart_map_terkelola, chart_map_belum,
)

# ── inject CSS ───────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)

# ── load data ────────────────────────────────────────────
df      = load_data()
geojson = load_geojson()

# ── sidebar / filter ─────────────────────────────────────
provinsi_sel, jenis_tpa_sel, timbulan_range = render_sidebar(df)
dff = apply_filters(df, provinsi_sel, jenis_tpa_sel, timbulan_range)

# ── header ───────────────────────────────────────────────
st.markdown("""
<div class="dashboard-header">
    <h1>♻️ Dashboard Pengelolaan Sampah Nasional</h1>
    <p>Analisis data timbulan &amp; pengelolaan sampah seluruh Indonesia</p>
</div>
""", unsafe_allow_html=True)

# ── KPI cards ────────────────────────────────────────────
render_kpi(dff)


# ── ROW 1 — Top 10 Kota & Distribusi Jenis TPA ───────────
def section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([3, 2])
with col_a:
    section("🏙️ Top 10 Kota/Kabupaten — Timbulan Terbesar")
    st.plotly_chart(chart_top10_kota(dff), use_container_width=True)

with col_b:
    section("🗑️ Distribusi Jenis TPA")
    st.plotly_chart(chart_jenis_tpa(dff), use_container_width=True)


# ── ROW 2 — Pengelolaan per Provinsi & Scatter ───────────
col_c, col_d = st.columns([3, 2])
with col_c:
    section("📊 Rata-rata Pengelolaan Sampah per Provinsi")
    st.plotly_chart(chart_pengelolaan_provinsi(dff), use_container_width=True)

with col_d:
    section("🔍 Timbulan vs % Belum Terkelola")
    st.plotly_chart(chart_scatter(dff), use_container_width=True)


# ── ROW 3 — Timbulan per Provinsi & Box Plot ─────────────
col_e, col_f = st.columns(2)
with col_e:
    section("🌏 Total Timbulan per Provinsi")
    st.plotly_chart(chart_timbulan_provinsi(dff), use_container_width=True)

with col_f:
    section("📦 Distribusi Timbulan per Jenis TPA")
    st.plotly_chart(chart_boxplot_tpa(dff), use_container_width=True)


# ── ROW 4 — PETA CHOROPLETH ──────────────────────────────
section("🗺️ Peta Persebaran Sampah Nasional")

if geojson:
    prov_map = agg_provinsi(dff)
    tab1, tab2, tab3 = st.tabs([
        "🟩 Total Timbulan",
        "✅ % Terkelola",
        "❌ % Belum Terkelola",
    ])
    with tab1:
        st.plotly_chart(chart_map_timbulan(prov_map, geojson), use_container_width=True)
    with tab2:
        st.plotly_chart(chart_map_terkelola(prov_map, geojson), use_container_width=True)
    with tab3:
        st.plotly_chart(chart_map_belum(prov_map, geojson), use_container_width=True)
else:
    st.info(
        "📍 File `gadm41_IDN_1.json` tidak ditemukan. "
        "Letakkan di folder yang sama untuk menampilkan peta.",
        icon="ℹ️",
    )


# ── TABEL DATA ───────────────────────────────────────────
section("📋 Tabel Data Detail")
with st.expander("Lihat Tabel Data", expanded=False):
    cols_show = [
        'Provinsi', 'Kota/Kabupaten', 'Jenis TPA',
        'Timbulan', '% S. Terkelola', '% S. Belum Terkelola',
    ]
    st.dataframe(
        dff[cols_show].sort_values('Timbulan', ascending=False).reset_index(drop=True),
        use_container_width=True,
        height=400,
    )
    csv = dff[cols_show].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="data_sampah_filter.csv",
        mime="text/csv",
    )


# ── FOOTER ───────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 2rem 0 0.5rem; color:#388E3C; font-size:0.8rem;">
    ♻️ Dashboard Pengelolaan Sampah Nasional &nbsp;|&nbsp; Data: KLHK &nbsp;|&nbsp; Built with Streamlit
</div>
""", unsafe_allow_html=True)
