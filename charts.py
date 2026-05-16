import plotly.express as px
import plotly.graph_objects as go

from theme import (
    HIJAU_TUA, HIJAU_MED, HIJAU_MUDA, HIJAU_CERAH, HIJAU_PALE,
    KUNING, KUNING_PALE, MERAH, MERAH_PALE, HIJAU_PALET,
)

_LAYOUT_BASE = dict(
    paper_bgcolor='white',
    plot_bgcolor='white',
    font_color=HIJAU_TUA,
)

_XGRID = dict(gridcolor='#E8F5E9')
_YGRID = dict(gridcolor='#E8F5E9')


# ──────────────────────────────────────────────
# ROW 1
# ──────────────────────────────────────────────

def chart_top10_kota(dff):
    """Bar horizontal Top 10 Kota/Kab timbulan terbesar."""
    top10 = (
        dff.groupby('Kota/Kabupaten')['Timbulan']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        top10,
        x='Timbulan', y='Kota/Kabupaten',
        orientation='h',
        color='Timbulan',
        color_continuous_scale=[[0, HIJAU_PALE], [0.5, HIJAU_MED], [1, HIJAU_TUA]],
        labels={'Timbulan': 'Timbulan (tpd)', 'Kota/Kabupaten': ''},
        text='Timbulan',
    )
    fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
    fig.update_layout(
        **_LAYOUT_BASE,
        yaxis={'categoryorder': 'total ascending'},
        coloraxis_showscale=False,
        margin=dict(l=10, r=60, t=10, b=10),
        height=360,
    )
    fig.update_xaxes(**_XGRID)
    return fig


def chart_jenis_tpa(dff):
    """Donut chart distribusi Jenis TPA."""
    jenis = dff['Jenis TPA'].value_counts().reset_index()
    jenis.columns = ['Jenis TPA', 'Jumlah']
    fig = px.pie(
        jenis,
        names='Jenis TPA', values='Jumlah',
        color_discrete_sequence=HIJAU_PALET,
        hole=0.45,
    )
    fig.update_traces(textposition='outside', textinfo='percent+label')
    fig.update_layout(
        **_LAYOUT_BASE,
        margin=dict(l=10, r=10, t=20, b=10),
        height=360,
        showlegend=False,
    )
    return fig


# ──────────────────────────────────────────────
# ROW 2
# ──────────────────────────────────────────────

def chart_pengelolaan_provinsi(dff):
    """Grouped bar: % terkelola vs belum per provinsi (top 15)."""
    prov_agg = (
        dff.groupby('Provinsi')[['% S. Terkelola', '% S. Belum Terkelola']]
        .mean()
        .round(2)
        .reset_index()
        .sort_values('% S. Terkelola', ascending=False)
        .head(15)
    )
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Terkelola',
        x=prov_agg['Provinsi'], y=prov_agg['% S. Terkelola'],
        marker_color=HIJAU_MUDA,
        text=prov_agg['% S. Terkelola'].apply(lambda x: f'{x:.1f}%'),
        textposition='auto',
    ))
    fig.add_trace(go.Bar(
        name='Belum Terkelola',
        x=prov_agg['Provinsi'], y=prov_agg['% S. Belum Terkelola'],
        marker_color=MERAH,
        opacity=0.7,
    ))
    fig.update_layout(
        **_LAYOUT_BASE,
        barmode='group',
        margin=dict(l=10, r=10, t=10, b=80),
        height=370,
        legend=dict(orientation='h', yanchor='bottom', y=1.01, xanchor='right', x=1),
        xaxis_tickangle=-35,
        yaxis_title='Persentase (%)',
    )
    fig.update_xaxes(**_XGRID)
    fig.update_yaxes(**_YGRID)
    return fig


def chart_scatter(dff):
    """Scatter: Timbulan vs % Belum Terkelola."""
    fig = px.scatter(
        dff, x='Timbulan', y='% S. Belum Terkelola',
        color='Provinsi',
        hover_data=['Kota/Kabupaten', 'Jenis TPA'],
        labels={'Timbulan': 'Timbulan (tpd)', '% S. Belum Terkelola': '% Belum Terkelola'},
        color_discrete_sequence=px.colors.sequential.Greens_r,
    )
    fig.update_traces(marker=dict(size=7, opacity=0.75))
    fig.update_layout(
        **_LAYOUT_BASE,
        margin=dict(l=10, r=10, t=10, b=10),
        height=370,
        showlegend=False,
    )
    fig.update_xaxes(**_XGRID)
    fig.update_yaxes(**_YGRID)
    return fig


# ──────────────────────────────────────────────
# ROW 3
# ──────────────────────────────────────────────

def chart_timbulan_provinsi(dff):
    """Bar vertikal total timbulan per provinsi (top 15)."""
    prov = (
        dff.groupby('Provinsi')['Timbulan']
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )
    fig = px.bar(
        prov, x='Provinsi', y='Timbulan',
        color='Timbulan',
        color_continuous_scale=[[0, HIJAU_PALE], [1, HIJAU_TUA]],
        labels={'Timbulan': 'Total Timbulan (tpd)'},
        text='Timbulan',
    )
    fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
    fig.update_layout(
        **_LAYOUT_BASE,
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=10, b=80),
        height=360,
        xaxis_tickangle=-35,
    )
    fig.update_xaxes(**_XGRID)
    fig.update_yaxes(**_YGRID)
    return fig


