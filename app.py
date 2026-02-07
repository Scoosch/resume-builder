import streamlit as st
from fpdf import FPDF
import base64

# --- CONFIGURATION & PAGE SETUP ---
st.set_page_config(layout="wide", page_title="The Pivot Resume Builder")

# --- CUSTOM CSS FOR PREVIEW ---
# This mimics the "Harvard" look in the web preview
st.markdown("""
<style>
    .resume-preview {
        font-family: 'Times New Roman', Times, serif;
        background-color: white;
        padding: 40px;
        color: black;
        border: 1px solid #ddd;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 { text-align: center; text-transform: uppercase; font-size: 24px; margin-bottom: 5px; color: black; }
    .contact-info { text-align: center; font-size: 14px; margin-bottom: 20px; }
    h2 { 
        text-transform: uppercase; 
        font-size: 16px; 
        border-bottom: 1px solid black; 
        margin-top: 20px; 
        margin-bottom: 10px; 
        padding-bottom: 2px;
        color: black;
    }
    h3 { font-size: 14px; font-weight: bold; margin: 5px 0 2px 0; color: black; }
    .sub-header { font-style: italic; font-size: 14px; display: flex; justify-content: space-between; }
    ul { margin-top: 0; padding-left: 20px; font-size: 14px; }
    li { margin-bottom: 2px; }
</style>
""", unsafe_allow_html=True)

# --- PDF GENERATOR CLASS ---
class PDF(FPDF):
    def header(self):
        # No header content on pages to maximize space, margins handle it
        pass

    def section_title(self, label):
        self.set_font('Times', 'B', 12)
        self.cell(0, 6, label.upper(), 0, 1, 'L')
        self.line(10, self.get_y(), 200, self.get_y()) # Horizontal line
        self.ln(2)

    def section_content_header(self, role, company, location, date):
        self.set_font('Times', 'B', 11)
        self.cell(0, 5, role, 0, 1, 'L')
        self.set_font('Times', 'I', 11)
        # Using a simple trick for right alignment of dates on the same line
        self.cell(100, 5, company, 0, 0, 'L')
        self.cell(0, 5, f"{location}  |  {date}", 0, 1, 'R')

    def bullet_point(self, text):
        self.set_font('Times', '', 11)
        # Clean bullet handling
        if text.strip():
            self.cell(5, 5, "-", 0, 0, 'R')
            self.multi_cell(0, 5, text)
        
# --- SIDEBAR INPUTS ---
st.sidebar.title("Resume Inputs")

with st.sidebar.expander("1. Personal Details", expanded=True):
    name = st.text_input("Full Name", "Joshua E. Doyle")
    contact_info = st.text_input("Contact Line (City, Phone, Email, LinkedIn)", "Robbinsdale, MN | (555) 123-4567 | scoosch@example.com | linkedin.com/in/scoosch")
    summary = st.text_area("Professional Summary", "Culinary professional and self-taught technologist pivoting into IT. Proven ability to troubleshoot complex systems, manage time-sensitive workflows, and apply technical skills in networking and hardware management. CompTIA A+ Certified.")

with st.sidebar.expander("2. Technical Projects (The Pivot)", expanded=True):
    st.info("💡 Tip: Treat your homelab like a job. List 'Home Lab' as the employer.")
    
    proj_1_role = st.text_input("Project 1 Role/Title", "Home Lab Administrator")
    proj_1_tech = st.text_input("Project 1 Tech Stack / Context", "Proxmox, OPNsense, Cisco Networking")
    proj_1_date = st.text_input("Project 1 Date", "2024 - Present")
    proj_1_bullets = st.text_area("Project 1 Details (One per line)", 
        "Designed and deployed a virtualized home lab environment using Proxmox VE hosting multiple LXC containers and VMs.\n"
        "Configured OPNsense firewall with VLANs to segregate IoT traffic from core network devices.\n"
        "Managed Cisco Catalyst switches to learn CLI command structure and layer 2 switching protocols.")

    proj_2_role = st.text_input("Project 2 Role/Title", "3D Printing & Hardware Prototyping")
    proj_2_tech = st.text_input("Project 2 Tech Stack", "Bambu Lab, CAD, Hardware Troubleshooting")
    proj_2_date = st.text_input("Project 2 Date", "2023 - Present")
    proj_2_bullets = st.text_area("Project 2 Details", 
        "Maintained and calibrated Bambu Lab 3D printers for high-precision manufacturing.\n"
        "Troubleshot hardware failures involving extruder assemblies and thermal runaway protection.\n"
        "Utilized G-code and slicer software to optimize print quality and reduce material waste.")

