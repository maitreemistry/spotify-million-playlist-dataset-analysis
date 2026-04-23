import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------- CONFIG ----------------------
st.set_page_config(page_title="Spotify Dashboard", layout="wide")

# ---------------------- STYLING ----------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #121212;
    color: white;
}
h1, h2, h3 {
    color: #1DB954;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- TITLE ----------------------
st.title("🎧 Spotify Playlist Intelligence Dashboard")

# ---------------------- KPIs ----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🎵 Total Tracks", "66,346,428")
col2.metric("📂 Total Playlists", "1,000,000")
col3.metric("📊 Avg Tracks/Playlist", "66.34")
col4.metric("⏱ Avg Duration (mins)", "3.91")

st.divider()

# ---------------------- PLAYLIST AVERAGES ----------------------
st.subheader("📊 Playlist Averages")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Tracks per Playlist", "66.34")
col2.metric("Avg Albums per Playlist", "49.59")
col3.metric("Avg Followers per Playlist", "2.59")

st.divider()

# ---------------------- FILTERS ----------------------
col1, col2 = st.columns(2)

# with col1:
#     artist_filter = st.selectbox("Filter by Artist", ["All","Drake","Kendrick Lamar"])

with col2:
    top_n = st.slider("Top N Artists", 5, 10, 10)

# ---------------------- TOP ARTISTS ----------------------
st.subheader("🔥 Top Artists")

artists = [
    "Drake","Kanye West","Kendrick Lamar","Rihanna",
    "The Weeknd","Eminem","Ed Sheeran","Future",
    "Justin Bieber","J. Cole"
]

counts = [
    847160,413297,353624,339570,316603,
    294667,272116,250734,243119,241560
]

df_artists = pd.DataFrame({"Artist": artists, "Mentions": counts})
df_artists = df_artists.head(top_n)

col1, col2 = st.columns([2,1])

with col1:
    fig, ax = plt.subplots()
    ax.barh(df_artists["Artist"], df_artists["Mentions"])
    ax.invert_yaxis()
    ax.set_xlabel("Mentions")
    st.pyplot(fig)

with col2:
    st.dataframe(df_artists, use_container_width=True)

st.info("🎧 Drake dominates playlist appearances, indicating strong cross-playlist popularity.")

st.divider()

# ---------------------- TOP TRACKS ----------------------
st.subheader("🎵 Top Tracks")

tracks_data = [
    ("HUMBLE.","Kendrick Lamar",46574),
    ("One Dance","Drake",43447),
    ("Broccoli","DRAM",41309),
    ("Closer","The Chainsmokers",41079),
    ("Congratulations","Post Malone",39987),
    ("Caroline","Aminé",35202),
    ("iSpy","KYLE",35138),
    ("Bad and Boujee","Migos",34999),
    ("Location","Khalid",34990),
    ("XO TOUR Llif3","Lil Uzi Vert",34922)
]

df_tracks = pd.DataFrame(tracks_data, columns=["Track","Artist","Plays"])
st.dataframe(df_tracks, use_container_width=True)

st.divider()

# ---------------------- TOP ALBUMS ----------------------
st.subheader("💿 Top Albums")

albums_data = [
    ("Views","Drake",208533),
    ("Stoney","Post Malone",156488),
    ("More Life","Drake",141701),
    ("DAMN.","Kendrick Lamar",141638),
    ("Beauty Behind The Madness","The Weeknd",136517),
    ("Coloring Book","Chance The Rapper",133050),
    ("American Teen","Khalid",120946),
    ("Culture","Migos",120017),
    ("Purpose","Justin Bieber",114885),
    ("The Life Of Pablo","Kanye West",113024)
]

df_albums = pd.DataFrame(albums_data, columns=["Album","Artist","Mentions"])

col1, col2 = st.columns([2,1])

with col1:
    fig2, ax2 = plt.subplots()
    ax2.barh(df_albums["Album"], df_albums["Mentions"])
    ax2.invert_yaxis()
    st.pyplot(fig2)

with col2:
    st.dataframe(df_albums, use_container_width=True)

st.divider()


# ---------------------- TOP FOLLOWED PLAYLISTS ----------------------
st.subheader("📈 Top Followed Playlists")

playlist_data = [
    ("That's What I Like",71643,39),
    ("Breaking Bad",53519,106),
    ("One Tree Hill",45942,111),
    ("My Little Pony",31539,85),
    ("Q1",27830,81),
    ("Jack's Playlist",23500,29),
    ("Rock Hits",22102,56),
    ("TOP POP",15842,52),
    ("FARRUKO",15123,13),
    ("Wiz Khalifa",14812,115)
]

df_playlists = pd.DataFrame(playlist_data, columns=[
    "Playlist","Followers","Tracks"
])

st.dataframe(df_playlists, use_container_width=True)

st.divider()


# ---------------------- PLAYLIST INSIGHTS ----------------------
st.subheader("📊 Playlist Insights")

col1, col2 = st.columns(2)

with col1:
    st.metric("Avg Albums per Playlist", "49.59")
    st.metric("Avg Followers per Playlist", "2.59")

with col2:
    labels = ['Personal', 'Collaborative']
    sizes = [97.7, 2.3]

    fig3, ax3 = plt.subplots()
    ax3.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig3)

