import streamlit as st
import random
from translator_cardinal import evaluator as evaluator_c
from translator_ordinal import evaluator as evaluator_o
from translator_ordinal_adessive import evaluator as evaluator_oa
import utils

st.set_page_config(
    page_title="Viis numbrit",
    page_icon=":flag-ee:",
    menu_items={'About': "Viis numbrit - helping Estonian language learners to practice numbers"}
)

MODE_1 = 'cardinal (e.g. "six")'
MODE_2 = 'ordinal (e.g. "sixth")'                      
MODE_3 = 'cardinal + ordinal, randomly mixed'
MODE_4 = 'ordinal adessive (e.g. "on the sixth")'

st.title('Viis numbrit   :flag-ee:')

# Initialize session state if not already done
if 'first_run' not in st.session_state:
    st.session_state['first_run'] = 0
    st.session_state['numbers_to_show'] = []
    st.session_state['setup_submitted'] = False
    st.session_state['form_submitted'] = False
    st.session_state['number_cnt'] = 5


with st.form("setup_form"):  
    max_number = st.number_input(label = "Biggest value allowed in the list (10-9999):",
                                min_value = 10,
                                max_value = 9999,
                                value = 100,
                                placeholder = "Type a number here...",
                                )
    
    mode = st.radio(label = 'Type of numbers to practice:', options = [MODE_1, MODE_2, MODE_3, MODE_4])
          
    st.session_state['setup_submitted'] = st.form_submit_button("Generate my numbers!", type="primary")

if st.session_state['setup_submitted']:
    st.session_state['numbers_to_show'] = []
    st.session_state['form_submitted'] = False
    if mode == MODE_3:
        st.session_state['mix_pattern'] = []
        for x in range(st.session_state['number_cnt']):
            rand_01 = random.randint(0,1)
            if x == 4 and 0 not in st.session_state['mix_pattern']:
                st.session_state['mix_pattern'].append(0)
            elif x == 4 and 1 not in st.session_state['mix_pattern']:
                st.session_state['mix_pattern'].append(1)
            else:
                st.session_state['mix_pattern'].append(rand_01)


    while len(st.session_state['numbers_to_show']) < st.session_state['number_cnt']:
        next_rand_num = random.randint(1, max_number)
        if next_rand_num not in st.session_state['numbers_to_show']:
            st.session_state['numbers_to_show'].append(next_rand_num)

    st.session_state['first_run'] += 1

    with st.form("answer_form"):

        if mode == MODE_1:
            for i in range(st.session_state['number_cnt']):
                label = str(st.session_state['numbers_to_show'][i])
                st.text_input(label = label, key = i)
                
        if mode == MODE_2:
            for j in range(st.session_state['number_cnt']):
                    label = str(st.session_state['numbers_to_show'][j])
                    st.text_input(label = f"*{label}.*", key = j)

        if mode == MODE_3:
            st.write("Ordinals are formatted as *italic* and marked with a dot.")
            for k in range(st.session_state['number_cnt']):
                    label = str(st.session_state['numbers_to_show'][k])
                    if st.session_state['mix_pattern'][k] == 0:
                        st.text_input(label = label, key = k)
                    else:
                        st.text_input(label = f"*{label}.*", key = k)

        if mode == MODE_4:
            for l in range(st.session_state['number_cnt']):
                    label = str(st.session_state['numbers_to_show'][l])
                    st.text_input(label = f"*{label}. (...korrusel/kohal/etc.)*", key = l)

        st.write("Having an issue finding a special character on your keyboard? Here you are: **ü**")

        st.form_submit_button("Submit",
                              type = "primary",
                              on_click = utils.form_submitted)

if '0' in st.session_state and st.session_state['form_submitted']:
    correct_cnt = 0

    for i in range (0, st.session_state['number_cnt']):
        num_i = st.session_state['numbers_to_show'][i]
        if mode == MODE_1:
            correct_i = evaluator_c(num_i)
        elif mode == MODE_2:
            correct_i = evaluator_o(num_i)
        elif mode == MODE_4:
            correct_i = evaluator_oa(num_i)
        else:   # = MODE 3 (mixed 1 and 2)
            if st.session_state['mix_pattern'][i] == 0:
                correct_i = evaluator_c(num_i)
            else:
                correct_i = evaluator_o(num_i)

        answer_i = st.session_state[i].strip().lower()

        if answer_i == correct_i:
            correct_cnt += 1
            if mode == MODE_1:
                st.markdown(f"{num_i}  {correct_i} ✅")
            elif mode == MODE_2:
                st.markdown(f"*{num_i}.  {correct_i}* ✅")
            elif mode == MODE_4:
                st.markdown(f"*{num_i}. (...korrusel/kohal/etc.)  {correct_i}* ✅")
            elif st.session_state['mix_pattern'][i] == 0:
                st.markdown(f"{num_i}  {correct_i} ✅")
            else:
                st.markdown(f"*{num_i}.  {correct_i}* ✅")

        else:
            if mode == MODE_1:
                st.markdown(f"{num_i}  ~~{answer_i}~~ ❌ Correct: {correct_i}")
            elif mode == MODE_2:
                st.markdown(f"*{num_i}.  ~~{answer_i}~~ ❌ Correct: {correct_i}*")
            elif mode == MODE_4:
                st.markdown(f"*{num_i}. (...korrusel/kohal/etc.)  ~~{answer_i}~~ ❌ Correct: {correct_i}*")
            elif st.session_state['mix_pattern'][i] == 0:
                st.markdown(f"{num_i}  ~~{answer_i}~~ ❌ Correct: {correct_i}")
            else:
                st.markdown(f"*{num_i}.  ~~{answer_i}~~ ❌ Correct: {correct_i}*")

    st.write("")
    if correct_cnt == 1:
        st.write(f"**{correct_cnt} correct answer out of 5.**")
    elif correct_cnt == 5:
        st.write(f"**{correct_cnt} correct answers out of 5. Congrats!**  :muscle: :muscle: :muscle: :muscle: :muscle:")
    else:
        st.write(f"**{correct_cnt} correct answers out of 5.**")
