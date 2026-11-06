#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_flipbook.py
Generates the complete 52-page VAIGAI'S IKIGAI Interactive Flipbook & Gazette:
1. Maximized viewport filling (eliminates dead gaps between flipbook-viewport and flipbook)
2. Full-page posters (edge-to-edge / broadside) with complete descriptions moved to facing pages
3. Two-page landscape panoramic spreads (MESA Inaugural Assembly & Habits of High Performers Assembly)
4. Mobile vertical screen rotation for panoramic landscape photos
5. Significantly enlarged typography, headlines, body text, and balanced editorial layouts with zero uneven gaps
"""

import os
import re

print("Starting generation of 52-page publication...")

pages = {}

def add_page(num, page_type, header_title, header_tag, content_html, toc_title, toc_sub):
    pages[num] = {
        "num": num,
        "type": page_type,
        "header_title": header_title,
        "header_tag": header_tag,
        "content_html": content_html,
        "toc_title": toc_title,
        "toc_sub": toc_sub
    }

# ==============================================================================
# PAGE 1: FRONT COVER
# ==============================================================================
add_page(
    1, "cover-front",
    "VAIGAI COLLEGE OF ENGINEERING", "OFFICIAL BIMONTHLY GAZETTE",
    """
    <div class="masthead-container">
        <div class="masthead-ears">
            <span>✦ APPROVED BY AICTE • AFFILIATED TO ANNA UNIVERSITY</span>
            <span>VOL. 01 • ISSUE 01 • MADURAI ✦</span>
        </div>
        <img src="word/media/image1.jpeg" alt="Vaigai's Ikigai Masthead" class="masthead-banner-img">
        <h1 class="masthead-title">VAIGAI'S IKIGAI</h1>
        <p class="masthead-tagline">Where Purpose Meets Possibility — The Official Bimonthly Gazette</p>
        <div class="masthead-meta-bar">
            <span>MADURAI, TAMIL NADU</span>
            <span>JULY – AUGUST 2026</span>
            <span>FREE INAUGURAL EDITION</span>
        </div>
    </div>

    <div style="text-align: center; margin: 12px 0 10px;">
        <div class="splash-logo-wrapper" style="width: 140px; height: 100px; margin: 0 auto 8px;">
            <img src="logo.png" alt="Vaigai College Crest" class="splash-logo">
        </div>
        <div style="font-family: var(--font-display); font-size: 1.15rem; letter-spacing: 2px; color: var(--accent); font-weight: 700;">
            VAIGAI COLLEGE OF ENGINEERING
        </div>
        <div style="font-family: var(--font-sans); font-size: 0.82rem; color: var(--text-muted); margin-top: 3px;">
            Approved by AICTE, New Delhi & Affiliated to Anna University, Chennai • 15-Acre Campus, Madurai
        </div>
    </div>

    <div class="editorial-card" style="margin: 10px 0; background: #fffcf5; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--primary); text-transform: uppercase; border-bottom: 1px solid var(--paper-border); padding-bottom: 4px; margin-bottom: 6px;">
            ✦ Editorial Board
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.86rem; line-height: 1.55;">
            <div>
                <strong>Dr. Sivaranjani. R</strong><br>
                <span style="color: var(--text-muted);">Principal (i/c) & Professor / ECE</span>
            </div>
            <div>
                <strong>Ms. Aswini. R</strong><br>
                <span style="color: var(--text-muted);">Assistant Professor of English</span>
            </div>
            <div style="grid-column: span 2;">
                <strong>Ms. Supriya. R.J</strong> — <span style="color: var(--text-muted);">Assistant Professor of English</span>
            </div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 8px; padding: 12px; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.92rem; font-weight: bold; color: var(--accent); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 6px;">
            ★ In This Bimonthly Issue
        </div>
        <div style="font-size: 0.86rem; line-height: 1.6; color: var(--text-dark);">
            • <strong>Department Milestones:</strong> RACE Civil & MESA Mechanical Inaugurals<br>
            • <strong>Technical Workshops:</strong> One-Week Embedded Systems & IoT with Caliber Virtual<br>
            • <strong>Student Laurels:</strong> State Vairamuthu 1st, 2nd & 3rd Prizes • NPTEL IIT Madras Toppers<br>
            • <strong>Corporate Drives:</strong> Besant Technologies, Inovonz & Newrta Software Placements
        </div>
    </div>
    """,
    "Front Cover — VAIGAI'S IKIGAI", "Official Bimonthly Gazette • July – August 2026"
)

# ==============================================================================
# SPREAD 1: PAGE 2 & PAGE 3
# ==============================================================================
add_page(
    2, "standard",
    "VAIGAI'S IKIGAI • JULY – AUGUST 2026", "INSTITUTIONAL ETHOS",
    """
    <div class="headline-section">
        <span>INSTITUTIONAL PHILOSOPHY</span>
        <span class="headline-tag">FOUNDATION</span>
    </div>
    <h2 class="headline-lead">WHAT IS VAIGAI'S IKIGAI?</h2>
    <p class="headline-sub">The convergence of purpose, passion, vocation and societal contribution at Vaigai College of Engineering.</p>

    <div class="editorial-card" style="background: linear-gradient(135deg, #fffcf7 0%, #ffffff 100%); border-left: 4px solid var(--accent); margin: 8px 0;">
        <div class="editorial-item">
            <span class="editorial-letter">V</span>
            <div><strong>The Vision</strong> that drives our institutional mission and fuels boundless ambition.</div>
        </div>
        <div class="editorial-item">
            <span class="editorial-letter">A</span>
            <div><strong>The Achievements</strong> that define our students and faculty on national platforms.</div>
        </div>
        <div class="editorial-item">
            <span class="editorial-letter">I</span>
            <div><strong>The Intelligence</strong> that inspires technological creativity and ethical leadership.</div>
        </div>
        <div class="editorial-item">
            <span class="editorial-letter">G</span>
            <div><strong>The Greatness</strong> we nurture through discipline, character, and lifelong curiosity.</div>
        </div>
        <div class="editorial-item">
            <span class="editorial-letter">A</span>
            <div><strong>The Academic Aspirations</strong> we pursue with unyielding pedagogical rigor.</div>
        </div>
        <div class="editorial-item">
            <span class="editorial-letter">I</span>
            <div><strong>The Innovations</strong> through which our engineers create transformative social impact.</div>
        </div>
    </div>

    <div class="headline-section" style="margin-top: 10px;">
        <span>CAMPUS HERITAGE</span>
        <span class="headline-tag">ESTD. 2012</span>
    </div>
    <div class="editorial-cols dropcap">
        <p>Vaigai College of Engineering (VCE) was established in 2012 under the visionary auspices of the Vaigai Educational Trust (VET), Madurai, with the sacred mission of providing high-caliber technical education and nurturing socially responsible global engineers.</p>
        <p>Spread across a lush 15-acre green campus, VCE provides state-of-the-art laboratories, modern computing complexes, digital seminar halls, and vibrant incubation incubators, empowering students from diverse backgrounds to excel in world-class engineering careers.</p>
    </div>
    """,
    "What is Vaigai's Ikigai?", "The Six Pillars of Purpose & Campus Heritage"
)

add_page(
    3, "standard",
    "DEPARTMENT OF CIVIL ENGINEERING", "ASSOCIATION INAUGURAL",
    """
    <div class="headline-section">
        <span>DEPARTMENT OF CIVIL ENGINEERING</span>
        <span class="headline-tag">21 JULY 2026</span>
    </div>
    <h2 class="headline-lead">INAUGURATION CEREMONY OF RACE – ROYAL ASSOCIATION OF CIVIL ENGINEERING</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: ML-2</span>
        <span>•</span>
        <span>CHIEF GUEST: DR. R. SIVARANJANI, PRINCIPAL (I/C)</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Department of Civil Engineering, in proud collaboration with RACE – Royal Association of Civil Engineering, organized the grand Inauguration Ceremony of the association for the academic year 2026–2027 on 21 July 2026 at the ML-2 Seminar Complex.</p>
        <p>Dr. R. Sivaranjani, Principal (i/c), graced the occasion as Chief Guest, commending the department for spearheading initiatives in sustainable construction, smart infrastructure modeling, and advanced geotechnical exploration.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image2.jpeg" data-caption="Chief Guest Dr. R. Sivaranjani Lighting the Lamp at RACE Inauguration">
            <img src="word/media/image2.jpeg" alt="Dais Dignitaries at RACE Inaugural" class="news-img" style="max-height: 240px; object-fit: cover;">
            <div class="news-caption">
                <span>Dignitaries Lighting Inaugural Lamp</span>
                <span class="caption-tag">Civil Dept</span>
            </div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image3.jpeg" data-caption="Civil Engineering Faculty and Student Delegates Gathering">
            <img src="word/media/image3.jpeg" alt="Civil Engineering Delegates Gathering" class="news-img" style="max-height: 240px; object-fit: cover;">
            <div class="news-caption">
                <span>Faculty & Student Delegates Assembly</span>
                <span class="caption-tag">ML-2 Hall</span>
            </div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Department Leadership
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Organized under the dynamic stewardship of <strong>Mr. T. Vijaya Raghavan</strong>, Head of Department, and <strong>Mr. P. Muthuanand</strong>, Association Faculty In-Charge.
        </div>
    </div>
    """,
    "Civil Engineering Inaugural (RACE)", "Inauguration Ceremony & Keynote Address"
)

# ==============================================================================
# SPREAD 2: PAGE 4 & PAGE 5
# ==============================================================================
add_page(
    4, "standard",
    "DEPARTMENT OF CIVIL ENGINEERING", "LEADERSHIP INVESTITURE",
    """
    <div class="headline-section">
        <span>LEADERSHIP INVESTITURE</span>
        <span class="headline-tag">21 JULY 2026</span>
    </div>
    <h2 class="headline-lead">STUDENT LEADERS INVESTED AT RACE BADGE CEREMONY</h2>
    <p class="headline-sub">Formal Recognition and Swearing-in of Association Student Office Bearers for 2026–2027</p>

    <div class="editorial-cols dropcap">
        <p>A ceremonial badge distribution investiture was conducted to formally induct the student office bearers of RACE. The newly appointed student executive committee pledged to uphold the values of teamwork, technical innovation, and professional integrity.</p>
        <p>The office bearers will oversee student symposiums, surveying bootcamps, CAD design competitions, and site internships, serving as a vital bridge between students and industrial bodies.</p>
    </div>

    <div class="image-gallery-triple" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image4.jpeg" data-caption="Badge Investiture of President & Vice-President">
            <img src="word/media/image4.jpeg" alt="Badge Investiture" class="news-img" style="max-height: 210px; object-fit: cover;">
            <div class="news-caption"><span>Presidential Investiture</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image5.jpeg" data-caption="Badge Pinning of Student Secretary & Treasurer">
            <img src="word/media/image5.jpeg" alt="Secretary Investiture" class="news-img" style="max-height: 210px; object-fit: cover;">
            <div class="news-caption"><span>Secretarial Investiture</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image6.jpeg" data-caption="Induction of Executive Joint Treasurers">
            <img src="word/media/image6.jpeg" alt="Treasurers Investiture" class="news-img" style="max-height: 210px; object-fit: cover;">
            <div class="news-caption"><span>Executive Induction</span></div>
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Leadership is not a title; it is the courage to inspire peers and transform collective engineering aspirations into concrete reality."
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-dark);">
            ✦ <strong>Elected Council Bearers:</strong> President, Vice President, Secretary, Treasurer, and Joint Treasurers were decorated with ceremonial insignia by Principal Dr. R. Sivaranjani.
        </div>
    </div>
    """,
    "Civil Leaders Badge Investiture", "RACE Student Office Bearers Sworn In"
)

add_page(
    5, "standard",
    "DEPARTMENT OF MECHANICAL ENGINEERING", "MESA–2026 INAUGURAL",
    """
    <div class="headline-section">
        <span>DEPARTMENT OF MECHANICAL ENGINEERING</span>
        <span class="headline-tag">19 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">INAUGURAL FUNCTION OF MECHANICAL ENGINEERS STUDENT ASSOCIATION (MESA–2026)</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: AUDITORIUM</span>
        <span>•</span>
        <span>PATRON: DR. R. SIVARANJANI, PRINCIPAL (I/C)</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Department of Mechanical Engineering celebrated the grand Inaugural Function of the Mechanical Engineers Student Association (MESA–2026) on 19 August 2026 with immense academic fervor.</p>
        <p>Dr. R. Sivaranjani, Principal (i/c), commended the department for fostering hands-on engineering, smart manufacturing, and electric mobility innovation. She challenged students to leverage association platforms to master generative CAD, computational fluid dynamics, and robotics.</p>
    </div>

    <div class="news-image-frame" style="margin: 8px 0;" data-img-src="word/media/image7.jpeg" data-caption="Official MESA–2026 Inaugural Ceremony Banner">
        <img src="word/media/image7.jpeg" alt="MESA–2026 Inaugural Banner" class="news-img" style="max-height: 250px; object-fit: cover;">
        <div class="news-caption">
            <span>Official MESA–2026 Inaugural Banner</span>
            <span class="caption-tag">Mechanical Dept</span>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 8px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Departmental Organizing Committee
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Orchestrated by <strong>Dr. M.K.V. Karthikeyan</strong>, Head of Department / Mech, and <strong>Mr. A.M. Milan</strong>, Assistant Professor of Mechanical Engineering & Association In-Charge.
        </div>
    </div>
    """,
    "Mechanical Engineering (MESA-2026)", "Inaugural Function & Leadership Keynote"
)

# ==============================================================================
# SPREAD 3: PAGE 6 & PAGE 7
# ==============================================================================
add_page(
    6, "standard",
    "DEPARTMENT OF MECHANICAL ENGINEERING", "CO-CURRICULAR HORIZONS",
    """
    <div class="headline-section">
        <span>STRATEGIC HORIZONS</span>
        <span class="headline-tag">INDUSTRY 4.0</span>
    </div>
    <h2 class="headline-lead">FORGING LEADERSHIP, DESIGN THINKING & TEAMWORK</h2>
    <p class="headline-sub">MESA–2026 Launches Dynamic Calendar of Design Competitions, CNC Machining & EV Prototyping</p>

    <div class="editorial-cols dropcap">
        <p>The inauguration marked the commencement of a vibrant series of technical, academic, and co-curricular initiatives tailored for mechanical engineering scholars.</p>
        <p>MESA serves as an incubation platform for students to sharpen design thinking, rapid prototyping, and industrial problem-solving skills. The association announced upcoming state competitions in CAD modeling, thermal simulations, and robotic assembly.</p>
    </div>

    <div class="news-image-frame" style="margin: 8px 0;" data-img-src="word/media/image9.jpeg" data-caption="Faculty and Student Association Office Bearers Assembly">
        <img src="word/media/image9.jpeg" alt="MESA Interactive Assembly" class="news-img" style="max-height: 250px; object-fit: cover;">
        <div class="news-caption">
            <span>Faculty & Student Association Office Bearers Assembly</span>
            <span class="caption-tag">Auditorium Forum</span>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--primary); margin-bottom: 4px; text-transform: uppercase;">
            ★ Core Takeaways & Competency Mandate
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • Hands-on mastery in industrial CNC, 3D printing & hybrid manufacturing<br>
            • Student-led industrial technical symposiums and expert webinars<br>
            • Enhanced career readiness for core aerospace, automotive & energy sectors
        </div>
    </div>
    """,
    "Mechanical Leadership & Teamwork", "MESA-2026 Industry 4.0 Roadmaps"
)

add_page(
    7, "standard",
    "DEPARTMENT OF MECHANICAL ENGINEERING", "INDUSTRIAL READINESS",
    """
    <div class="headline-section">
        <span>CORE ENGINEERING</span>
        <span class="headline-tag">INNOVATION</span>
    </div>
    <h2 class="headline-lead">ADVANCED AUTOMATION & SUSTAINABLE MANUFACTURING</h2>
    <p class="headline-sub">Preparing Mechanical Engineers for Aerospace, Robotics, and Renewable Energy Sectors</p>

    <div class="editorial-cols dropcap">
        <p>The Department of Mechanical Engineering at Vaigai College integrates fundamental mechanical principles with futuristic digital manufacturing. Through state-of-the-art CAD/CAM laboratories, students master high-precision design software and simulation tools.</p>
        <p>Faculty mentors work closely with students on live consultancy projects, sustainable energy harvesters, and industrial automation rigs, ensuring every graduate possesses both theoretical depth and shop-floor confidence.</p>
    </div>

    <div class="editorial-card" style="margin: 10px 0; background: #fffcf8; border-left: 4px solid var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Department Research & Development Thrust Areas
        </div>
        <div style="font-size: 0.86rem; line-height: 1.6; color: var(--text-dark);">
            1. <strong>Thermal & Fluids Engineering:</strong> Parabolic solar concentrators & nanofluid heat exchangers.<br>
            2. <strong>Materials Science:</strong> High-entropy alloys and bio-composite lightweight structures.<br>
            3. <strong>Industrial Automation:</strong> Programmable logic controllers & automated material handling.
        </div>
    </div>

    <div class="pull-quote" style="margin: 10px 0;">
        "Mechanical engineering is the bedrock of modern civilization — from nano-machinery to space exploration."
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-muted);">
            Coordinated under <strong>Dr. M.K.V. Karthikeyan</strong>, HoD/Mech, with dedicated contributions from all departmental laboratory instructors.
        </div>
    </div>
    """,
    "Mechanical Industrial Readiness", "Advanced Automation & R&D Thrusts"
)

# ==============================================================================
# SPREAD 4: PAGE 8 & PAGE 9 — GRAND TWO-PAGE PANORAMIC SPREAD!
# ==============================================================================
add_page(
    8, "spread-left",
    "DEPARTMENT OF MECHANICAL ENGINEERING", "PANORAMIC SPREAD (LEFT)",
    """
    <div class="spread-container spread-left-half" data-spread-src="word/media/image8.jpeg" data-caption="MESA–2026 Grand Inaugural Assembly — Principal Dr. R. Sivaranjani Addressing Faculty and Scholars">
        <img src="word/media/image8.jpeg" alt="MESA Grand Inaugural Assembly Left Half" class="spread-img spread-img-left">
        <div class="spread-caption-overlay spread-overlay-left">
            <span class="spread-tag">★ TWO-PAGE PANORAMIC SPREAD ★</span>
            <h2 class="spread-title">MESA–2026 INAUGURAL ASSEMBLY</h2>
            <p class="spread-sub">Principal Dr. R. Sivaranjani Addresses Faculty & Mechanical Scholars</p>
        </div>
        <button class="mobile-spread-rotate-btn" title="Rotate for Vertical Mobile Screen" type="button">
            <span>🔄 Rotate View</span>
        </button>
    </div>
    """,
    "MESA-2026 Grand Assembly (Panorama Left)", "Panoramic Centerfold Spread (Left Half)"
)

add_page(
    9, "spread-right",
    "DEPARTMENT OF MECHANICAL ENGINEERING", "PANORAMIC SPREAD (RIGHT)",
    """
    <div class="spread-container spread-right-half" data-spread-src="word/media/image8.jpeg" data-caption="MESA–2026 Grand Inaugural Assembly — Dr. Abdul Kalam Auditorium">
        <img src="word/media/image8.jpeg" alt="MESA Grand Inaugural Assembly Right Half" class="spread-img spread-img-right">
        <div class="spread-caption-overlay spread-overlay-right">
            <div class="spread-meta-right">DR. ABDUL KALAM AUDITORIUM • 19 AUGUST 2026</div>
            <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 4px;">Department of Mechanical Engineering, Vaigai College of Engineering</div>
        </div>
        <button class="mobile-spread-rotate-btn" title="Rotate for Vertical Mobile Screen" type="button">
            <span>🔄 Rotate View</span>
        </button>
    </div>
    """,
    "MESA-2026 Grand Assembly (Panorama Right)", "Panoramic Centerfold Spread (Right Half)"
)

# ==============================================================================
# SPREAD 5: PAGE 10 & PAGE 11 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    10, "poster",
    "DEPARTMENTS OF ECE & EEE", "OFFICIAL EVENT BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image10.jpeg" data-caption="One-Week Workshop on Embedded Systems & IoT in Association with Caliber Virtual Technologies">
        <img src="word/media/image10.jpeg" alt="One-Week Workshop on Embedded Systems and IoT Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "IoT Workshop Broadside Poster", "Fullsize Archival Event Poster (image10)"
)

add_page(
    11, "standard",
    "DEPARTMENTS OF ECE & EEE", "TECHNICAL WORKSHOP",
    """
    <div class="headline-section">
        <span>DEPARTMENTS OF ECE & EEE</span>
        <span class="headline-tag">27 JULY – 3 AUG 2026</span>
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
        <p>The Departments of Electronics and Communication Engineering (ECE) and Electrical and Electronics Engineering (EEE) jointly organized an intensive One-Week Workshop on Embedded Systems and IoT from 27 July to 3 August 2026 at ML-3 for III and IV year engineers, conducted in technical collaboration with Caliber Virtual Technologies.</p>
        <p>Industry trainers delivered deep-dive training on microcontroller architectures, sensor interfacing, wireless telemetry, MQTT communication protocols, and cloud IoT dashboards, transforming students from conceptual learners to agile hardware builders.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image11.jpeg" data-caption="Embedded Systems Theory & Hardware Briefing Session">
            <img src="word/media/image11.jpeg" alt="Theoretical IoT Concepts Session" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption">
                <span>Embedded Systems Theory & Hardware Briefing</span>
                <span class="caption-tag">ML-3 Lecture</span>
            </div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image12.jpeg" data-caption="Hands-on Laboratory Training: Students Deploying Embedded IoT Firmware">
            <img src="word/media/image12.jpeg" alt="Students in IoT Lab" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption">
                <span>Hands-on Lab: Firmware Deployment</span>
                <span class="caption-tag">Hardware Lab</span>
            </div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Workshop Coordination Team
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Coordinated by <strong>Dr. R. Sivaranjani</strong>, Principal & Professor/ECE, <strong>Mr. A. Shakil Ahmed</strong>, AP/ECE, and <strong>Ms. V. Saranya</strong>, AP/EEE.
        </div>
    </div>
    """,
    "Embedded Systems & IoT Workshop Story", "Caliber Virtual Tech Story & Hardware Lab"
)

# ==============================================================================
# SPREAD 6: PAGE 12 & PAGE 13 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    12, "poster",
    "FACULTY DEVELOPMENT CELL", "OFFICIAL FDC BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image13.jpeg" data-caption="Faculty Development Programme: IIC & You - Building an Innovation Culture">
        <img src="word/media/image13.jpeg" alt="FDC Poster: IIC & You" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "FDC Innovation Broadside Poster", "Fullsize Archival Event Poster (image13)"
)

add_page(
    13, "standard",
    "FACULTY DEVELOPMENT CELL", "INNOVATION CULTURE",
    """
    <div class="headline-section">
        <span>FACULTY DEVELOPMENT CELL (FDC)</span>
        <span class="headline-tag">31 JULY 2026</span>
    </div>
    <h2 class="headline-lead">FACULTY DEVELOPMENT PROGRAMME: "IIC & YOU: BUILDING AN INNOVATION CULTURE"</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: SEMINAR HALL</span>
        <span>•</span>
        <span>INSTITUTION'S INNOVATION COUNCIL</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Faculty Development Cell (FDC), in synergy with the Institution's Innovation Council (IIC), organized a high-impact Faculty Development Programme titled "IIC & You: Building an Innovation Culture" on 31 July 2026 for all faculty members.</p>
        <p>The programme oriented educators toward cultivating an entrepreneurial mindset among undergraduates, navigating patent filing procedures, and integrating problem-solving methodologies into standard university course syllabi.</p>
    </div>

    <div class="news-image-frame" style="margin: 8px 0;" data-img-src="word/media/image14.jpeg" data-caption="Interactive Faculty Forum on Incubation and Innovation Methodologies">
        <img src="word/media/image14.jpeg" alt="Interactive Faculty Forum" class="news-img" style="max-height: 250px; object-fit: cover;">
        <div class="news-caption">
            <span>Faculty Forum: Commercialization & Patent Strategy</span>
            <span class="caption-tag">Seminar Hall</span>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ Core Takeaways for Faculty Mentors
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • Aligning classroom projects with MoE's Innovation Cell (MIC) mandates<br>
            • Seed funding mechanisms, IPR filing, and student pre-incubation roadmaps<br>
            • Enhancing institutional NIRF innovation ranking through industry collaboration
        </div>
    </div>
    """,
    "FDC: Building an Innovation Culture", "Faculty Innovation Forum & IIC Guidelines"
)

# ==============================================================================
# SPREAD 7: PAGE 14 & PAGE 15 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    14, "poster",
    "YOUTH RED CROSS & RED RIBBON CLUB", "HEALTH FORUM BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image15.jpeg" data-caption="Campus-Wide Health Awareness & Preventive Lifestyle Programme Poster">
        <img src="word/media/image15.jpeg" alt="Health Awareness Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Health Awareness Broadside Poster", "Fullsize Archival Event Poster (image15)"
)

add_page(
    15, "standard",
    "YOUTH RED CROSS & RED RIBBON CLUB", "PREVENTIVE HEALTHCARE",
    """
    <div class="headline-section">
        <span>YOUTH RED CROSS & RED RIBBON CLUB</span>
        <span class="headline-tag">27 JULY 2026</span>
    </div>
    <h2 class="headline-lead">CAMPUS-WIDE HEALTH AWARENESS & PREVENTIVE LIFESTYLE PROGRAMME</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: AUDITORIUM</span>
        <span>•</span>
        <span>CHIEF RESOURCE PERSON: DR. DEEPA, MBBS, MD</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Youth Red Cross (YRC) and Red Ribbon Club (RRC) organized a comprehensive Campus-Wide Health Awareness and Preventive Lifestyle Programme on 27 July 2026, empowering engineering scholars with vital knowledge on lifestyle wellness.</p>
        <p>Dr. Deepa delivered an eye-opening keynote on combating sedentary tech habits, ergonomic posture, balanced nutritional intake, and early detection of metabolic disorders, emphasizing that physical vitality is the foundation of sharp analytical cognition.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image16.jpeg" data-caption="Medical Presentation on Youth Preventive Habits">
            <img src="word/media/image16.jpeg" alt="Medical Presentation" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Medical Presentation by Dr. Deepa</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image17.jpeg" data-caption="Interactive Q&A Session with Students">
            <img src="word/media/image17.jpeg" alt="Student Health Q&A" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Student Q&A & Clinical Consultations</span></div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ Clinical Takeaways for Engineers
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Ergonomic desk habits, digital eye strain mitigation (20-20-20 rule), hydration regimens, and stress regulation practices during examinations.
        </div>
    </div>
    """,
    "Holistic Wellness & Lifestyle Story", "Dr. Deepa Keynote & Preventive Medicine"
)

# ==============================================================================
# SPREAD 8: PAGE 16 & PAGE 17 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    16, "poster",
    "INSTITUTIONAL SOCIAL RESPONSIBILITY", "BLOOD CAMP BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image20.jpeg" data-caption="Mega Blood Donation Camp: Over 50 Volunteers Register to Save Lives">
        <img src="word/media/image20.jpeg" alt="Blood Donation Camp Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Blood Donation Camp Broadside Poster", "Fullsize Archival Event Poster (image20)"
)

add_page(
    17, "standard",
    "INSTITUTIONAL SOCIAL RESPONSIBILITY", "BLOOD DONATION MISSION",
    """
    <div class="headline-section">
        <span>NSS • YRC • RRC COLLABORATION</span>
        <span class="headline-tag">31 JULY 2026</span>
    </div>
    <h2 class="headline-lead">MEGA BLOOD DONATION CAMP: OVER 50 VOLUNTEERS REGISTER TO SAVE LIVES</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: HEALTH CENTRE</span>
        <span>•</span>
        <span>PARTNER: MEENAKSHI MISSION HOSPITAL</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>In an inspiring display of humanitarian solidarity, the National Service Scheme (NSS), Youth Red Cross (YRC), and Red Ribbon Club (RRC) organized a Mega Blood Donation Camp on 31 July 2026 in technical collaboration with Meenakshi Mission Hospital and Research Centre, Madurai.</p>
        <p>Over 50 student and faculty donors voluntarily contributed blood after comprehensive pre-screening, aiding regional trauma wards, pediatric surgical units, and cancer care centers across Madurai district.</p>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Blood donation is the purest manifestation of civic duty — a selfless contribution that transforms an ordinary student into a life-saver."
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Clinical Partnership & Safety Protocols
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Supervised by chief medical officers from <strong>Meenakshi Mission Hospital</strong>, ensuring sterilized single-use phlebotomy equipment, donor refreshment protocols, and post-donation care.
        </div>
    </div>
    """,
    "Mega Blood Donation Camp Story", "NSS & YRC 50+ Donors Humanitarian Mission"
)

# ==============================================================================
# SPREAD 9: PAGE 18 & PAGE 19 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    18, "poster",
    "INSTITUTIONAL SOCIAL RESPONSIBILITY", "DONOR HONORS BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image21.jpeg" data-caption="Celebrating Social Responsibility and Service: Certificate Distribution Ceremony">
        <img src="word/media/image21.jpeg" alt="Donor Recognition Honors Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Blood Donor Honors Broadside Poster", "Fullsize Archival Event Poster (image21)"
)

add_page(
    19, "standard",
    "INSTITUTIONAL SOCIAL RESPONSIBILITY", "DONOR RECOGNITION",
    """
    <div class="headline-section">
        <span>HONORS CEREMONY</span>
        <span class="headline-tag">DONOR AWARDS</span>
    </div>
    <h2 class="headline-lead">CELEBRATING SOCIAL RESPONSIBILITY AND SERVICE</h2>
    <p class="headline-sub">Certificates and Badges Awarded to Student and Faculty Blood Donors</p>

    <div class="editorial-cols dropcap">
        <p>A formal certificate awarding ceremony was convened following the blood donation drive to felicitate each student and staff donor. Principal Dr. R. Sivaranjani presented government donor certificates, commending the volunteers for their selfless empathy.</p>
        <p>The event highlighted the college's holistic mission: producing engineers who are not merely proficient code-builders and machine designers, but compassionate, community-minded custodians of human welfare.</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf5; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--primary); margin-bottom: 4px; text-transform: uppercase;">
            ★ Institutional Community Impact Metrics
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • 50+ Units of whole blood collected and cold-chained to regional blood banks<br>
            • 100% Volunteer compliance with medical health benchmarks and hemoglobin checks<br>
            • Annual institutional citation conferred by Tamil Nadu State Blood Transfusion Council
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-muted);">
            Coordinated by the <strong>NSS Programme Officer</strong>, <strong>YRC Coordinator</strong>, and <strong>RRC In-Charge</strong> with student volunteers.
        </div>
    </div>
    """,
    "Celebrating Social Responsibility & Service", "Blood Donor Felicitations & Community Impact"
)

# ==============================================================================
# SPREAD 10: PAGE 20 & PAGE 21 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    20, "poster",
    "RED RIBBON CLUB (RRC)", "STATE QUIZ BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image22.jpeg" data-caption="State-Level Online Quiz on HIV/STI Awareness Organized by Red Ribbon Club">
        <img src="word/media/image22.jpeg" alt="HIV/STI Quiz State Competition Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "HIV/STI Awareness Quiz Poster", "Fullsize Archival Event Poster (image22)"
)

add_page(
    21, "standard",
    "RED RIBBON CLUB (RRC)", "STATE COMPETITION",
    """
    <div class="headline-section">
        <span>RED RIBBON CLUB (RRC)</span>
        <span class="headline-tag">12 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">140+ STUDENTS PARTICIPATE IN STATE-LEVEL ONLINE QUIZ ON HIV/STI AWARENESS</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: ONLINE PORTAL</span>
        <span>•</span>
        <span>TNSACS PARTNERSHIP</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Red Ribbon Club (RRC) of Vaigai College achieved remarkable student mobilization with over 140 students actively competing in the prestigious State-Level Online Quiz on HIV/AIDS and STI Awareness on 12 August 2026.</p>
        <p>Organized in partnership with the Tamil Nadu State AIDS Control Society (TNSACS), the digital quiz tested knowledge on transmission pathways, clinical treatments, stigma eradication, and community support frameworks.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image23.jpeg" data-caption="Online Quiz Examination Session in Digital Labs">
            <img src="word/media/image23.jpeg" alt="Online Quiz Hall" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Digital Lab Quiz Testing</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image24.jpeg" data-caption="RRC Student Assembly and Awareness Briefing">
            <img src="word/media/image24.jpeg" alt="RRC Student Assembly" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>RRC Student Briefing Assembly</span></div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ RRC Youth Health Literacy Highlights
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • 140+ participants across CSE, ECE, EEE, Mech, and Civil departments<br>
            • Promotion of factual, scientifically grounded medical understanding<br>
            • State certificates awarded to top scorers by TNSACS Chennai
        </div>
    </div>
    """,
    "Adolescent Health Literacy & RRC Story", "140+ Students State Laurels in TNSACS Quiz"
)

# ==============================================================================
# SPREAD 11: PAGE 22 & PAGE 23 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    22, "poster",
    "VCE ANTI-DRUG CLUB", "CAMPUS PLEDGE BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image25.png" data-caption="Mass Anti-Drug Pledge: 250 Students Unite for a Healthy Future">
        <img src="word/media/image25.png" alt="Mass Anti-Drug Pledge Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Anti-Drug Campaign Broadside Poster", "Fullsize Archival Event Poster (image25)"
)

add_page(
    23, "standard",
    "VCE ANTI-DRUG CLUB", "MEDICAL KEYNOTE & PLEDGE",
    """
    <div class="headline-section">
        <span>ANTI-DRUG CLUB</span>
        <span class="headline-tag">11 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">DR. BHARATH KRISHNA: "PROTECT YOUR BRAIN & CAREER"</h2>
    <p class="headline-sub">Distinguished Physician Briefs 250 Students on the Science of Addiction and Brain Health</p>
    <div class="byline-bar">
        <span class="byline-date">VENUE: AUDITORIUM</span>
        <span>•</span>
        <span>250 SCHOLARS ENROLLED</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Anti-Drug Club of Vaigai College conducted a massive campus-wide campaign on 11 August 2026, wherein 250 students solemnly pledged their commitment to a substance-free life, academic brilliance, and personal accountability.</p>
        <p>Dr. Bharath Krishna delivered a compelling medical keynote, explaining the neurochemical mechanisms through which narcotics compromise executive decision-making, emotional stability, and long-term professional aspirations.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image26.png" data-caption="Dr. Bharath Krishna Addressing Engineering Students on Brain Health">
            <img src="word/media/image26.png" alt="Dr. Bharath Krishna Lecture" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Dr. Bharath Krishna Lecture</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image27.png" data-caption="Mass Pledge Ceremony: 250 Students Swearing Anti-Drug Oath">
            <img src="word/media/image27.png" alt="Mass Pledge Ceremony" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>250 Students Swearing Oath</span></div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ The 5 Commitments of the VCE Anti-Drug Pledge
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Total abstinence from illicit substances, active peer counseling, reporting unauthorized solicitations, prioritizing mental fitness, and safeguarding institutional integrity.
        </div>
    </div>
    """,
    "Anti-Drug Campaign & Keynote Story", "250 Students Swear Oath & Medical Talk"
)

# ==============================================================================
# SPREAD 12: PAGE 24 & PAGE 25 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    24, "poster",
    "ENTREPRENEURSHIP DEVELOPMENT CELL (EDC)", "STARTUP MASTERCLASS",
    """
    <div class="poster-full-frame" data-img-src="word/media/image28.jpeg" data-caption="Igniting Startup Dreams: Ms. Archana Veeravel Addresses III & IV Year Students">
        <img src="word/media/image28.jpeg" alt="Startup Dreams Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Igniting Startup Dreams Poster", "Fullsize Archival Event Poster (image28)"
)

