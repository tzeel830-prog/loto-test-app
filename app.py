import streamlit as st
import time

# ---------------------------------------------------------
# Page Config & Styling
# ---------------------------------------------------------
st.set_page_config(page_title="Hadeeqa Manpower - WPR Grand Test", page_icon="📝", layout="centered")

# Header & Banner
st.info("🌟 Created by: Hadeeqa Manpower Recruitment Agency | Saudi Aramco WPR Grand Test (100 MCQs) 🌟")

TOTAL_TIME_SECONDS = 60 * 60  # 60 Minutes
PASS_PERCENT = 80

# ---------------------------------------------------------
# EXACT 100 MCQs WITH SHUFFLED ANSWERS (A, B, C, D)
# ---------------------------------------------------------
QUESTIONS = [
    {"n": 1, "q": "For how long a certificate is issued to Issuer and receiver?", "options": ["2 Years", "2 Months", "3 Years", "2 ½ Years"], "answer": 0},
    {"n": 2, "q": "Who will sign certificates of issuer?", "options": ["Manager of construction", "Their division/department head", "Head of T & D", "Shift supervisor"], "answer": 1},
    {"n": 3, "q": "Who will sign certificates of receiver?", "options": ["Manager of construction", "Head of T & D", "Their superintendent (division/department head)", "Shift supervisor"], "answer": 2},
    {"n": 4, "q": "A restricted area requires...", "options": ["That receiver responds to emergency", "Fire-watch to be present", "That work permit is issued/used", "Work Permit system to be implemented"], "answer": 3},
    {"n": 5, "q": "What do you call an area where work permits are required?", "options": ["A restricted area", "A controlled area", "A sensitive area", "A dangerous area"], "answer": 0},
    {"n": 6, "q": "Which of the following is Not a restricted area?", "options": ["Loading pier", "Dump site", "Gasoline station", "Tank farm"], "answer": 1},
    {"n": 7, "q": "Who decides whether an area should be restricted or not?", "options": ["Loss prevention", "Issuer", "The department manager", "As mentioned in GI 2.100"], "answer": 2},
    {"n": 8, "q": "Within how much distance from a hydrocarbon line, work permit is required?", "options": ["23 ft", "Inside fence area only", "100 ft", "75 ft (23 m)"], "answer": 3},
    {"n": 9, "q": "Within how many feet of a power line, work permit is required?", "options": ["50 ft (15 m)", "100 ft", "200 ft", "150 ft"], "answer": 0},
    {"n": 10, "q": "Who can decide that work/job is low risk (Low Risk Activity)?", "options": ["Receiver", "Proponent Management", "Shift Supervisor", "The Issuer"], "answer": 1},
    {"n": 11, "q": "Why is work permit required in restricted area?", "options": ["Precautions", "Control workers", "To control hazards", "To control equipment movement"], "answer": 2},
    {"n": 12, "q": "Why do we use the work permit system?", "options": ["To renew certificate", "To prevent accident", "To log accident", "To carryout job safely"], "answer": 3},
    {"n": 13, "q": "What is the purpose of work permit system?", "options": ["To authorize specific construction or maintenance work", "To authorize all work activities during T&I", "To document when receiver start works", "To ensure hot work is not done"], "answer": 0},
    {"n": 14, "q": "Work permit must be issued for...", "options": ["General work on general location", "Specific work on/at specific location", "Specific location and general work", "Specific work on general location"], "answer": 1},
    {"n": 15, "q": "We use work permit in hazardous area to...", "options": ["Check expired certificates", "Identify alternate services", "(To) be sure that precautions are taken", "Use a designated representative"], "answer": 2},
    {"n": 16, "q": "We use work permit in hazardous area to identify...", "options": ["The designated representative", "Expired permits", "Alternate receiver", "Hazards and recommend precautions"], "answer": 3},
    {"n": 17, "q": "A work permit lists...", "options": ["Minimum safety precautions", "Maximum safety precautions", "Government safety precautions", "OSHA safety precautions"], "answer": 0},
    {"n": 18, "q": "Who should point out all hazards and write on the work permit?", "options": ["The standby man", "The issuer / Designated representative", "The Firewatch", "The receiver"], "answer": 1},
    {"n": 19, "q": "Who should keep the work permit on job site?", "options": ["The Firewatch", "The issuer", "The receiver", "The standby man"], "answer": 2},
    {"n": 20, "q": "What must an Issuer & Receiver write along with his sign, while issuing/receiving work permit?", "options": ["Time and date and certificate number", "Gas test, badge number and certificate number", "Name, badge number and organization code", "Organization code, badge number and certificate number"], "answer": 3},
    {"n": 21, "q": "Who should ask for work permit before starting work?", "options": ["The receiver", "Standby man", "The Firewatch", "Group supervisor"], "answer": 0},
    {"n": 22, "q": "The receiver receive/request work permit from...", "options": ["Operation's Supervisor", "Certified Operation's Supervisor (Issuer)", "Authorized issuer", "Saudi Aramco Employee"], "answer": 1},
    {"n": 23, "q": "Who will issue work permit?", "options": ["Designated Receiver", "Senior operator", "Authorized issuer", "Saudi Aramco Employee"], "answer": 2},
    {"n": 24, "q": "What should receiver do first, before he asks for work permit from issuer?", "options": ["Tell his supervisor to go with him", "Shutoff the circuit breaker", "Get tools ready", "Present his certificate to issuer (and request for permit)"], "answer": 3},
    {"n": 25, "q": "Can a receiver refuse to sign a work permit?", "options": ["Yes, when he is not agreed with conditions", "No, he cannot", "When he thinks safety precautions are not sufficient", "He must sign"], "answer": 0},
    {"n": 26, "q": "Where must the receiver keep work permit after it is issued?", "options": ["With senior crew member", "Display at the job site or in his possession", "In the control room", "Within the 75 meters"], "answer": 1},
    {"n": 27, "q": "Why Issuer and Receiver go to site for Joint Site Inspection?", "options": ["To check other activities in area", "To count workforce", "To discuss safety hazards and precautions", "To check weather condition"], "answer": 2},
    {"n": 28, "q": "Which section of work permit form, receiver can fill/write-in?", "options": ["Section 2 - Hazard identification", "Hazard analysis checklist", "Cannot fill any section", "Section 1 - Work Description"], "answer": 3},
    {"n": 29, "q": "Who goes on the joint site inspection?", "options": ["The issuer/designated representative and receiver", "The issuer and the area foreman", "The issuer and designative representative", "The issuer and gas tester"], "answer": 0},
    {"n": 30, "q": "When is Joint Site Inspection (JSI) performed?", "options": ["When job is not urgent", "Before issuing work permit", "Always before confined space entry", "When work permit is to be cancel"], "answer": 1},
    {"n": 31, "q": "Who leads the joint site inspection?", "options": ["Receiver", "Firewatch", "Issuer (or his Designated representative)", "Firewatch and standby man"], "answer": 2},
    {"n": 32, "q": "Which section is considered as cornerstone in new work permit form?", "options": ["Joint site inspection", "Risk assessment", "Job safety analysis", "Hazard analysis checklist"], "answer": 3},
    {"n": 33, "q": "Work permit is issued for how many operational shifts?", "options": ["One operational shift", "Two operational shifts", "24 consecutive hours", "Two receivers shift"], "answer": 0},
    {"n": 34, "q": "Normally, the maximum time covered by a renewed permit shall not exceed...", "options": ["16 hours", "24 hours", "8 hours", "30 hours"], "answer": 1},
    {"n": 35, "q": "For how long an Extended Work Permit is approved/issued?", "options": ["Not more than 30 days", "30 days", "Not more than one operational shift", "10 days"], "answer": 0},
    {"n": 36, "q": "Who must sign a work permit to renew/extend?", "options": ["The new area Foreman and receiver", "Superintendent countersign", "The new issuer and receiver", "Designated representative and receiver"], "answer": 2},
    {"n": 37, "q": "To whom, the receiver can delegate/hand-over the permit when leaving job site?", "options": ["Certified issuer", "Senior craftsman", "Supervisor or Foreman", "Certified receiver"], "answer": 3},
    {"n": 38, "q": "Can a renewed permit be transferred?", "options": ["No, (already) renewed permit cannot be transferred", "Once there is no new permit copy available", "Yes, but only for one shift", "After taking sign from unit Foreman"], "answer": 0},
    {"n": 39, "q": "Who must sign the work permit to close it?", "options": ["Competent person", "(Both) Issuer and Receiver", "Gas Tester, Issuer and Receiver", "Designated Representative"], "answer": 1},
    {"n": 40, "q": "When must the work permit be closed?", "options": ["After gas test taken", "Before another permit is issued", "When the work is finished and/or work crew leaves", "Just before the end of shift"], "answer": 2},
    {"n": 41, "q": "Which is Saudi Aramco approved personal single gas monitor?", "options": ["Any calibrated gas monitor", "TX-1", "MX4", "T40 Rattler"], "answer": 3},
    {"n": 42, "q": "What information 'Work Location Box' on work permit gives?", "options": ["Exact location where receiver can work", "Where the receiver can go", "Very equipment which receiver can use", "None of above"], "answer": 0},
    {"n": 43, "q": "A work permit must be written in...", "options": ["Arabic", "English", "Ink pen", "Arabic and led pencil"], "answer": 1},
    {"n": 44, "q": "The issuer must stop work if...", "options": ["When the issuer goes to his office", "The issuer left the job site", "The job is found (to be) unsafe", "The issuer lost his copy of permit"], "answer": 2},
    {"n": 45, "q": "The receiver must stop work if...", "options": ["He cannot find the issuer", "The designated representative must leave", "The issuer leaves the job site", "The work site become unsafe"], "answer": 3},
    {"n": 46, "q": "In Saudi Aramco facilities areas, who can stop unsafe work?", "options": ["Everyone (Anyone)", "Proponent manager", "Receiver and issuer", "Safety Officers"], "answer": 0},
    {"n": 47, "q": "How many steps are there in Stop Work Authority?", "options": ["Only three steps", "Five", "Too many steps", "As much required by issuer"], "answer": 1},
    {"n": 48, "q": "What is the difference between hot work and cold work?", "options": ["Cold work use ignition source", "Both use an ignition source", "Hot work involves ignition source, while cold work does not", "Neither use an ignition source"], "answer": 2},
    {"n": 49, "q": "Cold work includes...", "options": ["Scaffold erection and using backhoe", "Abrasive blasting and painting", "Carpentry work and brush painting", "Sand removal and scaffold erection"], "answer": 3},
    {"n": 50, "q": "What should be checked before allowing entry into confined space?", "options": ["Lighting, standby man and air mover", "Gas test, Firewatch and barricade", "Firewatch, standby man and gas test", "Air mover, respirator, and countersignature"], "answer": 0},
    {"n": 51, "q": "At what depth of an excavation, confined space entry permit requirement starts?", "options": ["4 m", "4 ft (1.2 m)", "2.2 m", "1.2 ft"], "answer": 1},
    {"n": 52, "q": "What is required distance for a scaffold base from edge of excavation?", "options": ["Height of scaffold x depth of excavation", "2.6 m", "1.5 x depth of excavation", "1 m"], "answer": 2},
    {"n": 53, "q": "Motor vehicles and heavy equipment shall be kept away from edge of excavation by...", "options": ["1.5 x depth of excavation", "1.8 m (6 ft)", "3 m (10 ft)", "2 m (6.5 ft) or the depth of excavation"], "answer": 3},
    {"n": 54, "q": "Which equipment can operate within 2-m from edge of excavation?", "options": ["Excavation and Backfilling Equipment", "Crane", "Welding truck", "None of above"], "answer": 0},
    {"n": 55, "q": "What is minimum required distance to be maintained from energized overhead 50kV powerline?", "options": ["25 ft", "10 ft", "20 ft", "3 ft"], "answer": 1},
    {"n": 56, "q": "Who will take gas test in Saudi Aramco?", "options": ["Anyone who know how to use gas monitor", "Work permit receiver", "Saudi Aramco Certified Gas Tester", "Third party certified Gas Tester"], "answer": 2},
    {"n": 57, "q": "What information gas tester needs to write on work permit?", "options": ["Time and date and certificate number", "Organization code, badge number and gas test result", "Gas test, badge number, Name and certificate number", "Gas test result, his badge number and sign"], "answer": 3},
    {"n": 58, "q": "What are the common gases checked in a gas test?", "options": ["O2, LEL, H2S, CO", "Oxygen level", "Flammable gas, inert gas and heavy gas", "Oxygen, flammable and toxic gases"], "answer": 0},
    {"n": 59, "q": "What is oxygen deficiency?", "options": ["Oxygen that is not pure", "Lower than 20% oxygen", "Too much oxygen", "A lower-than acceptable amount/range of oxygen"], "answer": 1},
    {"n": 60, "q": "At which level of oxygen, breathing apparatus is required?", "options": ["At 25%", "Less than 10%", "Less than 20%", "Greater than 15%"], "answer": 2},
    {"n": 61, "q": "Hot work is NOT allowed if LEL reading is...", "options": ["10%", "0.05", "Below 0.5%", "Above 0% (0.0)"], "answer": 3},
    {"n": 62, "q": "On which reading of LEL, entry is not permitted in confined space?", "options": ["10% LEL (0.1 LEL) and above", "0.5 LEL", "0.05 LEL", "50% LEL"], "answer": 0},
    {"n": 63, "q": "On which concentration of H2S, breathing apparatus is required?", "options": ["5 PPM", "10 PPM and above", "1 PPM", "Above 50 PPM"], "answer": 1},
    {"n": 64, "q": "Confined space entry is not allowed if H2S is...", "options": ["CO is 1000 ppm", "LEL 10%", "Above 100 ppm", "All of Above"], "answer": 2},
    {"n": 65, "q": "When Firewatch is required?", "options": ["When a gas test is over %LEL", "For high-risk job", "Whenever a fire could occur", "Whenever an ignition source is used"], "answer": 3},
    {"n": 66, "q": "What is the main responsibility of Firewatch?", "options": ["To monitor an ignition source", "Help welder in welding work", "Check electrical generators", "Use proper PPEs"], "answer": 0},
    {"n": 67, "q": "Who will stay on hot work location for 30 minutes after work is finished?", "options": ["Pipefitter", "Firewatch", "Standby man", "Any person"], "answer": 1},
    {"n": 68, "q": "For welding activity, portable fire extinguisher shall be available within...", "options": ["23 m (75 ft)", "Not required for welding job", "3 m (10 ft)", "7.5 m (25 ft)"], "answer": 2},
    {"n": 69, "q": "During welding operation, where will your fire extinguisher be located?", "options": ["With welder", "On welding machine", "Downwind position", "Upwind position/direction"], "answer": 3},
    {"n": 70, "q": "Which work permit requires sewers (drains) to be covered up to 75 ft?", "options": ["Hot work permit", "Cold work permit", "No work permit has such requirement", "Confined space entry permit"], "answer": 0},
    {"n": 71, "q": "When LOTO is installed?", "options": ["Before work is finished", "Before work permit is issued", "When supervisor wants to", "When extending a permit"], "answer": 1},
    {"n": 72, "q": "Where must Lock Out Tag Out (LOTO) be used?", "options": ["All electrical works in restricted area", "Where a person has to work on live equipment", "Where energy can cause injury", "Where work is on instrument panel"], "answer": 2},
    {"n": 73, "q": "What are the 4 steps process to make sure electrical equipment is properly isolated?", "options": ["Lock, Tag, Try and Clear", "Clear area, lock equipment test switch and tag", "LOCK, TRY, CLEAR & TAG", "LOCK, TAG, CLEAR & TRY"], "answer": 3},
    {"n": 74, "q": "We isolate equipment to make sure that it cannot...", "options": ["Start-up, leak or cause electric shock", "Slip trip or fall", "Shutdown by accident", "Taken to shop for repair"], "answer": 0},
    {"n": 75, "q": "Which Isolation method is required for Confined Space Entry?", "options": ["Single Block Valve", "Disconnection and Blinding (Positive Isolation)", "Double Block and Bleed", "Any method"], "answer": 1},
    {"n": 76, "q": "Why do we install tag with lock?", "options": ["To record a gas test", "To list safety precautions", "To communicate reason and authorization of isolation", "To explain why lock is installed"], "answer": 2},
    {"n": 77, "q": "Who will install lock and hold tag for maintenance work?", "options": ["Maintenance only", "Each member of crew", "Operations Only", "Operations & Maintenance"], "answer": 3},
    {"n": 78, "q": "Who should be the first organization to install lock and tag?", "options": ["Operations", "SCECO", "Maintenance", "Power distribution"], "answer": 0},
    {"n": 79, "q": "How many keys for one lock used in LOTO?", "options": ["3 for each lock", "One only", "As many crew members", "One for issuer and one for receiver"], "answer": 1},
    {"n": 80, "q": "Who can remove lock once installed?", "options": ["Anyone who want to start equipment", "Foreman of working crew", "The one who installed lock / lock owner", "No one can remove it once locked"], "answer": 2},
    {"n": 81, "q": "Who can forcefully remove an isolation lock when owner of lock cannot be contacted?", "options": ["No one can remove a lock once installed", "Supervisor of working crew", "Person who installs lock", "Operation's shift superintendent"], "answer": 3},
    {"n": 82, "q": "What is the most dangerous source of energy?", "options": ["Potential (Stored) Energy", "Drained energy", "Disconnected energy", "Connected energy"], "answer": 0},
    {"n": 83, "q": "When installing blind on line containing H2S, what precautions will be taken?", "options": ["Use of cartage respirator", "Use of SCBA", "Use of any respirator", "No need to use respirator"], "answer": 1},
    {"n": 84, "q": "Chemical Hazard Bulletin (CHB) provides what important information?", "options": ["How to use chemical", "Only physical properties of chemical", "Hazards involved and precautions for handling chemical", "Expiry date of chemical"], "answer": 2},
    {"n": 85, "q": "What is the required setback distance for excavation spoil soil from edge?", "options": ["2 m (6.6 ft)", "1.2 m (4 ft)", "Any distance", "0.6 m (2 ft)"], "answer": 3},
    {"n": 86, "q": "What is the hazard in excavation by backhoe?", "options": ["Accidental contact with underground utility lines", "1 m (3 ft)", "1.8 m (6 ft)", "It can rupture underground utility lines or pipelines"], "answer": 0},
    {"n": 87, "q": "Ladder should extend how much above the landing area?", "options": ["30 ft", "3 ft (1 m)", "30 in", "3 metre"], "answer": 1},
    {"n": 88, "q": "What is a confined space?", "options": ["Small rooms and CCRs", "Storerooms", "Structure/Space not designed for human occupancy", "Buildings to store computer & equipment"], "answer": 2},
    {"n": 89, "q": "If any part of body enters a confined space, it will be considered as Entry.", "options": ["2 parts", "Legs", "Head and neck", "Any"], "answer": 3},
    {"n": 90, "q": "What do we call the person required to be at job site due to special skill?", "options": ["Standby man", "Competent person", "Designated representative", "Certified"], "answer": 0},
    {"n": 91, "q": "What is the main responsibility of Confined Space Entry Standby Man?", "options": ["To record progress of work", "To monitor confined space entry when crew is inside space", "Only to be present in area", "Inform rescue in case of emergency"], "answer": 1},
    {"n": 92, "q": "To work in high noise area, which PPE is required?", "options": ["Safety Glasses", "Safety glasses and face shield", "Hearing protection (Earplug/Earmuff)", "Proper footwear protection"], "answer": 2},
    {"n": 93, "q": "What is the purpose of using Full-Body Harness and Lanyard?", "options": ["To control movement of a worker", "To show safety officer", "To keep protect harness", "To arrest a fall (to protect from falling)"], "answer": 3},
    {"n": 94, "q": "Heavy equipment operations are the most common causes of work-related fatalities in Saudi Aramco.", "options": ["True", "False"], "answer": 0},
    {"n": 95, "q": "When conducting a gas test in H2S suspected environment, SCBA or SABA must be used.", "options": ["False", "True"], "answer": 1},
    {"n": 96, "q": "Positive isolation must be achieved during equipment opening line break.", "options": ["True", "False"], "answer": 0},
    {"n": 97, "q": "The safety of work site is a sole responsibility of an issuer.", "options": ["True", "False"], "answer": 1},
    {"n": 98, "q": "Any worker can be assigned as standby man.", "options": ["True", "False"], "answer": 1},
    {"n": 99, "q": "Breathing in high concentration of H2S is lethal (can cause death).", "options": ["True", "False"], "answer": 0},
    {"n": 100, "q": "Isolation locks usually have two keys to ensure when one lost, other can be used.", "options": ["False", "True"], "answer": 0}
]

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if 'started' not in st.session_state:
    st.session_state.started = False
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# App Titles
st.title("Hadeeqa Manpower Recruitment Agency")
st.caption("Saudi Aramco WPR Grand Test - 100 Questions")

