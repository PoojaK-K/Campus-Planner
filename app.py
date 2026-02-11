import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Career & Lifestyle Planner", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #1d4350, #a43931);
}
h1, h2, h3, label {
    color: white;
}
.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}
.stButton>button {
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "form"

if "plan" not in st.session_state:
    st.session_state.plan = ""

# ---------------- PAGE 1 ----------------
if st.session_state.page == "form":

    st.title("🎓 AI-Based Career & Lifestyle Planner")

    name = st.text_input("Your Name")
    course = st.text_input("Course of Study (Eg: IT, CSE, B.Com, MBA, B.Sc etc.)")
    year = st.selectbox("Year of Study", ["1st Year", "2nd Year", "3rd Year", "Final Year"])
    interest = st.text_input("Area of Interest")
    budget = st.number_input("Enter Your Learning Budget (₹ per year)", min_value=0)
    diet_needed = st.radio("Do you need a Personalized Diet Plan?", ["Yes", "No"])

    if st.button("Generate Personalized Plan 🚀"):

        if name and course and interest:

            plan = f"Hello {name},\n\n"
            plan += f"📘 Course: {course}\n"
            plan += f"🎯 Area of Interest: {interest}\n\n"

            # Year Logic
            if year == "1st Year":
                plan += "• Focus on building strong academic foundations.\n"
                plan += "• Explore different domains within your course.\n"
            elif year == "2nd Year":
                plan += "• Start certifications and practical mini projects.\n"
            elif year == "3rd Year":
                plan += "• Focus on internships and skill specialization.\n"
            else:
                plan += "• Prepare for placements or higher studies seriously.\n"

            # Budget Logic
            if budget < 5000:
                plan += f"\n💰 With ₹{budget}, focus on free online platforms, library resources, and open-source tools.\n"
            elif 5000 <= budget < 25000:
                plan += f"\n💰 With ₹{budget}, invest in selected certifications and workshops.\n"
            else:
                plan += f"\n💰 With ₹{budget}, consider advanced certifications, mentorship programs, and premium skill training.\n"

            # Career Enhancement
            plan += "\n🚀 Career Enhancement Tips:\n"
            plan += "• Build a strong resume & LinkedIn profile.\n"
            plan += "• Participate in hackathons / seminars.\n"
            plan += "• Improve communication & problem-solving skills.\n"

            # Diet Plan
            if diet_needed == "Yes":
                plan += "\n🍎 Personalized Diet Plan:\n"
                plan += "Morning: Warm water + fruits + nuts for energy.\n"
                plan += "Afternoon: Balanced meal (carbohydrates + protein + vegetables).\n"
                plan += "Evening: Light snacks (sprouts / boiled corn / healthy snacks).\n"
                plan += "Night: Light dinner (soup / chapati / salad).\n"
                plan += "\n🏥 Healthcare Tips:\n"
                plan += "• Drink 2-3 liters of water daily.\n"
                plan += "• Avoid excessive junk food.\n"
                plan += "• Maintain 7-8 hours sleep.\n"
                plan += "• Exercise at least 20 minutes daily.\n"

            st.session_state.plan = plan
            st.session_state.page = "plan"
            st.rerun()

        else:
            st.warning("Please fill all required fields.")

# ---------------- PAGE 2 ----------------
elif st.session_state.page == "plan":

    st.title("📋 Your Customized Career Plan")

    st.markdown(f"<div class='card'>{st.session_state.plan}</div>", unsafe_allow_html=True)

    if st.button("Proceed to Feedback ➡"):
        st.session_state.page = "feedback"
        st.rerun()

# ---------------- PAGE 3 ----------------
elif st.session_state.page == "feedback":

    st.title("⭐ User Feedback Form")

    questions = [
        "1. Personalization quality",
        "2. Career guidance relevance",
        "3. Budget recommendation usefulness",
        "4. Course-specific suggestions",
        "5. Clarity of the action plan",
        "6. Diet & healthcare suggestions",
        "7. Efficiency of the plan",
        "8. Ease of use",
        "9. Would you recommend to others",
        "10. Overall satisfaction"
    ]

    ratings = []

    for q in questions:
        rating = st.slider(q, 1, 5, 3)
        ratings.append(rating)

    if st.button("Submit Feedback ⭐"):

        avg_rating = sum(ratings) / len(ratings)

        st.subheader(f"📊 Average Rating: {round(avg_rating,2)} / 5")

        if avg_rating >= 4:
            st.success("🌟 We’re delighted that you found the system satisfactory and effective!")
        elif avg_rating >= 3:
            st.info("🙂 Thank you! We will continue refining and improving the experience.")
        else:
            st.error("We sincerely apologize for not meeting expectations.")
            st.info("💙 We assure you continuous improvements for better personalization.")

    if st.button("Start Over 🔄"):
        st.session_state.page = "form"
        st.rerun()
