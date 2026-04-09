import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_generator import (
    get_teams, get_points_table, get_top_batsmen, get_top_bowlers,
    get_latest_match, get_toss_analysis
)
from ml_model import MatchPredictor

# --- Page Configuration ---
st.set_page_config(
    page_title="TATA IPL 2025 Summary",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Professional Custom CSS ---
st.markdown("""
    <style>
    /* Main Background Pattern - Gold/Royal theme for Champions */
    .stApp {
        background-color: #0d1117;
        background-image: radial-gradient(circle at top center, rgba(184, 134, 11, 0.15), transparent 600px);
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #F8FAFC !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #FFD700, #DAA520, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        font-weight: 900;
        font-size: 3.5rem;
        margin-bottom: 0px;
    }

    /* Subheader accents */
    .section-title {
        border-left: 5px solid #DAA520;
        padding-left: 15px;
        margin-top: 30px;
        margin-bottom: 20px;
        color: #F1F5F9;
        font-size: 1.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* DataFrame styling overrides */
    div[data-testid="stDataFrame"] {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 215, 0, 0.2);
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    /* Sleek Metric Cards */
    .metric-card-container {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 2rem;
    }
    .pro-metric {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(218, 165, 32, 0.2);
        border-radius: 16px;
        padding: 25px 20px;
        text-align: center;
        flex: 1;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .pro-metric:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(255, 215, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border: 1px solid rgba(255, 215, 0, 0.5);
    }
    .pro-title {
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94A3B8;
        margin-bottom: 10px;
    }
    .pro-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #F8FAFC;
        margin: 0;
        line-height: 1.2;
    }
    .pro-winner {
        background: linear-gradient(45deg, #FFD700, #FBBF24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
    }

    /* Prediction Card */
    .prediction-card {
        background: linear-gradient(145deg, rgba(15,23,42,0.8), rgba(30,41,59,0.8));
        border: 1px solid rgba(218, 165, 32, 0.4);
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    
    /* Champion Banner Specific */
    .champ-banner {
        background: linear-gradient(90deg, rgba(220,38,38,0.2) 0%, rgba(30,41,59,0.5) 50%, rgba(220,38,38,0.2) 100%);
        border: 1px solid #DC2626;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 0 20px rgba(220,38,38,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Data ---
@st.cache_data
def load_data():
    teams = get_teams()
    points_df = get_points_table()
    bat_df = get_top_batsmen()
    bowl_df = get_top_bowlers()
    latest_match_info, latest_match_df = get_latest_match()
    toss_pie, toss_bar = get_toss_analysis()
    return teams, points_df, bat_df, bowl_df, latest_match_info, latest_match_df, toss_pie, toss_bar

@st.cache_resource
def load_model():
    return MatchPredictor()

teams, points_df, bat_df, bowl_df, latest_match_info, latest_match_df, toss_pie, toss_bar = load_data()
predictor = load_model()

# --- Header Layer ---
st.markdown('<div class="gradient-text">TATA IPL 2025</div>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5rem; color: #F8FAFC; text-transform: uppercase; font-weight: 600; letter-spacing: 2px;'>Championship Summary Dashboard</p>", unsafe_allow_html=True)

st.markdown("""
<div class="champ-banner">
    <h2 style="color: #FFD700; margin:0;">🏆 2025 CHAMPIONS: ROYAL CHALLENGERS BENGALURU 🏆</h2>
    <p style="color: #E2E8F0; margin-top: 5px; font-size: 1.1rem;">Maiden IPL Title • Defeated Punjab Kings by 6 Runs</p>
</div>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Official_Logo.svg/1200px-Indian_Premier_League_Official_Logo.svg.png", width=120)
    st.title("Hub Navigation")
    menu = st.radio("", [
        "🏁 Final Standings", 
        "⭐ Orange & Purple Caps", 
        "🏆 Grand Final Summary", 
        "⚖️ Team Head-to-Head", 
        "🪙 Tournament Conditions", 
        "🤖 Retrospective Simulator"
    ], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#DAA520; font-size:14px; font-weight:bold;'>Season completed permanently.</div>", unsafe_allow_html=True)

# --- Helper function for Plotly Layouts ---
def apply_pro_layout(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1", family="Inter"),
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False)
    )
    return fig

# --- Sections ---

if menu == "🏁 Final Standings":
    st.markdown('<div class="section-title">Final League Stage Standings</div>', unsafe_allow_html=True)
    
    # Quick Stats Row
    st.markdown(f"""
        <div class="metric-card-container">
            <div class="pro-metric" style="border-top: 4px solid #EF4444;"><div class="pro-title">League Table Topper</div><div class="pro-value pro-winner">PBKS</div></div>
            <div class="pro-metric" style="border-top: 4px solid #3B82F6;"><div class="pro-title">Points Required to Qualify</div><div class="pro-value text-blue-400">16</div></div>
            <div class="pro-metric" style="border-top: 4px solid #10B981;"><div class="pro-title">Teams Tied for Top Spot</div><div class="pro-value">2</div></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Points Table Grid
    col1, col2 = st.columns([3, 1])
    with col1:
        st.dataframe(
            points_df, 
            use_container_width=True,
            hide_index=False,
            column_config={
                "Team": st.column_config.TextColumn("Franchise Name", width="large"),
                "NRR": st.column_config.NumberColumn("Net Run Rate", format="%.3f"),
                "Points": st.column_config.ProgressColumn(
                    "Total Points",
                    min_value=0,
                    max_value=28,
                    format="%d"
                )
            }
        )
    with col2:
        st.success("✅ **Playoff Qualifiers:**\n1. Punjab Kings\n2. Royal Challengers Bengaluru\n3. Gujarat Titans\n4. Mumbai Indians")

elif menu == "⭐ Orange & Purple Caps":
    st.markdown('<div class="section-title">Official Award Winners</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔥 Orange Cap (Most Runs)", "🎯 Purple Cap (Most Wickets)"])
    
    with tab1:
        st.markdown(f"### 🏆 Orange Cap Winner: **{bat_df.iloc[0]['Player']}** ({bat_df.iloc[0]['Runs']} Runs)")
        fig1 = px.bar(
            bat_df, x="Player", y="Runs", text="Runs",
            hover_data=["Team", "Strike Rate", "Average"],
            color="Runs", color_continuous_scale="Oranges"
        )
        fig1.update_traces(textposition='outside', marker_line_width=0, opacity=0.9, textfont_size=16)
        apply_pro_layout(fig1)
        st.plotly_chart(fig1, use_container_width=True)

    with tab2:
        st.markdown(f"### 🎯 Purple Cap Winner: **{bowl_df.iloc[0]['Player']}** ({bowl_df.iloc[0]['Wickets']} Wickets)")
        fig2 = px.bar(
            bowl_df, x="Player", y="Wickets", text="Wickets",
            hover_data=["Team", "Economy", "Average"],
            color="Wickets", color_continuous_scale="Purples"
        )
        fig2.update_traces(textposition='outside', marker_line_width=0, opacity=0.9, textfont_size=16)
        apply_pro_layout(fig2)
        st.plotly_chart(fig2, use_container_width=True)

elif menu == "🏆 Grand Final Summary":
    st.markdown('<div class="section-title">Grand Final: RCB vs PBKS</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="metric-card-container" style="justify-content: center;">
            <div class="pro-metric" style="border-top: 4px solid #DC2626;">
                <div class="pro-title">{latest_match_info["Team 1"]}</div>
                <div class="pro-value" style="color: #F87171;">{latest_match_info["Score 1"]}</div>
            </div>
            <div class="pro-metric" style="background: transparent; border:none; max-width: 150px;">
                <div class="pro-value" style="color: #64748B; font-size: 4rem; padding-top: 10px;">VS</div>
            </div>
            <div class="pro-metric" style="border-top: 4px solid #EF4444;">
                <div class="pro-title">{latest_match_info["Team 2"]}</div>
                <div class="pro-value" style="color: #FCA5A5;">{latest_match_info["Score 2"]}</div>
            </div>
        </div>
        <div style="text-align: center; font-size: 1.8rem; margin-bottom: 2rem;">
            Match Result: <span style="color: #FFD700; font-weight: bold;">{latest_match_info["Winner"]}</span> 👑
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Grand Final Over-by-Over Chase")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=latest_match_df['Over'], y=latest_match_df['RCB Runs'], mode='lines+markers', name='RCB (Bat First)', line=dict(color='#DC2626', width=4), fill='tozeroy', fillcolor='rgba(220, 38, 38, 0.1)'))
    fig.add_trace(go.Scatter(x=latest_match_df['Over'], y=latest_match_df['PBKS Runs'], mode='lines+markers', name='PBKS (Chasing)', line=dict(color='#EF4444', width=4), fill='tonexty', fillcolor='rgba(239, 68, 68, 0.1)'))
    
    fig.update_layout(xaxis_title="Over", yaxis_title="Cumulative Runs", hovermode="x unified")
    apply_pro_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "⚖️ Team Head-to-Head":
    st.markdown('<div class="section-title">2025 Franchise Performance Comparison</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
       t1 = st.selectbox("Select Franchise 1", teams, index=2)
    with col2:
       t2 = st.selectbox("Select Franchise 2", teams, index=7)
       
    if t1 == t2:
        st.warning("⚠️ Please select two distinct franchises to compare.")
    else:
        st.markdown("<br>", unsafe_allow_html=True)
        t1_stats = points_df[points_df['Team'] == t1].iloc[0]
        t2_stats = points_df[points_df['Team'] == t2].iloc[0]
        
        comp_df = pd.DataFrame({
            "Metric": ["Wins", "Losses", "Points"],
            t1: [t1_stats["Wins"], t1_stats["Losses"], t1_stats["Points"]],
            t2: [t2_stats["Wins"], t2_stats["Losses"], t2_stats["Points"]]
        })
        
        fig = go.Figure(data=[
            go.Bar(name=t1, x=comp_df['Metric'], y=comp_df[t1], marker_color='#DAA520', opacity=0.9, text=comp_df[t1], textposition='auto'),
            go.Bar(name=t2, x=comp_df['Metric'], y=comp_df[t2], marker_color='#3B82F6', opacity=0.9, text=comp_df[t2], textposition='auto')
        ])
        fig.update_layout(barmode='group')
        apply_pro_layout(fig)
        st.plotly_chart(fig, use_container_width=True)

elif menu == "🪙 Tournament Conditions":
    st.markdown('<div class="section-title">Pitch Context & Toss Strategy of 2025</div>', unsafe_allow_html=True)
    labels, values = toss_pie
    decision_labels, decision_values = toss_bar
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Toss Impact on Outcome")
        fig1 = px.pie(names=labels, values=values, hole=0.6, color_discrete_sequence=['#F59E0B', '#3B82F6'])
        fig1.update_traces(textinfo='percent', hoverinfo='label+percent', textfont_size=16)
        fig1.update_layout(annotations=[dict(text='Toss Win<br>Impact', x=0.5, y=0.5, font_size=18, showarrow=False, font_color="#CBD5E1")])
        apply_pro_layout(fig1)
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.markdown("### Batting First vs Chasing")
        fig2 = px.bar(x=decision_labels, y=decision_values, text=[f"{v}%" for v in decision_values], color=decision_labels, color_discrete_sequence=['#EC4899', '#8B5CF6'])
        fig2.update_traces(textposition='auto', marker_line_width=0, opacity=0.9, textfont_size=20)
        fig2.update_layout(yaxis_title="Tournament Win Rate (%)", showlegend=False)
        apply_pro_layout(fig2)
        st.plotly_chart(fig2, use_container_width=True)

elif menu == "🤖 Retrospective Simulator":
    st.markdown('<div class="section-title">Oracle Predictor Engine</div>', unsafe_allow_html=True)
    st.markdown("Trained on the final 2025 dataset, see what the ML model thought the win probability was for historical matchups!")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
       team_a = st.selectbox("Franchise A", teams, index=2, key='pred_A') # default to RCB
    with col2:
       team_b = st.selectbox("Franchise B", teams, index=7, key='pred_B') # default to PBKS
       
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔮 SIMULATE 2025 MATCHUP", use_container_width=True, type="primary"):
        if team_a == team_b:
             st.error("Invalid configuration. Select two distinct franchises.")
        else:
             with st.spinner("Analyzing 2025 permutations and squad strengths..."):
                 winner, prob = predictor.predict_winner(team_a, team_b)
             
             st.markdown(f"""
                 <div class="prediction-card">
                     <h3 style="color: #94A3B8; text-transform: uppercase;">Simulated Prediction</h3>
                     <h1 style="color: #FFD700; font-size: 3rem; margin: 10px 0;">{winner}</h1>
                     <div style="font-size: 5rem; font-weight: 900; background: linear-gradient(135deg, #DAA520, #FBBF24); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{prob}%</div>
                     <p style="color: #64748B; font-size: 1.1rem;">Model confidence based on final 2025 data.</p>
                 </div>
             """, unsafe_allow_html=True)
