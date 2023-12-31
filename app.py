import streamlit as st
import pandas as pd

def main():
    try:
        df = pd.read_csv(r"https://raw.githubusercontent.com/tobiarnold/Movie_Recommendation/main/movies.csv")
        st.set_page_config(page_title="Movie Recommendation", page_icon="🎬", layout="wide")
        streamlit_style = """
               <style>
               div.block-container{padding-top:0rem;}
               [data-testid="stToolbar"]    {visibility: hidden;
                                               height: 0%;
                                               position: fixed;}
               [data-testid="stHeader"] {background: rgba(0,0,0,0);}
               .stApp {
                   background-image: url("https://raw.githubusercontent.com/tobiarnold/Movie_Recommendation/main/sl_121019_25870_69.jpg");
                   background-attachment: fixed;
                   background-size: cover;}
                .title-wrapper {
                   text-align: center;}
               .css-16idsys.e1nzilvr4 p {
                   color: blue; 
                   font-size: 22px;}
               [data-testid="stTickBarMin"] {color: white;}
               [data-testid="stTickBarMax"] {color: white;}
               [data-testid="stText"] {font-size: 18px}
                .css-7ym5gk.ef3psqc11 button {font-weight: bold;}
                .css-1vbkxwb.e1nzilvr4 p {font-size: 22px;color: blue;}
                .css-16idsys.e1nzilvr5 {color: white;}
                .css-183lzff.exotz4b0 {color: white;}
                .css-5rimss.e1nzilvr5 {color: white;}
               </style>
           """
        st.markdown(streamlit_style, unsafe_allow_html=True)
        # st.title("🎬 Random Movie Recommendation",container_style={'text-align': 'center'})
        st.markdown("<h1 style='text-align: center;color: white;'>🎬 Random Movie Recommendation</h1>",
                    unsafe_allow_html=True)
        genre = st.selectbox("Choose Genre",
                             options=['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama',
                                      'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance',
                                      'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western'])
        rating = st.slider("Choose Rating", df["vote_average"].min(), df["vote_average"].max(), (2.0, 10.0), step=1.0)

        year = st.slider("Choose Year", df["release_date"].min(), df["release_date"].max(),
                         (int(df["release_date"].min()), (int(df["release_date"].max()))))
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("Generate Random Movie"):
                df = df[df["genres"].str.contains(genre, case=False)]
                df = df[(df["vote_average"] >= rating[0]) & (df["vote_average"] <= rating[1])]
                df = df[(df["release_date"] >= year[0]) & (df["release_date"] <= year[1])]
                df_title = df.sample(n=1)
        try:
            with col2:
                text_title=df_title["title"]
                st.text(text_title.iloc[0])
                text_overview=df_title["overview"]
            st.write(text_overview.iloc[0])
            df_table = df_title.drop(["title","overview"], axis=1)
            st.dataframe(df_table)
        except:
            st.text("press button to generate random movie recommendations")
    except:
        st.text("Please choose other parameters or reload Webpage!")
main()