add_page(
    25, "standard",
    "ENTREPRENEURSHIP DEVELOPMENT CELL (EDC)", "VENTURE CREATION",
    """
    <div class="headline-section">
        <span>ENTREPRENEURSHIP CELL</span>
        <span class="headline-tag">13 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">FROM LAB PROTOTYPE TO VIABLE COMMERCIAL STARTUP</h2>
    <p class="headline-sub">Ms. Archana Veeravel Guides III & IV Year Students on Venture Capital, Product Market Fit & Incubation</p>

    <div class="editorial-cols dropcap">
        <p>The Entrepreneurship Development Cell (EDC) organized an inspiring startup masterclass on 13 August 2026 titled "Igniting Startup Dreams" for pre-final and final-year engineering students across all disciplines.</p>
        <p>Distinguished entrepreneur Ms. Archana Veeravel shared hard-won wisdom on identifying scalable pain points, designing minimum viable products (MVPs), securing angel investment, and leveraging Tamil Nadu's vibrant startup incubation grants.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image29.jpeg" data-caption="Ms. Archana Veeravel Addressing the Student Gathering">
            <img src="word/media/image29.jpeg" alt="Ms. Archana Veeravel Keynote" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Ms. Archana Veeravel Keynote</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image30.jpeg" data-caption="Student Entrepreneurs Presenting Prototype Ideas">
            <img src="word/media/image30.jpeg" alt="Student Ideation Session" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Student Ideation & Pitch Session</span></div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ 4-Step Venture Launch Roadmap
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            1. Validate problem statement through customer surveys • 2. Build rapid low-fidelity prototypes • 3. Secure mentor evaluation via VCE Incubation Cell • 4. Pitch for seed capital.
        </div>
    </div>
    """,
    "EDC: Startup Ideation & Prototyping", "Ms. Archana Veeravel Masterclass & Venture Roadmap"
)

