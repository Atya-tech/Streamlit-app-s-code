import streamlit as st
import numpy as np
import pandas as pd
import os
def app():     
    with st.container():
        st.markdown("""
<!DOCTYPE html>
<html>

<body>
  <h2 style="text-align: center; color: green;">
  Welcome To Embed-View
  </h2>
 <marquee behavior="scroll" direction="left" scrollamount="10">Empowering Innovations in  Embed-View's Integrated Hardware and Software Solutions </marquee>
</body>
</html>
""",unsafe_allow_html=True)
        st.markdown(f"""
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
 padding-bottom: 0; margin-top: 1.6em; margin-bottom: 0em;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGBn8i3JgM&#x2F;laww-FQSu63W_Y7sIOjqGA&#x2F;view?embed" allowfulscreen='false'>
  </iframe>
</div>
""",unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: Black;'>What we do ?</h1>", unsafe_allow_html=True)
        st.subheader("Accelerating Human Break throughs Together")
        st.write(
                """
                With our customers, we co-create solutions across:
                - Pharma
                - Agriculture               
                - Healthcare
                """
            )
        st.write("---")
    st.markdown("<h1 style='text-align: center; color: Black;'>Our Projects</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Inter, sans-serif;
}}

.body{{
    display:flex;
    justify-content: center;
}}
.wrapper {{
    position: relative;
    width: 100%;
    height: 100%;
    padding: 20px;
    display: flex;
    align-content: center;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
}}

.card {{
    position: relative;
    width: 325px;
    height: 450px;
    background: #000;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
}}

.poster {{
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}}

.poster::before {{
    content: '';
    position: absolute;
    bottom: -45%;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    transition: .3s;
}}

.card:hover .poster::before {{
    bottom: 0;
}}

.poster img {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: .3s;
}}

.card:hover .poster img {{
    transform: scale(1.1);
}}

.details {{
    position: absolute;
    bottom: -100%;
    left: 0;
    width: 100%;
    height: auto;
    padding: 1.5em 1.5em 2em;
    background: #000a;
    backdrop-filter: blur(16px) saturate(120%);
    transition: .3s;
    color: #fff;
    z-index: 2;
}}

.card:hover .details {{
    bottom: 0;
}}

.details h1 {{
    font-weight: 700;
    font-size: 1.5em;
    margin-bottom: 5px;
    color: #fff;
}}

.details .desc {{
    color: #fff;
    opacity: .8;
    line-height: 1.5;
    margin-bottom: 1em;
}}
                </style>
<div class="wrapper">
    <div class="card">
        <div class="poster"><img src="https://i.imgur.com/MXMMXOu.jpeg"></div>
        <div class="details">
            <h1>Pharma</h1>
            <p class="desc">
            "Revolutionizing pharmaceutical industry through innovative projects, enhancing Pharma accessibility and quality globally."
            </p>
        </div>
    </div>
    <div class="card">
        <div class="poster"><img src="https://i.imgur.com/GkcE5xt.jpeg" alt="Location Unknown"></div>
        <div class="details">
            <h1>Agriculture</h1>
            <p class="desc">
                "Developing cutting-edge agricultural sensors to optimize farming practices, empowering farmers with data-driven insights."
            </p>
        </div>
    </div>
    <div class="card">
        <div class="poster"><img src="https://3.bp.blogspot.com/-mD0t4hlg9PU/WWTg6LvVHiI/AAAAAAAAEEs/pug6YRgDbCQsGMNySx1V6Yn_42cgexnmACLcBGAs/s1600/health-care.jpg" auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Location Unknown"></div>
        <div class="details">
            <h1>Health care</h1>
            <p class="desc">
                "Empowering healthcare with state-of-the-art technology, revolutionizing patient care and advancing medical breakthroughs worldwide."
            </p>
        </div>
    </div>
</div>

  
</body>
</html> """,unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: Black;'>Our Solutions</h1>", unsafe_allow_html=True)
    st.subheader("Custom Silicon to Product Development Company")
    st.write("""Embed-View Solutions maintains strong partnerships with leading foundries such as TSMC, UMC, Global Foundries, and Tower Jazz, which enables us to leverage the latest process technologies and manufacturing capabilities. Our collaborative approach and dedication to excellence have earned us the trust of clients worldwide, making us the preferred partner for embedded system development.
Whether you're seeking to optimize existing designs or embark on a groundbreaking project, Embed-View Solutions stands ready to realize your embedded vision with precision and innovation. Let us be your partner in shaping the future of embedded technology.
""")
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: Black;'>Industries We Cater to </h1>", unsafe_allow_html=True)
    st.markdown(f"""
<style>
body {{
  margin: 0;
  font-family: 'Muli', sans-serif;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  overflow-x: hidden;
}}

