import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="1G–5G Network Evolution",
    page_icon="📡",
    layout="wide"
)

# =====================================================
# PROFESSIONAL UI DESIGN
# =====================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

.kpi-card {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #ddd;
    background-color: #f8f9fa;
    margin-bottom: 15px;
}

.kpi-value {
    font-size: 28px;
    font-weight: 700;
}

.kpi-label {
    font-size: 15px;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 20px;
}

.generation-card {
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
    background-color: #ffffff;
}

.footer {
    text-align: center;
    padding: 25px;
    margin-top: 40px;
    border-top: 1px solid #ddd;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# DATA
# =====================================================

data = {
    "Generation": ["1G", "2G", "3G", "4G", "5G"],

    "Technology": [
        "Analog",
        "GSM / CDMA",
        "UMTS / HSPA",
        "LTE",
        "5G NR"
    ],

    "Speed_Mbps": [
        0.0024,
        0.064,
        2,
        100,
        1000
    ],

    "Display_Speed": [
        "2.4 Kbps",
        "64 Kbps",
        "2 Mbps",
        "100 Mbps+",
        "1 Gbps+"
    ],

    "Feature": [
        "Basic Voice Calls",
        "SMS & Digital Voice",
        "Mobile Internet",
        "High-Speed Internet",
        "Ultra-Fast & Low Latency"
    ],

    "Applications": [
        "Voice Communication",
        "SMS & MMS",
        "Video Calls & Web Browsing",
        "Streaming & Online Gaming",
        "IoT, Smart Cities & AR/VR"
    ],

    "Period": [
        "1980s",
        "1990s",
        "2000s",
        "2010s",
        "2020s"
    ]
}

df = pd.DataFrame(data)


# =====================================================
# CALCULATIONS
# =====================================================

speed_1g = df.iloc[0]["Speed_Mbps"]
speed_5g = df.iloc[4]["Speed_Mbps"]

speed_multiplier = speed_5g / speed_1g


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📡 Network Dashboard")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "📊 Speed Analysis",
        "🔍 Generation Details",
        "📈 Advanced Analytics",
        "🕒 Evolution Timeline",
        "📘 About Project",
        "📋 Project Summary",
        "📥 Download Report"
    ]
)


# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">'
        '📡 1G–5G Speed & Feature Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Mobile Network Evolution & Performance Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "This dashboard analyzes the evolution of mobile "
        "communication technologies from 1G to 5G."
    )

    # -------------------------------------------------
    # KPI CARDS
    # -------------------------------------------------

    st.header("📊 Key Project Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Generations",
            "5"
        )

    with c2:
        st.metric(
            "Highest Speed",
            "1 Gbps+"
        )

    with c3:
        st.metric(
            "Technology",
            "5G NR"
        )

    with c4:
        st.metric(
            "Speed Growth",
            f"{speed_multiplier:,.0f}×"
        )

    st.divider()

    # -------------------------------------------------
    # GENERATION FILTER
    # -------------------------------------------------

    st.header("🔍 Network Generation Filter")

    selected = st.selectbox(
        "Select Generation",
        df["Generation"]
    )

    selected_row = df[
        df["Generation"] == selected
    ].iloc[0]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Generation",
            selected_row["Generation"]
        )

    with c2:
        st.metric(
            "Speed",
            selected_row["Display_Speed"]
        )

    with c3:
        st.metric(
            "Technology",
            selected_row["Technology"]
        )

    st.info(
        f"📌 {selected_row['Feature']}"
    )

    st.divider()

    # -------------------------------------------------
    # SPEED CHART
    # -------------------------------------------------

    st.header("🚀 Network Speed Comparison")

    fig = px.bar(
        df,
        x="Generation",
        y="Speed_Mbps",
        text="Display_Speed",
        title="1G → 5G Speed Evolution"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -------------------------------------------------
    # NETWORK EVOLUTION
    # -------------------------------------------------

    st.subheader("📡 Mobile Network Evolution")

    flow_cols = st.columns(5)

    for i, row in df.iterrows():

        with flow_cols[i]:

            st.markdown(
                f"""
                <div class="generation-card">
                    <h2 style="text-align:center;">
                        {row['Generation']}
                    </h2>

                    <p style="text-align:center;">
                        <b>{row['Technology']}</b>
                    </p>

                    <p style="text-align:center;">
                        {row['Display_Speed']}
                    </p>

                    <p style="text-align:center;">
                        {row['Period']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    # -------------------------------------------------
    # PROJECT HIGHLIGHTS
    # -------------------------------------------------

    st.subheader("🎯 Project Highlights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        **📈 Speed Evolution**

        Mobile network speeds increased
        dramatically from 1G to 5G.
        """)

    with col2:
        st.info("""
        **🌐 Connectivity**

        Each generation introduced better
        connectivity and new services.
        """)

    with col3:
        st.info("""
        **🤖 Future Technology**

        5G supports IoT, smart cities,
        AR/VR and intelligent applications.
        """)


# =====================================================
# SPEED ANALYSIS
# =====================================================

elif page == "📊 Speed Analysis":

    st.title("📊 Speed Analysis")

    # -------------------------------------------------
    # BAR CHART
    # -------------------------------------------------

    fig = px.bar(
        df,
        x="Generation",
        y="Speed_Mbps",
        text="Display_Speed",
        title="Mobile Network Speed by Generation"
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------------------------------
    # LINE CHART
    # -------------------------------------------------

    st.subheader("📈 Speed Growth Trend")

    line = px.line(
        df,
        x="Generation",
        y="Speed_Mbps",
        markers=True,
        title="Speed Growth from 1G to 5G"
    )

    st.plotly_chart(
        line,
        use_container_width=True
    )

    st.info(
        "The chart represents the selected reference speeds "
        "used for this educational dashboard."
    )


# =====================================================
# GENERATION DETAILS
# =====================================================

elif page == "🔍 Generation Details":

    st.title("🔍 Generation Details")

    generation = st.selectbox(
        "Choose Generation",
        df["Generation"]
    )

    row = df[
        df["Generation"] == generation
    ].iloc[0]

    st.header(
        f"{generation} — {row['Technology']}"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Speed",
            row["Display_Speed"]
        )

    with c2:
        st.metric(
            "Period",
            row["Period"]
        )

    with c3:
        st.metric(
            "Technology",
            row["Technology"]
        )

    st.divider()

    st.subheader("✨ Main Feature")

    st.write(
        row["Feature"]
    )

    st.subheader("🌐 Applications")

    st.write(
        row["Applications"]
    )


# =====================================================
# ADVANCED ANALYTICS
# =====================================================

elif page == "📈 Advanced Analytics":

    st.title("📈 Advanced Network Analytics")

    st.write(
        "Compare network generations using speed "
        "and performance-related metrics."
    )

    st.divider()

    # -------------------------------------------------
    # 1G vs 5G
    # -------------------------------------------------

    st.header("⚡ 1G vs 5G")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "1G Speed",
            "2.4 Kbps"
        )

    with c2:
        st.metric(
            "5G Speed",
            "1 Gbps+"
        )

    with c3:
        st.metric(
            "Speed Increase",
            f"{speed_multiplier:,.0f}×"
        )

    st.divider()

    # -------------------------------------------------
    # SPEED IMPROVEMENT
    # -------------------------------------------------

    st.header("📊 Speed Improvement")

    improvement = []

    for i in range(len(df)):

        if i == 0:

            improvement.append(0)

        else:

            previous = df.iloc[i - 1]["Speed_Mbps"]
            current = df.iloc[i]["Speed_Mbps"]

            percentage = (
                (current - previous)
                / previous
            ) * 100

            improvement.append(percentage)

    improvement_df = pd.DataFrame({
        "Generation": df["Generation"],
        "Speed Improvement (%)": improvement
    })

    fig = px.bar(
        improvement_df,
        x="Generation",
        y="Speed Improvement (%)",
        text="Speed Improvement (%)",
        title="Speed Improvement Between Generations"
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -------------------------------------------------
    # DATA TABLE
    # -------------------------------------------------

    st.header("📋 Analytical Data")

    st.dataframe(
        improvement_df,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "🏆 5G provides the highest represented speed "
        "among the generations in this dashboard."
    )


# =====================================================
# TIMELINE
# =====================================================

elif page == "🕒 Evolution Timeline":

    st.title("🕒 Mobile Network Evolution Timeline")

    for i in range(len(df)):

        st.subheader(
            f"{df.iloc[i]['Generation']} — "
            f"{df.iloc[i]['Period']}"
        )

        st.write(
            f"**Technology:** "
            f"{df.iloc[i]['Technology']}"
        )

        st.write(
            f"**Speed:** "
            f"{df.iloc[i]['Display_Speed']}"
        )

        st.write(
            f"**Feature:** "
            f"{df.iloc[i]['Feature']}"
        )

        st.write(
            f"**Applications:** "
            f"{df.iloc[i]['Applications']}"
        )

        st.divider()


# =====================================================
# ABOUT PROJECT
# =====================================================

elif page == "📘 About Project":

    st.title("📘 About the Project")

    st.markdown("""
    ### 1G–5G Speed & Feature Dashboard

    This project presents the evolution of mobile communication
    technologies from 1G to 5G using an interactive dashboard.

    It compares network generations based on speed, technology,
    features, applications, and development period.
    """)

    st.divider()

    # Objectives

    st.header("🎯 Objectives")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        **1.** Understand the evolution of mobile networks.

        **2.** Compare the speed of 1G, 2G, 3G, 4G and 5G.

        **3.** Identify major features of each generation.

        **4.** Analyze applications of different technologies.
        """)

    with col2:

        st.markdown("""
        **5.** Visualize network growth using charts.

        **6.** Study the improvement in mobile connectivity.

        **7.** Provide an easy-to-understand comparison.

        **8.** Present the information through an interactive dashboard.
        """)

    st.divider()

    # Methodology

    st.header("⚙️ Methodology")

    st.markdown("""
    ### Step 1 — Data Collection

    Information about 1G–5G technologies, speeds, features,
    applications and time periods is collected.

    ### Step 2 — Data Preparation

    The collected information is organized into a structured
    Pandas DataFrame.

    ### Step 3 — Data Analysis

    Network speeds and generation-wise improvements are analyzed.

    ### Step 4 — Visualization

    Plotly is used to create interactive bar charts and line charts.

    ### Step 5 — Dashboard Development

    Streamlit is used to combine the analysis and visualizations
    into an interactive web dashboard.

    ### Step 6 — Comparison

    Different generations are compared based on speed,
    technology, features and applications.
    """)

    st.divider()

    # Technologies Used

    st.header("💻 Technologies Used")

    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:
        st.metric(
            "Programming",
            "Python"
        )

    with tech_col2:
        st.metric(
            "Dashboard",
            "Streamlit"
        )

    with tech_col3:
        st.metric(
            "Visualization",
            "Plotly"
        )

    st.divider()

    # Conclusion

    st.header("✅ Conclusion")

    st.markdown("""
    The 1G–5G evolution demonstrates the continuous development of
    mobile communication technology.

    Each generation introduced improvements in speed, connectivity,
    capacity, reliability and new applications.

    1G primarily provided voice communication, while later generations
    introduced SMS, mobile internet, high-speed data services and
    advanced applications.

    5G further enables technologies such as IoT, smart cities,
    AR/VR and low-latency communication.

    This dashboard provides an interactive and visual way to understand
    the major differences between mobile network generations.
    """)

    st.success(
        "📌 Project Summary: Mobile networks evolved from basic voice "
        "communication to high-speed, intelligent and connected systems."
    )


# =====================================================
# PROJECT SUMMARY
# =====================================================

elif page == "📋 Project Summary":

    st.title("📋 Project Summary")

    st.markdown("""
    ## 📡 1G–5G Speed & Feature Dashboard

    This project provides an interactive visualization of the evolution
    of mobile communication networks from 1G to 5G.
    """)

    st.divider()

    # Project Overview

    st.header("🔎 Project Overview")

    overview_col1, overview_col2 = st.columns(2)

    with overview_col1:

        st.markdown("""
        ### Problem

        Understanding the differences between mobile network generations
        can be difficult because each generation introduced different
        technologies, speeds and applications.
        """)

    with overview_col2:

        st.markdown("""
        ### Solution

        This dashboard provides a simple visual comparison of 1G, 2G,
        3G, 4G and 5G using interactive charts, tables and analytics.
        """)

    st.divider()

    # Key Findings

    st.header("📊 Key Findings")

    findings = [
        "1G introduced basic analog voice communication.",
        "2G introduced digital communication and SMS.",
        "3G enabled mobile internet and video calling.",
        "4G provided high-speed mobile broadband.",
        "5G provides very high speed, high capacity and low latency.",
        "Mobile networks have continuously expanded their applications."
    ]

    for finding in findings:

        st.markdown(
            f"✅ {finding}"
        )

    st.divider()

    # Future Scope

    st.header("🚀 Future Scope")

    future_scope = [
        "Add 6G technology when reliable standardized data becomes available.",
        "Use real-world network speed datasets.",
        "Add live network speed monitoring.",
        "Add geographical network coverage maps.",
        "Include latency and bandwidth comparison.",
        "Add AI-based network performance prediction.",
        "Develop a mobile-friendly version of the dashboard."
    ]

    for item in future_scope:

        st.markdown(
            f"🔹 {item}"
        )

    st.divider()

    # References

    st.header("📚 References")

    st.markdown("""
    1. International Telecommunication Union (ITU) – Mobile communication standards.

    2. 3GPP – Mobile communication technology specifications.

    3. GSMA – Mobile industry and network technology information.

    4. Streamlit Documentation – Dashboard development using Python.

    5. Plotly Documentation – Interactive data visualization.

    6. Pandas Documentation – Data analysis and manipulation.
    """)

    st.divider()

    # Final Project Statement

    st.header("🎓 Final Project Statement")

    st.success("""
    The project demonstrates how mobile communication technology has
    evolved from basic voice communication in 1G to high-speed and
    intelligent connectivity in 5G.

    The interactive dashboard makes this evolution easy to analyze
    and understand.
    """)

    st.info(
        "💡 This dashboard can be extended with real-time data, "
        "6G analysis, AI-based prediction and geographical visualization."
    )


# =====================================================
# DOWNLOAD REPORT
# =====================================================

elif page == "📥 Download Report":

    st.title("📥 Download Project Data")

    st.write(
        "Download the network dataset for your "
        "project documentation."
    )

    # CSV

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        "⬇️ Download CSV Dataset",
        csv,
        "1G_5G_network_dataset.csv",
        "text/csv"
    )

    st.divider()

    # Data Preview

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "✅ Dataset ready for project documentation."
    )


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

<b>1G–5G Speed & Feature Dashboard</b><br>

Mobile Network Evolution |
Developed using Python, Streamlit & Plotly

</div>
""", unsafe_allow_html=True)