with st.sidebar.expander("3. Professional Experience"):
    job_1_role = st.text_input("Job 1 Title", "Retail & Customer Service Associate")
    job_1_company = st.text_input("Job 1 Company", "Local Frisbee Shop")
    job_1_loc = st.text_input("Job 1 Location", "Minneapolis, MN")
    job_1_date = st.text_input("Job 1 Date", "2024 - Present")
    job_1_bullets = st.text_area("Job 1 Details", "Managed inventory and point-of-sale systems.\nProvided technical advice on equipment specifications to customers.")

with st.sidebar.expander("4. Education & Skills"):
    degree = st.text_input("Degree / Certificate", "CompTIA A+ Certification")
    school = st.text_input("Institution", "CompTIA")
    edu_date = st.text_input("Education Date", "2023")
    
    degree_2 = st.text_input("Degree 2", "Culinary Arts Degree")
    school_2 = st.text_input("Institution 2", "Culinary School")
    edu_date_2 = st.text_input("Education Date 2", "2008")

    skills_tech = st.text_area("Technical Skills", "Hardware: PC Building, Troubleshooting, 3D Printers\nNetworking: TCP/IP, DNS, DHCP, Cisco IOS, VLANs\nSoftware: Windows 10/11, Linux (Ubuntu), Proxmox VE")

# --- LIVE PREVIEW GENERATION ---
st.title("📄 Live Resume Preview")

# Constructing HTML for Preview
html_content = f"""
<div class="resume-preview">
    <h1>{name}</h1>
    <div class="contact-info">{contact_info}</div>
    
    <h2>Professional Summary</h2>
    <p>{summary}</p>

    <h2>Technical Projects</h2>
    <h3>{proj_1_role}</h3>
    <div class="sub-header"><span>{proj_1_tech}</span><span>{proj_1_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in proj_1_bullets.split('\n') if line)}</ul>
    
    <h3>{proj_2_role}</h3>
    <div class="sub-header"><span>{proj_2_tech}</span><span>{proj_2_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in proj_2_bullets.split('\n') if line)}</ul>

    <h2>Experience</h2>
    <h3>{job_1_role}</h3>
    <div class="sub-header"><span>{job_1_company}, {job_1_loc}</span><span>{job_1_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in job_1_bullets.split('\n') if line)}</ul>

    <h2>Education & Certifications</h2>
    <p><strong>{degree}</strong>, {school} <span style="float:right">{edu_date}</span></p>
    <p><strong>{degree_2}</strong>, {school_2} <span style="float:right">{edu_date_2}</span></p>

    <h2>Technical Skills</h2>
    <p>{skills_tech.replace(chr(10), '<br>')}</p>
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)

# --- PDF GENERATION LOGIC ---
def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(20, 20, 20)
    
    # Header
    pdf.set_font('Times', 'B', 24)
    pdf.cell(0, 10, name.upper(), 0, 1, 'C')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, contact_info, 0, 1, 'C')
    pdf.ln(5)

    # Summary
    if summary:
        pdf.section_title("Professional Summary")
        pdf.set_font('Times', '', 11)
        pdf.multi_cell(0, 5, summary)
        pdf.ln(3)

    # Technical Projects (The Pivot)
    pdf.section_title("Technical Projects")
    
    # Project 1
    if proj_1_role:
        pdf.section_content_header(proj_1_role, proj_1_tech, "", proj_1_date)
        for line in proj_1_bullets.split('\n'):
            pdf.bullet_point(line)
        pdf.ln(3)
        
    # Project 2
    if proj_2_role:
        pdf.section_content_header(proj_2_role, proj_2_tech, "", proj_2_date)
        for line in proj_2_bullets.split('\n'):
            pdf.bullet_point(line)
        pdf.ln(3)

    # Experience
    pdf.section_title("Professional Experience")
    if job_1_role:
        pdf.section_content_header(job_1_role, job_1_company, job_1_loc, job_1_date)
        for line in job_1_bullets.split('\n'):
            pdf.bullet_point(line)
        pdf.ln(3)

    # Education
    pdf.section_title("Education & Certifications")
    pdf.set_font('Times', '', 11)
    if degree:
        pdf.cell(140, 5, f"{degree}, {school}", 0, 0)
        pdf.cell(0, 5, edu_date, 0, 1, 'R')
    if degree_2:
        pdf.cell(140, 5, f"{degree_2}, {school_2}", 0, 0)
        pdf.cell(0, 5, edu_date_2, 0, 1, 'R')
    pdf.ln(3)

    # Skills
    pdf.section_title("Technical Skills")
    pdf.set_font('Times', '', 11)
    pdf.multi_cell(0, 5, skills_tech)

    return pdf.output(dest='S').encode('latin-1')

# --- DOWNLOAD BUTTON ---
st.write("---")
pdf_bytes = create_pdf()
st.download_button(
    label="Download PDF Resume (ATS Optimized)",
    data=pdf_bytes,
    file_name="resume.pdf",
    mime="application/pdf"
)