.categories__title {{
 color: rgb(77, 55, 102);
  font-size: 28px;
  position: absolute;
  padding-left: 30px;
}}
.carousel-item {{
  width: 200px;
  height: 250px;
  border-radius: 20px;
  background-color: #95bcd6;
  overflow: hidden;
  margin-right: 10px;
  margin-top: 70px;
  display: inline-block;
  cursor: pointer;
  -webkit-transition: 1000ms all;
  transition: 1000ms all;
  -webkit-transform-origin: center left;
  transform-origin: center left;
  position: relative;
}}

.carousel-item:hover ~ .carousel-item {{
  -webkit-transform: translate3d(100px, 0, 0);
  transform: translate3d(100px, 0, 0);
}}

.carousel__container:hover .carousel-item {{
  opacity: 0.3;
}}

.carousel__container:hover .carousel-item:hover {{
  -webkit-transform: scale(1.5);
  transform: scale(1.5);
  opacity: 1;
}}

.carousel-item__img {{
  width: 200px;
  height: 250px;
  -o-object-fit: cover;
  object-fit: cover;
}}

.carousel-item__details {{
  background: -webkit-gradient(
    linear,
    left bottom,
    left top,
    from(rgba(0, 0, 0, 0.9)),
    to(rgba(0, 0, 0, 0))
  );
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.9) 0%,
    rgba(0, 0, 0, 0) 100%
  );
  font-size: 10px;
  opacity: 0;
  -webkit-transition: 45ms opacity;
  transition: 45ms opacity;
  padding: 10px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}}

.carousel-item__details:hover {{
  opacity: 1;
}}

.carousel-item__details span {{
  /* width: 10px;
  height: 10px; */
  font-size: 0.9rem;
  color: #2ecc71;
  /* background-color: white; */
}}

.carousel-item__details .controls {{
  padding-top: 180px;
}}

.carousel-item__details .carousel-item__details--title,
.carousel-item__details--subtitle {{
  color: #fff;
  margin: 5px 0;
}}
</style>
<div class="background"></div>
    <div class="background-texture"></div>
    <section class="carousel">
      <div class="carousel__container">
        <div class="carousel-item">
          <img
            class="carousel-item__img"
            src="https://png.pngtree.com/element_our/sm/20180411/sm_5ace0628840fa.png"
            alt="people"
          />
          <div class="carousel-item__details">
            <div class="controls">
              <span class="fas fa-play-circle"></span>
              <span class="fas fa-plus-circle"></span>
            </div>
            <h5 class="carousel-item__details--title">Agriculture</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img
            class="carousel-item__img"
            src="https://png.pngtree.com/png-clipart/20200709/original/pngtree-automotive-car-logo-design-png-image_3595547.jpg"
            alt="people"
          />
          <div class="carousel-item__details">
            <div class="controls">
              <span class="fas fa-play-circle"></span>
              <span class="fas fa-plus-circle"></span>
            </div>
            <h5 class="carousel-item__details--title">Automotive</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img
            class="carousel-item__img"
            src="https://img.freepik.com/premium-vector/logo-medical-device_690981-383.jpg"
            alt="people"
          />
          <div class="carousel-item__details">
            <div class="controls">
              <span class="fas fa-play-circle"></span>
              <span class="fas fa-plus-circle"></span>
            </div>
            <h5 class="carousel-item__details--title"> Medical Devices</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img
            class="carousel-item__img"
            src="https://creativevip.net/resource-images/15-cloud-computing-icons-2.png"
            alt="people"
          />
          <div class="carousel-item__details">
            <div class="controls">
              <span class="fas fa-play-circle"></span>
              <span class="fas fa-plus-circle"></span>
            </div>
            <h5 class="carousel-item__details--title">Cloud Security</h5>
          </div>
        </div>
        <div class="carousel-item">
          <img
            class="carousel-item__img"
            src="https://i.imgur.com/e31FaZ4.jpeg"
            alt="people"
          />
          <div class="carousel-item__details">
            <div class="controls">
              <span class="fas fa-play-circle"></span>
              <span class="fas fa-plus-circle"></span>
            </div>
            <h5 class="carousel-item__details--title">Embedded</h5>
          </div>
        </div>
        
    """,unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: Black;'>Our mission: complete client success</h1>", unsafe_allow_html=True)
    st.write("""
When it comes to digital transformation, why settle for a vendor when what you need is a partner? 
Someone who understands your industry and your company and how to execute your strategy efficiently and completely. 
Someone you can count on to deliver essential solutions and measurable results again and again. Persistent is that partner.""")
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: Black;'>OUR GALLERY</h1>", unsafe_allow_html=True)
    st.markdown(f"""
