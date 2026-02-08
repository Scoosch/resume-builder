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
        "Oversaw daily front-of-house operations, ensuring high standards of guest service and staff performance.\n"
        "Managed scheduling, inventory control, and vendor relationships to optimize operational efficiency.\n"
        "Resolved escalated customer issues with a focus on retention and satisfaction.")

    # Job 5 (New from History)
    st.markdown("### Job 5: Hospitality Management")
    job_5_role = st.text_input("Job 5 Title", "Restaurant Manager")
    job_5_company = st.text_input("Job 5 Company", "Pizza Lucé")
    job_5_loc = st.text_input("Job 5 Location", "Minnesota")
    job_5_date = st.text_input("Job 5 Date", "February 2015 - August 2017")
    job_5_bullets = st.text_area("Job 5 Details", 
        "Led shift operations in a high-volume dining environment, coordinating between kitchen and service teams.\n"
        "Trained and mentored new staff members on service protocols and menu knowledge.\n"
        "Handled cash management and closing duties with accuracy and accountability.")

with st.sidebar.expander("4. Leadership & Community", expanded=False):
    lead_role = st.text_input("Leadership Role", "League Coordinator")
    lead_org = st.text_input("Organization", "Twin Cities Disc Golf League")
    lead_date = st.text_input("Leadership Date", "2018 - Present")
    lead_bullets = st.text_area("Leadership Details", 
        "Organize weekly events for 50+ members, managing scheduling and digital scorekeeping.\n"
        "Facilitate conflict resolution and enforce league rules to ensure fair play.")

with st.sidebar.expander("5. Education & Skills", expanded=False):
    degree = st.text_input("Degree/Cert", "CompTIA A+ Certification")
    school = st.text_input("Institution", "CompTIA")
    edu_date = st.text_input("Edu Date", "July 2023 - July 2026")
    
    degree_2 = st.text_input("Degree 2", "A.A.S. Restaurant Management")
    school_2 = st.text_input("Institution 2", "Le Cordon Bleu College of Culinary Arts")
    edu_date_2 = st.text_input("Edu Date 2", "May 2007")
    
    skills_tech = st.text_area("Technical Skills", "Hardware: PC Building, Troubleshooting, Hydraulic Testing\nNetworking: TCP/IP, DNS, DHCP, Cisco IOS, Active Directory\nSoftware: Windows, Linux (Ubuntu), Proxmox VE, ServiceNow")

# --- LIVE PREVIEW GENERATION ---
st.title("📄 Live Resume Preview")

# Helper function to generate HTML list items safely
def get_bullets_html(text_input):
    if not text_input:
        return ""
    bullets = []
    for line in text_input.split('\n'):
        if line.strip():
            bullets.append(f'<li>{html.escape(line)}</li>')
    return "".join(bullets)

formatted_skills = html.escape(skills_tech).replace('\n', '<br>')

# Create a complete standalone HTML document
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        margin: 0;
        padding: 20px;
        background-color: #f5f5f5;
    }}
    .resume-preview {{
        font-family: 'Times New Roman', Times, serif;
        background-color: white;
        padding: 40px;
        color: black;
        border: 1px solid #ddd;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-radius: 5px;
        max-width: 850px;
        margin: 0 auto;
    }}
    .resume-preview h1 {{ 
        text-align: center; 
        text-transform: uppercase; 
        font-size: 24px; 
        margin-bottom: 5px; 
        color: black;
    }}
    .resume-preview .contact-info {{ 
        text-align: center; 
        font-size: 14px; 
        margin-bottom: 20px; 
        color: #333;
    }}
    .resume-preview h2 {{ 
        text-transform: uppercase; 
        font-size: 16px; 
        border-bottom: 1px solid black; 
        margin-top: 20px; 
        margin-bottom: 10px; 
        padding-bottom: 2px;
        color: black;
    }}
    .resume-preview h3 {{ 
        font-size: 14px; 
        font-weight: bold; 
        margin: 5px 0 2px 0; 
        color: black;
    }}
    .resume-preview p {{
        color: black;
        margin: 5px 0;
        font-size: 14px;
    }}
    .sub-header {{ 
        font-style: italic; 
        font-size: 14px; 
        display: flex; 
        justify-content: space-between;
        color: black;
        margin-bottom: 5px;
    }}
    .resume-preview ul {{ 
        margin-top: 0; 
        padding-left: 20px; 
        font-size: 14px;
        color: black;
        list-style-type: disc;
    }}
    .resume-preview li {{ 
        margin-bottom: 2px;
        color: black;
    }}