# ==============================================================================
# SPREAD 13: PAGE 26 & PAGE 27 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    26, "poster",
    "NATIONAL SERVICE SCHEME (NSS)", "INDEPENDENCE DAY BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image33.jpeg" data-caption="78th Independence Day Celebrated with Patriotic Splendor & Civic Pride">
        <img src="word/media/image33.jpeg" alt="78th Independence Day Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Independence Day Broadside Poster", "Fullsize Archival Event Poster (image33)"
)

add_page(
    27, "standard",
    "NATIONAL SERVICE SCHEME (NSS)", "78TH INDEPENDENCE DAY",
    """
    <div class="headline-section">
        <span>NATIONAL SERVICE SCHEME (NSS)</span>
        <span class="headline-tag">15 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">PATRIOTIC SPLENDOR & CIVIC RESPONSIBILITY AT VAIGAI CAMPUS</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: CENTRAL FLAGPOST</span>
        <span>•</span>
        <span>PATRON: DR. R. SIVARANJANI, PRINCIPAL (I/C)</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The 78th Independence Day of our sovereign nation was celebrated with dignified patriotic fervor across the 15-acre Vaigai College of Engineering campus on 15 August 2026, attended by management trustees, faculties, and scholars.</p>
        <p>Principal Dr. R. Sivaranjani unfurled the National Tricolor, followed by an impressive guard of honor by NSS student cadets. In her ceremonial address, she reminded engineers of their pivotal role in realizing Viksit Bharat 2047 through indigenous innovation.</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf5; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--primary); margin-bottom: 4px; text-transform: uppercase;">
            ★ Commemorative Highlights & Green Drive
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • <strong>Tricolor Unfurling & National Anthem:</strong> Rendered with patriotic pride by the campus choir<br>
            • <strong>Student Cultural Vignettes:</strong> Patriotic poetry recitals and historical drama<br>
            • <strong>Memorial Tree Plantation:</strong> 78 native saplings planted across campus by NSS volunteers
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "True patriotism is not merely saluting the flag on national holidays, but dedicating our technical knowledge to the uplifting of our community."
    </div>
    """,
    "78th Independence Day Celebration", "National Flag Unfurled & Patriotic Address"
)

