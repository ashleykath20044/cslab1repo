import streamlit as st

st.set_page_config(page_title="Architecture Quiz")

st.title("Architecture Quiz")
st.write("Test your knowledge of basic architecture concepts!")
st.write("---")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'score' not in st.session_state:
    st.session_state.score = 0

#Q1: multiple choice: columns
st.subheader("Question 1: Classical Column Orders")
st.image("Images/columns.jpg", width=400)

q1_answer = st.radio(
    "Which classical column order is known for its ornate capital with acanthus leaves and scrolls?",
    ["Doric", "Ionic", "Corinthian", "Tuscan"], key="q1")#NEW

#Q2: multi-select: drawing types
st.subheader("Question 2: Architectural Drawing Types")
st.image("Images/Drawings.jpg", width=400)
q2_answer = st.multiselect(
    "Select ALL types of orthographic architectural drawings:",
    ["Plan", "Elevation", "Section", "Perspective", "Axonometric", "Isometric"], key="q2")#NEW

#Q3: number input: Frank Lloyd Wright
st.subheader("Question 3: Frank Lloyd Wright")
st.image("Images/FallingWater.jpg", width=400)

q3_answer = st.number_input(
    "What year was Frank Lloyd Wright's 'Fallingwater' house completed?",
    min_value=1800, max_value=2026, step=1, key="q3") #NEW

#Q4: select box: materials
st.subheader("Question 4: Construction Materials")
q4_answer = st.selectbox(
    "Which material is most commonly used for structural frames in modern skyscrapers?",
    ["Wood", "Brick", "Steel", "Concrete"], key="q4") #NEW

#Q5: slider: gothic period
st.subheader("Question 5: Gothic Architecture")
q5_answer = st.slider(
    "In approximately which century did Gothic architecture become most popular in Europe?",
    min_value=10, max_value=20, step=1, key="q5") #NEW

submit_button = st.button("Submit Quiz")

if submit_button:
    st.session_state.submitted = True
    score = 0
    
    if q1_answer == "Corinthian":
        score += 1
    
    correct_q2 = set(["Plan", "Elevation", "Section"])
    if set(q2_answer) == correct_q2:
        score += 1
    
    if q3_answer == 1937:
        score += 1
    
    if q4_answer == "Steel":
        score += 1
    
    if q5_answer == 13:
        score += 1
    
    st.session_state.score = score

if st.session_state.submitted:
    st.write("---")
    st.subheader("Quiz Results")
    
    score = st.session_state.score
    total = 5
    percentage = (score / total) * 100
    
    if percentage >= 80:
        st.success(f"Yay, you could become an architect! You scored {score}/{total} ({percentage:.0f}%)")
        st.balloons()  #NEW
    elif percentage >= 60:
        st.info(f"Good job, almost there! You scored {score}/{total} ({percentage:.0f}%)")
    else:
        st.warning(f"Keep on studying! You scored {score}/{total} ({percentage:.0f}%)")
    
    st.write("Answer Key")
    
    st.write("Question 1: Corinthian")
    if q1_answer == "Corinthian":
        st.write("Correct!")
    else:
        st.write(f"Incorrect! You answered: {q1_answer}")
    
    st.write("Question 2: Plan, Elevation, Section")
    if set(q2_answer) == set(["Plan", "Elevation", "Section"]):
        st.write("Correct!")
    else:
        st.write(f"Incorrect! You answered: {', '.join(q2_answer) if q2_answer else 'None'}")
    
    st.write("Question 3: 1937")
    if q3_answer == 1937:
        st.write("Correct!")
    else:
        st.write(f"Incorrect! You answered: {q3_answer}")
    
    st.write("Question 4: Steel")
    if q4_answer == "Steel":
        st.write("Correct!")
    else:
        st.write(f"Incorrect! You answered: {q4_answer}")
    
    st.write("Question 5: 13th century")
    if q5_answer == 13:
        st.write("Correct!")
    else:
        st.write(f"Incorrect! You answered: {q5_answer}th century")
    
    if st.button("Try Again"):
        st.session_state.submitted = False
        st.session_state.score = 0
        st.rerun()  #NEW
