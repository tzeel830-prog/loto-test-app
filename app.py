import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Hadeeqa Manpower - LOTO Test", page_icon="📝", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    .stButton>button { width: 100%; font-weight: bold; }
    .main-header { text-align: center; color: #1a73e8; }
    .sub-header { text-align: center; color: #555; font-weight: normal; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

PASS_PERCENT = 90

# 29 LOTO Questions
QUESTIONS = [
    {"n": 1, "q": "Who is authorized to stop unsafe work?", "options": ["Only Managers", "All personnel", "Safety Inspectors only", "Supervisors only"], "answer": 1},
    {"n": 2, "q": "What are the 5 steps to stop work?", "options": ["Stop, Notify, Investigate, Communicate and Follow up", "Isolate, Tag, Test, Clear, Report", "Stop, Clear, Lock, Tag, Verify", "Notify, Lock, Tag, Clear, Restart"], "answer": 0},
    {"n": 3, "q": "Do contractor employees have authority to stop work?", "options": ["NO", "Only with written permission", "YES", "Only in extreme emergencies"], "answer": 2},
    {"n": 4, "q": "Locking and tagging equipment lets other operators know that the equipment is safe to work on and cannot be __________?", "options": ["Moved", "Cleaned", "Repaired", "Energized"], "answer": 3},
    {"n": 5, "q": "Isolation, lockout and hold tag (LOTO) applies to all conditions where unexpected startup of equipment can happen during _________?", "options": ["Normal operations", "Servicing and maintenance", "Emergency shutdown", "Daily inspection"], "answer": 1},
    {"n": 6, "q": "While equipment is being worked on, isolation and LOTO will prevent _________?", "options": ["Any operational delay", "Equipment breakdown", "A sudden release of energy or accidental startup", "High power consumption"], "answer": 2},
    {"n": 7, "q": "An isolation plan is needed for complex or non-routine isolations?", "options": ["TRUE", "FALSE", "Optional", "Only for electrical work"], "answer": 0},
    {"n": 8, "q": "What do you call the placement of a lockout device on to an energy isolating device?", "options": ["Tagout", "Hold tag", "Lockout", "Isolation"], "answer": 2},
    {"n": 9, "q": "Sometime 'DO NOT OPERATE' warning devices are placed on an energy isolation device, what is this called?", "options": ["Lockout", "Hold tag", "Safety notice", "Tag out / Hold tag"], "answer": 3},
    {"n": 10, "q": "What do you call workers who operate or use equipment that require servicing or maintenance under LOTO?", "options": ["Affected personnel", "Authorized personnel", "Safety Officers", "Contractors"], "answer": 0},
    {"n": 11, "q": "You can return a system to service after completing isolation only when any affected personnel are _________?", "options": ["On break", "Cleared from the area", "In the control room", "Notified by phone"], "answer": 1},
    {"n": 12, "q": "The minimum requirements, the roles and responsibilities for proponents, employees and contractors are defined in _________.", "options": ["GI 2.100", "GI 6.012", "GI 7.001", "SAEP 31"], "answer": 1},
    {"n": 13, "q": "Ensuring that personnel/operators comply with the LOTO requirements is the responsibility of department managers, division heads and _________.", "options": ["Contractors", "Safety Officers", "Supervisors", "Technicians"], "answer": 2},
    {"n": 14, "q": "The LOTO procedure is carried out only by personnel who are _________.", "options": ["On duty", "Senior staff", "Certified riggers", "Trained and authorized"], "answer": 3},
    {"n": 15, "q": "Circuit breakers and disconnect switches are examples of isolating points for _________.", "options": ["Electrical energy", "Mechanical energy", "Hydraulic energy", "Pneumatic energy"], "answer": 0},
    {"n": 16, "q": "Potential energy is also known as _________?", "options": ["Kinetic energy", "Stored energy", "Thermal energy", "Chemical energy"], "answer": 1},
    {"n": 17, "q": "What type of lock and tag must be used for isolation and lockout/tagout?", "options": ["Any heavy duty brass lock", "Standard commercial padlock", "Saudi Aramco approved lock, with one key and a Saudi Aramco tag", "Combination padlock with tag"], "answer": 2},
    {"n": 18, "q": "Select the type of energy that can cause harm or injury if not isolated.", "options": ["Electrical energy", "Sound energy", "Light energy", "Solar energy"], "answer": 0},
    {"n": 19, "q": "Select a method of Primary Isolation for piping equipment?", "options": ["Double block and bleed", "Blinding", "Single block valve", "Line disconnection"], "answer": 2},
    {"n": 20, "q": "Select a method of Positive Isolation for piping equipment?", "options": ["Single block valve", "Control valve closure", "Blinding", "Pressure relief valve"], "answer": 2},
    {"n": 21, "q": "Select the correct order for the electrical isolation steps.", "options": ["Lock, Tag, Clear, Try", "Clear, Lock, Tag, Try", "Tag, Lock, Try, Clear", "Try, Lock, Tag, Clear"], "answer": 0},
    {"n": 22, "q": "You should always verify that the isolation and lock-out and hold-tag has been properly done and equipment is ready to work on.", "options": ["FALSE", "TRUE", "Optional", "Only for high voltage"], "answer": 1},
    {"n": 23, "q": "For maintenance involving a small number of workers (usually less than six) a multiple lock clip (hasp) can be used at each isolation point.", "options": ["FALSE", "Not allowed", "TRUE", "Only with written permission"], "answer": 2},
    {"n": 24, "q": "Locks and tags can be removed only when _________.", "options": ["Shift changes", "Work time is over", "Supervisor requests it", "Equipment is safe to re-energize"], "answer": 3},
    {"n": 25, "q": "After completing maintenance, the first step of the LOTO removal procedure is to _________.", "options": ["Restore the work area", "Remove lockout devices", "Notify affected personnel", "Follow startup procedure"], "answer": 0},
    {"n": 26, "q": "The emergency procedure for the removal of a lock-out device is used when _________.", "options": ["Work is finished early", "The lock owner is not available", "Key is misplaced temporarily", "Shift supervisor changes"], "answer": 1},
    {"n": 27, "q": "Before LOTO devices are removed, all personnel who need to remain in the area must be _________.", "options": ["Evacuated", "Given extra PPE", "Notified of the start up", "Re-assigned"], "answer": 2},
    {"n": 28, "q": "An individual lock and tag should only be removed by _________.", "options": ["Safety officer", "Area supervisor", "Any authorized worker", "The person who installed it"], "answer": 3},
    {"n": 29, "q": "What are the steps to remove isolation, lock and tags, when work is completed?", "options": ["A. Restore the work area, B. Notify affected personnel, C. Remove all lockout devices and hold tags, D. Follow the startup procedure", "A. Remove tags, B. Clear area, C. Start machine, D. Report", "A. Notify manager, B. Unlock, C. Start system, D. Report", "A. Follow startup, B. Clear area, C. Start machine, D. Report"], "answer": 0}
]

# Session state initialization
if 'started' not in st.session_state:
    st.session_state.started = False
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.markdown("<h1 class='main-header'>Hadeeqa Manpower Recruitment Agency</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>Human Assets Training Institute - WPR LOTO Test</h3>", unsafe_allow_html=True)

# SCREEN 1: Student Details Registration
if not st.session_state.started and not st.session_state.submitted:
    with st.form("student_info"):
        st.subheader("Student Details")
        name = st.text_input("Student Full Name *")
        roll = st.text_input("Roll / ID Number *")
        email = st.text_input("Email Address *")
        
        btn = st.form_submit_button("Start Test")
        
        if btn:
            if name and roll and email:
                st.session_state.student_name = name
                st.session_state.student_roll = roll
                st.session_state.student_email = email
                st.session_state.started = True
                st.session_state.start_time = time.time()
                st.rerun()
            else:
                st.error("Please fill all required fields!")

# SCREEN 2: Question Engine (One-by-One)
elif st.session_state.started and not st.session_state.submitted:
    q_data = QUESTIONS[st.session_state.q_index]
    
    # Progress Bar
    progress = (st.session_state.q_index + 1) / len(QUESTIONS)
    st.progress(progress)
    st.caption(f"Question {st.session_state.q_index + 1} of {len(QUESTIONS)}")
    
    st.markdown(f"### {q_data['n']}. {q_data['q']}")
    
    already_selected = st.session_state.answers.get(q_data['n'], None)
    
    selected_option = st.radio(
        "Select Answer:", 
        q_data['options'], 
        index=already_selected if already_selected is not None else 0,
        disabled=(already_selected is not None)
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if already_selected is None:
            if st.button("Lock Answer & Next"):
                idx = q_data['options'].index(selected_option)
                st.session_state.answers[q_data['n']] = idx
                
                if st.session_state.q_index + 1 < len(QUESTIONS):
                    st.session_state.q_index += 1
                else:
                    st.session_state.submitted = True
                st.rerun()
        else:
            if st.button("Next Question"):
                if st.session_state.q_index + 1 < len(QUESTIONS):
                    st.session_state.q_index += 1
                else:
                    st.session_state.submitted = True
                st.rerun()

# SCREEN 3: Submission & Final Thank You Screen
elif st.session_state.submitted:
    st.success("✅ Aapka test kamyabi se submit ho gaya hai!")
    st.info("Result baad me announce kiya jayega.")
    st.caption("Aap ab is tab/window ko band kar sakte hain.")