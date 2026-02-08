import streamlit as st
from fpdf import FPDF
import html

# --- CONFIGURATION & PAGE SETUP ---
st.set_page_config(layout="wide", page_title="The Pivot Resume Builder")

# --- PDF GENERATOR CLASS ---
class PDF(FPDF):
    def header(self):
        pass 

    def section_title(self, label):
        self.set_font('Times', 'B', 12)
        self.cell(0, 6, label.upper(), 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y()) 
        self.ln(2)

    def section_content_header(self, role, company, location, date):
        self.set_font('Times', 'B', 11)
        self.cell(0, 5, role, 0, 1, 'L')
        self.set_font('Times', 'I', 11)
        self.cell(100, 5, company, 0, 0, 'L')
        self.cell(0, 5, f"{location} | {date}", 0, 1, 'R')

    def bullet_point(self, text):
        self.set_font('Times', '', 11)
        if text.strip():
            self.cell(5, 5, "-", 0, 0, 'R')
            self.multi_cell(0, 5, text)
        
# --- SIDEBAR INPUTS ---
st.sidebar.title("Resume Inputs")

with st.sidebar.expander("1. Personal Details", expanded=False):
    name = st.text_input("Full Name", "Joshua Doyle")
    contact_info = st.text_input("Contact Line", "2600 York Ave N, Robbinsdale, MN 55422 | 763.234.0901 | scoosch@gmail.com")
    summary = st.text_area("Professional Summary", "Dedicated and customer-oriented IT professional with a passion for technology. Recently certified CompTIA A+ with a strong understanding of hardware, software, and networking. Proven ability to provide excellent customer service and resolve technical issues quickly and efficiently in fast-paced environments.")

with st.sidebar.expander("2. Technical Projects (The Pivot)", expanded=False):
    st.info("💡 These projects bridge the gap between your detailed history and your future in IT.")
    proj_1_role = st.text_input("Project 1 Role", "Home Lab Administrator")
    proj_1_tech = st.text_input("Project 1 Tech", "Proxmox, OPNsense, Cisco Networking")
    proj_1_date = st.text_input("Project 1 Date", "2024 - Present")
    proj_1_bullets = st.text_area("Project 1 Details", 
        "Designed and deployed a virtualized home lab environment using Proxmox VE.\n"
        "Configured OPNsense firewall with VLANs to segregate IoT traffic.\n"
        "Managed Cisco Catalyst switches to learn CLI command structure and layer 2 protocols.")

    proj_2_role = st.text_input("Project 2 Role", "3D Printing & Hardware Prototyping")
    proj_2_tech = st.text_input("Project 2 Tech", "Bambu Lab, CAD, G-Code")
    proj_2_date = st.text_input("Project 2 Date", "2023 - Present")
    proj_2_bullets = st.text_area("Project 2 Details", 
        "Maintained and calibrated Bambu Lab 3D printers for high-precision manufacturing.\n"
        "Troubleshot hardware failures involving extruder assemblies and thermal runaway protection.")

with st.sidebar.expander("3. Professional Experience", expanded=True):
    # Job 1
    st.markdown("### Job 1: IT Help Desk")
    job_1_role = st.text_input("Job 1 Title", "Help Desk Technician")
    job_1_company = st.text_input("Job 1 Company", "Arvig Enterprises")
    job_1_loc = st.text_input("Job 1 Location", "Maple Grove/Edina, MN")
    job_1_date = st.text_input("Job 1 Date", "March 2024 - January 2025") 
    job_1_bullets = st.text_area("Job 1 Details", 
        "Provided technical support for internet, TV, and phone services, troubleshooting connectivity and hardware issues.\n"
        "Diagnosed and resolved Tier 1 customer incidents using ticketing systems to track resolution status.\n"
        "Guided users through remote troubleshooting steps to restore service functionality.")

    # Job 2
    st.markdown("### Job 2: Remote Communications")
    job_2_role = st.text_input("Job 2 Title", "Phone Operator")
    job_2_company = st.text_input("Job 2 Company", "Time Communications")
    job_2_loc = st.text_input("Job 2 Location", "Maple Grove/Edina, MN")
    job_2_date = st.text_input("Job 2 Date", "September 2023 - March 2024")
    job_2_bullets = st.text_area("Job 2 Details", 
        "Managed high-volume inbound calls with professional customer service standards.\n"
        "Demonstrated reliability and time management while working independently in a remote environment.\n"
        "Utilized communication software to route calls accurately and efficiently.")

    # Job 3
    st.markdown("### Job 3: Logistics & Service")
    job_3_role = st.text_input("Job 3 Title", "Customer Service Professional")
    job_3_company = st.text_input("Job 3 Company", "Gotta Go Gotta Throw")
    job_3_loc = st.text_input("Job 3 Location", "Golden Valley, MN")
    job_3_date = st.text_input("Job 3 Date", "August 2020 - December 2022")
    job_3_bullets = st.text_area("Job 3 Details", 
        "Resolved customer inquiries via email and phone regarding product specifications and orders.\n"
        "Organized warehouse inventory and coordinated shipping logistics for accurate order fulfillment.\n"
        "Maintained store organization and led team efforts to ensure positive customer experiences.")

    # Job 4 (New from History)
    st.markdown("### Job 4: Hospitality Management")
    job_4_role = st.text_input("Job 4 Title", "Restaurant Manager")
    job_4_company = st.text_input("Job 4 Company", "Patrick's Restaurant and Bakery")
    job_4_loc = st.text_input("Job 4 Location", "Richfield/Edina, MN")
    job_4_date = st.text_input("Job 4 Date", "February 2018 - February 2020")
    job_4_bullets = st.text_area("Job 4 Details", 
        "Oversaw daily front-of-house operations,