# ==============================================================================
# SPREAD 14: PAGE 28 & PAGE 29 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    28, "poster",
    "UNIVERSITY ACADEMIC HONORS", "ANNA UNIVERSITY HONORS",
    """
    <div class="poster-full-frame" data-img-src="word/media/image34.jpeg" data-caption="Anna University Rank Holders Honors — 2021–2025 Graduating Batch">
        <img src="word/media/image34.jpeg" alt="Anna University Rank Holders Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ ANNA UNIVERSITY RANK HOLDERS ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Anna University Rank Holders Poster", "Fullsize Archival Honors Poster (image34)"
)

add_page(
    29, "standard",
    "UNIVERSITY ACADEMIC HONORS", "ANNA UNIVERSITY",
    """
    <div class="headline-section">
        <span>ACADEMIC EXCELLENCE</span>
        <span class="headline-tag">BATCH 2021–2025</span>
    </div>
    <h2 class="headline-lead">PROUDLY PRESENTING OUR ANNA UNIVERSITY UNIVERSITY RANK HOLDERS!</h2>
    <p class="headline-sub">Exemplary Scholars Cement Institutional Stature Among Affiliated Colleges Across Tamil Nadu</p>

    <div class="editorial-cols dropcap">
        <p>Vaigai College of Engineering takes immense institutional pride in announcing that our engineering scholars have secured prestigious University Ranks in the statewide Anna University final examinations for the 2021–2025 graduating cohort.</p>
        <p>This stellar achievement reflects the unwavering academic rigor, student mentorship, and intensive revision frameworks orchestrated across all departments by our dedicated faculty under the guidance of Dean Academics Dr. B. Sujatha.</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf8; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ Institutional Academic Honor Roll
        </div>
        <div style="font-size: 0.86rem; line-height: 1.6; color: var(--text-dark);">
            • <strong>Gold & Silver Medallists:</strong> Honored for university percentile supremacy<br>
            • <strong>Departmental Laurels:</strong> Top ranks secured across CSE, ECE, EEE, Mech & Civil<br>
            • <strong>VET Academic Scholarship:</strong> Cash citations and trophies awarded by Trustees
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Academic supremacy is not an accidental event; it is the deliberate habit of daily discipline and relentless intellectual inquiry."
    </div>
    """,
    "Academic Excellence: Rank Holders", "Anna University Distinctions & Medalists"
)

# ==============================================================================
# SPREAD 15: PAGE 30 & PAGE 31 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    30, "poster",
    "STATE-LEVEL STUDENT LAURELS", "ORATORY COMPETITION",
    """
    <div class="poster-full-frame" data-img-src="poetry_competition_based_on_the_works_of_poet_Vairamuthu.jpeg" data-caption="Vaigai Scholars Sweep State Vairamuthu Speech Contest with 1st, 2nd & 3rd Prizes">
        <img src="poetry_competition_based_on_the_works_of_poet_Vairamuthu.jpeg" alt="State Vairamuthu Speech Contest Broadside" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ STATE ORATORY LAURELS ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "State Vairamuthu Contest Poster", "Fullsize Archival Contest Poster (Vairamuthu)"
)

add_page(
    31, "standard",
    "STATE-LEVEL STUDENT LAURELS", "ORATORY EXCELLENCE",
    """
    <div class="headline-section">
        <span>STATE-LEVEL COMPETITIONS</span>
        <span class="headline-tag">01 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">VAIGAI SCHOLARS SWEEP STATE VAIRAMUTHU SPEECH CONTEST WITH 1ST, 2ND & 3RD PRIZES!</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: STATE FORUM</span>
        <span>•</span>
        <span>LITERARY ASSOCIATION HONORS</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>In a historic literary sweep, students of Vaigai College of Engineering captured the 1st, 2nd, and 3rd Prizes at the prestigious State-Level Speech Competition based on the literary works of poet Kaviperarasu Vairamuthu on 01 August 2026.</p>
        <p>Competing against eloquent orators from premier engineering and arts colleges across Tamil Nadu, our scholars mesmerized adjudicators with their profound linguistic grace, philosophical depth, and passionate delivery.</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf5; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--primary); margin-bottom: 4px; text-transform: uppercase;">
            ★ State Laureates & Winning Topics
        </div>
        <div style="font-size: 0.86rem; line-height: 1.6; color: var(--text-dark);">
            • <strong>1st Prize:</strong> K. Saravanan (IV CSE) — <em>"Vairamuthu's Environmental Epics: Earth & Literature"</em><br>
            • <strong>2nd Prize:</strong> M. Priyadharshini (III ECE) — <em>"Societal Awakening in Kallikkattu Ithikasam"</em><br>
            • <strong>3rd Prize:</strong> R. Manikandan (III MECH) — <em>"Scientific Temper in Modern Tamil Poetry"</em>
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Language is the soul of thought; when engineering minds embrace poetic mastery, they become complete communicators."
    </div>
    """,
    "Vaigai Scholars Sweep Vairamuthu Contest", "Historical 1st, 2nd & 3rd Prizes in State Oratory"
)

# ==============================================================================
# SPREAD 16: PAGE 32 & PAGE 33 — GRAND TWO-PAGE PANORAMIC SPREAD!
# ==============================================================================
add_page(
    32, "spread-left",
    "TRAINING & PLACEMENT CELL (TPC)", "PANORAMIC SPREAD (LEFT)",
    """
    <div class="spread-container spread-left-half" data-spread-src="word/media/image36.jpeg" data-caption="Habits of High Performers: Dr. B. Sujatha Addressing College-Wide Academic Assembly at Dr. Abdul Kalam Auditorium">
        <img src="word/media/image36.jpeg" alt="Habits of High Performers Left Half" class="spread-img spread-img-left">
        <div class="spread-caption-overlay spread-overlay-left">
            <span class="spread-tag">★ TWO-PAGE PANORAMIC SPREAD ★</span>
            <h2 class="spread-title">HABITS OF HIGH PERFORMERS</h2>
            <p class="spread-sub">Dr. B. Sujatha Addresses the College-Wide Academic Assembly</p>
        </div>
        <button class="mobile-spread-rotate-btn" title="Rotate for Vertical Mobile Screen" type="button">
            <span>🔄 Rotate View</span>
        </button>
    </div>
    """,
    "High Performers Panorama (Left Half)", "Auditorium Centerfold Spread (Left Half)"
)

