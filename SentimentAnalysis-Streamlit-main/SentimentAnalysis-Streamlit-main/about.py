import streamlit as st
from pathlib import Path
from PIL import Image


def renderApp():
    # st.title("hello")
    st.markdown(
        """<h3 class="stT">Team Member's</h3>
                """,
        unsafe_allow_html=True,
    )
    current_dir = Path(__file__).parent if "_file__" in locals() else Path.cwd()
    css_file = current_dir / "style" / "main.css"
    # Gourav
    resume_file = current_dir / "Assest" / "cv.pdf"
    profile_pic = current_dir / "Assest" / "profile-pic.png"
    # harsh Dad
    resum_har = current_dir / "Assest" / "hcv.pdf"
    harsh_pic = current_dir / "Assest" / "hcv.png"
    # Ishani
    resum_ish = current_dir / "Assest" / "icv.pdf"
    ishani_pic = current_dir / "Assest" / "iscv.png"
    # Harsh jas
    resum_jas = current_dir / "Assest" / "jascv.pdf"
    jas_pic = current_dir / "Assest" / "jasimg.png"

    # PAGE_TITLE = "INTRO"
    NAME = "Gourav Sharma"
    DESCRIPTION = "FrontEnd Developer"
    EMAIL = "gouravsharma2806@gmail.com"
    # st.title("Gourav")

    HNAME = "Harsh Dad"
    HDES = "FrontEnd Developer"
    HEMAIL = "harshdad20186@acropolis.in"

    INAME = "Ishani Pandey"
    IDES = "Designer"
    IEMAIL = "ishanipandey20829@acropolis.in"

    JNAME = "Harsh Jaiswal"
    JDES = "Researcher"
    JEMAIL = "harshjaiswal20527@acropolis.in "

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    # Gourav
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    # harsh Dad
    with open(resum_har, "rb") as pdf_harsh:
        PDFharsh = pdf_harsh.read()
    # Ishani
    with open(resum_ish, "rb") as pdf_ishani:
        PDFishani = pdf_ishani.read()

    # Jaiswal
    with open(resum_jas, "rb") as pdf_jasiwal:
        PDFjasiwal = pdf_jasiwal.read()

    profile_pic = Image.open(profile_pic)
    harsh_pic = Image.open(harsh_pic)
    ishani_pic = Image.open(ishani_pic)
    jas_pic = Image.open(jas_pic)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    col8, col9 = st.columns(2, gap="small")
    with col8:
        st.image(harsh_pic, width=230)
    with col9:
        st.title(HNAME)
        st.write(HDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFharsh,
            file_name=resum_har.name,
            mime="application/octet-stream",
        )
        st.write("📫", HEMAIL)

    col10, col11 = st.columns(2, gap="small")
    with col10:
        st.image(ishani_pic, width=230)
    with col11:
        st.title(INAME)
        st.write(IDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFishani,
            file_name=resum_har.name,
            mime="application/octet-stream",
        )
        st.write("📫", IEMAIL)

    col13, col14 = st.columns(2, gap="small")
    with col13:
        st.image(jas_pic, width=230)
    with col14:
        st.title(JNAME)
        st.write(JDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFjasiwal,
            file_name=resum_jas.name,
            mime="application/octet-stream",
        )
        st.write("📫", JEMAIL)

    # st.markdown(
    #     """<h3 class="stT">Project Document's</h3>
    #             """,
    #     unsafe_allow_html=True,
    # )
