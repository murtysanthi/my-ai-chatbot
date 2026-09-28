import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="wide"
)
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🤖 My AI Chatbot")

st.header("Ask Me Anything")

st.subheader("💡 Clear Your Doubts")

st.text("Enter your questions and explore interesting topics!")

st.markdown(
    "**This AI application will clear your doubts and make learning interesting!**"
)

st.caption("Simple AI Chatbot using Streamlit")

# ---------------- CODE EXAMPLE ----------------
with st.expander("🐍 View Python Example"):

    st.code("""
question = input("Enter your question: ")

if question:
    print("AI: Let me help you understand this topic!")
    """, language="python")

# ---------------- FORMULA ----------------
st.latex(r"E = mc^2")

st.divider()

# ---------------- USER INPUT ----------------
st.header("📝 Enter Your Details")

question = st.text_input(
    "❓ Enter your question:",
    placeholder="Example: What is Artificial Intelligence?"
)

message = st.text_area(
    "💬 Enter your message:",
    placeholder="Write your message here..."
)

# ---------------- NUMBER INPUT ----------------
age = st.number_input(
    "🎂 Enter your age:",
    min_value=1,
    max_value=100,
    value=18
)

# ---------------- SLIDER ----------------
value = st.slider(
    "📊 Select a value:",
    min_value=0,
    max_value=100,
    value=50
)

# ---------------- SELECT BOX ----------------
option = st.selectbox(
    "📚 Choose a subject:",
    ["Python", "Artificial Intelligence", "Machine Learning",
     "Data Science", "DBMS", "Other"]
)

# ---------------- MULTISELECT ----------------
options = st.multiselect(
    "💻 Select your interests:",
    ["Python", "Java", "C", "AI", "ML", "Web Development", "DBMS"]
)

# ---------------- RADIO BUTTON ----------------
choice = st.radio(
    "👤 Select your learning level:",
    ["Beginner", "Intermediate", "Advanced"]
)

# ---------------- CHECKBOX ----------------
agree = st.checkbox(
    "I want to receive AI-generated explanations."
)

# ---------------- TOGGLE ----------------
dark_mode = st.toggle(
    "🌙 Enable dark mode"
)

# ---------------- DATE ----------------
date = st.date_input(
    "📅 Select today's date:"
)

# ---------------- TIME ----------------
time = st.time_input(
    "⏰ Select a time:"
)

# ---------------- COLOR PICKER ----------------
color = st.color_picker(
    "🎨 Choose your favorite color:",
    "#00FF00"
)

# ---------------- FILE UPLOADER ----------------
uploaded_file = st.file_uploader(
    "📁 Upload a file:",
    type=["txt", "pdf", "csv"]
)

# ---------------- COLUMNS ----------------
st.divider()

st.header("⚙️ Chatbot Settings")

col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.slider(
        "AI Creativity",
        0.0,
        1.0,
        0.5
    )

with col2:
    max_words = st.number_input(
        "Maximum Words",
        min_value=50,
        max_value=1000,
        value=200
    )

with col3:
    language = st.selectbox(
        "Language",
        ["English", "Telugu", "Hindi"]
    )

# ---------------- CHATBOT SECTION ----------------
st.divider()

st.header("🤖 Chatbot")

if st.button("🚀 Ask AI", type="primary"):

    if question:

        with st.spinner("🤖 AI is thinking..."):
            import time
            time.sleep(2)

        st.success("Answer generated successfully!")

        st.chat_message("user").write(question)

        st.chat_message("assistant").write(
            "🤖 Let me help you understand this topic! "
            "Your question was: " + question
        )

    else:
        st.warning("⚠️ Please enter a question first.")

# ---------------- CHAT INPUT ----------------
st.divider()

st.header("💬 Chat")

user_message = st.chat_input(
    "Type your message here..."
)

if user_message:
    st.chat_message("user").write(user_message)

    st.chat_message("assistant").write(
        "Thanks for your message! 🤖"
    )

# ---------------- PROGRESS ----------------
st.divider()

st.header("📈 Learning Progress")

progress = st.progress(0)

if st.button("Start Learning"):
    for i in range(101):
        progress.progress(i)

    st.success("🎉 Learning session completed!")

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("⚙️ Settings")

    st.write("### About")

    st.info(
        "This is a beginner-friendly AI chatbot "
        "interface created using Streamlit."
    )

    st.checkbox("Enable notifications")

    st.selectbox(
        "Choose theme",
        ["Default", "Light", "Dark"]
    )

    if st.button("🗑️ Clear Chat"):
        st.info("Chat cleared!")

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "🤖 My AI Chatbot | Built with Python & Streamlit"
)