st.info("🤝 Only ~2% playlists are collaborative → users mostly curate individually.")

st.divider()

# ---------------------- DISTRIBUTION ----------------------
st.subheader("📈 Playlist Length Distribution")

# data = np.random.exponential(scale=50, size=5000)

# fig4, ax4 = plt.subplots()
# ax4.hist(data, bins=60)
# ax4.set_xlabel("Tracks per Playlist")
# ax4.set_ylabel("Count")
# st.pyplot(fig4)

st.image("dist.png", caption="Playlist Distribution")

st.info("📈 Most playlists are short, with a long-tail of very large playlists.")

st.divider()

# ---------------------- RECOMMENDATION SYSTEM ----------------------
st.subheader("🎯 Song Recommendation System")

selected_song = st.selectbox("Select a song", ["Shape of You"])

st.write(f"Showing recommendations for: **{selected_song}**")

rec_data = [
    ("That's What I Like","Bruno Mars",0.296,26769),
    ("Closer","The Chainsmokers",0.285,40629),
    ("Despacito - Remix","Luis Fonsi",0.248,29924),
    ("Stay","Zedd",0.243,22449),
    ("Something Just Like This","The Chainsmokers",0.225,20368),
    ("I Don't Wanna Live Forever","Zayn",0.2256566683612947)
    ("Castle on the Hill","Ed Sheeran",0.224,12706),
    ("It Ain't Me","Kygo",0.223,20128),
    ("Paris","The Chainsmokers",0.222,16087),
    ("I'm the One","DJ Khaled",0.207,30800)
]

df_rec = pd.DataFrame(rec_data, columns=["Track","Artist","Confidence","Popularity"])

st.dataframe(df_rec, use_container_width=True)

# Confidence visualization
st.subheader("📊 Recommendation Confidence")

fig5, ax5 = plt.subplots()
ax5.barh(df_rec["Track"], df_rec["Confidence"])
ax5.invert_yaxis()
st.pyplot(fig5)

st.divider()

# ---------------------- PROJECT DESCRIPTION ----------------------
st.subheader("📌 About This Project")

st.write("""
This project analyzes **66M+ tracks across 1M Spotify playlists**.

### Features:
- 📊 Popularity analysis of artists, tracks, albums  
- 📈 Playlist behavior insights  
- 🎯 Recommendation system based on co-occurrence  

### Recommendation Logic:
- Tracks appearing together in playlists  
- Confidence score (association strength)  
- Global popularity weighting  

This dashboard presents insights in a clean, interactive format suitable for analytics and exploration.
""")