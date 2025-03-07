import smtplib
import streamlit as st
from email.message import EmailMessage
import json
import os
import plotly.graph_objects as go
# Set Page Config
st.set_page_config(page_title="My Digital Footprint", page_icon="📚", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "Projects", "Skills & Achievements", "Profile","Testimonials","Timeline", "Contact"]
choice = st.sidebar.radio("Go to", pages)


# Home Section
if choice == "Home":
    # Add custom CSS animations and styles
    st.markdown("""
    <style>
    /* General Fade-in Animation */
    .fade-in {
        animation: fadeIn 2s ease-out;
    }

    /* Slide In from Left */
    .slide-in-left {
        animation: slideInLeft 1.5s ease-out;
    }

    /* Slide In from Right */
    .slide-in-right {
        animation: slideInRight 1.5s ease-out;
    }

    /* Keyframes for the animations */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    @keyframes slideInLeft {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }

    @keyframes slideInRight {
        0% { transform: translateX(100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }

    /* Styling for text */
    .header, .main-title, .subheader {
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: Left;  /* Ensure all titles stay centered */
        transition: transform 0.3s ease;  /* Add transition for movement */
    }

    .header:hover, .main-title:hover, .subheader:hover {
        transform: translateY(-10px);  /* Move the heading up when hovered */
    }

    /* Styling for links without underline */
    .details-link {
        color: #007bff;
        font-size: 1.1em;
        font-weight: bold;
        transition: color 0.3s;
    }
    .details-link:hover {
        color: #0056b3;
        text-decoration: none;
    }

    /* Icon Styling */
    .icon {
        margin-right: 10px;
        font-size: 1.5em;
        transition: transform 0.3s ease;
    }
    .icon:hover {
        transform: scale(1.1);
    }

    /* Container styling */
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-top: 20px;
    }

    .container p {
        margin: 10px 0;
        font-size: 1.1em;
        color: #444;
    }

    /* Styling for the separator */
    .separator {
        margin: 30px 0;
        border-top: 2px solid #ddd;
        width: 100%;
    }

    /* Styling for the personal details without labels */
    .details {
        color: #007bff !important;
        font-size: 1.1em !important;
        font-weight: bold !important;
        transition: color 0.3s !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # Create a two-column layout for image and personal details
    col1, col2 = st.columns([1, 3])  # First column for the image, second for details
    
    # Display the image with slide-in effect from left
    with col1:
        st.markdown('<div class="slide-in-left">', unsafe_allow_html=True)
        st.image("person.jpg", width=200)  # Replace with your actual image file
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display personal details with slide-in effect from right
    with col2:
        st.markdown('<div class="slide-in-right">', unsafe_allow_html=True)
        st.markdown("<h1 class='header fade-in'>Adut Gai Chol Chol</h1>", unsafe_allow_html=True)
        
        # Display details with icons
        st.markdown("""
        <div class="container fade-in">
            <p class="details">
                <span class="icon">📞</span><a href="tel:+250792080543" class="details-link">0792080543</a> | 
                <span class="icon">✉️</span><a href="mailto:ug2321358@ines.ac.rw" class="details-link">ug2321358@ines.ac.rw</a> | 
                <span class="icon">🌍</span> Rwanda | 
                <span class="icon">🏫</span><a href="https://www.ines.ac.rw/" target="_blank" class="details-link">INES Ruhengeri</a> | 
                <span class="icon">🎓</span> Software Engineering (Year 3)
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Add separator between sections
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Display the main introduction text with fade-in animation
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h1 class='main-title fade-in'>Welcome to My Digital Footprint</h1>", unsafe_allow_html=True)
    st.write("""
    👋 Hi, I'm Adut Gai Chol Chol, a passionate third-year Software Engineering student at INES Ruhengeri.  
    I am passionate about technology and innovation, particularly in mobile and web development.  
    My dream is to develop solutions that improve digital services in Rwanda and beyond.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Add separator between sections
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Display the "Why I Chose Software Engineering?" section with slide-in effect
    st.markdown('<div class="slide-in-left">', unsafe_allow_html=True)
    st.markdown("<h2 class='subheader fade-in'>Why I Chose Software Engineering?</h2>", unsafe_allow_html=True)
    st.write("""
    - To solve real-world problems through technology.
    - To create innovative applications that enhance people's lives.
    - To contribute to the digital transformation of Africa.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Add the resume download button
    st.download_button(
        label="Download My Resume",
        data=open("resume.pdf", "rb").read(),  # Path to your resume file
        file_name="Adut_Gai_Chol_Chol_Resume.pdf",
        mime="application/pdf",
    )

# Include Font Awesome CDN to load icons

# Projects Section
elif choice == "Projects":
    st.title("🚀 My Projects")
    st.write("Here are some of the projects I have worked on:")

    # Add a filter for project categories
    category_filter = st.selectbox("Filter by Category", ["All", "Year 1", "Year 2", "Year 3", "Dissertation", "Group Work", "Individual Assignment", "Commercial Work"])

    st.markdown("""
    <head>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    </head>
    """, unsafe_allow_html=True)

    # List of all projects with their categories
    projects = [
        {"name": "Enhanced Greeting App", "description": "A smart greeting application that personalizes user interactions.", "icon": "fas fa-smile", "category": "Individual Assignment"},
        {"name": "Unified App", "description": "An integrated services mobile app for Rwanda.", "icon": "fas fa-cogs", "category": "Dissertation"},
        {"name": "Construction Website", "description": "A website for showcasing construction projects.", "icon": "fas fa-hard-hat", "category": "Year 1"},
        {"name": "Travel Agency Website", "description": "A website for booking flights, hotels, and activities.", "icon": "fas fa-plane-departure", "category": "Year 2"},
        {"name": "Student Management System", "description": "A system for managing student data and records.", "icon": "fas fa-users", "category": "Group Work"},
        {"name": "Health Tracker System", "description": "A system to track health-related data and progress.", "icon": "fas fa-heartbeat", "category": "Year 3"},
        {"name": "AI Chatbot", "description": "An AI-powered chatbot for various interactions.", "icon": "fas fa-robot", "category": "Personal"},
        {"name": "Hagana Cleaning Services Website", "description": "A commercial website for cleaning services.", "icon": "fas fa-broom", "category": "Commercial Work"},
        {"name": "Cloud Storage System", "description": "A cloud-based storage and file sharing system.", "icon": "fas fa-cloud", "category": "Group Work"}
    ]

    # Filter projects based on category filter
    filtered_projects = [
        project for project in projects
        if category_filter == "All" or category_filter == project["category"]
    ]

    # Create 3 columns for each row
    col1, col2, col3 = st.columns(3)

    # Define card style (height and width) for uniformity
    card_style = """
    <style>
        .card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            height: 300px; /* Set uniform height */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center; /* Center content horizontally */
            text-align: center; /* Center text inside */
        }

        .card:hover {
            transform: translateY(-10px);
        }

        .card i {
            font-size: 48px; /* Increase icon size */
            color: #4CAF50;
            margin-bottom: 15px; /* Add some space between icon and title */
        }

        .card-title {
            font-size: 22px;
            font-weight: bold;
            color: #333;
            margin-top: 10px;
        }

        .card-description {
            font-size: 16px;
            color: #777;
            margin-top: 10px;
        }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    # Display filtered projects in 3-column cards
    for i, project in enumerate(filtered_projects):
        if i % 3 == 0:
            col1, col2, col3 = st.columns(3)

        if i % 3 == 0:
            with col1:
                st.markdown(f"""
                    <div class="card">
                        <div><i class="{project['icon']}"></i></div>
                        <div class="card-title">{project['name']}</div>
                        <div class="card-description">{project['description']}</div>
                    </div>
                """, unsafe_allow_html=True)

        elif i % 3 == 1:
            with col2:
                st.markdown(f"""
                    <div class="card">
                        <div><i class="{project['icon']}"></i></div>
                        <div class="card-title">{project['name']}</div>
                        <div class="card-description">{project['description']}</div>
                    </div>
                """, unsafe_allow_html=True)

        else:
            with col3:
                st.markdown(f"""
                    <div class="card">
                        <div><i class="{project['icon']}"></i></div>
                        <div class="card-title">{project['name']}</div>
                        <div class="card-description">{project['description']}</div>
                    </div>
                """, unsafe_allow_html=True)

        if (i + 1) % 3 == 0:
            st.markdown("---")

    # Display message if no projects match filter
    if not filtered_projects:
        st.write("No projects found matching your category filter.")

elif choice == "Skills & Achievements":
    st.markdown("<h1 style='text-align: center;'>🏆 Skills & Achievements</h1>", unsafe_allow_html=True)
    
    # Technical Skills with Progress Bars
    st.markdown("<h2 style='text-align: center;'>💻 Technical Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.write("**HTML & CSS** (Mastered)")
        st.progress(100)
        st.write("**Python** (Intermediate)")
        st.progress(60)
        st.write("**Database Management** (Mastered)")
        st.progress(100)

    with col2:
        st.write("**PHP** (Intermediate)")
        st.progress(60)
        st.write("**JavaScript** (Intermediate)")
        st.progress(60)
        st.write("**Flutter** (Beginner)")
        st.progress(30)
    st.markdown("---")
    
    # Soft Skills on One Line with Separator | and Centered
    st.markdown("<h2 style='text-align: center;'>🤝 Soft Skills</h2>", unsafe_allow_html=True)
    soft_skills = ["✅Problem-solving", "✅Communication", "✅Teamwork", "✅Adaptability"]
    st.markdown(f"<p style='text-align: center;'>{' | '.join(soft_skills)}</p>", unsafe_allow_html=True)  # Center the soft skills
    st.markdown("---")
    
    # Certifications with Each on a New Line and Centered
    st.markdown("<h2 style='text-align: center;'>🎓 Certifications & Achievements</h2>", unsafe_allow_html=True)
    
    certificates = [
        "📜 Leadership Skills🎖️",
        "📜 PHP Certificate (Online Course)🎖️", 
        "📜 Python Certificate (Online Course)🎖️", 
        "📜 JavaScript Certificate (Online Course)🎖️", 
       
    ]
    
    # Centering each certificate on a new line
    for certificate in certificates:
        st.markdown(f"<p style='text-align: center;'>{certificate}</p>", unsafe_allow_html=True)


# Sample profile information
if choice == "Profile":
    # Default profile information
    default_name = "Adut Gai Chol Chol"
    default_email = "ug2321358@ines.ac.rw"
    default_phone = "0792080543"
    default_university = "INES Ruhengeri University"  # Updated to avoid brackets
    default_fieldOfStudy = "Software Engineering"
    default_bio = "Software Engineering student at INES Ruhengeri."
    default_image = "person.jpg"  # Ensure the correct image path or URL

    st.title("👤 Personal Profile")

    # Custom styling with animations and hover effect
    st.markdown("""
    <style>
        /* Profile container */
        .profile-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            gap: 30px;
            margin-bottom: 30px;
        }

        /* Animation for text */
        .fade-in {
            animation: fadeIn 2s ease-out;
        }

        .slide-up {
            animation: slideUp 2s ease-out;
        }

        /* Hover effect */
        .hover-move {
            transition: transform 0.3s ease, color 0.3s ease;
        }

        .hover-move:hover {
            transform: translateY(-5px); /* Moves text up slightly */
        }

        /* Keyframes for fade-in animation */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        /* Keyframes for slide-up animation */
        @keyframes slideUp {
            from {
                transform: translateY(20px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        /* Styling for profile details */
        .profile-details {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
        }

        p {
            font-size: 18px;
            text-decoration: none;
        }

        /* Styling for links */
        a:hover {
            text-decoration: none !important;
            color: #3498db !important;
        }
        a{
            text-decoration: none !important;
            color: inherit !important;
        }


        
    </style>
    """, unsafe_allow_html=True)

    # Profile container with image and details
    profile_container = st.container()

    with profile_container:
        # Create layout with two columns: one for the image, the other for the details
        col1, col2 = st.columns([1, 3])

        # Display profile picture in a circular shape with proper styling
        with col1:
            st.image(default_image, width=200, use_container_width=True)  # Display image

        # Display profile details with fade-in, slide-up animations and hover effect
        with col2:
            st.markdown(f"<p class='fade-in slide-up hover-move'>Name: {default_name}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='fade-in slide-up hover-move'>Email: <a href='mailto:{default_email}'>{default_email}</a></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='fade-in slide-up hover-move'>Phone Number: <a href='tel:{default_phone}'>{default_phone}</a></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='fade-in slide-up hover-move'>University: <a href='https://www.ines.ac.rw' target='_blank'>{default_university}</a></p>", unsafe_allow_html=True)
            st.markdown(f"<p class='fade-in slide-up hover-move'>Field of Study: {default_fieldOfStudy}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='fade-in slide-up hover-move'>Bio: {default_bio}</p>", unsafe_allow_html=True)



# Path to the testimonials JSON file
testimonials_file = "testimonials.json"

# Load existing testimonials from the file (if any)
if os.path.exists(testimonials_file):
    with open(testimonials_file, "r") as file:
        testimonials = json.load(file)
else:
    testimonials = []

# Section for testimonials
if choice == "Testimonials":
    st.title("Testimonials")

    # Form to submit new testimonials
    with st.form("testimonial_form", clear_on_submit=True):
        author = st.text_input("Your Name:")
        testimonial = st.text_area("Testimonial:", height=150)
        submitted = st.form_submit_button("Submit Testimonial")

        if submitted:
            if author and testimonial:
                # Create a new testimonial object
                new_testimonial = {"author": author, "testimonial": testimonial}
                
                # Append the new testimonial to the existing list
                testimonials.append(new_testimonial)

                # Save the updated testimonials list to the JSON file
                with open(testimonials_file, "w") as file:
                    json.dump(testimonials, file)

                st.success("Thank you for your testimonial!")
            else:
                st.error("Please fill in both fields.")

    # Display the submitted testimonials in the desired format
    st.subheader("What Others Say:")
    if testimonials:
        for testimonial in testimonials:
            # Display each testimonial in the format: "Testimonial text" – Author's name
            st.markdown(f"\"{testimonial['testimonial']}\" - {testimonial['author']}")
            st.markdown("---")
    else:
        st.write("No testimonials yet. Be the first to leave one!")


if choice == "Timeline":
    st.title("📌 My Journey")

    milestones = [
        {"year": "2021", "event": "Learned Programming Languages"},
        {"year": "2022", "event": "Started Computer Science Degree"},
        {"year": "2023", "event": "Completed Internship at Ikugugu Company"},
        {"year": "2025", "event": "Published Research Paper"}
    ]

    years = [m["year"] for m in milestones]
    events = [m["event"] for m in milestones]

    fig = go.Figure()

    # Change timeline line to blue
    fig.add_trace(go.Scatter(
        x=[1] * len(years),
        y=years,
        mode="lines",
        line=dict(color="#007BFF", width=5),  # 🔹 **Blue Line**
        showlegend=False
    ))

    # Add markers and events with black text
    fig.add_trace(go.Scatter(
        x=[1] * len(years),
        y=years,
        mode="markers+text",
        text=events,
        textposition="middle right",
        marker=dict(size=18, color="#007BFF", line=dict(width=3, color="white")),  # 🔹 **Blue Markers**
        textfont=dict(size=16, color="#000000", family="Arial, sans-serif"),  # 🔹 **Black Text**
        showlegend=False
    ))

    fig.update_layout(
        title="📍 Academic & Professional Milestones",  # Title
        title_font=dict(color="#000000", size=24, family="Arial, sans-serif"),  # 🔹 **Black Title Text**
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(
            showgrid=False, 
            showline=False, 
            showticklabels=True, 
            tickmode="array", 
            tickvals=years, 
            ticktext=years,
            tickfont=dict(color="#000000", size=16)  # 🔹 **Black Years**
        ),
        height=600,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=50, r=50, t=50, b=50)
    )

    st.plotly_chart(fig)

elif choice == "Contact":
    st.title("Leave Me a Message!!!")

    # Include the Font Awesome CDN link in the header of the page
    st.markdown(
        """
        <head>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
        </head>
        """, 
        unsafe_allow_html=True
    )

    # Define the URLs to link to your profiles
    links = {
        "LinkedIn": "https://www.linkedin.com/in/adut-gai-chol-aba40a355",
        "Email": "mailto:ug2321358@ines.ac.rw",
        "Phone": "tel:+1234567890",
        "GitHub": "https://github.com/adutgai",
        "Portfolio": "https://student-portfolio-hfaj7gazwjhzwnhhvwahwy.streamlit.app/"
    }

    # Define the Font Awesome icons (using HTML) with smaller size for footer-like appearance
    icons_html = {
        "LinkedIn": '<i class="fab fa-linkedin" style="font-size:20px; color:#0077b5; margin-right: 10px;"></i>',
        "Email": '<i class="fas fa-envelope" style="font-size:20px; color:#ff7f50; margin-right: 10px;"></i>',
        "Phone": '<i class="fas fa-phone" style="font-size:20px; color:#34b7f1; margin-right: 10px;"></i>',
        "GitHub": '<i class="fab fa-github" style="font-size:20px; color:#636363FF; margin-right: 10px;"></i>',
        "Portfolio": '<i class="fas fa-user" style="font-size:20px; color:#ff69b4; margin-right: 10px;"></i>',
    }

    # Contact form for messages
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", key="name")
        email = st.text_input("Email", key="email")
        subject = st.text_input("Subject", key="subject")
        message = st.text_area("Message", key="message")
        submitted = st.form_submit_button("Send")

        if submitted:
            try:
                msg = EmailMessage()
                msg["From"] = email
                msg["To"] = st.secrets["email"]["username"]
                msg["Subject"] = subject
                msg.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")

                with smtplib.SMTP(st.secrets["email"]["smtp_server"], st.secrets["email"]["port"]) as server:
                    server.starttls()
                    server.login(st.secrets["email"]["username"], st.secrets["email"]["password"])
                    server.send_message(msg)
                st.success("Message sent successfully!")
            except Exception as e:
                st.error(f"Failed to send message: {str(e)}")

    # Add some vertical spacing before the icons to move them to the bottom
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Display the icons in a single line with no columns
    st.markdown(
        f"""
        <div style="display: flex; justify-content: left;">
            <a href="{links['LinkedIn']}">{icons_html['LinkedIn']}</a>
            <a href="{links['Email']}">{icons_html['Email']}</a>
            <a href="{links['Phone']}">{icons_html['Phone']}</a>
            <a href="{links['GitHub']}">{icons_html['GitHub']}</a>
            <a href="{links['Portfolio']}">{icons_html['Portfolio']}</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Add more vertical space to push the icons to the bottom
    st.markdown("<br><br><br>", unsafe_allow_html=True)
