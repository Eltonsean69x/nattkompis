import streamlit as st
from datetime import datetime

st.set_page_config(page_title='Nattkompis 🌙', page_icon='🌙', layout='centered')
st.markdown('''<style>.stApp{background:linear-gradient(180deg,#19172d,#322743);color:#fff}.block-container{max-width:690px;padding-top:2rem}h1,h2,h3,p,label{color:#fff!important}div.stButton>button{background:#e9b9d0;color:#30223d;border-radius:20px;border:0;font-weight:700}div[data-testid="stMetric"]{background:#4a395c;border-radius:16px;padding:12px}</style>''', unsafe_allow_html=True)

if 'ping' not in st.session_state: st.session_state.ping=False
if 'messages' not in st.session_state: st.session_state.messages=[]

st.title('🌙 Nattkompis')
st.caption('En liten plats för stora nattkänslor 💜')
st.header('Du är inte ensam i natt ❤️')
st.write('Vaken med din bebis? Här finns plats för en pratstund, även mitt i natten.')
st.info('✨ DEMO: Antal vakna mammor och chattmeddelanden är exempel, inte riktiga användare. Ingen information delas med andra.')

regioner=['Stockholm','Västra Götaland','Skåne','Västernorrland','Västerbotten','Dalarna','Uppsala','Östergötland','Jönköping','Örebro','Norrbotten','Halland','Värmland','Gävleborg','Kalmar','Kronoberg','Blekinge','Gotland','Jämtland','Södermanland','Västmanland']
region=st.selectbox('📍 Välj ditt län',regioner,index=3)
col1,col2=st.columns(2)
with col1: st.metric('🌙 Vakna i Sverige','47 (demo)')
with col2: st.metric('💜 I ditt län','6 (demo)')
st.write('')
if st.button('🔔 Jag är vaken! PING',use_container_width=True):
    st.session_state.ping=not st.session_state.ping
if st.session_state.ping: st.success('💜 Din ping är aktiv i den här demon. Du är inte ensam!')
else: st.caption('Tryck för att visa att du är vaken (endast på din skärm).')

st.divider()
st.subheader('💬 Nattchatten')
st.caption(f'Visar exempel på en chatt för {region}. Meddelanden stannar i din egen session.')
for name,message in [('Emma (demo)','Är det fler som matar bebis just nu? 🍼'),('Sara (demo)','Japp! Tredje gången i natt 😅'),('Maja (demo)','Skönt att veta att man inte är ensam ❤️')]:
    st.chat_message('assistant',avatar='🌷').write(f'**{name}:** {message}')
for msg in st.session_state.messages:
    st.chat_message('user',avatar='💜').write(msg)
msg=st.chat_input('Skriv ett meddelande (demo)...')
if msg: st.session_state.messages.append(msg); st.rerun()

st.divider()
st.subheader('👩‍🍼 Hitta mammavänner')
st.write('I en framtida version kan du hitta andra mammor i din stad, med barn i liknande ålder.')
st.text_input('Din ort (frivilligt)',placeholder='T.ex. Sundsvall')
st.selectbox('Bebisens ålder',['0–3 månader','4–6 månader','7–12 månader','1–2 år','2+ år'])
st.caption('💜 Prototyp skapad för att testa idén. Inga riktiga konton, vänförfrågningar eller privata meddelanden finns ännu.')