<style>
    .gallery-container {{
        position: relative;
        flex-grow: 1;
        margin: auto;
        max-width: 1200px;
        max-height: 1200px;
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        grid-template-rows: repeat(4, 1fr);
        grid-gap: 2vmin;
        justify-items: center;
        align-items: center;
    }}

    .gallery-container img {{
        z-index: 1;
        grid-column: span 2;
        max-width: 100%;
        margin-bottom: -52%;
        clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        transform: scale(1);
        transition: all .25s;
    }}

    .gallery-container img:nth-child(7n + 1) {{
        grid-column: 2 / span 2;
    }}

    .gallery-container img:hover {{
        z-index: 2;
        transform: scale(2);
    }}
</style>
<div class="gallery-container">
    <img src="https://i.imgur.com/IJ3uixt.png" alt="">
    <img src="https://i.imgur.com/KV134jw.png" alt="">
    <img src="https://i.imgur.com/1JX47ym.png" alt="">
    <img src="https://i.imgur.com/NnFv3o9.png" alt="">
    <img src="https://i.imgur.com/PrV06oD.png" alt="">
    <img src="https://i.imgur.com/nxHoIEI.png" alt="">
    <img src="https://i.imgur.com/zXDoWnK.png" alt="">
    <img src="https://i.imgur.com/gZiVx3o.png" alt="">
    <img src="https://i.imgur.com/QuVmVvk.png" alt="">
    <img src="https://i.imgur.com/yBCChWE.png" alt="">
</div>
""", unsafe_allow_html=True)
    st.write("___")
    
    footer()


def footer():
        st.markdown("""

                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                            <title>Responsive Footer</title>
                            <!-- Font Awesome CDN -->
                            <link
                            rel="stylesheet"
                            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"
                            />
                            <!-- Google Fonts -->
                            <link
                            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap"
                            rel="stylesheet"
                            />
                            <!-- Stylesheet -->
                            <style>
                            /* Add your CSS styles here */
                            body {
                                font-family: 'Poppins', sans-serif;
                                margin: 0;
                                padding: 0;
                            }
                            footer {
                                background-color: #fff;
                                padding: 20px;
                                text-align: center;
                            }
                            .row {
                                display: flex;
                                justify-content: space-around;
                                margin-bottom: 20px;
                            }
                            .column {
                                flex: 1;
                                padding: 0 20px;
                            }
                            .column h3 {
                                font-size: 18px;
                                margin-bottom: 10px;
                            }
                            .column p {
                                font-size: 14px;
                                line-height: 1.6;
                            }
                            input[type="email"] {
                                width: 100%;
                                padding: 8px;
                                margin-bottom: 10px;
                                border: 1px solid #ccc;
                                border-radius: 4px;
                                box-sizing: border-box;
                            }
                            button {
                                background-color: #4CAF50;
                                color: white;
                                padding: 8px 20px;
                                border: none;
                                border-radius: 4px;
                                cursor: pointer;
                            }
                            button:hover {
                                background-color: #45a049;
                            }
                            .social {
                                margin-top: 10px;
                            }
                            .social i {
                                margin-right: 10px;
                                font-size: 24px;
                            }
                            .secondary p {
                                margin: 5px 0;
                            }
                            .copyright p {
                                font-size: 12px;
                                color: #777;
                            }
                            </style>
                        </head>
                        <body>
                            <footer>
                            <div class="row primary">
                                <div class="column about">
                                <h3>Company Name</h3>
                                <p>
                                    EmbedView Solutions streamlines complex projects by offering both hardware and software development. They design sensors to collect data, build programs to analyze it, and store everything securely in the cloud. This one-stop shop creates custom solutions that seamlessly link data collection, analysis, and visualization.
                                </p>
                                </div>
                                <div class="column links">
                                <h3>Quick Links</h3>
                                <ul>
                                    <li>
                                    <a href="#faq">F.A.Q</a>
                                    </li>
                                    <li>
                                    <a href="#cookies-policy">Cookies Policy</a>
                                    </li>
                                    <li>
                                    <a href="#terms-of-services">Terms Of Service</a>
                                    </li>
                                    <li>
                                    <a href="#support">Support</a>
                                    </li>
                                    <li>
                                    <a href="#careers">Careers</a>
                                    </li>
                                </ul>
                                </div>
                                <div class="column subscribe">
                                <h3>Subscribe</h3>
                                <div>
                                    <input type="email" placeholder="Your email id here" />
                                    <button>Subscribe</button>
                                </div>
                                <div class="social">
                                    <i class="fab fa-facebook-square"></i>
                                    <i class="fab fa-instagram-square"></i>
                                    <i class="fab fa-twitter-square"></i>
                                    <i class="fab fa-Linkedin-square"></i>
                                </div>
                                </div>
                            </div>

                        
                        """, unsafe_allow_html=True)