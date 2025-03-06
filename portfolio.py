import streamlit as st

# Set Page Config
st.set_page_config(page_title="My Digital Footprint", page_icon="🌍", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "Projects", "Skills & Achievements", "Profile", "Contact"]
choice = st.sidebar.radio("Go to", pages)

# Home Section
if choice == "Home":
    st.image("person.jpg", width=200)  # Replace with your actual image file
    st.title("Welcome to My Digital Footprint")
    st.write("""
    👋 Hi, I'm Adut Gai Chol Chol, a passionate third year Software Engineering student at INES Ruhengeri.  
    I am passionate about technology and innovation, particularly in mobile and web development.  
    My dream is to develop solutions that improve digital services in Rwanda and beyond.
    """)
    st.subheader("Why I Chose Software Engineering?")
    st.write("""
    - To solve real-world problems through technology.
    - To create innovative applications that enhance people's lives.
    - To contribute to the digital transformation of Africa.
    """)

# Projects Section
elif choice == "Projects":
    st.title("🚀 My Projects")
    st.write("Here are some of the projects I have worked on:")

    # Project 1: Enhanced Greeting App
    col1, col2 = st.columns(2)
    with col1:
        st.image("person.jpg", use_container_width=True)  # Replace with actual image
    with col2:
        st.subheader("Enhanced Greeting App")
        st.write("A smart greeting application that personalizes user interactions.")
        st.markdown("[🔗 View on GitHub](#)")  # Replace # with actual link
        st.markdown("[🌐 Live Demo](#)")  # Replace # with actual link

    st.markdown("---")  # Separator

    # Project 2: Unified App
    col3, col4 = st.columns(2)
    with col3:
        st.image("person.jpg", use_container_width=True)  # Replace with actual image
    with col4:
        st.subheader("Unified App")
        st.write("An integrated services mobile app for Rwanda.")
        st.markdown("[🔗 View on GitHub](#)")  # Replace # with actual link
        st.markdown("[🌐 Live Demo](#)")  # Replace # with actual link")
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

 # Replace with your actual image file

import streamlit as st

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

# If condition for "Contact" section
if choice == "Contact":
    st.title("📬 Contact Me")

    # Embed the Google Form into your Streamlit app
    st.markdown("""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSejjjeC1OmhO0lH4a84yvsscpqQ5u3PBPVOxSBmyRQFmmXP8Q/viewform?embedded=true&hl=en" width="600" height="700" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """, unsafe_allow_html=True)

