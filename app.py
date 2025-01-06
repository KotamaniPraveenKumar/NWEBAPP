import streamlit as st
import base64

# Add custom CSS
def add_custom_css():
    custom_css = """
    <style>
    body {
        font-family: 'Poppins', Arial, sans-serif;
        color: #2c3e50;
        background-image: url("http://hintergrundbild.org/wallpaper/full/f/d/b/35908-full-size-vintage-hintergrundbilder-1920x1080-fuer-computer.jpg");
        background-size: cover;
        background-position: center;
        height: 100vh;
    }

    .container {
        background-color: rgba(255, 255, 255, 0.85);
        margin: 30px auto;
        max-width: 800px;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(5px);
    }

    h1 {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 4px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        border-bottom: 3px solid #1e90ff;
        padding-bottom: 10px;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        margin: 15px 0;
        padding: 10px;
        background: #f8f9fa;
        border-radius: 8px;
        transition: background 0.3s ease, transform 0.3s ease;
        cursor: pointer;
    }

    li:hover {
        background: #e0e0e0;
        transform: translateY(-5px);
    }

    button {
        padding: 10px 20px;
        background: #1e90ff;
        border: none;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    button:hover {
        background: #0a74da;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Sample data for services
services = {
    "decor": {
        "Wedding Decor": "We provide exceptional wedding decorations to make your day special.",
        "Birthday Decor": "Celebrate your special day with vibrant and unique birthday decorations designed to match your personality and theme.",
        "Saree Decor": "Elegant saree draping and decor to enhance traditional ceremonies and create a memorable ambiance.",
        "Dothi Decor": "Graceful dothi arrangements and decor, perfect for cultural and traditional events.",
        "Corporate Decor": "Professional and sophisticated decorations tailored for corporate events, conferences, and office parties.",
        "Candle Ceremony": "Romantic and serene candlelight decorations to make your special ceremonies unforgettable.",
    },
    "photography": {
        "Wedding Photography": "Capture your special moments with our professional photographers.",
        "Model Photography": "Capture your special moments with our professional photographers, delivering stunning visuals and timeless memories.",
    },
    "sounds": {
        "DJ Services": "High-energy DJ services for events and parties.",
        "Live Band Sound": "Experience the magic of live music with our professional sound systems, ensuring crystal-clear audio for vocals and instruments to captivate your audience.",
        "Conference and Seminar Audio": "Deliver your message with clarity using our state-of-the-art sound systems designed for conferences, seminars, and presentations.",
        "Orchestra Setup": "Enhance your classical and grand events with premium sound systems, ensuring every note of the orchestra resonates beautifully.",
    },
    "Hospitality": {
        "Catering Services": "Delicious catering options for events of any size, featuring customizable menus and exceptional flavors.",
        "Event Management": "Comprehensive event planning and management to ensure a seamless and stress-free experience.",
        "Guest Accommodation": "Comfortable and luxurious accommodation arrangements for your guests.",
        "Welcome Services": "Warm and personalized guest welcomes, including reception and hospitality desks.",
        "Transportation Coordination": "Efficient and reliable transportation services to ensure smooth travel for guests and participants.",
        "Venue Decoration": "Stunning decor setups that enhance the ambiance and align with your event’s theme.",
        "Beverage Services": "Wide selection of beverages, including cocktails, mocktails, and curated drink menus.",
        "Host and Hostess Services": "Professional and courteous hosts and hostesses to ensure a memorable guest experience.",
        "Security Services": "Well-trained security personnel to maintain safety and order during events.",
        "Cleanup and Maintenance": "Post-event cleanup and maintenance to leave the venue spotless."
    },
    "Logistics": {
        "Delivery Services": "Fast and reliable delivery solutions, ensuring your goods reach their destination on time and in perfect condition.",
        "Warehouse Solutions": "Secure and efficient warehouse management services, tailored to meet your storage needs.",
        "Event Transportation": "Seamless logistics and transportation for events, including equipment and materials handling.",
        "Inventory Management": "Advanced inventory tracking and management to streamline operations and minimize disruptions.",
        "Freight Services": "Comprehensive freight solutions for local and international shipments, ensuring smooth transit.",
        "Courier Services": "Quick and efficient courier services for small packages and urgent deliveries.",
        "Logistics Planning": "Expert logistics planning and coordination to optimize supply chains and reduce costs.",
        "Packing and Moving": "Professional packing and moving services for safe and hassle-free relocations."
    },
    "freelancer": {
        "Graphic Designers": "Creative design solutions for your business.",
        "Web Developers": "Professional and responsive web development services to bring your ideas to life.",
        "Photographers": "Professional photography services to capture stunning visuals for your events, products, or brand.",
        "Video Editors": "High-quality video editing services to create impactful and polished videos.",
        "Event Executors": "Professional event execution services to ensure smooth and flawless implementation of your plans."
    },
}

# Streamlit App
def main():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.title("Service Categories")
    add_custom_css()

    # Main navigation for categories
    category = st.selectbox("Select a Category", ["Select"] + list(services.keys()))

    if category != "Select":
        st.subheader(f"{category.capitalize()} Services")
        subcategories = services[category]

        # Subcategory selection
        subcategory = st.selectbox("Select a Subcategory", ["Select"] + list(subcategories.keys()))

        if subcategory != "Select":
            description = subcategories[subcategory]
            st.markdown(f"### {subcategory}")
            st.write(description)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