add_page(
    33, "spread-right",
    "TRAINING & PLACEMENT CELL (TPC)", "PANORAMIC SPREAD (RIGHT)",
    """
    <div class="spread-container spread-right-half" data-spread-src="word/media/image36.jpeg" data-caption="Dr. Abdul Kalam Auditorium — Vaigai College of Engineering">
        <img src="word/media/image36.jpeg" alt="Habits of High Performers Right Half" class="spread-img spread-img-right">
        <div class="spread-caption-overlay spread-overlay-right">
            <div class="spread-meta-right">DR. ABDUL KALAM AUDITORIUM • 8 JULY 2026</div>
            <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 4px;">Training & Placement Cell, Vaigai College of Engineering</div>
        </div>
        <button class="mobile-spread-rotate-btn" title="Rotate for Vertical Mobile Screen" type="button">
            <span>🔄 Rotate View</span>
        </button>
    </div>
    """,
    "High Performers Panorama (Right Half)", "Auditorium Centerfold Spread (Right Half)"
)

# ==============================================================================
# SPREAD 17: PAGE 34 & PAGE 35 — FULLSIZE POSTER & FACING STORY
# ==============================================================================
add_page(
    34, "poster",
    "TRAINING & PLACEMENT CELL (TPC)", "EXPERT TALK BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image35.jpeg" data-caption="Expert Talk on Success is a Skill: Habits of High Performers by Dr. B. Sujatha">
        <img src="word/media/image35.jpeg" alt="Success is a Skill Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ FULL BROADSIDE POSTER ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Success is a Skill Broadside Poster", "Fullsize Archival Event Poster (image35)"
)

add_page(
    35, "standard",
    "TRAINING & PLACEMENT CELL (TPC)", "EXPERT TALK",
    """
    <div class="headline-section">
        <span>TRAINING & PLACEMENT CELL</span>
        <span class="headline-tag">8 JULY 2026</span>
    </div>
    <h2 class="headline-lead">EXPERT TALK ON "SUCCESS IS A SKILL: HABITS OF HIGH PERFORMERS"</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: AUDITORIUM</span>
        <span>•</span>
        <span>SPEAKER: DR. B. SUJATHA, DEAN ACADEMICS</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Training and Placement Cell (TPC) organized a transformative Expert Talk on "Success Is a Skill: Habits of High Performers" on 8 July 2026 at the Dr. Abdul Kalam Auditorium for engineering scholars across all departments.</p>
        <p>Dr. B. Sujatha, Dean Academics, unraveled the cognitive, emotional, and behavioral habits that distinguish top engineers, demonstrating that sustained excellence is not hereditary talent, but an engineered system of daily micro-habits.</p>
    </div>

    <div class="news-image-frame" style="margin: 8px 0;" data-img-src="word/media/image37.jpeg" data-caption="Dr. B. Sujatha Delivering Keynote on Habits of High Performers">
        <img src="word/media/image37.jpeg" alt="Auditorium Session by Dr. Sujatha" class="news-img" style="max-height: 250px; object-fit: cover;">
        <div class="news-caption">
            <span>Dean Dr. B. Sujatha Mentoring Engineering Scholars</span>
            <span class="caption-tag">Auditorium Lecture</span>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ The 5 Cornerstone Habits of High Performers
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            1. <strong>Deliberate Daily Practice:</strong> Consistent coding and math problem-solving • 2. <strong>Deep Work Blocks:</strong> Distraction-free technical study • 3. <strong>Radical Accountability:</strong> Owning personal growth • 4. <strong>Curiosity:</strong> Staying ahead of AI disruption.
        </div>
    </div>
    """,
    "Success is a Skill: Story & Habits", "Dr. B. Sujatha Masterclass on High Performance"
)

# ==============================================================================
# SPREAD 18: PAGE 36 & PAGE 37 — NPTEL IIT MADRAS TOPPERS
# ==============================================================================
add_page(
    36, "standard",
    "NPTEL IIT MADRAS EXCELLENCE", "OCTOBER 2025 SESSION",
    """
    <div class="headline-section">
        <span>NPTEL IIT MADRAS ONLINE CERTIFICATION</span>
        <span class="headline-tag">OCTOBER 2025</span>
    </div>
    <h2 class="headline-lead">TOPPERS IN NPTEL ONLINE CERTIFICATION EXAM CONDUCTED BY IIT MADRAS</h2>
    <p class="headline-sub">Faculty and Students Secure Top 1% and 2% National Percentiles in Advanced Engineering Disciplines</p>

    <div class="nptel-grid">
        <div class="nptel-card">
            <img src="nptel_media/image1.png" alt="Dr. R. Sivaranjani" class="nptel-avatar">
            <div class="nptel-name">DR. R. SIVARANJANI</div>
            <div class="nptel-role">PRINCIPAL & PROF/ECE</div>
            <div class="nptel-course">Integrated Circuits & VLSI</div>
            <div class="nptel-badge">TOPPER</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image5.png" alt="Ms. R. Aswini" class="nptel-avatar">
            <div class="nptel-name">MS. R. ASWINI</div>
            <div class="nptel-role">AP / ENGLISH</div>
            <div class="nptel-course">Developing Soft Skills & Personality</div>
            <div class="nptel-badge">TOPPER (1%)</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image6.png" alt="Ms. R.J. Supriya" class="nptel-avatar">
            <div class="nptel-name">MS. R.J. SUPRIYA</div>
            <div class="nptel-role">AP / ENGLISH</div>
            <div class="nptel-course">Technical Communication</div>
            <div class="nptel-badge">TOPPER (2%)</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image8.jpeg" alt="Mr. Aravindraj" class="nptel-avatar">
            <div class="nptel-name">MR. ARAVINDRAJ</div>
            <div class="nptel-role">HOD / EEE</div>
            <div class="nptel-course">Electronic Systems Design</div>
            <div class="nptel-badge">TOPPER</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image9.png" alt="Ms. B. Karkuzhali" class="nptel-avatar">
            <div class="nptel-name">MS. B. KARKUZHALI</div>
            <div class="nptel-role">AP / CSE</div>
            <div class="nptel-course">Python for Data Science</div>
            <div class="nptel-badge">TOPPER (2%)</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image10.png" alt="Ms. S. Revathi" class="nptel-avatar">
            <div class="nptel-name">MS. S. REVATHI</div>
            <div class="nptel-role">AP / ECE</div>
            <div class="nptel-course">Microcontrollers & DSP</div>
            <div class="nptel-badge">TOPPER</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image11.png" alt="Mr. T. Vijaya Raghavan" class="nptel-avatar">
            <div class="nptel-name">MR. T. VIJAYA RAGHAVAN</div>
            <div class="nptel-role">HOD / CIVIL</div>
            <div class="nptel-course">Fluid Dynamics & Hydrology</div>
            <div class="nptel-badge">ELITE + GOLD</div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-dark);">
            ✦ NPTEL (National Programme on Technology Enhanced Learning) is a joint initiative of the IITs and IISc, offering certified coursework aligned with the highest global technical standards.
        </div>
    </div>
    """,
    "NPTEL IIT Madras Toppers (Oct 2025)", "National 1% & 2% Percentile Distinctions"
)

add_page(
    37, "standard",
    "NPTEL IIT MADRAS EXCELLENCE", "APRIL 2026 SESSION",
    """
    <div class="headline-section">
        <span>NPTEL IIT MADRAS ONLINE CERTIFICATION</span>
        <span class="headline-tag">APRIL 2026</span>
    </div>
    <h2 class="headline-lead">DR. R. SIVARANJANI LEADS AS TOPPER WITH 92% IN IIT MADRAS NPTEL EXAM</h2>
    <p class="headline-sub">Principal Sets Benchmark with Gold Medal Distinction Alongside Faculty Achievers</p>

    <div class="nptel-grid">
        <div class="nptel-card">
            <img src="nptel_media/image12.png" alt="Dr. R. Sivaranjani" class="nptel-avatar">
            <div class="nptel-name">DR. R. SIVARANJANI</div>
            <div class="nptel-role">PRINCIPAL & PROF/ECE</div>
            <div class="nptel-course">Microprocessors & Interfacing</div>
            <div class="nptel-badge">92% TOPPER (GOLD)</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image13.png" alt="Dr. B. Sujatha" class="nptel-avatar">
            <div class="nptel-name">DR. B. SUJATHA</div>
            <div class="nptel-role">DEAN ACADEMICS & PROF/ECE</div>
            <div class="nptel-course">Digital Signal Processing</div>
            <div class="nptel-badge">TOPPER (ELITE)</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image14.png" alt="Dr. M.K.V. Karthikeyan" class="nptel-avatar">
            <div class="nptel-name">DR. M.K.V. KARTHIKEYAN</div>
            <div class="nptel-role">HOD / MECH</div>
            <div class="nptel-course">Manufacturing Automation</div>
            <div class="nptel-badge">ELITE</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image15.png" alt="Mr. A. Shakil Ahmed" class="nptel-avatar">
            <div class="nptel-name">MR. A. SHAKIL AHMED</div>
            <div class="nptel-role">AP / ECE</div>
            <div class="nptel-course">Sensors & Actuators</div>
            <div class="nptel-badge">ELITE</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image16.png" alt="Ms. V. Saranya" class="nptel-avatar">
            <div class="nptel-name">MS. V. SARANYA</div>
            <div class="nptel-role">AP / EEE</div>
            <div class="nptel-course">Power Electronics & Drives</div>
            <div class="nptel-badge">ELITE</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image17.png" alt="Mr. P. Muthuanand" class="nptel-avatar">
            <div class="nptel-name">MR. P. MUTHUANAND</div>
            <div class="nptel-role">AP / CIVIL</div>
            <div class="nptel-course">Environmental Engineering</div>
            <div class="nptel-badge">ELITE</div>
        </div>

        <div class="nptel-card">
            <img src="nptel_media/image18.png" alt="Ms. M. Deepa" class="nptel-avatar">
            <div class="nptel-name">MS. M. DEEPA</div>
            <div class="nptel-role">AP / MATHS</div>
            <div class="nptel-course">Probability & Statistics</div>
            <div class="nptel-badge">ELITE</div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-dark);">
            ✦ Dr. R. Sivaranjani's phenomenal 92% Gold score in IIT Madras certification serves as an enduring source of inspiration for scholars across all five engineering branches.
        </div>
    </div>
    """,
    "NPTEL IIT Madras Toppers (Apr 2026)", "Dr. Sivaranjani Leads with 92% Gold Distinctions"
)

# ==============================================================================
# SPREAD 19: PAGE 38 & PAGE 39 — FULLSIZE POSTERS (BESANT ON-CAMPUS & SELECTIONS)
# ==============================================================================
add_page(
    38, "poster",
    "CAMPUS RECRUITMENT DRIVES", "BESANT DRIVE BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image38.jpeg" data-caption="On-Campus Recruitment Drive by Besant Technologies Pvt Ltd">
        <img src="word/media/image38.jpeg" alt="Besant Technologies On-Campus Drive Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ BESANT ON-CAMPUS DRIVE ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Besant Recruitment Drive Poster", "Fullsize Archival Drive Poster (image38)"
)

add_page(
    39, "poster",
    "CAMPUS RECRUITMENT DRIVES", "BESANT SELECTIONS BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image39.jpeg" data-caption="16 Students Selected for Besant Job-Ready Internship & Placement Program (JRIP)">
        <img src="word/media/image39.jpeg" alt="16 Students Selected for Besant JRIP Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ 16 STUDENTS SELECTED BROADSIDE ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Besant 16 Selected Students Poster", "Fullsize Archival Selection Poster (image39)"
)

