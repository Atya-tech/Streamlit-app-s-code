
import streamlit as st
from streamlit_option_menu import option_menu

def app():
    st.markdown("<h1 style='text-align: center; color: Black;'>Real world products & solutions</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align:center; font-size:36px;'>Our Features & Services</h1>", unsafe_allow_html=True)
    st.write("<h1 style='text-align:center; font-size:20px;'>Delivering domain expertise and technology-driven offerings to help you turn digital challenges into opportunities.</h1>", unsafe_allow_html=True)
    st.markdown("""
<style>
body {
  font-family: 'Raleway', sans-serif;
  background-color: #F2F2F2;
}

h3 {
  font-family: 'Baloo Bhaina';
  text-align: center;
  color: #00868b;
  font-size: 4rem;
}

h4 {
  text-transform: uppercase;
  margin-top: 40px;
  disply: block;
  font-family: 'Baloo Bhaina';
}

#cards-container {
  width: 100%;
  height: auto;
}

.card-wrapper {
  width: 49%;
  text-align: center;
  display: inline-block;
  padding: 20px;
  10px height: 400px;
}

.card {
  height: 280px;
  width: 300px;
  margin: 0 auto;
  position: relative;
  border-radius: 5px;
  overflow: hidden;
  box-shadow: 0px 5px 5px gray;
  background-color: #fff;
  padding: 0;
  z-index: 0;
}

.card-top {
  height: 100px;
  position: relative;
  background-color: #fff;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.icon {
  position: absolute;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: #d3d3d3;
  border: 5px solid #fff;
  box-sizing: border-box;
  left: 100px;
  top: 40PX;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2.9rem;
}

.card-content {
  padding: 10px;
  height: auto;
  background-color: #fff;
  height: 100%;
}

.card-title {
  color: #OOO;
}

.card-content p,
.overlay p {
  font-family: 'Raleway', sans-serif;
  color: #333;
  padding: 10px;
}

.overlay p {
  color: #fff;
}


/* card-top colors */

.gradient-red {
  background: linear-gradient( to top, transparent, #FF4B4B), linear-gradient( to bottom, transparent, rgba(255, 0, 0, 0.8));
}

.gradient-blue {
  background: linear-gradient( to top, transparent, #FF4B4B), linear-gradient( to bottom, transparent, rgba(255, 0, 0, 0.8));
}

.gradient-green {
  background: linear-gradient(to top right, transparent, #FF4B4B), linear-gradient( to bottom left, transparent, rgba(255, 0, 0, 0.8));
}

.gradient-pink {
  background: linear-gradient(to bottom left, transparent, #FF4B4B), linear-gradient( to top right, transparent, rgba(255, 0, 0, 0.8));
}


/* overlay  */

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 300px;
  height: 280px;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  flex-direction: column;
  color: #FFF;
  justify-content: center;
  padding: 10px;
  border-radius: 5px;
}


/*overlay-btn  */

.overlay-btn {
  background-color: transparent;
  color: #FFF;
  font-family: 'Railway', sans-serif;
  font-weight: bold;
  border: none;
  border-radius: 0px;
  border-bottom: 1px solid #FFF;
  transiton: all 0.2s ease;
}

.overlay-btn:hover {
  color: #FFF39A;
  background-color: transparent;
  border-bottom: 1px solid #FFF39A;
  transform: scale(1);
}


/* slide */

.slider {
  transform: translateX(-100%);
  transition: all 0.4s ease-out;
}

.card:hover .slider {
  transform: translateX(0);
}


/* fade*/

.fade {
  transition: all 0.6s ease-in;
  opacity: 0;
}

.card:hover .fade {
  opacity: 1;
}


/* Zoom */

.zoom {
  opacity: 0;
  transition: all 0.7s ease-in;
  border-radius: 5px;
  transform: scale(0);
}

.card:hover .zoom {
  opacity: 1;
  transform: scale(1.1);
}


/* flip */

.flip-container {
  perspective: 1000px;
}

.flip-card {
  transition: transform 3s ease;
  transform-style: preserve-3d;
  poistion: relative;
}

.front,
.back {
  position: absolute;
  top: 0;
  left: 0;
  height: 280px;
  width: 300px;
  box-sizing: border-box;
  border-radius: 5px;
}

.front {
  z-index: 5;
  background-color: #fff;
}

.back {
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  flex-direction: column;
  color: #FFF;
  justify-content: center;
  padding: 10px;
  transform: rotateY(180deg);
}

.flip-card:hover {
  transform: rotateY(180deg);
}

.flip-card:hover .back {
  transform: rotateY(-180deg);
}
</style>
<br /><br />
<section id="cards-container">
  <div class="card-wrapper">
    <div class="card">
      <div class="card-top gradient-blue">
        <div class="icon">
          <i class="fa fa-bug"></i>
        </div>
      </div>
      <div class="card-content">
        <h4 class="card-title">Hardware Design and Development</h4>
      </div>
      <div class="overlay fade">
        <h4>1</h4>
        <p>Industry-leading hardware solutions capture diverse data, from conception to production.</p>
      </div>
    </div>
  </div>

  <!--  Fade  -->
  <div class="card-wrapper">
    <div class="card">
      <div class="card-top gradient-blue">
        <div class="icon">
          <i class="fa fa-bug"></i>
        </div>
      </div>
      <div class="card-content">
        <h4 class="card-title">Software Product Development</h4>
      </div>
      <div class="overlay fade">
        <h4>2</h4>
        <p>Skilled team crafts robust software enhancing hardware offerings, driving efficiency.</p>
      </div>
    </div>
  </div>


  <!-- Zoom -->
  <div class="card-wrapper">
    <div class="card">
      <div>
        <div class="card-top gradient-green">
          <div class="icon">
            <i class="fa fa-rocket"></i>
          </div>
        </div>
        <div class="card-content">
          <h4 class="card-title">Cloud Services</h4>
        </div>
      </div>
      <div class="overlay zoom">
        <h4>3</h4>
        <p>Embracing cloud technology, we offer tailored services for secure data management.</p>
      </div>
    </div>
  </div>

  <div class="card-wrapper">
    <div class="card">
      <div class="card-top gradient-blue">
        <div class="icon">
          <i class="fa fa-bug"></i>
        </div>
      </div>
      <div class="card-content">
        <h4 class="card-title">Customized Dashboards</h4>
      </div>
      <div class="overlay fade">
        <h4>4</h4>
        <p>Crafting customized dashboards for insightful data-driven decision-making.</p>
      </div>
    </div>
  </div>
</section>
<!--End of  Flipping caption -->""",unsafe_allow_html=True)
    st.write("<h1 style='text-align:left; font-size:36px;'>Hardware Design and Development</h1>", unsafe_allow_html=True)
    st.write(
       """
  - Complete product development service
  - Customised single board computers and carrier boards for SoM (System-on-Modules)
  - Industrial Gateway, Sensor Nodes, Control, and Data Acquisition Systems which featuring CAN bus, RS485/422, RS232, Ethernet, Sensor, and Industrial Input/Output
  - Design Review and Feasibility Analysis
        """)
    st.write("<h1 style='text-align:left; font-size:36px;'>Software Product Development</h1>", unsafe_allow_html=True)
    st.write(
       """
  - Our team crafts robust, scalable software solutions, seamlessly integrating with hardware offerings. These feature advanced algorithms and user-friendly interfaces.
  - We stay at technology's forefront, ensuring our products remain innovative, empowering businesses to streamline operations.
  - Through tailored software solutions, we enable businesses to optimize processes, drive productivity, facilitating operational efficiency.
          """
    )
    st.write("<h1 style='text-align:left; font-size:36px;'>Cloud Services</h1>", unsafe_allow_html=True)
    st.write(
       """
  - Recognizing cloud technology's importance, we offer tailored services for secure data storage and analytics.
  - Our cloud solutions provide actionable insights through customized dashboards, driving informed decision-making.
          """
    )
    st.write("<h1 style='text-align:left; font-size:36px;'>Customized Dashboards</h1>", unsafe_allow_html=True)
    st.write(
       """
    - We specialize in crafting bespoke dashboards to turn raw data into actionable intelligence.
    - Leveraging advanced data visualization and user-centric design, our dashboards empower clients to make confident, data-driven decisions by monitoring key metrics and trends in real-time.
          """
    )
    st.write("___")
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
