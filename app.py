import streamlit as st
from fpdf import FPDF

# --- CONFIGURATION & PAGE SETUP ---
st.set_page_config(layout="wide", page_title="The Pivot Resume Builder")

# --- CUSTOM CSS FOR PREVIEW ---
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
        pass # Margins handle the spacing

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
        self.cell(0, 5, f"{location}  |  {date}", 0, 1, 'R')

    def bullet_point(self, text):
        self.set_font('Times', '', 11)
        if text.strip():
            self.cell(5, 5, "-", 0, 0, 'R')
            self.multi_cell(0, 5, text)
        
# --- SIDEBAR INPUTS ---
st.sidebar.title("Resume Inputs")

with st.sidebar.expander("1. Personal Details", expanded=False):
    name = st.text_input("Full Name", "Joshua E. Doyle")
    contact_info = st.text_input("Contact Line", "Robbinsdale, MN | (555) 123-4567 | scoosch@example.com")
    summary = st.text_area("Professional Summary", "Culinary professional and self-taught technologist pivoting into IT. Proven ability to troubleshoot complex systems, manage time-sensitive workflows, and apply technical skills in networking and hardware management. CompTIA A+ Certified.")

with st.sidebar.expander("2. Technical Projects (The Pivot)", expanded=True):
    st.info("💡 Highlight your Homelab & 3D Printing here.")
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

with st.sidebar.expander("3. Professional Experience (Mgmt & Ops)", expanded=True):
    st.info("💡 We added your Chef experience here to show Management skills.")
    
    # Job 1 (Current/Retail)
    job_1_role = st.text_input("Job 1 Title", "Retail & Customer Service Associate")
    job_1_company = st.text_input("Job 1 Company", "Local Frisbee Shop")
    job_1_loc = st.text_input("Job 1 Location", "Minneapolis, MN")
    job_1_date = st.text_input("Job 1 Date", "2024 - Present")
    job_1_bullets = st.text_area("Job 1 Details", 
        "Manage inventory tracking and point-of-sale systems accuracy.\n"
        "Provide technical product advice, requiring rapid learning of new inventory specs.")

    # Job 2 (Restaurant/Management)
    st.markdown("---")
    job_2_role = st.text_input("Job 2 Title", "Executive Chef / Kitchen Manager")
    job_2_company = st.text_input("Job 2 Company", "High-Volume Restaurant Group")
    job_2_loc = st.text_input("Job 2 Location", "Minneapolis, MN")
    job_2_date = st.text_input("Job 2 Date", "2015 - 2023")
    job_2_bullets = st.text_area("Job 2 Details", 
        "Managed back-of-house operations, including staff scheduling, inventory logistics, and vendor relations.\n"
        "Implemented cost-control systems reducing waste by 15% through strict inventory tracking.\n"
        "Maintained compliance with strict health and safety protocols under high-pressure conditions.")

with st.sidebar.expander("4. Leadership & Community", expanded=True):
    lead_role = st.text_input("Leadership Role", "League Coordinator")
    lead_org = st.text_input("Organization", "Twin Cities Disc Golf League")
    lead_date = st.text_input("Leadership Date", "2018 - Present")
    lead_bullets = st.text_area("Leadership Details", 
        "Organize weekly events for 50+ members, managing scheduling and digital scorekeeping.\n"
        "Facilitate conflict resolution and enforce league rules to ensure fair play.\n"
        "Coordinate with local parks departments for course maintenance and event permits.")

with st.sidebar.expander("5. Education & Skills", expanded=False):
    degree = st.text_input("Degree/Cert", "CompTIA A+ Certification")
    school = st.text_input("Institution", "CompTIA")
    edu_date = st.text_input("Edu Date", "2023")
    skills_tech = st.text_area("Technical Skills", "Hardware: PC Building, Troubleshooting, 3D Printers\nNetworking: TCP/IP, DNS, DHCP, Cisco IOS\nSoftware: Windows, Linux (Ubuntu), Proxmox VE")

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

    <h2>Professional Experience</h2>
    <h3>{job_1_role}</h3>
    <div class="sub-header"><span>{job_1_company}, {job_1_loc}</span><span>{job_1_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in job_1_bullets.split('\n') if line)}</ul>

    <h3>{job_2_role}</h3>
    <div class="sub-header"><span>{job_2_company}, {job_2_loc}</span><span>{job_2_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in job_2_bullets.split('\n') if line)}</ul>

    <h2>Leadership & Community</h2>
    <h3>{lead_role}</h3>
    <div class="sub-header"><span>{lead_org}</span><span>{lead_date}</span></div>
    <ul>{"".join(f'<li>{line}</li>' for line in lead_bullets.split('\n') if line)}</ul>

    <h2>Education & Certifications</h2>
    <p><strong>{degree}</strong>, {school} <span style="float:right">{edu_date}</span></p>

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

    # Technical Projects
    pdf.section_title("Technical Projects")
    if proj_1_role:
        pdf.section_content_header(proj_1_role, proj_1_tech, "", proj_1_date)
        for line in proj_1_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)
    if proj_2_role:
        pdf.section_content_header(proj_2_role, proj_2_tech, "", proj_2_date)
        for line in proj_2_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)

    # Experience
    pdf.section_title("Professional Experience")
    if job_1_role:
        pdf.section_content_header(job_1_role, job_1_company, job_1_loc, job_1_date)
        for line in job_1_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)
    if job_2_role:
        pdf.section_content_header(job_2_role, job_2_company, job_2_loc, job_2_date)
        for line in job_2_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)

    # Leadership
    if lead_role:
        pdf.section_title("Leadership & Community")
        pdf.section_content_header(lead_role, lead_org, "", lead_date)
        for line in lead_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)

    # Education & Skills
    pdf.section_title("Education & Skills")
    pdf.set_font('Times', '', 11)
    if degree:
        pdf.cell(140, 5, f"{degree}, {school}", 0, 0)
        pdf.cell(0, 5, edu_date, 0, 1, 'R')
    pdf.ln(3)
    pdf.set_font('Times', 'B', 11)
    pdf.cell(0, 5, "Technical Skills:", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.multi_cell(0, 5, skills_tech)

    return pdf.output(dest='S').encode('latin-1')

# --- DOWNLOAD BUTTON ---
st.write("---")
pdf_bytes = create_pdf()
st.download_button(
    label="Download PDF Resume",
    data=pdf_bytes,
    file_name="resume.pdf",
    mime="application/pdf"
)