</style>
</head>
<body>
<div class="resume-preview">
    <h1>{html.escape(name)}</h1>
    <div class="contact-info">{html.escape(contact_info)}</div>
    
    <h2>Professional Summary</h2>
    <p>{html.escape(summary)}</p>

    <h2>Technical Projects</h2>
    <h3>{html.escape(proj_1_role)}</h3>
    <div class="sub-header"><span>{html.escape(proj_1_tech)}</span><span>{html.escape(proj_1_date)}</span></div>
    <ul>{get_bullets_html(proj_1_bullets)}</ul>
    
    <h3>{html.escape(proj_2_role)}</h3>
    <div class="sub-header"><span>{html.escape(proj_2_tech)}</span><span>{html.escape(proj_2_date)}</span></div>
    <ul>{get_bullets_html(proj_2_bullets)}</ul>

    <h2>Professional Experience</h2>
    <h3>{html.escape(job_1_role)}</h3>
    <div class="sub-header"><span>{html.escape(job_1_company)}, {html.escape(job_1_loc)}</span><span>{html.escape(job_1_date)}</span></div>
    <ul>{get_bullets_html(job_1_bullets)}</ul>

    <h3>{html.escape(job_2_role)}</h3>
    <div class="sub-header"><span>{html.escape(job_2_company)}, {html.escape(job_2_loc)}</span><span>{html.escape(job_2_date)}</span></div>
    <ul>{get_bullets_html(job_2_bullets)}</ul>

    <h3>{html.escape(job_3_role)}</h3>
    <div class="sub-header"><span>{html.escape(job_3_company)}, {html.escape(job_3_loc)}</span><span>{html.escape(job_3_date)}</span></div>
    <ul>{get_bullets_html(job_3_bullets)}</ul>
    
    {f'<h3>{html.escape(job_4_role)}</h3><div class="sub-header"><span>{html.escape(job_4_company)}, {html.escape(job_4_loc)}</span><span>{html.escape(job_4_date)}</span></div><ul>{get_bullets_html(job_4_bullets)}</ul>' if job_4_role else ''}
    
    {f'<h3>{html.escape(job_5_role)}</h3><div class="sub-header"><span>{html.escape(job_5_company)}, {html.escape(job_5_loc)}</span><span>{html.escape(job_5_date)}</span></div><ul>{get_bullets_html(job_5_bullets)}</ul>' if job_5_role else ''}

    <h2>Leadership & Community</h2>
    <h3>{html.escape(lead_role)}</h3>
    <div class="sub-header"><span>{html.escape(lead_org)}</span><span>{html.escape(lead_date)}</span></div>
    <ul>{get_bullets_html(lead_bullets)}</ul>

    <h2>Education & Certifications</h2>
    <p><strong>{html.escape(degree)}</strong>, {html.escape(school)} <span style="float:right">{html.escape(edu_date)}</span></p>
    <p><strong>{html.escape(degree_2)}</strong>, {html.escape(school_2)} <span style="float:right">{html.escape(edu_date_2)}</span></p>

    <h2>Technical Skills</h2>
    <p>{formatted_skills}</p>
</div>
</body>
</html>
"""

# Use st.components.v1.html for full control
import streamlit.components.v1 as components
components.html(html_content, height=1200, scrolling=True)

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
    if job_3_role:
        pdf.section_content_header(job_3_role, job_3_company, job_3_loc, job_3_date)
        for line in job_3_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)
    if job_4_role:
        pdf.section_content_header(job_4_role, job_4_company, job_4_loc, job_4_date)
        for line in job_4_bullets.split('\n'): pdf.bullet_point(line)
        pdf.ln(3)
    if job_5_role:
        pdf.section_content_header(job_5_role, job_5_company, job_5_loc, job_5_date)
        for line in job_5_bullets.split('\n'): pdf.bullet_point(line)
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
    if degree_2:
        pdf.cell(140, 5, f"{degree_2}, {school_2}", 0, 0)
        pdf.cell(0, 5, edu_date_2, 0, 1, 'R')
    pdf.ln(3)
    
    pdf.set_font('Times', 'B', 11)
    pdf.cell(0, 5, "Technical Skills:", 0, 1)
    pdf.set_font('Times', '', 11)
    pdf.multi_cell(0, 5, skills_tech)

    return pdf.output(dest='S').encode('latin-1', 'replace')

# --- DOWNLOAD BUTTON ---
st.write("---")
pdf_bytes = create_pdf()
st.download_button(
    label="Download PDF Resume",
    data=pdf_bytes,
    file_name="resume.pdf",
    mime="application/pdf"
)
