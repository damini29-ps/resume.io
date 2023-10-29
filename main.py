import streamlit as st
from PIL import Image
#from fpdf import FPDF
import base64

st.set_page_config(
    page_title="Portfolio",
    page_icon="shark",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a portfolio webite!"
    }
)


col1, col2 = st.columns(2)

with col1:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.title("Hi, I'm Damini Sharma")
    st.title('UI | UX DESIGNER  :sunglasses:')
    st.text("")
    st.text("")
    st.text("")
    st.write("I've completed my Master's in Information technology Degree and currently looking for some meaningful experience to improve my existing designing skills. I like to make content for Instagram and LinkedIn. I too have a collaborative spirit and like to work and support a community.I'm taking my first foray into the world of UI/UX.The first experience is priceless and unforgettable. I will do everything in my power to achieve my objectives. I am most interested in learning new skills, particularly UI/UX Design.") 
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Education", "Experience", "Projects", "Resume", "Links"])

    with tab1:
        st.header("Education")
        st.markdown(
    """
    - 2021-2023   |   Master’s Information Technology    |   Pillai College Of Arts, Commerce & Science, New Panvel   |    8.25 CGPA
    - 2018-2021   |   Bachelor’s Information Technology  |   MGM Institute of Computer Science & Information Technology, Kamothe   |   8.14 CGPA
    - APRIL 2021 - NOVEMBER 2021   |   Coursera - Google UX Design Certificate Course
    - JULY 2020 - OCTOBER 2020   |   Coursera - UI/UX Design - California Institute of Arts
    """
    )

    with tab2:
        st.header("RECZEE")
        st.markdown(
    """
    - Reczee - My responsibility was to overhaul the entire platform and give the website a more upscale appearance. 
    I redesigned the website structure including page format, buttons and color palettes to improve user experience. 
    - Website : Reczee - www.reczee.com
    """
        
    )

    with tab3:
        st.header("Projects")
        st.markdown(
    """
    - Event Maker Web-App UI Design 
    - The event maker web application is made for restaurants and clubs and enables users to connect in a contemporary manner thanks to its dark design and distinctive button layout. 
    Figma's smart animation is used to create interaction between the dates of matches. This uses excellent typography and colour contrasts
    - Website : https://www.behance.net/gallery/145142613/Event-Maker
    
    - SHAW Academy App UI Design
    -Shaw Academy is an already-existing program, and in this revamp I've added some new features including more imaginative user interface ideas. 
    The app's user interface is created with all age groups in mind and offers a welcoming environment. 
    And there are also some convenient payment options.
    - Website : https://www.behance.net/gallery/127960903/App-Clone


    - OrFresh Organic Food Website Design
    - All of the members of the OrFresh family are committed to good health. 
    I got my design ideas from several organic product designs on Behance. 
    The user interface is developed with both young and elderly users in mind, with innovative, user-friendly designs. 
    The website is becoming more interesting and engaging as a result of the tiny interactions made here.
    - Website : https://www.behance.net/gallery/174050039/OrFRESH-Webpage-Design
    """
    )
     
    
    
        
    with tab4:
        st.header("Resume Download")
        st.image("DAMINI SHARMA.jpg")
        
        def generate_pdf_content():
    # Replace this function with your code that generates the PDF content.
    # You can use any library (e.g., ReportLab, FPDF) to generate the PDF.
    # For the sake of this example, we'll just create a simple PDF content.
            content = "Download My Resume."
            return content

        def main():
            #st.title("Download Resume")

    # Create a download button
            #if st.button("Download Resume"):
                pdf_content = generate_pdf_content()
        # Set the filename and content type for the download
                #filename = "DAMINI SHARMA.pdf"
                #mime_type = "application/pdf"
        # Use the st.download_button function to display the download button
                #st.download_button(label="Download Resume", data=pdf_content, file_name=filename, mime=mime_type)

        #if __name__ == "__main__":
            #main()
        
        

        # Assuming you have a PDF file named "example.pdf"
        file_path = "DAMINI SHARMA.pdf"

# Read the PDF file and get its content as bytes
        with open(file_path, "rb") as file:
            pdf_content = file.read()

# Provide the file name and content to st.file_download()
        st.download_button("Download Resume", pdf_content, mime="application/pdf")


        #with open("DAMINI+SHARMA.PDF", "rb") as pdf_file:
            #btn = st.download_button(
                    #label="Download Resume",
                    #data=pdf_file,
                    #file_name=('DAMINI+SHARMA.pdf', "rb")
                    #mime_type="application/pdf"
                #)
        
        
        #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    with tab5:
        st.header("Links")
        st.markdown(
    """
    - Behance 
    """
    )
        def main():
            image_url = "qr_code.png"
            image_width = 100
            #image_height = 200
            st.image(image_url, caption="Scan", width=image_width)
        if __name__== "__main__":
            main()
    
        st.markdown(
    """
    - Linkedin 
    """
    )
        def main():
            image_url = "linkedin_qrcode.png"
            image_width = 100
            #image_height = 200
            st.image(image_url, caption="Scan", width=image_width)
            #st.write("https://www.behance.net/daminisharma2905")
        if __name__== "__main__":
            main()
    

    
with col2:
    st.image("Profile.jpg.png")
    
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

#st.image("Group 852.png")
    
    


