import streamlit as st
import yaml
import plotly.graph_objects as go

# Load YAMLs
with open("questions.yaml") as f:
    questions = yaml.safe_load(f)
with open("recommendations.yaml") as f:
    roadmap = yaml.safe_load(f)

# Page config
st.set_page_config(page_title="IAM Compass", page_icon=":open_file_folder:")

st.title(":open_file_folder: IAM Compass")
st.markdown("Assess your organisation’s Information Asset Maturity")

# Collect scores
scores = {}
st.markdown("### 📊 Rate each domain (1 = strongly disagree :unlock:, 5 = strongly agree :lock:)")
for domain, question in questions.items():
    scores[domain] = st.slider(f"**{domain}**: {question}", 1, 5, 3)

# Show chart & roadmap
if st.button("📈 Generate IAM Profile & Roadmap"):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=list(scores.keys()),
        fill='toself',
        name='IAM Maturity'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🗺️ Maturity Roadmap")
    for domain, score in scores.items():
        if score <= 3:
            st.markdown(f"#### 📍 {domain}")
            st.warning(f"**Now:** {roadmap[domain]['now']}")
            st.info(f"**Next:** {roadmap[domain]['next']}")
            st.success(f"**Future:** {roadmap[domain]['future']}")

st.markdown("---")
st.markdown("### 📚 References")
st.caption("Bosua, R. (2025). ARE WE MANAGING OUR DIGITAL ASSETS EFFECTIVELY? MIS202, Week 10.")
st.caption("Evans, N., & Price, J. (2020). Development of a holistic model for the management of an enterprise’s information assets. Nternational Journal of Information Management, 54, 102193. https://doi.org/10.1016/j.ijinfomgt.2020.102193")