def chart_boxplot_tpa(dff):
    """Box plot distribusi timbulan per jenis TPA."""
    fig = px.box(
        dff, x='Jenis TPA', y='Timbulan',
        color='Jenis TPA',
        color_discrete_sequence=HIJAU_PALET,
        labels={'Timbulan': 'Timbulan (tpd)'},
        points='outliers',
    )
    fig.update_layout(
        **_LAYOUT_BASE,
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=80),
        height=360,
        xaxis_tickangle=-20,
    )
    fig.update_xaxes(**_XGRID)
    fig.update_yaxes(**_YGRID)
    return fig


# ──────────────────────────────────────────────
# ROW 4
# ──────────────────────────────────────────────

def chart_gauge(dff):
    """Gauge chart rata-rata nasional % terkelola."""
    val = dff['% S. Terkelola'].mean()
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=val,
        number={'suffix': '%', 'font': {'size': 40, 'color': HIJAU_TUA}},
        delta={
            'reference': 50,
            'increasing': {'color': HIJAU_MUDA},
            'decreasing': {'color': MERAH},
        },
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': HIJAU_TUA},
            'bar': {'color': HIJAU_MUDA},
            'bgcolor': HIJAU_PALE,
            'steps': [
                {'range': [0, 30],  'color': MERAH_PALE},   # ← rgba-safe
                {'range': [30, 60], 'color': KUNING_PALE},
                {'range': [60, 100],'color': HIJAU_PALE},
            ],
            'threshold': {
                'line': {'color': HIJAU_TUA, 'width': 4},
                'thickness': 0.75,
                'value': val,
            },
        },
    ))
    fig.update_layout(
        **_LAYOUT_BASE,
        margin=dict(l=20, r=20, t=30, b=20),
        height=280,
    )
    return fig


def chart_heatmap(dff):
    """Heatmap % terkelola per provinsi & jenis TPA (top 10 provinsi)."""
    top_prov = dff.groupby('Provinsi')['Timbulan'].sum().nlargest(10).index
    pivot = (
        dff[dff['Provinsi'].isin(top_prov)]
        .pivot_table(
            index='Provinsi', columns='Jenis TPA',
            values='% S. Terkelola', aggfunc='mean',
        )
        .round(2)
    )
    fig = px.imshow(
        pivot,
        color_continuous_scale=[[0, MERAH_PALE], [0.5, KUNING], [1, HIJAU_MED]],
        labels={'color': '% Terkelola'},
        aspect='auto',
        text_auto='.1f',
    )
    fig.update_layout(
        **_LAYOUT_BASE,
        margin=dict(l=10, r=10, t=10, b=10),
        height=280,
        xaxis_tickangle=-20,
    )
    return fig


# ──────────────────────────────────────────────
# PETA CHOROPLETH
# ──────────────────────────────────────────────

def _choropleth_base(df_map, geojson, value_col, title, color_scale):
    """
    Selalu gunakan range data aktual (min–max) agar 3 warna
    merah–kuning–hijau terlihat jelas meski rentang nilai sempit.
    """
    vmin = df_map[value_col].min()
    vmax = df_map[value_col].max()
    # Midpoint persis di tengah rentang data
    vmid = (vmin + vmax) / 2

    fig = px.choropleth(
        df_map,
        geojson=geojson,
        featureidkey="properties.NAME_1",
        locations="NAME_1",
        color=value_col,
        color_continuous_scale=color_scale,
        range_color=[vmin, vmax],
        hover_name="Provinsi",
        hover_data={value_col: ':.2f', 'NAME_1': False},
        labels={value_col: title},
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        paper_bgcolor='white',
        margin=dict(l=0, r=0, t=40, b=0),
        height=480,
        title=dict(text=f"<b>{title}</b>", x=0.5, font=dict(size=16, color=HIJAU_TUA)),
        coloraxis_colorbar=dict(
            title=dict(
                text=title,
                font=dict(color=HIJAU_TUA),
            ),
            tickfont=dict(color=HIJAU_TUA),
            tickvals=[vmin, vmid, vmax],
            ticktext=[f"{vmin:.2f}", f"{vmid:.2f}", f"{vmax:.2f}"],
        ),
        font_color=HIJAU_TUA,
    )
    return fig


# Skala 3 warna konsisten: merah (rendah) → kuning (tengah) → hijau (tinggi)
_SCALE_RYG = [[0, MERAH], [0.5, KUNING], [1, HIJAU_MED]]
# Untuk "belum terkelola": hijau (rendah/bagus) → kuning → merah (tinggi/buruk)
_SCALE_GYR = [[0, HIJAU_MED], [0.5, KUNING], [1, MERAH]]
# Untuk timbulan: hijau muda → kuning → hijau tua (gradasi kepadatan)
_SCALE_TIM = [[0, HIJAU_PALE], [0.5, KUNING], [1, HIJAU_TUA]]


def chart_map_timbulan(df_map, geojson):
    return _choropleth_base(
        df_map, geojson,
        value_col='Timbulan',
        title='Total Timbulan (tpd)',
        color_scale=_SCALE_TIM,
    )


def chart_map_terkelola(df_map, geojson):
    # Rendah = merah (buruk), tinggi = hijau (baik)
    return _choropleth_base(
        df_map, geojson,
        value_col='% S. Terkelola',
        title='% Sampah Terkelola',
        color_scale=_SCALE_RYG,
    )


def chart_map_belum(df_map, geojson):
    # Rendah = hijau (bagus), tinggi = merah (buruk)
    return _choropleth_base(
        df_map, geojson,
        value_col='% S. Belum Terkelola',
        title='% Sampah Belum Terkelola',
        color_scale=_SCALE_GYR,
    )
