import streamlit as st
from generator import generate_ad_content

st.title('Multi-Platform Ad Generator')

business_name = st.text_input('Biznes Adı:')
product = st.text_area('Məhsul:')

if st.button('Reklamları yarat'):
    if business_name and product:
        platforms = ['Instagram', 'Facebook', 'TikTok']
        for platform in platforms:
            with st.spinner(f'{platform} üçün hazırlanır...'):
                result = generate_ad_content(platform, business_name, product)
                st.subheader(f'Platform: {platform}')
                st.write(result)
    else:
        st.warning('Zəhmət olmasa bütün sahələri doldurun.')