# ==============================================================================
# SPREAD 20: PAGE 40 & PAGE 41 — BESANT STORY & INOVONZ FULLSIZE POSTER
# ==============================================================================
add_page(
    40, "standard",
    "CAMPUS RECRUITMENT DRIVES", "BESANT SELECTION REPORT",
    """
    <div class="headline-section">
        <span>TRAINING AND PLACEMENT CELL</span>
        <span class="headline-tag">10 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">16 STUDENTS SELECTED FOR BESANT JOB-READY INTERNSHIP & PLACEMENT PROGRAM</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: PLACEMENT CELL</span>
        <span>•</span>
        <span>CORPORATE PARTNER: BESANT TECHNOLOGIES</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Training and Placement Cell (TPC) conducted a highly successful On-Campus Recruitment Drive on 10 August 2026 for final-year CSE and ECE students. Besant Technologies Pvt Ltd conducted comprehensive assessment procedures spanning quantitative aptitude, coding evaluation, and executive technical interviews.</p>
        <p>Vaigai College of Engineering proudly announces that 16 outstanding students from CSE, ECE, and EEE have been officially selected for the prestigious Job-Ready Internship & Placement Program (JRIP).</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf8; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ Corporate Recruitment Highlights
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            • 16 Selected engineering scholars inducted into advanced software development streams<br>
            • Corporate pre-placement internships preceding full-time software engineering roles<br>
            • Organized by Dr. R. Sivaranjani, Principal & Prof/ECE, and Ms. R.J. Supriya, AP/ENG
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Placement success is the ultimate testimony to our practical, industry-aligned engineering pedagogy."
    </div>
    """,
    "Besant Placement Drive Story", "16 Students Selected for JRIP Program Report"
)

add_page(
    41, "poster",
    "POOLED CAMPUS RECRUITMENT", "INOVONZ DRIVE BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image42.jpeg" data-caption="Pooled Campus Recruitment Drive Jointly with Inovonz Engineerics">
        <img src="word/media/image42.jpeg" alt="Inovonz Engineerics Pooled Campus Drive Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ INOVONZ POOLED DRIVE BROADSIDE ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Inovonz Pooled Drive Poster", "Fullsize Archival Drive Poster (image42)"
)

# ==============================================================================
# SPREAD 21: PAGE 42 & PAGE 43 — INOVONZ STORY & NEWTRA DRIVE POSTER
# ==============================================================================
add_page(
    42, "standard",
    "POOLED CAMPUS RECRUITMENT", "CORE ELECTRICAL DRIVE",
    """
    <div class="headline-section">
        <span>TRAINING AND PLACEMENT CELL</span>
        <span class="headline-tag">18 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">POOLED CAMPUS RECRUITMENT DRIVE JOINTLY WITH INOVONZ ENGINEERICS</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: TECHNICAL HALL</span>
        <span>•</span>
        <span>IV YEAR EEE STUDENTS</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>A high-impact Pooled Campus Recruitment Drive was organized by the Training and Placement Cell (TPC) jointly with Inovonz Engineerics on 18 August 2026 for IV year Electrical and Electronics Engineering students.</p>
        <p>The drive provided students with an intensive common recruitment platform, testing circuit analysis, programmable logic controllers, industrial drive systems, and power grid automation concepts.</p>
    </div>

    <div class="image-gallery-pair" style="margin: 8px 0;">
        <div class="news-image-frame" data-img-src="word/media/image40.jpeg" data-caption="Inovonz Technical Assessment Briefing">
            <img src="word/media/image40.jpeg" alt="Inovonz Recruitment Briefing" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Inovonz Corporate Briefing</span></div>
        </div>
        <div class="news-image-frame" data-img-src="word/media/image41.jpeg" data-caption="Candidates Undergoing Written Technical Screening">
            <img src="word/media/image41.jpeg" alt="Written Screening Session" class="news-img" style="max-height: 220px; object-fit: cover;">
            <div class="news-caption"><span>Technical Screening Examination</span></div>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Placement Coordination
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Organized under the dedicated leadership of <strong>Ms. V. Saranya</strong>, Assistant Professor of EEE, bolstering student competitiveness in core industrial engineering sectors.
        </div>
    </div>
    """,
    "Inovonz Pooled Campus Drive Story", "Industrial Automation Core Technical Screening"
)

add_page(
    43, "poster",
    "OFF-CAMPUS RECRUITMENT", "NEWTRA DRIVE BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image43.jpeg" data-caption="Off-Campus Recruitment Drive by Newrta Solutions Pvt Ltd">
        <img src="word/media/image43.jpeg" alt="Newrta Solutions Off-Campus Drive Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ NEWTRA OFF-CAMPUS DRIVE ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Newrta Off-Campus Drive Poster", "Fullsize Archival Drive Poster (image43)"
)

# ==============================================================================
# SPREAD 22: PAGE 44 & PAGE 45 — MAADHESH STAR PLACEMENT & STORY
# ==============================================================================
add_page(
    44, "poster",
    "OFF-CAMPUS RECRUITMENT", "STAR PLACEMENT BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image44.jpeg" data-caption="Mr. S. Maadhesh Placed as Software Developer at Newrta Solutions">
        <img src="word/media/image44.jpeg" alt="Mr. S. Maadhesh Star Placement Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ STAR SOFTWARE PLACEMENT ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "Mr. S. Maadhesh Star Placement Poster", "Fullsize Archival Star Placement Poster (image44)"
)

add_page(
    45, "standard",
    "OFF-CAMPUS RECRUITMENT", "STAR PLACEMENT REPORT",
    """
    <div class="headline-section">
        <span>TRAINING AND PLACEMENT CELL</span>
        <span class="headline-tag">19 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">MR. S. MAADHESH PLACED AS SOFTWARE DEVELOPER AT NEWTRA SOLUTIONS</h2>
    <div class="byline-bar">
        <span class="byline-date">DATE: 19 AUGUST 2026</span>
        <span>•</span>
        <span>ROLE: SOFTWARE DEVELOPER</span>
        <span>•</span>
        <span>IV YEAR CSE</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>An Off-Campus Recruitment Drive was coordinated by the Training and Placement Cell on 19 August 2026 for IV year CSE students. Newrta Solutions Pvt Ltd conducted rigorous technical assessments, live coding challenges, and system architecture rounds.</p>
        <p>Vaigai College of Engineering proudly announces that Mr. S. Maadhesh from Final Year CSE has triumphed through the multi-stage evaluation, securing a coveted appointment as Software Developer at Newrta Solutions.</p>
    </div>

    <div class="news-image-frame" style="margin: 8px 0;" data-img-src="word/media/image45.jpeg" data-caption="Newrta Solutions Placement Felicitations">
        <img src="word/media/image45.jpeg" alt="Newrta Solutions Placement Ceremony" class="news-img" style="max-height: 250px; object-fit: cover;">
        <div class="news-caption">
            <span>Mr. S. Maadhesh Congratulated by Management & Faculty</span>
            <span class="caption-tag">Placement Cell</span>
        </div>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Drive Coordinators
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            Orchestrated by <strong>Dr. R. Sivaranjani</strong>, Principal & Professor/ECE, and <strong>Ms. R.J. Supriya</strong>, Assistant Professor of English, reaffirming our commitment to premier IT career placements.
        </div>
    </div>
    """,
    "Newrta Software Developer Placement Story", "Mr. S. Maadhesh Career Triumph Report"
)

# ==============================================================================
# SPREAD 23: PAGE 46 & PAGE 47 — TACT BOOTCAMP FULLSIZE POSTER & STORY
# ==============================================================================
add_page(
    46, "poster",
    "TRAINING & PLACEMENT CELL (TPC)", "TACT BOOTCAMP BROADSIDE",
    """
    <div class="poster-full-frame" data-img-src="word/media/image46.jpeg" data-caption="TACT - Level 1: Intensive Placement Recruitment Competency Bootcamp Poster">
        <img src="word/media/image46.jpeg" alt="TACT - Level 1 Poster" class="poster-full-img">
        <div class="poster-hover-banner">
            <span class="poster-badge">★ TACT BOOTCAMP BROADSIDE ★</span>
            <span class="poster-action-hint">🔍 Tap to inspect high-res</span>
        </div>
    </div>
    """,
    "TACT Level 1 Bootcamp Poster", "Fullsize Archival Bootcamp Poster (image46)"
)

add_page(
    47, "standard",
    "TRAINING & PLACEMENT CELL (TPC)", "TACT LEVEL 1 BOOTCAMP",
    """
    <div class="headline-section">
        <span>TRAINING AND PLACEMENT CELL</span>
        <span class="headline-tag">20 AUGUST 2026</span>
    </div>
    <h2 class="headline-lead">TACT – LEVEL 1: INTENSIVE PLACEMENT RECRUITMENT COMPETENCY BOOTCAMP</h2>
    <div class="byline-bar">
        <span class="byline-date">VENUE: AUDITORIUM</span>
        <span>•</span>
        <span>FINAL-YEAR DELEGATES</span>
        <span>•</span>
        <span>TPC INITIATIVE</span>
    </div>

    <div class="editorial-cols dropcap">
        <p>The Training and Placement Cell (TPC) launched TACT – Level 1 on 20 August 2026 for IV year engineering students across all five disciplines. Dr. R. Sivaranjani, Principal (i/c), along with the Heads of Departments, mentored and inaugurated the intensive competency sprint.</p>
        <p>The bootcamp drilled scholars through competitive quantitative reasoning, logical deduction, situational HR challenges, verbal speed-reading, and corporate etiquette, eliminating interview anxieties and priming students for Fortune 500 recruitment filters.</p>
    </div>

    <div class="editorial-card" style="margin: 8px 0; background: #fffcf8; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.88rem; font-weight: bold; color: var(--accent); margin-bottom: 4px; text-transform: uppercase;">
            ★ TACT Level 1 Competency Modules
        </div>
        <div style="font-size: 0.86rem; line-height: 1.55; color: var(--text-dark);">
            1. Quantitative Aptitude & Speed Mathematics • 2. Logical Puzzles & Data Interpretation • 3. Corporate Verbal Nuance & Resume Structuring • 4. Mock Technical & Behavioral Panels.
        </div>
    </div>

    <div class="pull-quote" style="margin: 8px 0;">
        "Competency is where preparation meets opportunity. TACT equips every student with the confidence to conquer corporate evaluations."
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-muted);">
            Programme coordinated by <strong>Dr. R. Sivaranjani</strong>, Principal & Professor/ECE, and <strong>Ms. R.J. Supriya</strong>, Assistant Professor of English.
        </div>
    </div>
    """,
    "TACT Level 1 Intensive Bootcamp Story", "Placement Competency & Interview Preparation Report"
)

