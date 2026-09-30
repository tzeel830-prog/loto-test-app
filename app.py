import streamlit as st
import time
import pandas as pd
import os
import json

# ---------------------------------------------------------
# Page Config & Styling
# ---------------------------------------------------------
st.set_page_config(page_title="Hadeeqa Manpower - WPR Grand Test 2", page_icon="📝", layout="wide")

st.markdown("""
    
        🌟 Created by: Hadeeqa Manpower Recruitment Agency | Saudi Aramco WPR Grand Test #2 (100 Mixed MCQs) 🌟
    
""", unsafe_allow_html=True)

TOTAL_TIME_SECONDS = 60 * 60  # 60 Minutes
PASS_PERCENT = 80
RESULTS_FILE = "student_results_test2.csv"
DETAILED_ANSWERS_FILE = "student_detailed_answers_test2.json"

ADMIN_PASSWORD = "HadeeqaWPR@2026!"

# ---------------------------------------------------------
# File Helper Functions for Results Storage
# ---------------------------------------------------------
def load_results():
    if os.path.exists(RESULTS_FILE):
        return pd.read_csv(RESULTS_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Roll_Number", "Email", "Score", "Percentage", "Status", "Submission_Time"])

def load_detailed_answers():
    if os.path.exists(DETAILED_ANSWERS_FILE):
        with open(DETAILED_ANSWERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_result(name, roll, email, score, total, percentage, status, user_answers):
    df = load_results()
    new_entry = pd.DataFrame([{
        "Name": name,
        "Roll_Number": str(roll).strip(),
        "Email": email,
        "Score": f"{score}/{total}",
        "Percentage": f"{percentage}%",
        "Status": status,
        "Submission_Time": time.strftime("%Y-%m-%d %H:%M:%S")
    }])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(RESULTS_FILE, index=False)

    detailed_data = load_detailed_answers()
    detailed_data[str(roll).strip()] = {
        "Name": name,
        "Email": email,
        "Score": f"{score}/{total}",
        "Percentage": f"{percentage}%",
        "Status": status,
        "Answers": user_answers
    }
    with open(DETAILED_ANSWERS_FILE, "w") as f:
        json.dump(detailed_data, f, indent=4)

def is_already_submitted(roll_no):
    df = load_results()
    if df.empty:
        return False
    return str(roll_no).strip() in df["Roll_Number"].astype(str).str.strip().values

# ---------------------------------------------------------
# 100 BALANCED MCQs (Random Mix across 300 Question Bank)
# ---------------------------------------------------------
QUESTIONS = [
    {"n": 101, "q": "Who is responsible to take countersign of other issuer/department when underground utilities are known or suspected?", "options": ["Maintenance personals", "Issuer", "Designated representative", "Receiver"], "answer": 1},
    {"n": 102, "q": "When a permit is renewed, what should be done if it contains countersign of another organization/department?", "options": ["Notify all countersigning organizations", "No need to inform or take countersign again", "Inform shift supervisor", "Take countersign again with renewal"], "answer": 3},
    {"n": 103, "q": "Who must sign the work permit to close it?", "options": ["Competent person", "Gas Tester, Issuer and Receiver", "(Both) Issuer and Receiver", "Designated Representative"], "answer": 2},
    {"n": 104, "q": "Why is work permit closed?", "options": ["To allow gas test to be taken", "To communicate the status of work", "To make sure that work site is left in safe condition", "To stop work"], "answer": 2},
    {"n": 105, "q": "Which one is correct/appropriate for High-Risk Activity?", "options": ["Present additional or unique hazard", "Only requires more safety", "Require additional approval", "None of above"], "answer": 2},
    {"n": 106, "q": "When must be work permit closed?", "options": ["After gas test taken", "When the work is finished and/or work crew leaves", "Before another permit is issued", "Just before the end of shift"], "answer": 1},
    {"n": 107, "q": "Why checklist section is important to issuer and receiver?", "options": ["It defines the duration and scope of work", "It makes sure that important steps have been taken", "It controls the receiver's break time", "It tells them all the precautions to take"], "answer": 1},
    {"n": 108, "q": "'Use a fire blanket' or 'hand dig only', are the examples of...", "options": ["Basic safety", "Additional precautions", "Working criteria", "Not safety precautions"], "answer": 1},
    {"n": 109, "q": "Which is Saudi Aramco approved personal single gas monitor?", "options": ["Any calibrated gas monitor", "T40 Rattler", "TX-1", "MX4"], "answer": 3},
    {"n": 110, "q": "What information a 'Location Box' on work permit gives to receiver?", "options": ["Exact location where receiver can work", "Where the receiver can go", "Very equipment which receiver can use", "None of above"], "answer": 0},
    {"n": 111, "q": "What information a duration box on work permit gives to receiver?", "options": ["How many workers are allowed for work", "Up to which time receiver can work", "When to start and when must stop work", "Where receiver can work"], "answer": 2},
    {"n": 112, "q": "If the work permit is not issued during an emergency, what must be done to do the work?", "options": ["Superintendent must approve", "Perform joint site inspection", "All safety precautions must be taken", "Wear SCUBA and perform work"], "answer": 2},
    {"n": 113, "q": "A work permit must be written in...", "options": ["Arabic", "Ink pen", "Arabic and led pencil", "English"], "answer": 3},
    {"n": 114, "q": "The issuer must stop work if...", "options": ["When the issuer goes to his office", "The issuer left the job site", "The job is found (to be) unsafe", "The issuer lost his copy of permit"], "answer": 2},
    {"n": 115, "q": "What must the issuer do, after/when he stops site work?", "options": ["Write the reason on the permit", "Get a countersign", "Close, then extend the permit", "Give his copy to the receiver"], "answer": 0},
    {"n": 116, "q": "The receiver must stop work if...", "options": ["He cannot find the issuer", "The work site become unsafe", "The designated representative must leave", "The issuer leaves the job site"], "answer": 1},
    {"n": 117, "q": "What must receiver do if he stops work?", "options": ["Tell the designated representative", "Tell the senior craftsman", "Tell his immediate supervisor", "Tell/inform the issuer"], "answer": 3},
    {"n": 118, "q": "What would be a good example when a receiver must stop work?", "options": ["Material has not yet arrived", "(When) He hears an emergency alarm", "He cannot wait for the countersign", "The backhoe run out of fuel"], "answer": 1},
    {"n": 119, "q": "What might happen if a safety problem arises, and receiver does not stop work?", "options": ["Countersignature become void", "A Fire, Injury or Accident (can occur)", "Accident can occur", "The work permit expires"], "answer": 1},
    {"n": 120, "q": "Where will you find Stop Work Authority (SWA)?", "options": ["In Stop Work G.I", "CSM only", "Can download from Internet", "CSM, SMS, Safety Handbook"], "answer": 3},
    {"n": 121, "q": "Who can stop work in Saudi Aramco facilities areas?", "options": ["Proponent manager", "Recover and issuer", "Everyone (Anyone)", "Designated representative"], "answer": 2},
    {"n": 122, "q": "How many steps are there in stop work authority?", "options": ["Five", "Only three steps", "Too many steps", "As much required by Issuer"], "answer": 0},
    {"n": 123, "q": "Steps of Stop work authority are...", "options": ["Stop, notify, investigate, follow-up, communicate", "Stop, communicate, notify, investigate, follow-up", "Stop, notify, investigate, communicate, follow-up", "Communicate, investigate, stop and follow-up"], "answer": 2},
    {"n": 124, "q": "Select steps of Saudi Aramco Stop Work Authority.", "options": ["Communication, Notify all persons, Make Safety Alert", "Stop unsafe work, Investigate, Follow-up", "Communication, Stop unsafe work, Follow-up", "Notify all persons, Investigate, Follow-up"], "answer": 1},
    {"n": 125, "q": "In Saudi Aramco facility areas, anyone can get help from?", "options": ["Daily news bulletin", "Only from CSM", "Loss prevention monthly magazine", "CSM, SMS, Safety Handbook"], "answer": 3},
    {"n": 126, "q": "What is the difference between hot work and cold work?", "options": ["Cold use ignition source", "Both use an ignition source", "Hot work, use/involve ignition source, while cold work does not involve ignition source", "Neither use an ignition source"], "answer": 2},
    {"n": 127, "q": "Cold work includes...", "options": ["Sand removal and scaffold erection", "Scaffold erection and using backhoe", "Abrasive blasting and painting", "Carpentry work and brush painting"], "answer": 3},
    {"n": 128, "q": "An equipment opening/line break permit is required when?", "options": ["Operator purges an equipment", "Pipefitter open a line or install blind", "Operator release hydrocarbon to flair", "Craftsmen build scaffold"], "answer": 1},
    {"n": 129, "q": "What should be checked, before allowing entry into confined space?", "options": ["Gas test, Firewatch and barricade", "Lighting, standby man and air mover (ventilation)", "Firewatch, standby man and gas test", "Air mover, respirator, and countersignature"], "answer": 2},
    {"n": 130, "q": "What should be checked before issuing an equipment opening/line break permit?", "options": ["Safety harness, belt, and safety glass", "Sewer, man way and air mover", "Ignition source, gloves, and safety glass", "Wind direction, draining and ignition source"], "answer": 3},
    {"n": 131, "q": "If there is one welding machine and is to be used by a welding and an electric group, how many work permits are required?", "options": ["One", "Three", "Two work permits", "If issuer is agreeing one permit"], "answer": 2},
    {"n": 132, "q": "When going into a manhole to do welding job, what kind of permit is required?", "options": ["Hot work and confined space entry permits", "Cold work and confined space entry permits", "Hot and cold work permits", "Confined space entry permit"], "answer": 0},
    {"n": 133, "q": "When working for well-head tie-in job using crane and hand tools, what kind of permits are required?", "options": ["Hot work and cold work permits", "Hot work, cold work, and equipment opening/line break (release) permit", "Hot work and confined space entry permit", "Equipment opening/line break permit (release)"], "answer": 1},
    {"n": 134, "q": "With manual back filling, a crew need, engine operated compactor to do their job in 5 ft deep trench (excavation), what kind of permit is required?", "options": ["Cold work and confined space entry permits", "Hot work and cold work", "Hot work, cold work, and confined space entry permits", "Only confined space entry permit"], "answer": 2},
    {"n": 135, "q": "For electric operated x-ray equipment, what type of permit is required?", "options": ["Cold work permit", "Hot work permit", "No permit is required", "Confined space entry permit"], "answer": 1},
    {"n": 136, "q": "What type of work permit is required for sealed source radiography?", "options": ["Cold work permit", "Hot work permit", "No permit is required", "Equipment entry work permit"], "answer": 0},
    {"n": 137, "q": "The use of air compressor in an operational/restricted area requires which work permit?", "options": ["Equipment opening/line break", "Cold work permit", "Confined space entry", "Hot work permit"], "answer": 3},
    {"n": 138, "q": "Why cannot a pipefitter work on the same piece of equipment using a welder's work permit?", "options": ["Joint side inspection is not required for pipefitters job", "Each type of work involves different hazards", "Gas test are not required for pipefitters work", "Welders are usually contractors"], "answer": 1},
    {"n": 139, "q": "Can work in two different locations be covered under one work permit?", "options": ["Yes", "Only if agreed by issuer", "Only with superintendent approval", "No"], "answer": 3},
    {"n": 140, "q": "If mechanical and electrical groups are working on the same equipment in restricted area...", "options": ["Two work permits are required", "Each group must have its/their separate work permit", "When the maintenance person agrees to work without permit", "When the foreman and superintendent agree on one work permit"], "answer": 1},
    {"n": 141, "q": "What type of work permit is required to clean a tank from inside, perform inside inspection or work inside sewers?", "options": ["Cold work permit", "Hot/cold and confined space entry permit", "Hot and cold work permit", "Equipment opening/line break (Release)"], "answer": 1},
    {"n": 142, "q": "What type of permit is required to take vehicle or construction equipment, inside a restricted area?", "options": ["Confined space entry permit", "Vehicle entry permit", "Cold work permit", "Hot work permit"], "answer": 1},
    {"n": 143, "q": "What type of work permit is required when working in close proximity to a live electrical line?", "options": ["Cold work permit", "Hot work permit", "Hot work and confined space entry permit", "Equipment opening/line break permit"], "answer": 1},
    {"n": 144, "q": "Abrasive blasting (sand blasting) requires what type of work permit, in a restricted area?", "options": ["Cold work permit", "Hot work permit", "Hot work and confined space entry permit", "Equipment opening/line break permit"], "answer": 1},
    {"n": 145, "q": "Which duty/type of scaffold is required for abrasive/sand blasting job?", "options": ["Light duty", "Very light duty", "Any duty of scaffold", "Medium duty (Scaffold)"], "answer": 3},
    {"n": 146, "q": "What issuer will check before, issuing permit for crane lifting?", "options": ["Physical condition of lifting gears", "Crane's checklist", "Certificate of operator and rigger", "All of above"], "answer": 3},
    {"n": 147, "q": "At what depth of an excavation, confined space entry permit requirement starts?", "options": ["4 m", "4 ft (1.2 m)", "2.2 m", "1.2 ft"], "answer": 1},
    {"n": 148, "q": "What is required distance for a scaffold base, from edge of excavation?", "options": ["Height of scaffold x depth of excavation", "2.6 m", "1.5 x depth of excavation", "1 m"], "answer": 2},
    {"n": 149, "q": "Motor vehicles, and heavy equipment shall be kept away from the edge of the excavation...", "options": ["1.5 x depth of excavation", "2 m (6.5 ft) or the depth of excavation", "1.8 m (6 ft)", "3 m (10 ft)"], "answer": 1},
    {"n": 150, "q": "Which equipment can operate within 2-m from edge of excavation?", "options": ["Crane", "Welding truck", "Excavation and Backfilling Equipment", "None of above"], "answer": 2},
    {"n": 201, "q": "Why will receiver make sure that LOTO is implemented, and equipment is deenergised/depressurised?", "options": ["People/workers can get injured", "It did not make any difference", "Energy can injure people/workers", "Locks and Tags will destroy"], "answer": 2},
    {"n": 202, "q": "Before starting work on an equipment, it must be made sure that equipment is...", "options": ["Electrified isolated and shutdown", "Shutdown, isolated and de-energized", "Isolated repaired and certified", "De-energized with power turned on"], "answer": 1},
    {"n": 203, "q": "Removing fuse from electric circuit or disconnecting electrical wiring is an example of...", "options": ["Cleaning electrical equipment", "Electrical Isolation", "Isolating electrical equipment", "Purging"], "answer": 1},
    {"n": 204, "q": "What is 4 step process to ensure that the (electrical) equipment is properly isolated?", "options": ["LOCK, TRY, CLEAR & TAG", "Clear area, lock equipment test switch and tag the lock", "Lock, Tag, Try and Clear", "LOCK, TAG, CLEAR & TRY"], "answer": 3},
    {"n": 205, "q": "How can process equipment be cleaned?", "options": ["Water wash and steaming", "Purging and gas testing", "By water wash and/or steaming", "(By) treating and clarifying"], "answer": 2},
    {"n": 206, "q": "We isolate equipment to make sure it cannot be...", "options": ["Slip trip or fall", "Taken to shop for repair", "Start-up, leak or cause electric shock", "Shutdown by accident"], "answer": 2},
    {"n": 207, "q": "What are the mechanical methods of Isolation?", "options": ["Single Block Valve", "Double Block and Bleed", "Disconnection and Blinding", "All of Above"], "answer": 3},
    {"n": 208, "q": "Which method is considered as positive isolation?", "options": ["Install tag and purge", "Disconnection and Blinding", "Remove piping and install blind", "Install lockout and take gas test"], "answer": 1},
    {"n": 209, "q": "The only acceptable method of isolation for confined space entry to a vessel is...", "options": ["Single Block Valve", "Double Block and Bleed", "Any method which can be adopted", "Disconnection and Blinding (Positive Isolation)"], "answer": 3},
    {"n": 210, "q": "Double block and bleed isolation method is not approved for...", "options": ["Hot work on process piping or equipment", "Work on system containing flammable or toxic material", "Confined space entry", "All of Above"], "answer": 2},
    {"n": 211, "q": "Installing locks and tags on electrical breakers prevents accidental...", "options": ["Blind installation", "Purging equipment", "Start-up of equipment", "Nitrogen release"], "answer": 2},
    {"n": 212, "q": "Why are tags placed/installed with lock?", "options": ["To communicate the reason and authorization of isolation", "To explain why the lock is installed", "To record a gas test", "To list safety precautions"], "answer": 0},
    {"n": 213, "q": "When do we use Hold-Tags?", "options": ["Always have to put lock first", "It is not allowed to use lock only", "When isolation device is not a lockable device", "When lock cannot be placed on energy isolation device"], "answer": 2},
    {"n": 214, "q": "Who install receiver's locks?", "options": ["One member from each work crew", "Every member of the crew", "The Foreman and the receiver", "The receiver"], "answer": 3},
    {"n": 215, "q": "In group lockout ________ will install his lock.", "options": ["One member from each work crew", "Each member of the crew", "The Foreman and the receiver", "The receiver"], "answer": 1},
    {"n": 216, "q": "Isolated equipment, must be checked by field switch, before work starts (starting work), to make sure that...", "options": ["The correct equipment is isolated", "There is no gas in the area", "It has been purged and cleaned", "The receiver's tag is installed"], "answer": 0},
    {"n": 217, "q": "When isolation is performed and LOTO is completed, what is next step?", "options": ["Check the locks again to verify they are locked/closed", "Verification (verify that correct system is isolated)", "Do not make any delay and start job quickly", "Tell workers and start work"], "answer": 1},
    {"n": 218, "q": "When the operation person installs the padlock to the switchgear, what should he do next?", "options": ["Work safely", "Check the switch again to make sure that correct unit is isolated", "Ensure that the unit is isolated", "None of above"], "answer": 1},
    {"n": 219, "q": "After operations, who will install lock?", "options": ["Do the job quickly", "Receiver will install his lock", "Get tools and start work", "They can start the job with instructions of foreman"], "answer": 1},
    {"n": 220, "q": "When operators change shift...", "options": ["The lock must be changed", "The lock and tag must be changed", "The tag must be changed", "The keys are usually transferred to new shift"], "answer": 3},
    {"n": 221, "q": "When maintenance work on an equipment, who will Lock-out & Tag-out the equipment?", "options": ["Maintenance only", "Operations Only", "Each member of crew", "Operations & Maintenance"], "answer": 3},
    {"n": 222, "q": "Why must equipment be de-energized and de-pressurized before starting work is started?", "options": ["Electricity can be wasted", "People can be injured by stored energy", "Accidental start-up could happen", "Purged gas can be lost"], "answer": 1},
    {"n": 223, "q": "Who will install LOTO first?", "options": ["SCECO", "Operations", "Maintenance", "Power distribution"], "answer": 1},
    {"n": 224, "q": "What must operation do before they remove their locks and tags?", "options": ["Make sure the equipment can be safely started", "Clean and purge the breaker", "Take gas test and restart equipment", "Make sure the equipment is gas free"], "answer": 0},
    {"n": 225, "q": "How many keys with a pad lock used in LOTO?", "options": ["One only", "As many crew members", "3 for each lock", "One for issuer and one for receiver"], "answer": 0},
    {"n": 226, "q": "When implementing LOTO, for 4 different contractors/groups, how many locks are required?", "options": ["4", "Only one", "5", "6"], "answer": 0},
    {"n": 227, "q": "If only issuer and receiver (one group) is involved in an activity, which needs isolation of an equipment, how many locks are required?", "options": ["No lock is required", "1", "3", "2"], "answer": 3},
    {"n": 228, "q": "Who can/will remove lock?", "options": ["Anyone who want to start the equipment", "No one can remove it once it is locked", "Foreman of the working crew", "The one who installed lock / lock owner"], "answer": 3},
    {"n": 229, "q": "Is there any condition when a lock can be forcefully removed?", "options": ["It cannot be removed forcefully", "When work permit is finished", "When, the person who install lock, his supervisor or superintendent cannot be contacted", "When anyone need to start or energize that equipment"], "answer": 2},
    {"n": 230, "q": "Who can forcefully remove an isolation lock when owner of the lock cannot be contacted/found?", "options": ["No one can remove a lock once it is installed", "Operation's shift superintendent or foreman", "Supervisor of working crew", "Person who installs lock can remove it only"], "answer": 1},
    {"n": 231, "q": "What should be checked/conformed before removing a lock forcefully?", "options": ["Personnel and facilities are safe from injury or damage", "Lock can be removed without any checks or precautions", "Work permit is expired", "All workers are in rest shelter"], "answer": 0},
    {"n": 232, "q": "Hold tags and locks are primarily installed to protect the individual, doing the work from...", "options": ["Being injured in case of accidental start up", "To protect Locks & Tags", "No one will go before finishing work", "Loosing Energy"], "answer": 0},
    {"n": 233, "q": "What is the most dangerous source of energy?", "options": ["Drained energy", "Disconnected energy", "Potential (Stored) Energy", "Connected energy"], "answer": 2},
    {"n": 234, "q": "In a confined space entry, what is the most important thing to do?", "options": ["Get a hot permit", "Non sparking tools will be used", "Ensure that space is isolated", "Gas release can be made safely"], "answer": 2},
    {"n": 235, "q": "If standby man is not available on the site and the issuer speaks/tells you to sign a confined space enter permit, as a receiver what will you do?", "options": ["Sign permit and call standby man", "Start work and bring a Firewatch", "Sign permit, but wait for standby man to come", "Will not (Don't) sign the permit, until Standby man arrive/available at site."], "answer": 3},
    {"n": 236, "q": "When installing blind on (Previously) H2S containing line, what precautions will be taken?", "options": ["Use of cartage respirator", "Use of SCBA", "Use of any respirator", "No need to use respirator"], "answer": 1},
    {"n": 237, "q": "At 15-ppm H2S Concentration, which respiratory protection will be used?", "options": ["SCBA", "N-95 Dust mask", "Cartage respirator", "No respirator is required"], "answer": 0},
    {"n": 238, "q": "If issuer instructs to use SCBA for Confined Space Entry, you have only one SCABA and more than one worker to go in Confined Space, what will you do?", "options": ["Will continue work and inform issuer about situation", "Will stop the work and inform issuer about situation", "Will continue work and inform worker to take care", "Will stop work and stay on site until permit time is over"], "answer": 1},
    {"n": 239, "q": "What important information CHB provide about the chemical?", "options": ["How to use chemical", "Expiry date of the chemical", "Only physical properties of chemical", "Hazards involved and precautions for handling the chemical"], "answer": 3},
    {"n": 240, "q": "When issuing EOLB permit, which condition to be checked?", "options": ["Wind direction only", "Line direction", "Position of fire alarm", "Wind direction and Drainage"], "answer": 3},
    {"n": 241, "q": "What are the two major hazards of EOLB Permit?", "options": ["Release of Hazardous Material & Flammable Liquid/gas", "Fall of flange", "Flammable & Hazardous material", "Failure of Isolation"], "answer": 0},
    {"n": 242, "q": "What type of work permit is required when opening a line flange or equipment?", "options": ["Cold Work Permit", "Hot Work Permit", "Equipment Opening Line Brake (EOLB)", "No Work Permit is required"], "answer": 2},
    {"n": 243, "q": "EOLB permit is required for...", "options": ["Opening of pipeline associated with close system and may contained H2S", "Depressurising drainage of firewater pipeline with sprinkles", "Cleaning of an equipment", "Remove sludge from an equipment"], "answer": 0},
    {"n": 244, "q": "In which order should hydrocarbon process equipment be prepared before Entry [Confined Space Entry]?", "options": ["Gas test, draining, isolation, purging, cleaning", "Isolation, draining, purging, gas testing", "Drainage, isolation, purge, clean, gas test", "Blind, gas test, drain"], "answer": 1},
    {"n": 245, "q": "What will happen if issuer do not suggest warning signs and barricades, around an excavation?", "options": ["People may fall into excavation", "Rainwater can go inside excavation", "Vehicle/equipment may fall in excavation", "Both A & B"], "answer": 3},
    {"n": 246, "q": "How to protect excavation cave-in?", "options": ["Do not excavate", "Benching, Sloping and Shoring", "Use scaffolding bords to protect against cave-in", "Use only hand tools to dig"], "answer": 1},
    {"n": 247, "q": "What should be provided to protect vehicle from fall into excavations?", "options": ["Signage/standby man", "Barricade/blinking light", "Signage/barricade", "Standby man/barricade"], "answer": 1},
    {"n": 248, "q": "Why should gas test be taken before entering an excavation?", "options": ["To check the oxygen deficiency", "To check the presence of toxic gases", "To check the presence of explosive gas", "All of above"], "answer": 3},
    {"n": 249, "q": "Material and spoils shall be set back at least ____ from the edge of the excavation.", "options": ["0.6 m (2ft)", "1.2 m (4 ft)", "2 m (6.6 ft)", "Any distance"], "answer": 0},
    {"n": 250, "q": "What can happen when excavating with backhoe?", "options": ["1 m (3 ft)", "1.8 m (6 ft)", "It can rupture underground utility lines or pipelines", "Accidental contact with underground utility lines"], "answer": 2}
]

# ---------------------------------------------------------
# Helper Function: Generate HTML Paper Review
# ---------------------------------------------------------
def render_student_review_paper(user_answers_dict):
    for q in QUESTIONS:
        q_num = str(q['n'])
        user_selected_idx = user_answers_dict.get(int(q_num), None)
        if user_selected_idx is None:
            user_selected_idx = user_answers_dict.get(q_num, None)
            
        correct_idx = q['answer']
        
        if user_selected_idx is not None:
            user_selected_text = q['options'][user_selected_idx]
            correct_text = q['options'][correct_idx]
            
            if user_selected_idx == correct_idx:
                st.markdown(f"✅ **Q{q['n']}: {q['q']}**")
                st.caption(f"Your Answer: {user_selected_text} (Correct)")
            else:
                st.markdown(f"❌ **Q{q['n']}: {q['q']}**")
                st.error(f"Your Selected Answer: {user_selected_text}")
                st.success(f"Correct Answer: {correct_text}")
        else:
            st.warning(f"⚠️ **Q{q['n']}: {q['q']}** (Not Attempted)")
        st.write("---")

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
if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

st.title("Hadeeqa Manpower Recruitment Agency")
st.caption("Saudi Aramco WPR Grand Test #2 - 100 Questions")

# ---------------------------------------------------------
# SCREEN 1: Candidate Form
# ---------------------------------------------------------
if not st.session_state.started and not st.session_state.submitted:
    with st.form("student_info"):
        st.subheader("Candidate Information")
        name = st.text_input("Candidate Full Name *")
        roll = st.text_input("Roll / Badge Number *")
        email = st.text_input("Email Address *")
        
        btn = st.form_submit_button("Start 60-Minute Grand Test #2")
        
        if btn:
            if name and roll and email:
                if is_already_submitted(roll):
                    st.error(f"❌ Roll Number '{roll}' has ALREADY attempted this test! Single-attempt limit applies.")
                else:
                    st.session_state.student_name = name
                    st.session_state.student_roll = str(roll).strip()
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
# SCREEN 3: Result Submission & Student Review (Hidden Score)
# ---------------------------------------------------------
elif st.session_state.submitted:
    score = 0
    total = len(QUESTIONS)
    
    for q in QUESTIONS:
        if st.session_state.answers.get(q['n']) == q['answer']:
            score += 1
            
    percentage = round((score / total) * 100, 2)
    status = "PASS" if percentage >= PASS_PERCENT else "FAIL"
    
    if 'saved' not in st.session_state:
        save_result(
            st.session_state.student_name,
            st.session_state.student_roll,
            st.session_state.student_email,
            score,
            total,
            percentage,
            status,
            st.session_state.answers
        )
        st.session_state.saved = True
    
    st.balloons()
    st.success("✅ Grand Test #2 Submitted Successfully!")
    st.info(f" Candidate: **{st.session_state.student_name}** | Roll/Badge: **{st.session_state.student_roll}**")
    st.warning("🔒 Note: Your score has been recorded safely. The final result will be officially announced by Hadeeqa Manpower Recruitment Agency.")
    
    st.write("---")
    st.subheader("📝 Your Test Paper Review (Mistakes & Correct Answers)")
    st.caption("Marks and Pass/Fail status are hidden. You can review which answers were right or wrong below:")
    render_student_review_paper(st.session_state.answers)

# ---------------------------------------------------------
# SECRET ADMIN PORTAL (Detailed Inspector & PDF Report Generator)
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🔒 Admin Result Portal")

if not st.session_state.admin_logged_in:
    with st.sidebar.form("admin_login_form"):
        admin_pass = st.text_input("Admin Password", type="password")
        login_btn = st.form_submit_button("Login")
        
        if login_btn:
            if admin_pass == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Incorrect Password!")

if st.session_state.admin_logged_in:
    st.sidebar.success("Admin Logged In!")
    if st.sidebar.button("Logout Admin"):
        st.session_state.admin_logged_in = False
        st.rerun()
        
    df_results = load_results()
    detailed_answers = load_detailed_answers()
    
    st.subheader("📊 Candidate Summary Results (Admin View Only)")
    st.dataframe(df_results)
    
    st.write("---")
    st.subheader("🔍 Inspect Student Mistakes & Generate Report")
    
    if not df_results.empty:
        student_list = df_results["Roll_Number"].astype(str).tolist()
        selected_roll = st.selectbox("Select Student Roll Number to view mistakes:", student_list)
        
        if selected_roll in detailed_answers:
            s_data = detailed_answers[selected_roll]
            st.markdown(f"### Student: **{s_data['Name']}** | Score: **{s_data['Score']} ({s_data['Percentage']})** | Status: **{s_data.get('Status', 'N/A')}**")
            
            # Prepare Text Paper for Download/Send
            paper_text = f"HADEEQA MANPOWER RECRUITMENT AGENCY - TEST REPORT\n"
            paper_text += f"Candidate: {s_data['Name']}\nRoll/Badge: {selected_roll}\nScore: {s_data['Score']} ({s_data['Percentage']})\nStatus: {s_data.get('Status', 'N/A')}\n"
            paper_text += f"="*50 + "\n\n"
            
            user_ans_dict = s_data["Answers"]
            
            for q in QUESTIONS:
                q_num = str(q['n'])
                user_selected_idx = user_ans_dict.get(int(q_num), None)
                if user_selected_idx is None:
                    user_selected_idx = user_ans_dict.get(q_num, None)
                    
                correct_idx = q['answer']
                
                if user_selected_idx is not None:
                    user_selected_text = q['options'][user_selected_idx]
                    correct_text = q['options'][correct_idx]
                    
                    if user_selected_idx == correct_idx:
                        st.markdown(f"✅ **Q{q['n']}: {q['q']}**")
                        st.caption(f"Correct Choice: {user_selected_text}")
                        paper_text += f"[CORRECT] Q{q['n']}: {q['q']}\nAnswer: {user_selected_text}\n\n"
                    else:
                        st.markdown(f"❌ **Q{q['n']}: {q['q']}**")
                        st.error(f"Student Selected: {user_selected_text}")
                        st.success(f"Correct Answer: {correct_text}")
                        paper_text += f"[WRONG] Q{q['n']}: {q['q']}\nStudent Selected: {user_selected_text}\nCorrect Answer: {correct_text}\n\n"
                else:
                    st.warning(f"⚠️ **Q{q['n']}: {q['q']}** (Not Attempted)")
                    paper_text += f"[NOT ATTEMPTED] Q{q['n']}: {q['q']}\n\n"
                st.write("---")
            
            # Download Individual Student Paper Report Button
            st.download_button(
                label=f"📥 Download {s_data['Name']}'s Report Card (TXT/PDF Format)",
                data=paper_text.encode('utf-8'),
                file_name=f"Report_{selected_roll}_{s_data['Name']}.txt",
                mime="text/plain"
            )
        else:
            st.info("Is student ka detailed record available nahi hai.")
            
    csv_data = df_results.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download All Candidates Excel/CSV Summary",
        data=csv_data,
        file_name="WPR_Grand_Test_2_Results.csv",
        mime="text/csv"
    )
