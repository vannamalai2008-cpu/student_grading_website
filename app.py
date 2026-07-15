import streamlit as st

st.set_page_config(page_title="Student Portal", page_icon="??", layout="centered")

page = st.sidebar.selectbox("Go to page:", ["?? Home", "?? Grade Calculator"])

if page == "?? Home":
      st.title("?? Student Portal Home Page")
      st.write("### Welcome to the Student Performance Portal!")
      st.markdown("""
      This platform helps students and teachers analyze subject-wise academic scores instantly.

      * **Check Results:** Calculate exact percentages and check pass/fail statuses.
      * **Instant Feedback:** See your final semester qualification status.
      """)
      st.info("?? Note: The minimum passing marks required to clear any subject is 40 out of 100.")

elif page == "?? Grade Calculator":
      st.title("?? Student Grading Web Dashboard")
      col1, col2 = st.columns(2)
      with col1:
        math = st.number_input("Mathematics", min_value=0, max_value=100, value=75)
        science = st.number_input("Science", min_value=0, max_value=100, value=65)
        english = st.number_input("English", min_value=0, max_value=100, value=38)
      with col2:
        history = st.number_input("History", min_value=0, max_value=100, value=82)
        computer = st.number_input("Computer Science", min_value=0, max_value=100, value=90)

      subjects = {"Mathematics": math, "Science": science, "English": english, "History": history, "Computer Science": computer}
      st.markdown("---")

      all_passed = True
      total_marks = 0
      for subject, mark in subjects.items():
        total_marks += mark
        if mark >= 40:
          st.success(f"✅ **{subject}**: {mark}/100 — **PASS**")
        else:
          st.error(f"❌ **{subject}**: {mark}/100 — **FAIL**")
          all_passed = False

     st.markdown("---")
     percentage = (total_marks / 500) * 100
     st.metric(label="Overall Percentage", value=f"{percentage:.2f}%")

     if all_passed:
       st.success("?? FINAL RESULT: PASSED THE SEMESTER!")
     else:
       st.error("⚠️ FINAL RESULT: FAILED (Must clear all individual subjects)")