# ==============================================================================
# SPREAD 24: PAGE 48 & PAGE 49 — FACULTY SCHOLARSHIP (FDP & RESEARCH)
# ==============================================================================
add_page(
    48, "standard",
    "FACULTY DEVELOPMENT & RESEARCH", "SCHOLARLY ADVANCEMENT",
    """
    <div class="headline-section">
        <span>FACULTY ADVANCEMENT</span>
        <span class="headline-tag">JULY – AUG 2026</span>
    </div>
    <h2 class="headline-lead">16 FACULTY DEVELOPMENT PROGRAMMES & ADVANCED CERTIFICATIONS</h2>
    <p class="headline-sub">Faculty Members Complete Intensive Pedagogical and Emerging Technology Upskilling Across Premier Institutions</p>

    <div class="news-table-wrapper" style="overflow-x: auto; margin: 8px 0;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.82rem; line-height: 1.5; text-align: left;">
            <thead>
                <tr style="background: rgba(212, 175, 55, 0.15); border-bottom: 2px solid var(--accent); color: var(--primary);">
                    <th style="padding: 5px 6px;">Faculty Member</th>
                    <th style="padding: 5px 6px;">Dept</th>
                    <th style="padding: 5px 6px;">Programme & Certification</th>
                    <th style="padding: 5px 6px;">Host Institution</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. R. Sivaranjani</strong></td>
                    <td style="padding: 4px 6px;">ECE</td>
                    <td style="padding: 4px 6px;">AI in Microelectronics</td>
                    <td style="padding: 4px 6px;">IIT Madras NPTEL</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. B. Sujatha</strong></td>
                    <td style="padding: 4px 6px;">ECE</td>
                    <td style="padding: 4px 6px;">Digital Signal Processing</td>
                    <td style="padding: 4px 6px;">IIT Kharagpur</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. M.K.V. Karthikeyan</strong></td>
                    <td style="padding: 4px 6px;">MECH</td>
                    <td style="padding: 4px 6px;">Smart Materials & Robotics</td>
                    <td style="padding: 4px 6px;">NIT Trichy</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Mr. T. Vijaya Raghavan</strong></td>
                    <td style="padding: 4px 6px;">CIVIL</td>
                    <td style="padding: 4px 6px;">GIS & Remote Sensing</td>
                    <td style="padding: 4px 6px;">Anna University</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Mr. Aravindraj</strong></td>
                    <td style="padding: 4px 6px;">EEE</td>
                    <td style="padding: 4px 6px;">Electric Vehicle Powertrains</td>
                    <td style="padding: 4px 6px;">IIT Delhi</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Ms. B. Karkuzhali</strong></td>
                    <td style="padding: 4px 6px;">CSE</td>
                    <td style="padding: 4px 6px;">Deep Learning & NLP</td>
                    <td style="padding: 4px 6px;">IIT Roorkee</td>
                </tr>
                <tr>
                    <td style="padding: 4px 6px;"><strong>Ms. R. Aswini</strong></td>
                    <td style="padding: 4px 6px;">ENG</td>
                    <td style="padding: 4px 6px;">Applied Linguistics & Pedagogy</td>
                    <td style="padding: 4px 6px;">IIT Madras</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-dark);">
            ✦ Continuous Professional Development (CPD) ensures our educators remain abreast of international technological transformations, directly enriching student laboratory instruction.
        </div>
    </div>
    """,
    "16 Faculty Development Programmes", "Scholarly Certifications Across Premier Institutions"
)

add_page(
    49, "standard",
    "FACULTY DEVELOPMENT & RESEARCH", "SCHOLARLY CONTRIBUTIONS",
    """
    <div class="headline-section">
        <span>RESEARCH CONTRIBUTIONS</span>
        <span class="headline-tag">PEER-REVIEWED</span>
    </div>
    <h2 class="headline-lead">7 GROUNDBREAKING PEER-REVIEWED RESEARCH PAPERS PUBLISHED IN PREMIER JOURNALS</h2>
    <p class="headline-sub">Faculty Publications in High-Impact Scopus and Web of Science Indexed International Journals</p>

    <div class="news-table-wrapper" style="overflow-x: auto; margin: 8px 0;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.82rem; line-height: 1.5; text-align: left;">
            <thead>
                <tr style="background: rgba(212, 175, 55, 0.15); border-bottom: 2px solid var(--accent); color: var(--primary);">
                    <th style="padding: 5px 6px;">Lead Author</th>
                    <th style="padding: 5px 6px;">Title of Research Investigation</th>
                    <th style="padding: 5px 6px;">Journal & Indexing</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. R. Sivaranjani</strong> et al.</td>
                    <td style="padding: 4px 6px;">Low-Power VLSI Architecture for Real-Time Biomedical Signal Telemetry</td>
                    <td style="padding: 4px 6px;"><em>IEEE Transactions on CAS</em> (Scopus / WoS)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. B. Sujatha</strong> et al.</td>
                    <td style="padding: 4px 6px;">Adaptive Wavelet De-noising in High-Frequency Communication Channels</td>
                    <td style="padding: 4px 6px;"><em>Springer Wireless Networks</em> (Scopus)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Dr. M.K.V. Karthikeyan</strong> et al.</td>
                    <td style="padding: 4px 6px;">Thermal Efficiency Optimization in Parabolic Concentrators Using Hybrid Nanofluids</td>
                    <td style="padding: 4px 6px;"><em>Elsevier Solar Energy</em> (SCI, IF: 6.8)</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--paper-border);">
                    <td style="padding: 4px 6px;"><strong>Mr. T. Vijaya Raghavan</strong> et al.</td>
                    <td style="padding: 4px 6px;">Durability Assessment of Geopolymer Concrete Incorporating Industrial Slag</td>
                    <td style="padding: 4px 6px;"><em>Construction & Building Materials</em></td>
                </tr>
                <tr>
                    <td style="padding: 4px 6px;"><strong>Mr. Aravindraj</strong> et al.</td>
                    <td style="padding: 4px 6px;">Sensorless Speed Control of Permanent Magnet Synchronous Motors</td>
                    <td style="padding: 4px 6px;"><em>IET Electric Power Applications</em></td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="editorial-card" style="margin-top: 6px;">
        <div style="font-size: 0.86rem; color: var(--text-dark);">
            ✦ Our faculty's research initiatives address real-world industrial and environmental challenges, providing undergraduates with live opportunities to collaborate on funded investigatory publications.
        </div>
    </div>
    """,
    "7 High-Impact Research Papers", "Peer-Reviewed Scopus & SCI Indexed Publications"
)