# ---------------------------------------------------------
# SCREEN 1: Candidate Form
# ---------------------------------------------------------
if not st.session_state.started and not st.session_state.submitted:
    with st.form("student_info"):
        st.subheader("Candidate Information")
        name = st.text_input("Candidate Full Name *")
        roll = st.text_input("Roll / Badge Number *")
        email = st.text_input("Email Address *")
        
        btn = st.form_submit_button("Start 60-Minute Grand Test")
        
        if btn:
            if name and roll and email:
                st.session_state.student_name = name
                st.session_state.student_roll = roll
                st.session_state.student_email = email
                st.session_state.started = True
                st.session_state.start_time = time.time()
                st.rerun()
            else:
                st.error("Please fill all required details!")

# ---------------------------------------------------------
# SCREEN 2: Question Engine & Live Timer
# ---------------------------------------------------------
elif st.session_state.started and not st.session_state.submitted:
    elapsed_time = int(time.time() - st.session_state.start_time)
    remaining_time = TOTAL_TIME_SECONDS - elapsed_time
    
    if remaining_time <= 0:
        st.session_state.submitted = True
        st.error("⏰ Time is UP! Your 60 minutes have expired. Auto-submitting test...")
        st.rerun()

    mins, secs = divmod(remaining_time, 60)
    
    st.sidebar.markdown("### ⏱️ Time Remaining")
    st.sidebar.title(f"{mins:02d}:{secs:02d}")
    st.sidebar.progress(remaining_time / TOTAL_TIME_SECONDS)
    
    q_data = QUESTIONS[st.session_state.q_index]
    progress = (st.session_state.q_index + 1) / len(QUESTIONS)
    st.progress(progress)
    st.caption(f"Question {st.session_state.q_index + 1} of {len(QUESTIONS)}")
    
    st.markdown(f"### Q{q_data['n']}: {q_data['q']}")
    
    already_selected = st.session_state.answers.get(q_data['n'], None)
    
    selected_option = st.radio(
        "Select Option:", 
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

# ---------------------------------------------------------
# SCREEN 3: Result
# ---------------------------------------------------------
elif st.session_state.submitted:
    score = 0
    total = len(QUESTIONS)
    
    for q in QUESTIONS:
        if st.session_state.answers.get(q['n']) == q['answer']:
            score += 1
            
    percentage = round((score / total) * 100, 2)
    
    st.success("✅ Grand Test Submitted Successfully!")
    st.markdown(f"**Candidate:** {st.session_state.student_name} (Roll/Badge: {st.session_state.student_roll})")
    st.markdown(f"**Your Score:** {score} / {total} ({percentage}%)")
    
    if percentage >= PASS_PERCENT:
        st.balloons()
        st.success("🎉 Status: PASS")
    else:
        st.error("❌ Status: FAIL (Passing Requirement: 80%)")
