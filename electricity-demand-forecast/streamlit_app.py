""" GUI app main script """

import streamlit as st
from src.gui_app.app_pages import inference, exploration
# from app_pages import inference, exploration


st.set_page_config(page_title="Electricy Demand Predition", layout="wide")


APP_MODES = ["Exploratory Analysis", "Inference"]


def main():

    st.sidebar.title("What to do")
    st.title("Electricity Demand Forecast")
    st.write(
        """
    This work presents   time series analysis and modelling of electricity Demand for a Northern Indian region
    """
    )
    st.caption(
        "Source Code: [link](https://github.com/Uttkarsh3/Load-Forcasting)" 
    )
    st.caption(
        "Analysis Notebook: [link](https://github.com/Uttkarsh3/Load-Forcasting/blob/main/electricity-demand-forecast/notebooks/01-data-exploration.ipynb)"
    )
    # app_mode = st.sidebar.selectbox("Choose the app mode", APP_MODES, index=1)
    app_mode = st.sidebar.radio(
        label="Choose Page:",
        options=APP_MODES,
        captions=['', 'inference results from two models'],
        index=0,

    )
    if app_mode == "Inference":
        inference.main()
    elif app_mode == "Exploratory Analysis":
        exploration.main()


if __name__ == "__main__":
    main()
