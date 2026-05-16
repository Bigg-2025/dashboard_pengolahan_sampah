import streamlit as st
import pandas as pd


def render_kpi(dff: pd.DataFrame):
    """Render 5 KPI metric cards."""
    metrics = [
        ("Total Timbulan",          f"{dff['Timbulan'].sum():,.0f}",                "ton/hari (tpd)"),
        ("Rata-rata Terkelola",     f"{dff['% S. Terkelola'].mean():.1f}%",         "dari total sampah"),
        ("Rata-rata Belum Terkelola", f"{dff['% S. Belum Terkelola'].mean():.1f}%", "dari total sampah"),
        ("Jumlah Kota/Kab",        f"{dff['Kota/Kabupaten'].nunique()}",            "wilayah tercakup"),
        ("Jumlah Provinsi",        f"{dff['Provinsi'].nunique()}",                  "provinsi aktif"),
    ]

    cols = st.columns(5)
    for col, (label, value, sub) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
                <div class="sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
