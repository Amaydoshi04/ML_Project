import streamlit as st

st.set_page_config(page_title="Sleep", page_icon=":zzz:", layout="wide")

st.title("Sleep Savvy")
st.markdown("### Your one-stop shop to upgrade your sleep health.")


col = st.columns((3, 3, 3), gap="medium")

with col[0]:
    with st.container(border=True):
        st.markdown(
            "55.64% of people have poor sleep quality, and 62% say they don't sleep as well as they'd like."
        )


with col[1]:
    with st.container(border=True):
        st.markdown(
            "Adults need at least seven hours of sleep per night, but more than one-third sleep less than that."
        )

with col[2]:
    with st.container(border=True):
        st.markdown(
            "Up to two-thirds of adults experience insomnia, and 2–9% have obstructive sleep apnea."
        )

st.markdown("")
st.markdown("")

st.markdown("## Do you want to sleep better? Let's get started!")
