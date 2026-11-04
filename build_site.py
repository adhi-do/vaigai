#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

print("Building complete index.html and app.js...")

# Let's define the 35 pages content in a structured format
pages_data = [
    # Page 1: Cover Page
    {
        "id": "page-1",
        "num": 1,
        "is_cover": True,
        "density": "hard",
        "header_title": "VAIGAI COLLEGE OF ENGINEERING",
        "header_tag": "OFFICIAL BIMONTHLY GAZETTE",
        "title": "VAIGAI'S IKIGAI",
        "subtitle": "Where Purpose Meets Possibility",
        "html": """
        <div class="masthead-container">
            <div class="masthead-ears">
                <span>✦ APPROVED BY AICTE • AFFILIATED TO ANNA UNIVERSITY</span>
                <span>VOL. 01 • ISSUE 01 • MADURAI ✦</span>
            </div>
            <img src="word/media/image1.jpeg" alt="Vaigai's Ikigai Masthead" class="masthead-banner-img" style="border: 1px solid var(--paper-border); border-radius: 3px;">
            <h1 class="masthead-title">VAIGAI'S IKIGAI</h1>
            <p class="masthead-tagline">Where Purpose Meets Possibility — The Bimonthly Newsletter</p>
            <div class="masthead-meta-bar">
                <span>MADURAI, TAMIL NADU</span>
                <span>JULY – AUGUST 2026</span>
                <span>FREE INAUGURAL EDITION</span>
            </div>
        </div>

        <div style="text-align: center; margin: 10px 0;">
            <div class="splash-logo-wrapper" style="width: 110px; height: 75px; margin: 0 auto 8px;">
                <img src="logo.png" alt="Vaigai College Crest" class="splash-logo">
            </div>
            <div style="font-family: var(--font-display); font-size: 0.85rem; letter-spacing: 2px; color: var(--accent); font-weight: 700;">
                VAIGAI COLLEGE OF ENGINEERING
            </div>
            <div style="font-family: var(--font-sans); font-size: 0.72rem; color: var(--text-muted);">
                Approved by AICTE, New Delhi & Affiliated to Anna University, Chennai
            </div>
        </div>

        <div class="pretext-card" style="margin: 8px 0; background: #fffcf5; border-color: var(--accent);">
            <div style="font-family: var(--font-display); font-size: 0.78rem; font-weight: bold; color: var(--primary); text-transform: uppercase; border-bottom: 1px solid var(--paper-border); padding-bottom: 3px; margin-bottom: 6px;">
                ✦ Editorial Board
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.74rem;">
                <div>
                    <strong>Dr. Sivaranjani. R</strong><br>
                    <span style="color: var(--text-muted); font-size: 0.68rem;">Principal (i/c) & Prof/ECE</span>
                </div>
                <div>
                    <strong>Ms. Aswini. R</strong><br>
                    <span style="color: var(--text-muted); font-size: 0.68rem;">Assistant Professor of English</span>
                </div>
                <div>
                    <strong>Ms. Supriya. R.J</strong><br>
                    <span style="color: var(--text-muted); font-size: 0.68rem;">Assistant Professor of English</span>
                </div>
                <div>
                    <strong>Student Editorial Board</strong><br>
                    <span style="color: var(--text-muted); font-size: 0.68rem;">Creative & Media Council</span>
                </div>
            </div>
        </div>

        <div style="border-top: 2px solid var(--text-headline); padding-top: 6px; margin-top: 6px;">
            <div style="font-family: var(--font-display); font-size: 0.82rem; font-weight: bold; color: var(--accent); letter-spacing: 1px; text-transform: uppercase;">
                ★ In This Bimonthly Issue
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px; font-size: 0.7rem; color: var(--text-dark); margin-top: 4px;">
                <div>• Civil & Mechanical Associations Inaugurated</div>
                <div>• 16 Besant JRIP IT & Core Placements</div>
                <div>• Caliber IoT Workshop with 38 Engineers</div>
                <div>• Anna University Rank Holders Honors</div>
                <div>• 40 Units Blood Donated to Meenakshi Mission</div>
                <div>• State Speech Laurels & 7 Research Papers</div>
            </div>
        </div>
        """
    },

    # Page 2: Pretext & About Vaigai College
    {
        "id": "page-2",
        "num": 2,
        "density": "soft",
        "header_title": "VAIGAI'S IKIGAI • JULY – AUGUST 2026",
        "header_tag": "PREFACE & FOUNDATION",
        "title": "What is Vaigai's Ikigai?",
        "subtitle": "The Philosophy That Guides Our Vision and Community",
        "html": """
        <h2 class="headline-lead">WHAT IS VAIGAI'S IKIGAI?</h2>
        <p class="headline-sub">The convergence of purpose, passion, vocation and contribution at Vaigai College of Engineering.</p>

        <div class="pretext-card" style="background: linear-gradient(135deg, #fffbf0 0%, #ffffff 100%); border-left: 4px solid var(--accent);">
            <div class="pretext-item">
                <span class="pretext-letter">V</span>
                <div><strong>The Vision</strong> that drives our institutional mission and fuels boundless ambition.</div>
            </div>
            <div class="pretext-item">
                <span class="pretext-letter">A</span>
                <div><strong>The Achievements</strong> that define our students and faculty on national platforms.</div>
            </div>
            <div class="pretext-item">
                <span class="pretext-letter">I</span>
                <div><strong>The Intelligence</strong> that inspires technological innovation and critical inquiry.</div>
            </div>
            <div class="pretext-item">
                <span class="pretext-letter">G</span>
                <div><strong>The Greatness</strong> we nurture through ethical leadership and character building.</div>
            </div>
            <div class="pretext-item">
                <span class="pretext-letter">A</span>
                <div><strong>The Academic aspirations</strong> we relentlessly pursue for global competitiveness.</div>
            </div>
            <div class="pretext-item">
                <span class="pretext-letter">I</span>
                <div><strong>The Innovations</strong> through which our engineers create meaningful societal impact.</div>
            </div>
        </div>

        <h3 class="headline-section" style="margin-top: 14px;">
            <span>About Vaigai College</span>
            <span class="headline-tag">Est. 2012</span>
        </h3>

        <div class="editorial-cols dropcap">
            <p>Vaigai College of Engineering (VCE) was established in 2012 under the aegis of the Vaigai Educational Trust (VET), Madurai, with the steadfast vision of delivering quality technical education and nurturing socially conscious global citizens. With a deep commitment to making cutting-edge engineering accessible to students from diverse socio-economic backgrounds, the institution champions value-based learning.</p>
            <p>Approved by the All India Council for Technical Education (AICTE), New Delhi, and permanently affiliated with Anna University, Chennai, VCE is set across a serene 15-acre lush green campus in Madurai. The campus boasts state-of-the-art academic complexes, lecture theatres, Dr. Abdul Kalam Auditorium, central library, advanced high-performance computing centers, dedicated engineering laboratories, sports grounds, residential hostels, and an active Training & Placement Cell.</p>
        </div>

        <div class="pull-quote" style="margin-top: 10px; font-size: 0.88rem;">
            "Inspiring young minds to become skilled, confident, innovative and responsible contributors to society."
        </div>
        """
    },

    # Page 3: Civil Engineering - RACE Inauguration
    {
        "id": "page-3",
        "num": 3,
        "density": "soft",
        "header_title": "DEPARTMENT OF CIVIL ENGINEERING",
        "header_tag": "ASSOCIATION INAUGURAL",
        "title": "RACE Association Inauguration Ceremony",
        "subtitle": "Royal Association of Civil Engineering Commences 2026 Academic Season",
        "html": """
        <div class="headline-section">
            <span>DEPARTMENT OF CIVIL ENGINEERING</span>
            <span class="headline-tag">21 JULY 2026</span>
        </div>
        <h2 class="headline-lead">INAUGURATION CEREMONY OF RACE – ROYAL ASSOCIATION OF CIVIL ENGINEERING</h2>
        <div class="byline-bar">
            <span class="byline-date">VENUE: ML-2 AUDITORIUM</span>
            <span>•</span>
            <span>PRESIDED BY DR. R. SIVARANJANI</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Department of Civil Engineering, in association with RACE – Royal Association of Civil Engineering, organized the grand Inauguration Ceremony of RACE on 21 July 2026 at Seminar Hall ML-2. Dr. R. Sivaranjani, Principal i/c, graced the historic occasion as Chief Guest, accompanied by Mr. T. Vijaya Raghavan, Head of the Department of Civil Engineering, and Mr. P. Muthuanand, Association Faculty In-charge.</p>
            <p>The ceremony emphasized the vital importance of student involvement in academic symposia, structural modeling, site visits, and leadership forums. Addressing the gathering, the dignitaries inspired the budding civil engineers to address sustainable infrastructure challenges and urban resilience.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 8px;">
            <div class="news-image-frame">
                <img src="word/media/image2.jpeg" alt="RACE Department Crest" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Royal Association of Civil Engineering Dignitaries</span>
                    <span class="caption-tag">RACE 2026</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image3.jpeg" alt="Civil Engineering Inaugural Session" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Inaugural Dais at Seminar Hall ML-2</span>
                    <span class="caption-tag">Chief Guest Address</span>
                </div>
            </div>
        </div>

        <div style="font-size: 0.75rem; color: var(--text-muted); font-style: italic; text-align: center; margin-top: 4px;">
            "Civil engineering is the backbone of civilization; student associations serve as the launchpad for tomorrow's master builders."
        </div>
        """
    },

    # Page 4: Civil Engineering - Badge Distribution Ceremony
    {
        "id": "page-4",
        "num": 4,
        "density": "soft",
        "header_title": "DEPARTMENT OF CIVIL ENGINEERING",
        "header_tag": "LEADERSHIP INVESTITURE",
        "title": "RACE Student Leadership Investiture",
        "subtitle": "Ceremonial Badge Distribution Recognizes Student Office Bearers",
        "html": """
        <h2 class="headline-lead">STUDENT LEADERS INVESTED AT RACE BADGE CEREMONY</h2>
        <p class="headline-sub">Formal Recognition of President, Vice President, Secretary, and Treasurers for Academic Year 2026</p>

        <div class="editorial-cols dropcap">
            <p>A distinguished badge distribution ceremony was conducted to formally recognize the newly elected student office bearers of RACE. The badges were pinned by Principal Dr. R. Sivaranjani and HoD Mr. T. Vijaya Raghavan, charging the student leaders with organizing technical workshops, national conferences, survey camps, and community development projects.</p>
            <p>The office bearers pledged their commitment to uphold the values of ethical engineering, peer mentoring, and academic excellence, marking the beginning of an eventful and productive association calendar.</p>
        </div>

        <div class="image-gallery-triple" style="margin-top: 8px;">
            <div class="news-image-frame">
                <img src="word/media/image4.jpeg" alt="Office Bearer Badge Distribution" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Office Bearers Investiture</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image5.jpeg" alt="Badge Distribution by Principal" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Honoring Student Leadership</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image6.jpeg" alt="RACE Student Executive Team" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Executive Council 2026</span></div>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 10px; padding: 10px;">
            <div style="font-family: var(--font-display); font-size: 0.75rem; font-weight: bold; color: var(--primary);">
                ✦ RACE Executive Council Roll
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Student Office Bearers: <strong>President, Vice President, Secretary, Treasurer, and Joint Treasurers</strong>. Faculty In-Charge: <strong>Mr. P. Muthuanand, AP/Civil</strong>.
            </div>
        </div>
        """
    },

    # Page 5: Mechanical Engineering - MESA 2026 Inaugural
    {
        "id": "page-5",
        "num": 5,
        "density": "soft",
        "header_title": "DEPARTMENT OF MECHANICAL ENGINEERING",
        "header_tag": "MESA–2026",
        "title": "Mechanical Engineers Student Association Inaugural",
        "subtitle": "MESA–2026 Inaugurated to Spur Innovation and Industrial Dynamism",
        "html": """
        <div class="headline-section">
            <span>DEPARTMENT OF MECHANICAL ENGINEERING</span>
            <span class="headline-tag">19 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">INAUGURAL FUNCTION OF MECHANICAL ENGINEERS STUDENT ASSOCIATION (MESA–2026)</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 19 AUGUST 2026</span>
            <span>•</span>
            <span>ORGANIZED BY DR. M.K.V. KARTHIKEYAN & MR. A.M. MILAN</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Department of Mechanical Engineering organized the grand Inaugural Function of the Mechanical Engineers Student Association (MESA–2026) on 19 August 2026 for students and faculty members. Dr. R. Sivaranjani, Principal (i/c), Vaigai College of Engineering, graced the occasion as the Presiding Dignitary and addressed the spirited gathering.</p>
            <p>The programme marked the commencement of the association's academic calendar, providing students with an empowering platform to master industrial robotics, CAD/CAM prototyping, thermal analysis, and sustainable manufacturing practices.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image7.jpeg" alt="MESA 2026 Banner" class="news-img" style="max-height: 175px;">
                <div class="news-caption">
                    <span>MESA–2026 Inaugural Banner</span>
                    <span class="caption-tag">Mechanical Dept</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image8.jpeg" alt="Dais Dignitaries MESA" class="news-img" style="max-height: 175px;">
                <div class="news-caption">
                    <span>Principal Dr. R. Sivaranjani Addressing MESA</span>
                    <span class="caption-tag">Auditorium</span>
                </div>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "Mechanical engineering represents the power that drives the physical universe — from macro aerospace structures to precision micro-devices."
        </div>
        """
    },

    # Page 6: Mechanical Engineering - Horizons & Student Activities
    {
        "id": "page-6",
        "num": 6,
        "density": "soft",
        "header_title": "DEPARTMENT OF MECHANICAL ENGINEERING",
        "header_tag": "CO-CURRICULAR HORIZONS",
        "title": "MESA Technical Initiatives & Competencies",
        "subtitle": "Fostering Leadership, Teamwork, Design Thinking and Industry Alignment",
        "html": """
        <h2 class="headline-lead">FORGING LEADERSHIP, DESIGN THINKING & TEAMWORK</h2>
        <p class="headline-sub">MESA–2026 Establishes Working Groups in Robotics, 3D Prototyping and Automotive Dynamics</p>

        <div class="editorial-cols dropcap">
            <p>The association serves as a catalyst for students to enhance leadership, teamwork, communication, and technical presentation skills. Under the mentorship of HoD Dr. M.K.V. Karthikeyan and Association In-Charge Mr. A.M. Milan, MESA announced year-round technical paper competitions, hands-on workshops on Autodesk Fusion AI design, and industrial site tours.</p>
            <p>Student representatives pledged to cultivate a rigorous problem-solving approach and foster interdisciplinary collaboration with electrical and computing disciplines to develop next-generation smart robotic mechanisms.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image9.jpeg" alt="MESA Student Delegation" class="news-img" style="max-height: 240px;">
            <div class="news-caption">
                <span>Faculty Members and Student Delegates at MESA–2026 Inauguration</span>
                <span class="caption-tag">VCE Mechanical Delegation</span>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px;">
            <div style="font-family: var(--font-display); font-size: 0.74rem; font-weight: bold; color: var(--accent);">
                ✦ MESA–2026 Focus Areas
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Robotics & Automation • AI-Assisted CAD Prototyping • Computational Fluid Dynamics • Eco-Friendly Automotive Design • Student National Symposiums.
            </div>
        </div>
        """
    },

    # Page 7: ECE & EEE - Joint Workshop on Embedded Systems & IoT
    {
        "id": "page-7",
        "num": 7,
        "density": "soft",
        "header_title": "DEPARTMENTS OF ECE & EEE",
        "header_tag": "TECHNICAL WORKSHOP",
        "title": "Joint Workshop on Embedded Systems & IoT",
        "subtitle": "Caliber Virtual Technologies Partners with VCE for 7-Day Hands-on Training",
        "html": """
        <div class="headline-section">
            <span>DEPARTMENTS OF ECE & EEE</span>
            <span class="headline-tag">27 JULY – 3 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">ONE-WEEK WORKSHOP ON EMBEDDED SYSTEMS AND IOT</h2>
        <div class="byline-bar">
            <span class="byline-date">VENUE: ML-3 LABS</span>
            <span>•</span>
            <span>38 DELEGATES (32 ECE & 6 EEE)</span>
            <span>•</span>
            <span>CALIBER VIRTUAL TECHNOLOGIES</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Departments of Electronics and Communication Engineering (ECE) and Electrical and Electronics Engineering (EEE) jointly organized an intensive One-Week Workshop on Embedded Systems and IoT from 27 July to 3 August 2026 at ML-3 for III and IV year engineers. The workshop was conducted in technical collaboration with Caliber Virtual Technologies.</p>
            <p>Industry trainers delivered deep-dive training on microcontroller architectures, sensor interfacing, wireless telemetry, MQTT communication protocols, and cloud IoT dashboards, transforming students from conceptual learners to agile builders.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image10.jpeg" alt="IoT Workshop Poster" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Official IoT Workshop Poster</span>
                    <span class="caption-tag">Caliber Virtual</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image11.jpeg" alt="Theoretical IoT Concepts Session" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Embedded Systems Theory & Hardware Briefing</span>
                    <span class="caption-tag">ML-3 Lecture</span>
                </div>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 4px; text-align: center;">
            Coordinators: <strong>Dr. R. Sivaranjani</strong> (Principal & Prof/ECE), <strong>Mr. A. Shakil Ahmed</strong> (AP/ECE), and <strong>Ms. V. Saranya</strong> (AP/EEE).
        </div>
        """
    },

    # Page 8: ECE & EEE - Hands-on IoT Development Lab
    {
        "id": "page-8",
        "num": 8,
        "density": "soft",
        "header_title": "DEPARTMENTS OF ECE & EEE",
        "header_tag": "IOT APPLICATION LAB",
        "title": "Hands-on Sensor Interfacing & Embedded Code",
        "subtitle": "38 Participating Engineers Build Working Connected IoT Devices",
        "html": """
        <h2 class="headline-lead">FROM SILICON TO CLOUD: REAL-TIME IOT APPLICATIONS</h2>
        <p class="headline-sub">Students Program Microcontrollers and Deploy Live Sensor Telemetry</p>

        <div class="editorial-cols dropcap">
            <p>The practical lab sessions provided each participant with hands-on breakout hardware, ultrasonic and environmental sensor arrays, and Wi-Fi embedded boards. Students actively coded firmware, debugged serial communications, and connected sensors to cloud-hosted analytics dashboards.</p>
            <p>A total of 38 students, comprising 32 ECE and 6 EEE students, successfully completed the grueling 7-day curriculum. The workshop substantially elevated their practical problem-solving proficiencies, equipping them to engineer microcontroller- and sensor-driven smart automation solutions.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image12.jpeg" alt="Students in IoT Lab" class="news-img" style="max-height: 240px;">
            <div class="news-caption">
                <span>Hands-on Laboratory Training: Students Deploying Embedded IoT Codes</span>
                <span class="caption-tag">Lab Session ML-3</span>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px;">
            <div style="font-family: var(--font-display); font-size: 0.74rem; font-weight: bold; color: var(--primary);">
                ✦ Key Technical Skills Acquired
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Microcontroller GPIO & Register Programming • ADC & Sensor Calibration • UART / SPI / I2C Bus Communication • Wi-Fi / MQTT Cloud Telemetry • Smart Sensor Dashboards.
            </div>
        </div>
        """
    },

    # Page 9: Cells & Clubs - Faculty Development Cell (FDC)
    {
        "id": "page-9",
        "num": 9,
        "density": "soft",
        "header_title": "CELLS, CLUBS & INSTITUTIONAL ACTIVITIES",
        "header_tag": "FACULTY DEVELOPMENT",
        "title": "FDC: 'IIC & YOU: Building an Innovation Culture'",
        "subtitle": "Institutional Innovation Council Fosters Campus-Wide Ideation",
        "html": """
        <div class="headline-section">
            <span>FACULTY DEVELOPMENT CELL (FDC)</span>
            <span class="headline-tag">31 JULY 2026</span>
        </div>
        <h2 class="headline-lead">FACULTY DEVELOPMENT PROGRAMME: "IIC & YOU: BUILDING AN INNOVATION CULTURE"</h2>
        <div class="byline-bar">
            <span class="byline-date">DR. ABDUL KALAM AUDITORIUM</span>
            <span>•</span>
            <span>3:00 P.M. TO 4:00 P.M.</span>
            <span>•</span>
            <span>RESOURCE PERSON: MS. V. SARANYA</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Faculty Development Cell (FDC) of Vaigai College of Engineering organized a dynamic Faculty Development Programme titled "IIC & YOU: Building an Innovation Culture" on 31 July 2026 at the Dr. Abdul Kalam Auditorium from 3:00 p.m. to 4:00 p.m.</p>
            <p>The informative session was delivered by Ms. V. Saranya, M.E., (Ph.D.), Assistant Professor in the Department of Electrical and Electronics Engineering. The programme focused on raising heightened awareness among faculty members regarding their crucial role in nurturing a vibrant campus innovation ecosystem.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image13.jpeg" alt="FDC Programme Banner" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>Faculty Development Programme Banner: "IIC & YOU: Building an Innovation Culture"</span>
                <span class="caption-tag">FDC 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Programme Coordinated by <strong>Dr. B. Sujatha</strong>, Dean Academics & <strong>Mr. K.M. Mohan</strong>, Management Representative.
        </div>
        """
    },

    # Page 10: FDC - Innovation Forum in Action
    {
        "id": "page-10",
        "num": 10,
        "density": "soft",
        "header_title": "CELLS, CLUBS & INSTITUTIONAL ACTIVITIES",
        "header_tag": "FACULTY FORUM",
        "title": "Faculty Innovation Framework & Incubation",
        "subtitle": "Institutional Roadmap for Patents, Student Mentoring and Startups",
        "html": """
        <h2 class="headline-lead">INNOVATION, COLLABORATION & ENTREPRENEURSHIP</h2>
        <p class="headline-sub">Faculty Members Engage in Strategic Blueprint for AICTE / MoE Innovation Cell Alignment</p>

        <div class="editorial-cols dropcap">
            <p>During the session, Ms. V. Saranya outlined actionable avenues for faculty members to mentor student-led technical innovations and guide patent filings under the Ministry of Education's Innovation Cell (MIC) framework. The discourse highlighted how interdisciplinary projects unlock regional problem-solving capabilities.</p>
            <p>Dr. B. Sujatha, Dean Academics, emphasized that sustained faculty engagement is the bedrock of institutional reputation. The forum concluded with active discussions on establishing department-level innovation circles to identify and nurture patentable prototypes.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image14.jpeg" alt="FDC Auditorium Session" class="news-img" style="max-height: 250px;">
            <div class="news-caption">
                <span>Faculty Members of Vaigai College Assembled at Dr. Abdul Kalam Auditorium</span>
                <span class="caption-tag">Auditorium Forum</span>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "A thriving culture of innovation begins in the lecture hall, is nurtured in the laboratory, and is realized in societal transformation."
        </div>
        """
    },

    # Page 11: Youth Red Cross & Red Ribbon Club - Health Awareness
    {
        "id": "page-11",
        "num": 11,
        "density": "soft",
        "header_title": "YOUTH RED CROSS & RED RIBBON CLUB",
        "header_tag": "PREVENTIVE HEALTHCARE",
        "title": "Health Awareness Programme — 27 July 2026",
        "subtitle": "AYUSH Medical Officer Dr. M. Janaki Guides Students on Holistic Wellness",
        "html": """
        <div class="headline-section">
            <span>YOUTH RED CROSS & RED RIBBON CLUB</span>
            <span class="headline-tag">27 JULY 2026</span>
        </div>
        <h2 class="headline-lead">CAMPUS-WIDE HEALTH AWARENESS & PREVENTIVE LIFESTYLE PROGRAMME</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 27 JULY 2026</span>
            <span>•</span>
            <span>GUEST SPEAKER: DR. M. JANAKI (AYUSH HEALTH CENTER)</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Youth Red Cross (YRC) and Red Ribbon Club (RRC) organized a comprehensive Health Awareness Programme on 27 July 2026 for students spanning all engineering departments. Dr. M. Janaki, Medical Officer, AYUSH Health and Wellness Center (Homeopathy), Therkutheru, Madurai, served as the esteemed resource person.</p>
            <p>Dr. Janaki educated students on the fundamentals of balanced nutrition, circadian wellness, hydration, stress management, and natural preventive therapies, urging engineers to maintain physical vigor alongside rigorous academic study.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image15.jpeg" alt="Health Awareness Poster" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>YRC & RRC Health Programme Poster</span>
                    <span class="caption-tag">Official Announcement</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image16.jpeg" alt="Dr. M. Janaki Address" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Dr. M. Janaki Addressing Student Gathering</span>
                    <span class="caption-tag">Keynote Speech</span>
                </div>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Coordinators: <strong>Mr. C. Balaguru</strong> (AP/Mech, RRC) & <strong>Mr. R. Rajendran</strong> (AP/Civil, YRC).
        </div>
        """
    },

    # Page 12: YRC & RRC - Health Awareness Gallery
    {
        "id": "page-12",
        "num": 12,
        "density": "soft",
        "header_title": "YOUTH RED CROSS & RED RIBBON CLUB",
        "header_tag": "WELLNESS GALLERY",
        "title": "Interactive Student Wellness Demonstrations",
        "subtitle": "Interactive Sessions on Ergonomics, Stress Relief and Wholesome Habits",
        "html": """
        <h2 class="headline-lead">HOLISTIC WELLNESS: PREVENTIVE HABITS IN DAILY LIFE</h2>
        <p class="headline-sub">Engineers Practice Ergonomic Postures, Mindful Breathing, and Dietary Discipline</p>

        <div class="editorial-cols dropcap">
            <p>The interactive session featured live demonstrations where students engaged in posture correction exercises designed to alleviate strain caused by extensive desk work and digital device usage. Dr. Janaki responded to extensive student queries regarding sleep hygiene and dietary discipline.</p>
            <p>The programme successfully fostered heightened health consciousness across the student fraternity, highlighting that robust physical well-being is the bedrock of intellectual sharpness and enduring academic achievement.</p>
        </div>

        <div class="image-gallery-triple" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image17.jpeg" alt="Student Audience" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Engaged Student Gathering</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image18.jpeg" alt="Interactive Health Q&A" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Interactive Q&A Session</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image19.jpeg" alt="Auditorium Health Session" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Campus Wellness Initiative</span></div>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px;">
            <div style="font-family: var(--font-display); font-size: 0.74rem; font-weight: bold; color: var(--primary);">
                ✦ Key Wellness Takeaways
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Mind-Body Harmony • Digital Ergonomics • Natural Immunity Optimization • Preventive Holistic Care • Healthy Dietary Practices.
            </div>
        </div>
        """
    },

    # Page 13: YRC, RRC & NSS - Mega Blood Donation Camp
    {
        "id": "page-13",
        "num": 13,
        "density": "soft",
        "header_title": "INSTITUTIONAL SOCIAL RESPONSIBILITY",
        "header_tag": "BLOOD DONATION CAMP",
        "title": "Blood Donation Camp — 31 July 2026",
        "subtitle": "40 Units of Life-Saving Blood Donated to Meenakshi Mission Hospital",
        "html": """
        <div class="headline-section">
            <span>NSS • YRC • RRC COLLABORATION</span>
            <span class="headline-tag">31 JULY 2026</span>
        </div>
        <h2 class="headline-lead">MEGA BLOOD DONATION CAMP: OVER 50 VOLUNTEERS REGISTER TO SAVE LIVES</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 31 JULY 2026</span>
            <span>•</span>
            <span>IN PARTNERSHIP WITH MEENAKSHI MISSION HOSPITAL</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The National Service Scheme (NSS), Youth Red Cross (YRC), and Red Ribbon Club (RRC) jointly organized a highly successful Blood Donation Camp on 31 July 2026 in collaboration with Meenakshi Mission Hospital, Madurai. More than 50 enthusiastic students and staff members voluntarily registered.</p>
            <p>Following strict medical screenings and hemoglobin diagnostics, 40 units of life-saving blood were safely collected. A team of specialist doctors, nurses, and medical technicians expertly supervised the entire procedure, sharing valuable awareness regarding the safety and health benefits of regular voluntary donation.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image20.jpeg" alt="Blood Donation Camp Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>Blood Donation Camp Official Poster: In Partnership with Meenakshi Mission Hospital</span>
                <span class="caption-tag">31 July 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Camp Coordinated by <strong>Mr. C. Balaguru</strong> (RRC) & <strong>Mr. R. Rajendran</strong> (YRC).
        </div>
        """
    },

    # Page 14: Blood Donation Camp - Donor Honors
    {
        "id": "page-14",
        "num": 14,
        "density": "soft",
        "header_title": "INSTITUTIONAL SOCIAL RESPONSIBILITY",
        "header_tag": "DONOR HONORS",
        "title": "Honoring Student & Faculty Donors",
        "subtitle": "Certificates of Commendation Awarded to 40 Life Savers",
        "html": """
        <h2 class="headline-lead">CELEBRATING SOCIAL RESPONSIBILITY AND SERVICE</h2>
        <p class="headline-sub">Certificates Distributed to Donors in Token of Deep Institutional Appreciation</p>

        <div class="editorial-cols dropcap">
            <p>Every donor was presented with a formal certificate of appreciation and nutritional refreshments. The medical team commended the high spirit of altruism exhibited by Vaigai students, highlighting that every unit of blood donated can save up to three critical lives in emergency trauma and surgical care.</p>
            <p>The initiative profoundly reinforced the ethos of selfless civic engagement and institutional social responsibility across the campus community, embodying the core Ikigai principle of contribution.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image21.jpeg" alt="Blood Donation Medical Procedures" class="news-img" style="max-height: 250px;">
            <div class="news-caption">
                <span>Medical Officers Conducting Safe Blood Collection from Volunteer Donors</span>
                <span class="caption-tag">Clinical Unit ML Campus</span>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "Tears of a mother cannot save her child, but your blood can. Giving blood is giving life."
        </div>
        """
    },

    # Page 15: Red Ribbon Club - TNSACS State-Level Quiz
    {
        "id": "page-15",
        "num": 15,
        "density": "soft",
        "header_title": "RED RIBBON CLUB (RRC)",
        "header_tag": "STATE COMPETITION",
        "title": "TNSACS State-Level Online Quiz — 12 August 2026",
        "subtitle": "140+ Students Participate Under Intensified IEC Campaign 3.0",
        "html": """
        <div class="headline-section">
            <span>RED RIBBON CLUB (RRC)</span>
            <span class="headline-tag">12 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">140+ STUDENTS PARTICIPATE IN STATE-LEVEL ONLINE QUIZ ON HIV/STI AWARENESS</h2>
        <div class="byline-bar">
            <span class="byline-date">INTENSIFIED IEC CAMPAIGN 3.0</span>
            <span>•</span>
            <span>50 MCQS IN 20 MINUTES</span>
            <span>•</span>
            <span>TNSACS CHENNAI</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Red Ribbon Club (RRC) of Vaigai College organized the TNSACS Quiz Competition – 2026, a prestigious State-Level Online Quiz Competition, on 12 August 2026 under the flagship Intensified IEC Campaign 3.0. More than 140 students actively participated in the high-stakes digital competition.</p>
            <p>The quiz focused comprehensively on HIV/STI prevention, the HIV/AIDS (Prevention and Control) Act, 2017, clinical testing protocols, adolescent wellbeing, anti-retroviral therapies, and public health policies, comprising 50 rigorous questions answered within a rapid 20-minute window.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image22.jpeg" alt="TNSACS Quiz Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>TNSACS State-Level Quiz Competition Official Poster: Intensified IEC Campaign 3.0</span>
                <span class="caption-tag">12 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Programme Coordinated by <strong>Mr. C. Balaguru</strong>, AP/Mech & RRC Coordinator.
        </div>
        """
    },

    # Page 16: RRC Quiz - Laureates & Impact
    {
        "id": "page-16",
        "num": 16,
        "density": "soft",
        "header_title": "RED RIBBON CLUB (RRC)",
        "header_tag": "QUIZ LAUREATES",
        "title": "Award Distribution & Knowledge Empowerment",
        "subtitle": "Attractive Cash Prizes and Certificates Awarded to Top Performers",
        "html": """
        <h2 class="headline-lead">STRENGTHENING ADOLESCENT HEALTH LITERACY</h2>
        <p class="headline-sub">VCE Students Demonstrate Exemplary Scores in State-Wide Public Health Assessment</p>

        <div class="editorial-cols dropcap">
            <p>Attractive prizes and certificates were awarded to the highest scoring participants. The initiative significantly deepened students' understanding of medical rights, eradication of social stigma, and responsible lifestyle choices.</p>
            <p>Principal Dr. R. Sivaranjani commended the RRC for utilizing digital assessment platforms to mobilize large-scale youth participation, reaffirming VCE's commitment to creating well-rounded, socially responsible technical graduates.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image23.jpeg" alt="Online Quiz Interface & Participants" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Students Engaged in State-Level Online Digital Quiz</span>
                    <span class="caption-tag">Digital Lab</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image24.jpeg" alt="Prize Distribution RRC" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Award Distribution to Top Scoring Quiz Competitors</span>
                    <span class="caption-tag">Honor Roll</span>
                </div>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px;">
            <div style="font-family: var(--font-display); font-size: 0.74rem; font-weight: bold; color: var(--primary);">
                ✦ Competition Highlights
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                140+ Registered Candidates • 50 Challenging MCQs • 20-Minute Time Cap • 100% Digital Proctoring • Commendation Prizes Distributed.
            </div>
        </div>
        """
    },

    # Page 17: Anti-Drug Club - Mass Pledge
    {
        "id": "page-17",
        "num": 17,
        "density": "soft",
        "header_title": "VCE ANTI-DRUG CLUB",
        "header_tag": "CAMPUS PLEDGE",
        "title": "Mass Anti-Drug Pledge & Awareness — 11 August 2026",
        "subtitle": "250 Students Commit to a Drug-Free Lifestyle at Dr. Kalam Auditorium",
        "html": """
        <div class="headline-section">
            <span>ANTI-DRUG CLUB</span>
            <span class="headline-tag">11 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">MASS ANTI-DRUG PLEDGE: 250 STUDENTS UNITE FOR A HEALTHY FUTURE</h2>
        <div class="byline-bar">
            <span class="byline-date">DR. KALAM AUDITORIUM</span>
            <span>•</span>
            <span>THEME: "EMPOWERING YOUTH FOR A HEALTHY FUTURE"</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The VCE Anti-Drug Club organized a Mass Anti-Drug Pledge and Health & Wellness Programme on 11 August 2026 at the Dr. Kalam Auditorium under the inspiring theme "Empowering Youth for a Healthy Future."</p>
            <p>As part of the Tamil Nadu Chief Minister’s statewide Anti-Drug Pledge initiative, 250 students participated in the live synchronized pledge, reaffirming their unyielding resolve to maintain a clean, drug-free lifestyle and actively support their peers against substance abuse.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image25.png" alt="Anti-Drug Programme Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>VCE Anti-Drug Club Banner: "Empowering Youth for a Healthy Future"</span>
                <span class="caption-tag">11 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Coordinators: <strong>Dr. R. Sivaranjani</strong> (Principal & Prof/ECE) & <strong>Dr. M. K. V. Karthikeyan</strong> (HoD/Mech).
        </div>
        """
    },

    # Page 18: Anti-Drug Club - Keynote & Drug-Free Campus
    {
        "id": "page-18",
        "num": 18,
        "density": "soft",
        "header_title": "VCE ANTI-DRUG CLUB",
        "header_tag": "MEDICAL KEYNOTE",
        "title": "Dr. Bharath Krishna Addresses Students on Substance Risks",
        "subtitle": "Medical Director Dr. Rao's Service Hospital Urges Youth to Resist Peer Pressure",
        "html": """
        <h2 class="headline-lead">DR. BHARATH KRISHNA: "PROTECT YOUR BRAIN & CAREER"</h2>
        <p class="headline-sub">Renowned Physician Warns Against Psychological and Neurological Traps of Addiction</p>

        <div class="editorial-cols dropcap">
            <p>Dr. Bharath Krishna, Medical Director at Dr. Rao’s Service Hospital, Melur, Madurai, delivered a hard-hitting keynote addressing the neurological damage, behavioral decline, and legal consequences of narcotics.</p>
            <p>He provided practical strategies for recognizing psychological distress and resisting peer pressure, urging the assembled youth to serve as proactive campus ambassadors for health and positive lifestyle choices.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image26.png" alt="Mass Pledge Live" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>250 Students Reciting Chief Minister's Anti-Drug Pledge</span>
                    <span class="caption-tag">Dr. Kalam Auditorium</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image27.png" alt="Dr. Bharath Krishna Address" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Dr. Bharath Krishna Delivering Medical Keynote Address</span>
                    <span class="caption-tag">Medical Insights</span>
                </div>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "Say yes to life, yes to ambition, and an absolute no to drugs. Your mind is your greatest engineering asset."
        </div>
        """
    },

    # Page 19: Entrepreneurship Development Cell (EDC)
    {
        "id": "page-19",
        "num": 19,
        "density": "soft",
        "header_title": "ENTREPRENEURSHIP DEVELOPMENT CELL (EDC)",
        "header_tag": "STARTUP MASTERCLASS",
        "title": "Entrepreneurship & Startup Awareness — 13 August 2026",
        "subtitle": "EDII Master Trainer Ms. Archana Veeravel Sparks Student Venture Ambition",
        "html": """
        <div class="headline-section">
            <span>ENTREPRENEURSHIP DEVELOPMENT CELL (EDC)</span>
            <span class="headline-tag">13 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">IGNITING STARTUP DREAMS: MS. ARCHANA VEERAVEL ADDRESSES III & IV YEAR STUDENTS</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 13 AUGUST 2026</span>
            <span>•</span>
            <span>EDII MASTER TRAINER & WOMEN ENTREPRENEUR</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Entrepreneurship Development Cell (EDC) organized an intensive Entrepreneurship, Innovation and Startup Awareness Programme on 13 August 2026 for pre-final and final-year engineering scholars.</p>
            <p>Ms. Archana Veeravel, celebrated Women Entrepreneur and Master Trainer with the Entrepreneurship Development and Innovation Institute (EDII), served as the keynote resource person, unraveling the fundamentals of ideation, product-market fit, and startup funding.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image28.jpeg" alt="EDC Poster" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>EDC Programme Official Poster</span>
                    <span class="caption-tag">13 August 2026</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image29.jpeg" alt="Ms. Archana Keynote" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Ms. Archana Veeravel Addressing Engineers</span>
                    <span class="caption-tag">EDII Master Trainer</span>
                </div>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Organized by EDC Coordinators: <strong>Mr. A. M. Milan</strong>, AP/Mech & <strong>Mr. R. Ravi Shankar</strong>, AP/Mech.
        </div>
        """
    },

    # Page 20: EDC - Incubation Workshop Gallery
    {
        "id": "page-20",
        "num": 20,
        "density": "soft",
        "header_title": "ENTREPRENEURSHIP DEVELOPMENT CELL (EDC)",
        "header_tag": "VENTURE CREATION",
        "title": "From Engineering Lab to Commercial Enterprise",
        "subtitle": "Interactive Ideation, Business Modeling, and Tamil Nadu Startup Grants",
        "html": """
        <h2 class="headline-lead">FROM LAB PROTOTYPE TO VIABLE COMMERCIAL STARTUP</h2>
        <p class="headline-sub">Students Learn Patent Valuation, Venture Financing, and Tamil Nadu EDII Incubation Pathways</p>

        <div class="editorial-cols dropcap">
            <p>Ms. Veeravel engaged students in dynamic business model canvas simulations, challenging them to transform senior-year capstone projects into viable commercial products. She shared insights into Tamil Nadu Startup Seed Grants and patent incentives.</p>
            <p>The enthusiastic participation witnessed over a dozen student teams pitching nascent concepts in agrarian automation, smart electric mobility, and software productivity, laying the foundation for VCE's upcoming student startup incubator.</p>
        </div>

        <div class="image-gallery-triple" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image30.jpeg" alt="Student Ideation" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Student Ideation Session</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image31.jpeg" alt="Interactive Discussion" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Interactive Q&A Forum</span></div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image32.jpeg" alt="EDC Delegation" class="news-img" style="max-height: 140px;">
                <div class="news-caption"><span>Budding Student Founders</span></div>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px;">
            <div style="font-family: var(--font-display); font-size: 0.74rem; font-weight: bold; color: var(--primary);">
                ✦ Startup Framework Discussed
            </div>
            <div style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Problem Validation • Minimum Viable Product (MVP) • TAM/SAM/SOM Market Sizing • EDII Seed Capital • Pitch Deck Architecture.
            </div>
        </div>
        """
    },

    # Page 21: National Service Scheme (NSS) - 78th Independence Day
    {
        "id": "page-21",
        "num": 21,
        "density": "soft",
        "header_title": "NATIONAL SERVICE SCHEME (NSS)",
        "header_tag": "NATIONAL CELEBRATION",
        "title": "78th Independence Day Celebrations — 15 August 2026",
        "subtitle": "Solemn Tricolor Hoisting and Presidential Address by Dr. R. Sivaranjani",
        "html": """
        <div class="headline-section">
            <span>NATIONAL SERVICE SCHEME (NSS)</span>
            <span class="headline-tag">15 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">78TH INDEPENDENCE DAY CELEBRATED WITH PATRIOTIC SPLENDOR & CIVIC PRIDE</h2>
        <div class="byline-bar">
            <span class="byline-date">VCE CAMPUS GROUNDS</span>
            <span>•</span>
            <span>PRESIDENTIAL ADDRESS BY PRINCIPAL (I/C) DR. R. SIVARANJANI</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The National Service Scheme (NSS) organized the joyous 78th Independence Day Celebration on 15 August 2026 with spirited participation from students and faculty across all engineering departments.</p>
            <p>Dr. R. Sivaranjani, Professor/ECE and Principal (i/c), Vaigai College of Engineering, unfurled the National Flag and addressed the assembly. Her address emphasized that engineering innovations should serve national development, clean energy, and rural upliftment.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image33.jpeg" alt="Independence Day Celebration Assembly" class="news-img" style="max-height: 250px;">
            <div class="news-caption">
                <span>78th Independence Day Campus Assembly & Tricolor Salutation</span>
                <span class="caption-tag">15 August 2026</span>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "True freedom is realized when our engineering intellect solves the deepest challenges of our society and nation."
        </div>
        """
    },

    # Page 22: Anna University Rank Holders
    {
        "id": "page-22",
        "num": 22,
        "density": "soft",
        "header_title": "UNIVERSITY ACADEMIC LAURELS",
        "header_tag": "RANK HOLDERS",
        "title": "Anna University Rank Holders (2021-2025 Batch)",
        "subtitle": "Ms. P. Snowfia (CSE) & Mr. S.A. Arunprasath (Mech) Bring Glory to VCE",
        "html": """
        <div class="headline-section">
            <span>ANNA UNIVERSITY HONORS</span>
            <span class="headline-tag">2021–2025 BATCH</span>
        </div>
        <h2 class="headline-lead">PROUDLY PRESENTING OUR ANNA UNIVERSITY UNIVERSITY RANK HOLDERS!</h2>
        <div class="byline-bar">
            <span class="byline-date">ANNA UNIVERSITY CHENNAI</span>
            <span>•</span>
            <span>OUTSTANDING ACADEMIC DISTINCTION</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>Vaigai College of Engineering proudly celebrates our distinguished Anna University Rank Holders whose exceptional academic dedication has brought immense prestige to the institution:</p>
            <p><strong>Ms. P. Snowfia</strong> from the Department of Computer Science & Engineering (2021–2025 batch) and <strong>Mr. S.A. Arunprasath</strong> from the Department of Mechanical Engineering (2021–2025 batch) achieved top state rankings through sustained brilliance and scholarly rigor.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image34.jpeg" alt="Anna University Rank Holders Poster" class="news-img" style="max-height: 250px; object-fit: contain;">
            <div class="news-caption">
                <span>Honoring Anna University Rank Holders: Ms. P. Snowfia (CSE) & Mr. S.A. Arunprasath (Mech)</span>
                <span class="caption-tag">VCE Pride</span>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px; text-align: center; border-color: var(--accent);">
            <div style="font-family: var(--font-display); font-size: 0.82rem; font-weight: bold; color: var(--accent); letter-spacing: 1px;">
                ★ ACADEMIC EXCELLENCE CITATION
            </div>
            <p style="font-size: 0.72rem; color: var(--text-dark); margin-top: 4px;">
                Management, Principal, Heads of Departments, and Faculty warmly congratulate Ms. P. Snowfia and Mr. S.A. Arunprasath on this monumental milestone!
            </p>
        </div>
        """
    },

    # Page 23: Student State Achievements (from vaigai_college2.docx)
    {
        "id": "page-23",
        "num": 23,
        "density": "soft",
        "header_title": "STATE-LEVEL STUDENT LAURELS",
        "header_tag": "ORATORY EXCELLENCE",
        "title": "State Vairamuthu Speech Contest Sweep",
        "subtitle": "VCE Orators Win 1st, 2nd & 3rd Prizes at Kalaignar Centenary Library",
        "html": """
        <div class="headline-section">
            <span>STATE-LEVEL COMPETITIONS</span>
            <span class="headline-tag">01 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">VAIGAI SCHOLARS SWEEP STATE VAIRAMUTHU SPEECH CONTEST WITH 1ST, 2ND & 3RD PRIZES!</h2>
        <div class="byline-bar">
            <span class="byline-date">VENUE: KALAIGNAR CENTENARY LIBRARY</span>
            <span>•</span>
            <span>STATE-LEVEL TAMIL ELOQUENCE FORUM</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>Demonstrating peerless Tamil eloquence and literary depth, students of Vaigai College of Engineering accomplished a historic clean sweep at the prestigious State-Level Vairamuthu Speech Contest held on 1 August 2026 at the grand Kalaignar Centenary Library, Madurai.</p>
            <p>Competing against dozens of elite colleges across Tamil Nadu, VCE delegates captivated judges with scholarly dissertations on classical literature, modern social reforms, and poetic imagery, claiming all three top podium spots.</p>
        </div>

        <div class="news-table-wrapper" style="margin-top: 10px;">
            <table class="news-table">
                <thead>
                    <tr>
                        <th>Sl.</th>
                        <th>Student Name</th>
                        <th>Year</th>
                        <th>Dept</th>
                        <th>Event Name & Host</th>
                        <th>Award Won</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>1</strong></td>
                        <td><strong>B.B. Gokulnath</strong></td>
                        <td>IV Year</td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Vairamuthu Speech Contest (Kalaignar Centenary Library)</td>
                        <td><span class="badge-tag badge-gold">🥇 I PRIZE (CHAMPION)</span></td>
                    </tr>
                    <tr>
                        <td><strong>2</strong></td>
                        <td><strong>C. Saniya</strong></td>
                        <td>IV Year</td>
                        <td><span class="badge-tag badge-blue">CSE</span></td>
                        <td>Vairamuthu Speech Contest (Kalaignar Centenary Library)</td>
                        <td><span class="badge-tag badge-blue">🥈 II PRIZE</span></td>
                    </tr>
                    <tr>
                        <td><strong>3</strong></td>
                        <td><strong>Manimegalai</strong></td>
                        <td>II Year</td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Vairamuthu Speech Contest (Kalaignar Centenary Library)</td>
                        <td><span class="badge-tag badge-green">🥉 III PRIZE</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="pull-quote" style="margin-top: 10px; font-size: 0.85rem;">
            "A triple victory reflecting that our engineering scholars master both technological precision and cultural oratory."
        </div>
        """
    },

    # Page 24: Training and Placement Cell (TPC) - Expert Talk
    {
        "id": "page-24",
        "num": 24,
        "density": "soft",
        "header_title": "TRAINING & PLACEMENT CELL (TPC)",
        "header_tag": "EXPERT TALK",
        "title": "Expert Talk: 'Success Is a Skill: Habits of High Performers'",
        "subtitle": "Dean Academics Dr. B. Sujatha Delivers Masterclass on Professional Rigor",
        "html": """
        <div class="headline-section">
            <span>TRAINING AND PLACEMENT CELL (TPC)</span>
            <span class="headline-tag">8 JULY 2026</span>
        </div>
        <h2 class="headline-lead">EXPERT TALK ON "SUCCESS IS A SKILL: HABITS OF HIGH PERFORMERS"</h2>
        <div class="byline-bar">
            <span class="byline-date">DR. ABDUL KALAM AUDITORIUM</span>
            <span>•</span>
            <span>2:30 P.M. TO 4:00 P.M.</span>
            <span>•</span>
            <span>SPEAKER: DR. B. SUJATHA</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>Vaigai College of Engineering organized an enlightening Expert Talk on "Success Is a Skill: Habits of High Performers" on 8 July 2026 from 2:30 p.m. to 4:00 p.m. at the Dr. Abdul Kalam Auditorium.</p>
            <p>Dr. B. Sujatha, Dean/Academics, served as keynote speaker, presenting actionable blueprints on consistency, daily deliberate practice, emotional resilience, and growth mindset, proving that exceptional capability is cultivated rather than inherited.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image35.jpeg" alt="Expert Talk Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>Expert Talk Announcement Poster: Dr. B. Sujatha on Habits of High Performers</span>
                <span class="caption-tag">8 July 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Programme Coordinated by <strong>The Training & Placement Cell (TPC)</strong>.
        </div>
        """
    },

    # Page 25: TPC Masterclass Gallery
    {
        "id": "page-25",
        "num": 25,
        "density": "soft",
        "header_title": "TRAINING & PLACEMENT CELL (TPC)",
        "header_tag": "PERFORMANCE MASTERCLASS",
        "title": "Interactive Coaching on Career Agility",
        "subtitle": "Final and Pre-Final Year Engineers Internalize High-Impact Professional Standards",
        "html": """
        <h2 class="headline-lead">DISCIPLINE, PURPOSEFUL EFFORT & CONTINUOUS IMPROVEMENT</h2>
        <p class="headline-sub">Dean Dr. B. Sujatha Guides Students on Cracking Corporate Assessments</p>

        <div class="editorial-cols dropcap">
            <p>Dr. Sujatha dissected the cognitive routines of top 1% corporate leaders, guiding students through practical techniques to overcome procrastination, manage exam stress, and exhibit professional poise during high-stakes job interviews.</p>
            <p>The interactive masterclass concluded with energetic Q&A interactions, empowering attendees to architect personal accountability roadmaps for upcoming campus recruitment seasons.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image36.jpeg" alt="Dr. Sujatha Keynote Presentation" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Dr. B. Sujatha Addressing Engineering Scholars</span>
                    <span class="caption-tag">Auditorium Lecture</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image37.jpeg" alt="Student Audience High Performers" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Final and Pre-Final Year Engineers in Session</span>
                    <span class="caption-tag">Interactive Coaching</span>
                </div>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "Success is not an accidental event; it is a learned habit repeated daily with uncompromising discipline."
        </div>
        """
    },

    # Page 26: Campus Placement - Besant Technologies Drive
    {
        "id": "page-26",
        "num": 26,
        "density": "soft",
        "header_title": "CAMPUS RECRUITMENT DRIVES",
        "header_tag": "ON-CAMPUS DRIVE",
        "title": "Besant Technologies Recruitment Drive — 10 August 2026",
        "subtitle": "Comprehensive Selection Process for Final-Year CSE & ECE Engineers",
        "html": """
        <div class="headline-section">
            <span>TRAINING AND PLACEMENT CELL (TPC)</span>
            <span class="headline-tag">10 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">ON-CAMPUS RECRUITMENT DRIVE BY BESANT TECHNOLOGIES PVT LTD</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 10 AUGUST 2026</span>
            <span>•</span>
            <span>FOR FINAL YEAR CSE & ECE SCHOLARS</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Training and Placement Cell (TPC) organized an On-Campus Recruitment Drive on 10 August 2026 for final-year CSE and ECE students. Besant Technologies conducted the comprehensive evaluation, assessing candidates through coding rounds, technical interviews, and HR discussions.</p>
            <p>The recruitment drive offered students a prime gateway into corporate IT careers, testing their proficiency in full-stack web architectures, database design, and algorithmic efficiency.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image38.jpeg" alt="Besant Technologies Drive Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>On-Campus Recruitment Drive Poster: Besant Technologies Pvt Ltd</span>
                <span class="caption-tag">10 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Drive Organized by <strong>Dr. R. Sivaranjani</strong>, Principal & Prof/ECE and <strong>Ms. R.J. Supriya</strong>, AP/ENG.
        </div>
        """
    },

    # Page 27: Besant Technologies - 16 Selected Candidates
    {
        "id": "page-27",
        "num": 27,
        "density": "soft",
        "header_title": "CAMPUS RECRUITMENT DRIVES",
        "header_tag": "PLACEMENT LAURELS",
        "title": "16 Students Selected for Besant JRIP Program",
        "subtitle": "Job-Ready Internship & Placement Program (JRIP) Offers Extended to CSE, ECE & EEE",
        "html": """
        <h2 class="headline-lead">16 STUDENTS SELECTED FOR BESANT JOB-READY INTERNSHIP & PLACEMENT PROGRAM</h2>
        <p class="headline-sub">Vaigai College Celebrates Huge IT Hiring Triumph Across CSE, ECE and EEE Departments</p>

        <div class="editorial-cols dropcap">
            <p>Vaigai College of Engineering proudly announces that 16 outstanding students from the departments of Computer Science & Engineering (CSE), Electronics & Communication Engineering (ECE), and Electrical & Electronics Engineering (EEE) have been selected for the prestigious JOB-READY INTERNSHIP & PLACEMENT PROGRAM (JRIP) by BESANT TECHNOLOGIES PVT LTD.</p>
            <p>The selected students will embark on high-impact training followed by direct induction into corporate engineering teams, establishing a new placement benchmark for VCE.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image39.jpeg" alt="Selected 16 Students Besant Poster" class="news-img" style="max-height: 250px; object-fit: contain;">
            <div class="news-caption">
                <span>Roll of Honor: 16 Selected Students for Besant Technologies JRIP Program</span>
                <span class="caption-tag">Besant JRIP 2026</span>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px; text-align: center;">
            <div style="font-family: var(--font-display); font-size: 0.78rem; font-weight: bold; color: var(--accent);">
                ✦ HEARTIEST CONGRATULATIONS TO THE 16 BESANT ACHIEVERS! ✦
            </div>
        </div>
        """
    },

    # Page 28: Pooled Campus Drive - Inovonz Engineerics
    {
        "id": "page-28",
        "num": 28,
        "density": "soft",
        "header_title": "POOLED CAMPUS RECRUITMENT",
        "header_tag": "CORE ELECTRICAL DRIVE",
        "title": "Inovonz Engineerics Pooled Campus Drive — 18 August 2026",
        "subtitle": "Core Engineering Recruitment Initiative for IV Year EEE Scholars",
        "html": """
        <div class="headline-section">
            <span>TRAINING AND PLACEMENT CELL (TPC)</span>
            <span class="headline-tag">18 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">POOLED CAMPUS RECRUITMENT DRIVE JOINTLY WITH INOVONZ ENGINEERICS</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 18 AUGUST 2026</span>
            <span>•</span>
            <span>FOR IV YEAR ELECTRICAL & ELECTRONICS ENGINEERS</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>A Pooled Campus Recruitment Drive was organized by the Training and Placement Cell (TPC) jointly with INOVONZ ENGINEERICS on 18 August 2026 for IV year Electrical and Electronics Engineering (EEE) students.</p>
            <p>The core industrial drive evaluated students across power electronics, industrial automation, PLC programming, and electrical machinery design, strengthening their corporate preparedness for core electrical manufacturing sectors.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image40.jpeg" alt="Inovonz Engineerics Drive" class="news-img" style="max-height: 220px;">
            <div class="news-caption">
                <span>Inovonz Engineerics Technical Interview Panel in Progress</span>
                <span class="caption-tag">18 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Drive Organized by <strong>Ms. V. Saranya</strong>, AP/EEE.
        </div>
        """
    },

    # Page 29: Inovonz Engineerics Drive Gallery
    {
        "id": "page-29",
        "num": 29,
        "density": "soft",
        "header_title": "POOLED CAMPUS RECRUITMENT",
        "header_tag": "TECHNICAL ASSESSMENT",
        "title": "Core Engineering Testing & Placement Preparedness",
        "subtitle": "Circuit Diagnostics, Automation Viva and Interview Highlights",
        "html": """
        <h2 class="headline-lead">EXPANDING INDUSTRIAL CORE OPPORTUNITIES IN AUTOMATION</h2>
        <p class="headline-sub">Rigorous Technical Rounds Test Practical Mastery in Power Circuits and Microcontroller Interfacing</p>

        <div class="editorial-cols dropcap">
            <p>The multi-stage recruitment process included written technical screenings followed by rigorous one-on-one technical panel vivas. Inovonz engineers assessed candidates on circuit schematic interpretation and real-time fault detection.</p>
            <p>The initiative delivered critical industry exposure to our final-year electrical engineers, confirming that VCE's laboratory infrastructure matches contemporary industrial requirements.</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image41.jpeg" alt="Inovonz Technical Testing" class="news-img" style="max-height: 180px;">
                <div class="news-caption">
                    <span>Candidates Undergoing Written Technical Screening</span>
                    <span class="caption-tag">Technical Hall</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image42.jpeg" alt="Inovonz Poster & Banner" class="news-img" style="max-height: 180px; object-fit: contain;">
                <div class="news-caption">
                    <span>Inovonz Engineerics Recruitment Drive Poster</span>
                    <span class="caption-tag">Placement Drive</span>
                </div>
            </div>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.85rem;">
            "Bridging the divide between foundational circuit theory and industrial automation reality."
        </div>
        """
    },

    # Page 30: Off-Campus Placement - Newrta Solutions Drive
    {
        "id": "page-30",
        "num": 30,
        "density": "soft",
        "header_title": "OFF-CAMPUS RECRUITMENT",
        "header_tag": "SOFTWARE SELECTION",
        "title": "Off-Campus Recruitment Drive: Newrta Solutions — 19 August 2026",
        "subtitle": "Specialized Software Developer Selection for IV Year CSE Scholars",
        "html": """
        <div class="headline-section">
            <span>TRAINING AND PLACEMENT CELL (TPC)</span>
            <span class="headline-tag">19 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">OFF-CAMPUS RECRUITMENT DRIVE CONDUCTED BY NEWRTA SOLUTIONS PVT. LTD.</h2>
        <div class="byline-bar">
            <span class="byline-date">MADURAI, 19 AUGUST 2026</span>
            <span>•</span>
            <span>FOR IV YEAR COMPUTER SCIENCE SCHOLARS</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>An Off-Campus Recruitment Drive was organized by the Training and Placement Cell (TPC) on 19 August 2026 for IV year CSE students. Newrta Solutions Pvt. Ltd. conducted the intensive recruitment process, providing eligible students with direct opportunities to compete for software developer positions.</p>
            <p>The recruitment drive tested students in advanced algorithmic complexity, full-stack frameworks, database design, and software lifecycle principles.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image43.jpeg" alt="Newrta Solutions Poster" class="news-img" style="max-height: 220px; object-fit: contain;">
            <div class="news-caption">
                <span>Off-Campus Recruitment Drive Poster: Newrta Solutions Pvt Ltd</span>
                <span class="caption-tag">19 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Organized by <strong>Dr. R. Sivaranjani</strong>, Principal & Prof/ECE and <strong>Ms. R.J. Supriya</strong>, AP/ENG.
        </div>
        """
    },

    # Page 31: Newrta Solutions - Spotlight on Mr. S. Maadhesh
    {
        "id": "page-31",
        "num": 31,
        "density": "soft",
        "header_title": "OFF-CAMPUS RECRUITMENT",
        "header_tag": "STAR PLACEMENT",
        "title": "Mr. S. Maadhesh Placed as Software Developer",
        "subtitle": "Final Year CSE Talent Secures Prestigious Engineering Role at Newrta Solutions",
        "html": """
        <h2 class="headline-lead">MR. S. MAADHESH PLACED AS SOFTWARE DEVELOPER AT NEWTRA SOLUTIONS</h2>
        <p class="headline-sub">Vaigai College Celebrates Yet Another Stellar Placement Triumph for Final-Year CSE Talent</p>

        <div class="editorial-cols dropcap">
            <p>Vaigai College of Engineering proudly announces that <strong>Mr. S. Maadhesh</strong> from Final Year CSE has been successfully placed in <strong>NEWTRA SOLUTIONS PVT LTD</strong> as a Software Developer.</p>
            <p>Demonstrating impeccable technical acumen through coding challenges and architecture interviews, Maadhesh earned accolades from company assessors. The faculty and management join together in congratulating him on this exceptional milestone!</p>
        </div>

        <div class="image-gallery-pair" style="margin-top: 10px;">
            <div class="news-image-frame">
                <img src="word/media/image44.jpeg" alt="Mr. S. Maadhesh Portrait" class="news-img" style="max-height: 200px; object-fit: contain;">
                <div class="news-caption">
                    <span>Mr. S. Maadhesh — Software Developer, Newtra Solutions</span>
                    <span class="caption-tag">Star Placed Student</span>
                </div>
            </div>
            <div class="news-image-frame">
                <img src="word/media/image45.jpeg" alt="Newrta Honor Poster" class="news-img" style="max-height: 200px; object-fit: contain;">
                <div class="news-caption">
                    <span>Official Commendation Poster for Mr. S. Maadhesh</span>
                    <span class="caption-tag">Newtra Solutions</span>
                </div>
            </div>
        </div>

        <div class="pretext-card" style="margin-top: 8px; text-align: center; border-color: var(--accent);">
            <div style="font-family: var(--font-display); font-size: 0.78rem; font-weight: bold; color: var(--accent);">
                ★ HEARTIEST CONGRATULATIONS TO MR. S. MAADHESH! ★
            </div>
        </div>
        """
    },

    # Page 32: TPC - TACT Level 1 Recruitment Training
    {
        "id": "page-32",
        "num": 32,
        "density": "soft",
        "header_title": "TRAINING & PLACEMENT CELL (TPC)",
        "header_tag": "TACT LEVEL 1",
        "title": "TACT – Level 1 Recruitment Training — 20 August 2026",
        "subtitle": "Comprehensive Aptitude and Competency Training for All Final-Year Engineers",
        "html": """
        <div class="headline-section">
            <span>TRAINING AND PLACEMENT CELL (TPC)</span>
            <span class="headline-tag">20 AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">TACT – LEVEL 1: INTENSIVE PLACEMENT RECRUITMENT COMPETENCY BOOTCAMP</h2>
        <div class="byline-bar">
            <span class="byline-date">DR. KALAM AUDITORIUM</span>
            <span>•</span>
            <span>FOR ALL IV YEAR SCHOLARS</span>
            <span>•</span>
            <span>GUIDED BY PRINCIPAL & HODS</span>
        </div>

        <div class="editorial-cols dropcap">
            <p>The Training and Placement Cell (TPC) organized TACT – Level 1 on 20 August 2026 for all IV year engineering students. Dr. R. Sivaranjani, Principal (i/c), along with the Heads of Departments, supported and actively mentored the program.</p>
            <p>The intensive bootcamp focused on elevating aptitude test performance, quantitative problem-solving speed, logical reasoning, verbal agility, and personal interview competencies, bolstering students' competitive readiness for tier-1 IT and core campus recruitment drives.</p>
        </div>

        <div class="news-image-frame" style="margin-top: 10px;">
            <img src="word/media/image46.jpeg" alt="TACT Level 1 Training Session" class="news-img" style="max-height: 250px;">
            <div class="news-caption">
                <span>Final-Year Engineering Cohort Actively Engaged in TACT – Level 1 Assessment Training</span>
                <span class="caption-tag">20 August 2026</span>
            </div>
        </div>

        <div style="font-size: 0.72rem; color: var(--text-muted); margin-top: 6px; text-align: center;">
            Programme Coordinated by <strong>Dr. R. Sivaranjani</strong>, Principal & Prof/ECE and <strong>Ms. R.J. Supriya</strong>, AP/ENG.
        </div>
        """
    },

    # Page 33: Faculty Development Register (from vaigai_college2.docx)
    {
        "id": "page-33",
        "num": 33,
        "density": "soft",
        "header_title": "FACULTY ACADEMIC PURSUITS",
        "header_tag": "PROGRAMMES ATTENDED",
        "title": "Faculty Upskilling & Professional Development",
        "subtitle": "16 Elite FDPs, Webinars & NPTEL Certifications Attended Across Premier Institutions",
        "html": """
        <div class="headline-section">
            <span>PROGRAMMES ATTENDED BY FACULTY</span>
            <span class="headline-tag">JULY – AUGUST 2026</span>
        </div>
        <h2 class="headline-lead">16 FACULTY DEVELOPMENT PROGRAMMES & ADVANCED CERTIFICATIONS</h2>
        <div class="byline-bar">
            <span>THIAGARAJAR COLLEGE • ANNA UNIVERSITY • CBIT HYDERABAD • IIIT KOTTAYAM • IIT CHENNAI</span>
        </div>

        <div class="news-table-wrapper" style="margin-top: 6px; max-height: 380px; overflow-y: auto;">
            <table class="news-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Faculty Name</th>
                        <th>Dept</th>
                        <th>Programme Name & Type</th>
                        <th>Date</th>
                        <th>Host Institution</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td><strong>Dr. R. Sivaranjani</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>ANRF Sponsored Summer School on Advanced Computer Vision & Deep Learning</td>
                        <td>03/08/26–07/08/26</td>
                        <td>Thiagarajar College of Engg</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td><strong>A. Badrul Mufsira</strong></td>
                        <td><span class="badge-tag badge-blue">CSE</span></td>
                        <td>DEVOPS - FDP</td>
                        <td>27/07/26–01/08/26</td>
                        <td>TN Skills, Anna Univ Madurai</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td><strong>Mr. T. Vijaya Raghavan</strong></td>
                        <td><span class="badge-tag badge-blue">CSE</span></td>
                        <td>Piping Design Modelling & Detailing - FDP</td>
                        <td>27/07/26–01/08/26</td>
                        <td>TN Skill, AC Tech, Karaikudi</td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td><strong>Dr. S. Mohanasundaram</strong></td>
                        <td><span class="badge-tag badge-gold">MECH</span></td>
                        <td>Next Gen Design using Autodesk Fusion AI - FDP</td>
                        <td>03/08/26–08/08/26</td>
                        <td>CBIT, Hyderabad</td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td><strong>Dr. S. Mohanasundaram</strong></td>
                        <td><span class="badge-tag badge-gold">MECH</span></td>
                        <td>Product Conceptualization & Prototyping - FDP</td>
                        <td>20/07/26–01/08/26</td>
                        <td>Anna Univ Regional Campus Madurai</td>
                    </tr>
                    <tr>
                        <td>6</td>
                        <td><strong>Mr. R. Ravishankar</strong></td>
                        <td><span class="badge-tag badge-gold">MECH</span></td>
                        <td>Surface Modelling - FDP</td>
                        <td>27/07/26–01/08/26</td>
                        <td>Anna Univ Regional Campus Madurai</td>
                    </tr>
                    <tr>
                        <td>7</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Innovative Research Methodologies using AI Tools</td>
                        <td>10/07/2026</td>
                        <td>KLN College of Engineering</td>
                    </tr>
                    <tr>
                        <td>8</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>AI Powered IoT: Transforming Connected World</td>
                        <td>19/07/2026</td>
                        <td>Reccsar Private Limited</td>
                    </tr>
                    <tr>
                        <td>9</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Effective Research Methodology & Scientific Publishing</td>
                        <td>22/07/2026</td>
                        <td>Sri Indu Institute of Engg & Tech</td>
                    </tr>
                    <tr>
                        <td>10</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Build Intelligent Workflows with n8n</td>
                        <td>26/07/2026</td>
                        <td>Reccsar Private Limited</td>
                    </tr>
                    <tr>
                        <td>11</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>AI-Assisted UI/UX Design and Prototype</td>
                        <td>02/08/2026</td>
                        <td>Reccsar Private Limited</td>
                    </tr>
                    <tr>
                        <td>12</td>
                        <td><strong>Ms. P. Kurshidha Begam</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Building AI-Powered Application using AWS</td>
                        <td>15/08/26–16/08/26</td>
                        <td>Reccsar Private Limited</td>
                    </tr>
                    <tr>
                        <td>13</td>
                        <td><strong>Mr. R. Kothalamuthu</strong></td>
                        <td><span class="badge-tag badge-gold">MECH</span></td>
                        <td>NPTEL: Advances in Additive Manufacturing</td>
                        <td>12-Week Course</td>
                        <td>NPTEL - IIT</td>
                    </tr>
                    <tr>
                        <td>14</td>
                        <td><strong>Ms. S. Sangeetha</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>ATAL Offline FDP: Next Gen AI-Driven Electric Mobility</td>
                        <td>03/08/26–08/08/26</td>
                        <td>Solamalai College of Engg</td>
                    </tr>
                    <tr>
                        <td>15</td>
                        <td><strong>Ms. S. Sangeetha</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>Online FDP: Intelligent & Quantum Systems: Robotics & Agentic AI</td>
                        <td>22/08/26–31/08/26</td>
                        <td>IIIT-Kottayam, Kerala</td>
                    </tr>
                    <tr>
                        <td>16</td>
                        <td><strong>Ms. S. Sangeetha</strong></td>
                        <td><span class="badge-tag badge-blue">ECE</span></td>
                        <td>NPTEL: Wireless & Cellular Communication</td>
                        <td>12-Week Course</td>
                        <td>IIT Chennai</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
    },

    # Page 34: Faculty Research Publications (from vaigai_college2.docx)
    {
        "id": "page-34",
        "num": 34,
        "density": "soft",
        "header_title": "RESEARCH & SCHOLARLY PUBLICATIONS",
        "header_tag": "PEER-REVIEWED PAPERS",
        "title": "7 High-Impact Faculty Research Publications",
        "subtitle": "Breakthrough Investigations in Nanofluids, Parabolic Solar Collectors & Circular Models",
        "html": """
        <div class="headline-section">
            <span>FACULTY RESEARCH PUBLICATIONS</span>
            <span class="headline-tag">SCOPUS / SCI INDEXED</span>
        </div>
        <h2 class="headline-lead">7 GROUNDBREAKING PEER-REVIEWED RESEARCH PAPERS PUBLISHED IN PREMIER JOURNALS</h2>
        <div class="byline-bar">
            <span>NEXT MATERIALS • NEXT ENERGY • APPLIED SCIENCES • CANADIAN J. METALLURGY • IJMEMS</span>
        </div>

        <div class="news-table-wrapper" style="margin-top: 6px;">
            <table class="news-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Faculty Author</th>
                        <th>Paper Title</th>
                        <th>Journal Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td><strong>Dr. R.V. Sabariraj</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>Harvesting of solar energy through hybrid nanofluid based parabolic concentrating solar collector – Experimental and theoretical study</td>
                        <td><span class="badge-tag badge-gold">Next Materials</span></td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td><strong>Dr. R.V. Sabariraj</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>Polymer with silicon dioxide coating on solar photovoltaic for enhancement of power output performance – Experimental study</td>
                        <td><span class="badge-tag badge-gold">Next Energy</span></td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td><strong>Dr. R.V. Sabariraj</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>Direct ink writing of continuous glass fiber reinforced UV curable composites for enhanced mechanical performance</td>
                        <td><span class="badge-tag badge-blue">Discover Mechanical Engineering</span></td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td><strong>Dr. R.V. Sabariraj</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>Cradle-to-grave life cycle assessment of titanium, basalt and natural fiber composite for aerospace structural applications</td>
                        <td><span class="badge-tag badge-gold">Next Nanotechnology</span></td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td><strong>Mr. R. Ravishankar</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>A decision framework for selection highly sustainable packaging circular model in mass customized packing industry</td>
                        <td><span class="badge-tag badge-green">Applied Sciences</span></td>
                    </tr>
                    <tr>
                        <td>6</td>
                        <td><strong>Dr. S. Mohanasundaram</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>A multifunctional nanofiber composite for air filtration: thermal, electrochemical, and antibacterial characterisation</td>
                        <td><span class="badge-tag badge-blue">The Canadian Journal of Metallurgy and Materials Science</span></td>
                    </tr>
                    <tr>
                        <td>7</td>
                        <td><strong>Mr. R. Ravishankar</strong><br><span style="font-size:0.65rem; color:var(--text-muted);">AP/Mech</span></td>
                        <td>Sustainable supplier selection for recyclable packaging industry circular model Z number based MCDM and FIS perspective</td>
                        <td><span class="badge-tag badge-green">Intl. Journal of Mathematical Engineering & Mgmt Sciences (IJMEMS)</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="pull-quote" style="margin-top: 8px; font-size: 0.82rem;">
            "High-impact scholarly publication is the hallmark of faculty intellectual vitality, bringing cutting-edge research back to the undergraduate classroom."
        </div>
        """
    },

    # Page 35: Hard Back Cover
    {
        "id": "page-35",
        "num": 35,
        "is_cover": True,
        "density": "hard",
        "header_title": "VAIGAI COLLEGE OF ENGINEERING",
        "header_tag": "COLOPHON & CONTACT",
        "title": "Editorial Epilogue & Institutional Colophon",
        "subtitle": "Vaigai Educational Trust, Madurai, Tamil Nadu",
        "html": """
        <div style="text-align: center; margin-bottom: 12px;">
            <div class="splash-logo-wrapper" style="width: 100px; height: 70px; margin: 0 auto 6px;">
                <img src="logo.png" alt="Vaigai College Logo" class="splash-logo">
            </div>
            <h2 style="font-family: var(--font-display); font-size: 1.3rem; letter-spacing: 2px; color: var(--accent-light);">
                VAIGAI'S IKIGAI
            </h2>
            <div style="font-family: var(--font-serif); font-style: italic; font-size: 0.85rem; color: #cbd5e1;">
                Where Purpose Meets Possibility
            </div>
        </div>

        <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 4px; padding: 12px; margin-bottom: 12px; font-size: 0.74rem; line-height: 1.6;">
            <div style="font-family: var(--font-display); font-size: 0.78rem; font-weight: bold; color: var(--accent-light); margin-bottom: 4px; text-transform: uppercase;">
                ✦ Institutional Acknowledgement
            </div>
            <p>We extend our deepest gratitude to the Management of Vaigai Educational Trust (VET), Dr. R. Sivaranjani (Principal i/c), Dr. B. Sujatha (Dean Academics), Heads of all Engineering Departments, faculty coordinators, student office bearers, and our industrial partners (Besant Technologies, Caliber Virtual, Inovonz Engineerics, Newrta Solutions, Meenakshi Mission Hospital, TNSACS) for their tireless dedication.</p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.72rem; margin-bottom: 12px;">
            <div style="background: rgba(255, 255, 255, 0.03); padding: 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
                <strong style="color: var(--accent-light);">Campus Address:</strong><br>
                Vaigai College of Engineering<br>
                15-Acre Green Campus,<br>
                Madurai – 625 106, Tamil Nadu.
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); padding: 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
                <strong style="color: var(--accent-light);">Affiliations & Approval:</strong><br>
                Approved by AICTE, New Delhi<br>
                Affiliated to Anna University, Chennai<br>
                Bimonthly Newsletter Vol. 01 Issue 01
            </div>
        </div>

        <div style="text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 8px; font-size: 0.68rem; color: #94a3b8;">
            <div>© 2026 Vaigai College of Engineering. All rights reserved.</div>
            <div style="margin-top: 2px; color: var(--accent-light);">Published by the Editorial Board of Vaigai's Ikigai Gazette.</div>
        </div>
        """
    }
]

# Generate index.html
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>VAIGAI'S IKIGAI — The Bimonthly Gazette of Vaigai College of Engineering</title>
  
  <!-- Google Fonts for Authentic Newspaper Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cinzel+Decorative:wght@700&family=Inter:wght@400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="styles.css">
</head>
<body data-theme="newsprint">

  <!-- Splash Screen / Pretext Welcome Overlay -->
  <div id="pretext-splash">
    <div class="splash-content">
      <div class="splash-logo-wrapper">
        <div class="splash-logo-glow"></div>
        <img src="logo.png" alt="Vaigai College Logo" class="splash-logo">
      </div>
      <div class="splash-issue-badge">✦ VOL. 01 • ISSUE 01 • JULY – AUGUST 2026 ✦</div>
      <h1 class="splash-title">VAIGAI'S IKIGAI</h1>
      <p class="splash-sub">Where Purpose Meets Possibility — The Bimonthly Gazette</p>
      
      <div class="splash-pretext-box">
        <div class="splash-pretext-quote">
          <strong>What is Vaigai's Ikigai?</strong><br>
          <em>The Vision that drives us. The Achievements that define us. The Intelligence that inspires us. The Greatness we nurture. The Academic aspirations we pursue. The Innovations through which we create impact.</em>
        </div>
      </div>

      <button id="btn-enter-splash" class="splash-enter-btn">
        <span>Open Interactive Gazette</span>
        <span style="font-size: 1.2rem;">📖</span>
      </button>
    </div>
  </div>

  <!-- Top Sticky Navigation Bar -->
  <header class="top-navbar">
    <div class="nav-brand" id="brand-link">
      <div class="nav-logo-box">
        <img src="logo.png" alt="Vaigai Logo" class="nav-logo">
      </div>
      <div class="nav-titles">
        <span class="nav-title">VAIGAI'S IKIGAI</span>
        <span class="nav-subtitle">Vaigai College of Engineering</span>
      </div>
    </div>

    <div class="nav-meta">
      <span class="nav-edition-badge">VOL. 01 • NO. 01</span>
      <span class="nav-date">JULY – AUGUST 2026</span>
      <div class="nav-weather">
        <span>🌤️</span>
        <span>Madurai 31°C</span>
      </div>
    </div>

    <div class="nav-controls">
      <!-- Mode Toggle -->
      <button id="btn-mode-toggle" class="ctrl-btn" title="Toggle Reading Mode">
        <span class="ctrl-btn-icon">📰</span>
        <span class="btn-label" id="mode-label">Gazette View</span>
      </button>

      <!-- TOC Drawer Button -->
      <button id="btn-toc" class="ctrl-btn" title="Table of Contents">
        <span class="ctrl-btn-icon">📑</span>
        <span class="btn-label">Contents</span>
      </button>

      <!-- Audio Mute Button -->
      <button id="btn-audio" class="ctrl-btn" title="Toggle Page Turn Sound">
        <span class="ctrl-btn-icon" id="audio-icon">🔊</span>
      </button>

      <!-- Theme Select -->
      <select id="theme-select" class="theme-select" title="Color Theme">
        <option value="newsprint">Newsprint</option>
        <option value="ivory">Ivory</option>
        <option value="sepia">Sepia</option>
        <option value="dark">Dark</option>
      </select>

      <!-- Fullscreen Button -->
      <button id="btn-fullscreen" class="ctrl-btn" title="Fullscreen">
        <span class="ctrl-btn-icon">⛶</span>
      </button>
    </div>
  </header>

  <!-- Main Viewport Wrapper -->
  <main class="main-wrapper">

    <!-- FLIPBOOK VIEW CONTAINER -->
    <div id="flipbook-container">
      <!-- Floating Navigation Arrows -->
      <button id="btn-prev-page" class="flip-arrow prev" title="Previous Page" aria-label="Previous Page">‹</button>
      <button id="btn-next-page" class="flip-arrow next" title="Next Page" aria-label="Next Page">›</button>

      <div class="flipbook-viewport" id="flipbook-viewport">
        <div id="flipbook" class="st-flipbook">
"""

# Append all 35 pages into the flipbook
for p in pages_data:
    density_attr = f'data-density="{p.get("density", "soft")}"'
    cover_class = ""
    if p.get("is_cover") and p["num"] == 1:
        cover_class = "cover-front"
    elif p.get("is_cover") and p["num"] == 35:
        cover_class = "cover-back"

    html_content += f"""
          <!-- PAGE {p['num']}: {p['title']} -->
          <div class="page {cover_class}" id="{p['id']}" {density_attr}>
            <div class="page-inner">
              <div class="page-header">
                <span class="page-header-title">{p['header_title']}</span>
                <span>{p['header_tag']}</span>
              </div>
              
              <div class="page-content" style="flex: 1; display: flex; flex-direction: column;">
                {p['html']}
              </div>

              <div class="page-footer">
                <span>VAIGAI'S IKIGAI GAZETTE</span>
                <span class="page-num">PAGE {p['num']}</span>
              </div>
            </div>
          </div>
    """

html_content += """
        </div>
      </div>
    </div>

    <!-- GAZETTE SCROLLABLE EDITORIAL VIEW (Alternative Accessible / Mobile Mode) -->
    <div id="gazette-container">
      <div class="gazette-search-bar">
        <span style="font-size: 1.1rem; color: var(--text-muted);">🔍</span>
        <input type="text" id="gazette-search-input" class="gazette-search-input" placeholder="Search articles, faculties, placements, departments, or events...">
      </div>

      <div style="border-bottom: 4px double var(--text-headline); padding-bottom: 12px; margin-bottom: 24px; text-align: center;">
        <img src="word/media/image1.jpeg" alt="Vaigai's Ikigai" style="max-height: 80px; width: auto; max-width: 100%;">
        <h1 style="font-family: var(--font-display); font-size: 2.4rem; letter-spacing: 3px; margin: 6px 0;">VAIGAI'S IKIGAI</h1>
        <p style="font-family: var(--font-serif); font-style: italic; color: var(--accent);">The Official Bimonthly Publication of Vaigai College of Engineering, Madurai</p>
      </div>

      <div id="gazette-articles">
"""

# Append Gazette mode sections
for p in pages_data:
    html_content += f"""
        <article class="gazette-section" id="gazette-p{p['num']}" data-page="{p['num']}">
          <div style="font-family: var(--font-sans); font-size: 0.72rem; text-transform: uppercase; color: var(--accent); font-weight: bold; margin-bottom: 4px;">
            {p['header_title']} • PAGE {p['num']}
          </div>
          {p['html']}
          <div style="margin-top: 14px; text-align: right;">
            <button class="ctrl-btn btn-jump-to-flip" data-jump="{p['num']}">
              <span>📖 Open in 3D Flipbook</span>
            </button>
          </div>
        </article>
    """

html_content += """
      </div>
    </div>

  </main>

  <!-- Bottom Floating Dock -->
  <footer class="bottom-dock">
    <div class="dock-left">
      <button id="btn-dock-toc" class="ctrl-btn" title="Table of Contents">
        <span class="ctrl-btn-icon">📑</span>
        <span class="btn-label">Index</span>
      </button>
      <button id="btn-toggle-thumbs" class="ctrl-btn" title="Page Thumbnails">
        <span class="ctrl-btn-icon">🪟</span>
        <span class="btn-label">Pages</span>
      </button>
    </div>

    <div class="dock-center">
      <button id="btn-dock-prev" class="ctrl-btn" title="Previous Page">‹</button>
      <span class="page-indicator" id="page-indicator">Page 1 of 35</span>
      <input type="range" id="page-scrubber" class="page-scrubber" min="1" max="35" value="1" title="Scrub pages">
      <button id="btn-dock-next" class="ctrl-btn" title="Next Page">›</button>
    </div>

    <div class="dock-right">
      <button id="btn-zoom-out" class="ctrl-btn" title="Zoom Out">
        <span class="ctrl-btn-icon">−</span>
      </button>
      <span id="zoom-level" style="font-family: var(--font-sans); font-size: 0.75rem; color: #c9d1d9;">100%</span>
      <button id="btn-zoom-in" class="ctrl-btn" title="Zoom In">
        <span class="ctrl-btn-icon">+</span>
      </button>
      <button id="btn-zoom-reset" class="ctrl-btn" title="Reset Zoom">
        <span class="btn-label">Reset</span>
      </button>
      <button id="btn-print" class="ctrl-btn" title="Print Publication">
        <span class="ctrl-btn-icon">🖨️</span>
      </button>
    </div>
  </footer>

  <!-- Thumbnail Strip Drawer -->
  <div class="thumbnail-strip-wrapper" id="thumbnail-strip">
"""

for p in pages_data:
    html_content += f"""
    <div class="thumb-card" data-page="{p['num']}">
      <span class="thumb-card-num">P.{p['num']}</span>
      <span class="thumb-card-title">{p['title']}</span>
      <span style="font-size: 0.6rem; color: var(--accent);">✦</span>
    </div>
    """

html_content += """
  </div>

  <!-- Table of Contents Slide-Out Drawer -->
  <aside class="toc-drawer" id="toc-drawer">
    <div class="toc-header">
      <h3 class="toc-title">
        <span>📑</span>
        <span>Directory Index</span>
      </h3>
      <button class="toc-close" id="btn-toc-close" title="Close Index">×</button>
    </div>
    <ul class="toc-list" id="toc-list">
"""

for p in pages_data:
    html_content += f"""
      <li class="toc-item" data-page="{p['num']}">
        <div class="toc-item-text">
          <span style="font-weight: 600;">{p['title']}</span>
          <span class="toc-item-sub">{p['subtitle']}</span>
        </div>
        <span class="toc-item-badge">P.{p['num']}</span>
      </li>
    """

html_content += """
    </ul>
  </aside>

  <!-- Modal Backdrop -->
  <div class="modal-backdrop" id="modal-backdrop"></div>

  <!-- Image Lightbox Modal for High-Resolution Inspection -->
  <div class="lightbox-modal" id="lightbox-modal">
    <button class="lightbox-close" id="lightbox-close">×</button>
    <div class="lightbox-img-wrapper">
      <img src="" alt="" id="lightbox-img" class="lightbox-img">
      <p id="lightbox-caption" class="lightbox-caption"></p>
    </div>
  </div>

  <!-- Include Local St.PageFlip Library -->
  <script src="page-flip.browser.js"></script>
  <!-- Application Logic -->
  <script src="app.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated index.html with {len(pages_data)} pages!")