# ==============================================================================
# SPREAD 25: PAGE 50 & PAGE 51 — COLOPHON & INSTITUTIONAL VISION BROADSIDE
# ==============================================================================
add_page(
    50, "standard",
    "VAIGAI COLLEGE OF ENGINEERING", "COLOPHON & ACKNOWLEDGEMENTS",
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <div class="splash-logo-wrapper" style="width: 100px; height: 75px; margin: 0 auto 6px;">
            <img src="logo.png" alt="Vaigai Crest" class="splash-logo">
        </div>
        <h2 style="font-family: var(--font-display); font-size: 1.35rem; letter-spacing: 2px; color: var(--accent);">
            VAIGAI'S IKIGAI
        </h2>
        <div style="font-family: var(--font-serif); font-style: italic; font-size: 0.95rem; color: var(--text-muted);">
            Where Purpose Meets Possibility
        </div>
    </div>

    <div class="editorial-card" style="font-size: 0.86rem; line-height: 1.65; margin-bottom: 10px;">
        <div style="font-family: var(--font-display); font-size: 0.92rem; font-weight: bold; color: var(--primary); margin-bottom: 4px; text-transform: uppercase;">
            ✦ Institutional Acknowledgement
        </div>
        <p>We extend our deepest gratitude to the Management Trustees of Vaigai Educational Trust (VET), Dr. R. Sivaranjani (Principal i/c), Dr. B. Sujatha (Dean Academics), Heads of all Engineering Departments, faculty coordinators, student office bearers, and our valued corporate partners (Besant Technologies, Caliber Virtual Technologies, Inovonz Engineerics, Newrta Solutions, Meenakshi Mission Hospital, TNSACS) for their steadfast support.</p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.84rem; margin-bottom: 10px;">
        <div class="editorial-card" style="margin: 0; padding: 12px;">
            <strong style="color: var(--accent);">Campus Coordinates:</strong><br>
            Vaigai College of Engineering<br>
            15-Acre Serene Green Campus,<br>
            Madurai – 625 106, Tamil Nadu.
        </div>
        <div class="editorial-card" style="margin: 0; padding: 12px;">
            <strong style="color: var(--accent);">Statutory Approvals:</strong><br>
            Approved by AICTE, New Delhi<br>
            Affiliated to Anna University, Chennai<br>
            Bimonthly Newsletter Vol. 01 Issue 01
        </div>
    </div>

    <div class="pull-quote" style="margin: 10px 0; font-size: 0.98rem;">
        "Education is not merely the accumulation of technical data, but the awakening of purpose, character, and humanity."
    </div>
    """,
    "Institutional Colophon & Acknowledgements", "Editorial Board Note & College Coordinates"
)

add_page(
    51, "standard",
    "VAIGAI COLLEGE OF ENGINEERING", "INSTITUTIONAL VISION BROADSIDE",
    """
    <div style="text-align: center; margin: 15px 0 10px;">
        <div class="splash-logo-wrapper" style="width: 120px; height: 85px; margin: 0 auto 8px;">
            <img src="logo.png" alt="Vaigai Crest" class="splash-logo">
        </div>
        <h2 style="font-family: var(--font-display); font-size: 1.4rem; letter-spacing: 2px; color: var(--accent); margin-bottom: 4px;">
            VAIGAI COLLEGE OF ENGINEERING
        </h2>
        <p style="font-family: var(--font-serif); font-size: 0.98rem; font-style: italic; color: var(--text-muted);">
            Nurturing Socially Responsible Global Engineers Since 2012
        </p>
    </div>

    <div class="editorial-card" style="margin: 12px 0; background: #fffcf8; border-color: var(--accent);">
        <div style="font-family: var(--font-display); font-size: 0.92rem; font-weight: bold; color: var(--accent); margin-bottom: 6px; text-transform: uppercase;">
            ★ Our Institutional Mission
        </div>
        <p style="font-size: 0.88rem; line-height: 1.65; color: var(--text-dark);">
            To impart high-quality technical education, promote state-of-the-art research, foster ethical leadership, and cultivate an enduring spirit of social responsibility among young minds from diverse backgrounds.
        </p>
    </div>

    <div class="editorial-card" style="margin: 12px 0;">
        <div style="font-family: var(--font-display); font-size: 0.92rem; font-weight: bold; color: var(--primary); margin-bottom: 6px; text-transform: uppercase;">
            ★ Core Institutional Values
        </div>
        <div style="font-size: 0.88rem; line-height: 1.65; color: var(--text-dark);">
            • <strong>Academic Integrity:</strong> Uncompromising dedication to scientific rigor and ethics.<br>
            • <strong>Student Centricity:</strong> Empowering individual curiosity, creativity, and career goals.<br>
            • <strong>Societal Impact:</strong> Applying engineering solutions to elevate community welfare.
        </div>
    </div>

    <div style="text-align: center; margin-top: 15px; font-size: 0.86rem; color: var(--text-muted);">
        Madurai – 625 106, Tamil Nadu • www.vaigaicollege.com
    </div>
    """,
    "Institutional Vision Broadside", "Excellence in Engineering Education & Societal Transformation"
)

# ==============================================================================
# PAGE 52: BACK COVER
# ==============================================================================
add_page(
    52, "cover-back",
    "VAIGAI COLLEGE OF ENGINEERING", "BACK COVER",
    """
    <div style="text-align: center; margin: 30px 0 20px;">
        <div class="splash-logo-wrapper" style="width: 150px; height: 110px; margin: 0 auto 16px;">
            <img src="logo.png" alt="Vaigai College Seal" class="splash-logo">
        </div>
        <h1 style="font-family: var(--font-display); font-size: 2.1rem; letter-spacing: 3px; color: var(--accent-light);">
            VAIGAI'S IKIGAI
        </h1>
        <p style="font-family: var(--font-serif); font-style: italic; font-size: 1.15rem; color: #cbd5e1; margin-top: 6px;">
            Where Purpose Meets Possibility
        </p>
    </div>

    <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.35); border-radius: 6px; padding: 24px; margin: 24px 0; font-size: 0.92rem; line-height: 1.7; text-align: center;">
        <div style="font-family: var(--font-display); font-size: 1rem; font-weight: bold; color: var(--accent-light); margin-bottom: 10px; letter-spacing: 1.5px; text-transform: uppercase;">
            ✦ Bimonthly Gazette of Vaigai College of Engineering ✦
        </div>
        <p style="color: #e2e8f0;">
            Bringing together the vibrant academic achievements, state honors, technical breakthroughs, student leadership milestones, and corporate placements of our institution.
        </p>
    </div>

    <div style="margin-top: auto; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 16px; font-size: 0.84rem; color: #94a3b8;">
        <div>© 2026 Vaigai College of Engineering, Madurai. All Rights Reserved.</div>
        <div style="margin-top: 6px; color: var(--accent-light);">www.vaigaicollege.com • editorial@vaigaicollege.com</div>
    </div>
    """,
    "Back Cover — VAIGAI'S IKIGAI", "Where Purpose Meets Possibility • Volume 01 Issue 01"
)

print(f"Constructed all {len(pages)} pages successfully.")

# Build HTML for Flipbook pages
flipbook_pages_html = ""
for num in sorted(pages.keys()):
    p = pages[num]
    density = "hard" if (num == 1 or num == len(pages)) else "soft"
    
    extra_class = ""
    if p["type"] == "cover-front":
        extra_class = "cover-front"
    elif p["type"] == "cover-back":
        extra_class = "cover-back"
    elif p["type"] == "poster":
        extra_class = "poster-page"
    elif p["type"] == "spread-left":
        extra_class = "spread-page spread-left"
    elif p["type"] == "spread-right":
        extra_class = "spread-page spread-right"
        
    inner_class = "page-inner"
    if p["type"] == "poster":
        inner_class = "page-inner poster-page-inner"
    elif p["type"] in ("spread-left", "spread-right"):
        inner_class = "page-inner spread-page-inner"
        
    # Headers & footers
    header_block = ""
    if p["type"] not in ("cover-front", "spread-left", "spread-right"):
        header_block = f"""
              <div class="page-header">
                <span class="page-header-title">{p['header_title']}</span>
                <span>{p['header_tag']}</span>
              </div>
        """
        
    footer_block = ""
    if p["type"] not in ("spread-left", "spread-right"):
        footer_block = f"""
              <div class="page-footer">
                <span>VAIGAI'S IKIGAI GAZETTE</span>
                <span class="page-num">PAGE {num}</span>
              </div>
        """

    flipbook_pages_html += f"""
          <!-- PAGE {num}: {p['toc_title']} -->
          <div class="page {extra_class}" id="p{num}" data-density="{density}" data-page="{num}">
            <div class="page-watermark">IKIGAI</div>
            <div class="{inner_class}">
              {header_block}
              <div class="page-content">
                {p['content_html']}
              </div>
              {footer_block}
            </div>
          </div>
    """

# Build Table of Contents HTML
toc_html = ""
for num in sorted(pages.keys()):
    p = pages[num]
    toc_html += f"""
      <li class="toc-item" data-page="{num}">
        <div class="toc-item-text">
          <span style="font-weight: 600;">{p['toc_title']}</span>
          <span class="toc-item-sub">{p['toc_sub']}</span>
        </div>
        <span class="toc-item-badge">P.{num}</span>
      </li>
    """

# Build Gazette mode articles HTML
gazette_html = ""
for num in sorted(pages.keys()):
    p = pages[num]
    gazette_html += f"""
        <article class="gazette-section" id="gazette-p{num}" data-page="{num}">
          <div style="font-family: var(--font-sans); font-size: 0.8rem; text-transform: uppercase; color: var(--accent); font-weight: bold; margin-bottom: 6px;">
            VAIGAI COLLEGE OF ENGINEERING • PAGE {num}
          </div>
          {p['content_html']}
          <div style="margin-top: 14px; text-align: right;">
            <button class="gazette-jump-btn" data-page="{num}" style="background: rgba(212,175,55,0.12); border: 1px solid var(--accent); color: var(--accent); padding: 5px 12px; border-radius: 3px; font-size: 0.78rem; cursor: pointer;">
              Open in 3D Flipbook 📖
            </button>
          </div>
        </article>
    """

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>VAIGAI'S IKIGAI — The Official Bimonthly Gazette of Vaigai College of Engineering</title>
  
  <!-- Typography Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Inter:wght@400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="styles.css">
</head>
<body data-theme="newsprint">

  <!-- Slim Top Navigation Bar -->
  <header class="top-navbar">
    <div class="nav-brand" id="brand-link" title="Return to Cover Page">
      <div class="nav-logo-box">
        <img src="logo.png" alt="Vaigai Logo" class="nav-logo">
      </div>
      <div style="display: flex; flex-direction: column;">
        <span class="nav-title">VAIGAI'S IKIGAI</span>
        <span class="nav-subtitle">Vaigai College of Engineering</span>
      </div>
    </div>

    <div class="nav-meta">
      <span class="nav-edition-badge">VOL. 01 • NO. 01</span>
      <span>JULY – AUGUST 2026</span>
      <span>🌤️ Madurai 31°C</span>
    </div>

    <div class="nav-controls">
      <!-- Mode Toggle -->
      <button id="btn-mode-toggle" class="ctrl-btn" title="Toggle Reading Mode">
        <span>📰</span>
        <span class="btn-label" id="mode-label">Gazette View</span>
      </button>

      <!-- TOC Drawer Button -->
      <button id="btn-toc" class="ctrl-btn" title="Table of Contents">
        <span>📑</span>
        <span class="btn-label">Contents</span>
      </button>

      <!-- Audio Mute Button -->
      <button id="btn-audio" class="ctrl-btn" title="Toggle Page Turn Sound">
        <span id="audio-icon">🔊</span>
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
        <span>⛶</span>
      </button>
    </div>
  </header>

  <!-- Main Viewport Wrapper -->
  <main class="main-wrapper">

    <!-- Screen-Filling Flipbook View Container -->
    <div id="flipbook-container">
      <button id="btn-prev-page" class="flip-arrow prev" title="Previous Page" aria-label="Previous Page">‹</button>
      <button id="btn-next-page" class="flip-arrow next" title="Next Page" aria-label="Next Page">›</button>

      <div class="flipbook-viewport" id="flipbook-viewport">
        <div id="flipbook" class="st-flipbook">
{flipbook_pages_html}
        </div>
      </div>
    </div>

    <!-- Scrollable Gazette Mode (Alternative Editorial View) -->
    <div id="gazette-container">
      <div class="gazette-search-bar">
        <span style="font-size: 1.1rem; color: var(--text-muted);">🔍</span>
        <input type="text" id="gazette-search-input" class="gazette-search-input" placeholder="Search articles, faculties, placements, departments, or events...">
      </div>

      <div style="border-bottom: 4px double var(--text-headline); padding-bottom: 12px; margin-bottom: 24px; text-align: center;">
        <img src="word/media/image1.jpeg" alt="Vaigai's Ikigai" style="max-height: 75px; width: auto; max-width: 100%;">
        <h1 style="font-family: var(--font-display); font-size: 2.3rem; letter-spacing: 3px; margin: 4px 0;">VAIGAI'S IKIGAI</h1>
        <p style="font-family: var(--font-serif); font-style: italic; color: var(--accent);">The Official Bimonthly Publication of Vaigai College of Engineering, Madurai</p>
      </div>

      <div id="gazette-articles">
{gazette_html}
      </div>
    </div>

  </main>

  <!-- Slim Bottom Floating Dock -->
  <footer class="bottom-dock">
    <div class="dock-left">
      <button id="btn-dock-toc" class="ctrl-btn" title="Table of Contents">
        <span>📑</span>
        <span class="btn-label">Index</span>
      </button>
      <button id="btn-toggle-thumbs" class="ctrl-btn" title="Page Thumbnails">
        <span>🪟</span>
        <span class="btn-label">Pages</span>
      </button>
    </div>

    <div class="dock-center">
      <button id="btn-dock-prev" class="dock-nav-btn" title="Previous Page">‹</button>
      <div class="page-indicator-box">
        <span id="page-indicator" class="page-indicator-text">Page 1 of {len(pages)}</span>
      </div>
      <button id="btn-dock-next" class="dock-nav-btn" title="Next Page">›</button>
      <input type="range" id="page-scrubber" class="page-scrubber" min="1" max="{len(pages)}" value="1" title="Scrub pages">
    </div>

    <div class="dock-right">
      <div class="zoom-controls">
        <button id="btn-zoom-out" class="ctrl-btn" title="Zoom Out">−</button>
        <span id="zoom-level" class="zoom-text">100%</span>
        <button id="btn-zoom-in" class="ctrl-btn" title="Zoom In">+</button>
        <button id="btn-zoom-reset" class="ctrl-btn" title="Reset Zoom">↺</button>
      </div>
    </div>
  </footer>

  <!-- Thumbnail Bar Drawer -->
  <div class="thumb-bar-drawer" id="thumb-bar-drawer">
    <div class="thumb-track" id="thumb-track"></div>
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
{toc_html}
    </ul>
  </aside>

  <!-- Modal Backdrop -->
  <div class="modal-backdrop" id="modal-backdrop"></div>

  <!-- Fullscreen Poster & Event Broadside Viewer -->
  <div class="lightbox-modal" id="lightbox-modal" data-view="poster">
    <!-- Top Floating Navigation & Action Bar -->
    <div class="lightbox-top-bar">
      <div class="lightbox-event-tag" id="lightbox-event-tag">
        <span class="lightbox-tag-dot"></span>
        <span id="lightbox-tag-text">VAIGAI ARCHIVAL POSTER</span>
      </div>
      <div class="lightbox-actions">
        <button id="lightbox-rotate-btn" class="lightbox-btn" title="Rotate Image 90° for Mobile Screen">
          <span class="btn-icon">🔄</span>
          <span class="btn-text">Rotate</span>
        </button>
        <button id="lightbox-toggle-info" class="lightbox-btn info-toggle" title="Toggle Event Details & Story">
          <span class="btn-icon">ℹ️</span>
          <span class="btn-text" id="lightbox-info-btn-label">Event Details</span>
        </button>
        <button id="lightbox-jump-page" class="lightbox-btn jump-btn" title="Jump to Page in Publication">
          <span class="btn-icon">📖</span>
          <span class="btn-text">View in Page</span>
        </button>
        <button class="lightbox-close" id="lightbox-close" title="Close Fullscreen (Esc)">×</button>
      </div>
    </div>

    <!-- Main Viewport Area: Split/Overlay between Scaled Poster and Event Details -->
    <div class="lightbox-content-container" id="lightbox-content-container">
      <!-- Scaled Poster Frame (Scaled for Fullscreen by default) -->
      <div class="lightbox-poster-area" id="lightbox-poster-area">
        <div class="lightbox-img-frame" id="lightbox-img-frame" title="Click to toggle Event Details">
          <img src="" alt="" id="lightbox-img" class="lightbox-img">
        </div>
        <div class="lightbox-caption-bar" id="lightbox-caption-bar">
          <p id="lightbox-caption" class="lightbox-caption"></p>
          <button class="lightbox-caption-hint" id="lightbox-caption-hint" type="button">
            <span>ℹ️ Click to read the full event story & details</span>
            <span>▾</span>
          </button>
        </div>
      </div>

      <!-- Semi-Transparent Frosted Editorial Story Panel -->
      <div class="lightbox-info-panel" id="lightbox-info-panel">
        <div class="lightbox-info-header">
          <span class="info-kicker" id="lightbox-info-dept">DEPARTMENT EVENT</span>
          <span class="info-date-badge" id="lightbox-info-date">JULY – AUGUST 2026</span>
        </div>
        <h2 class="lightbox-info-headline" id="lightbox-info-title">Event Title</h2>
        <div class="lightbox-info-byline" id="lightbox-info-byline"></div>
        <div class="lightbox-info-body" id="lightbox-info-body"></div>
      </div>
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
    f.write(full_html)

print("Generated index.html successfully with 52 pages!")

