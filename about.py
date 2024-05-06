import streamlit as st
def app():
  st.markdown("<h1 style='text-align: center; color: Black;'>Hello, we are Embed-View</h1>", unsafe_allow_html=True)
  st.subheader("Embed-View Solutions is a dynamic technology firm specializing in the comprehensive development and delivery of innovative hardware and software solutions. With a core focus on end-to-end service provision, we excel in crafting tailored solutions that seamlessly integrate hardware sensor data collection, sophisticated software development, and cloud-based data storage and visualization.")
  st.markdown("<h1 style='text-align: center; color: Black;'> What we do ?</h1>", unsafe_allow_html=True)
  st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Allura&family=Nunito:wght@200;400;500;600;800&family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap');
    *{
    body{
       font-family: 'Poppins', sans-serif;
        background-color: hsl(0, 0%, 0%);
        font-size: 16px;
    }
    .container{
        max-width: 1500px;
        padding: 0 15px;
        margin:0px;
        margin-bottom:0px;
    }
    .section{
        padding: 20px 0;
        min-height: 50vh;
        display: flex;
    }
    .section-cards{
        display: flex;
        grid-template-columns: repeat(3, 1fr);
        gap: 60px;
        display: flex;
    }
    .section-card{
        background-color: hsl(220, 6%, 10%);
        padding: 120px 20px 30px;
        position: relative;
        z-index: 1;
        display: flex;
    }
    .section-card:nth-child(1){
        --color: #AA96DA;
    }
    .section-card:nth-child(2){
        --color: #C5FAD5;
    }
    .section-card:nth-child(3){
        --color: #FFBF69;
    }
    .section-card:nth-child(4){
        --color: #f2fac5;
    }
    .section-card::before{
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 100%;
        background-color: var(--color);
        z-index: -1;
        clip-path: circle(40px at 70px 70px);
        transition: clip-path 1s ease;
    }
    .section-card:hover::before{
        clip-path: circle(100%);
    }
    .section-card span{
        position: absolute;
        left: 0;
        top: 0;
        height: 80px;
        width: 80px;
        font-size: 50px;
        font-weight: bold;
        transform: translate(30px, 30px);
        display: flex;
        align-items: center;
        justify-content: center;
        color: hsl(0, 0%, 0%);
        transition: transform 1s ease;
    }
    .section-card:hover span{
        transform: translate(0, 30px);
    }
    
    .section-card h2{
        font-size: 26px;
        color: hsl(0, 0%, 100%);
        font-weight: 600;
        text-transform: capitalize;
        line-height: 1.3;
    }
    .section-card p{
        color: hsl(0, 0%, 85%);
        line-height: 1.5;
    }
    .section-card a{
        display: inline-block;
        text-transform: capitalize;
        color: hsl(0, 0%, 100%);
        margin-top: 20px;
        font-weight: 500;
    }
    .section-card a,
    .section-card h2,
    .section-card p{
        transition: color 1s ease;
    }
    .section-card:hover a,
    .section-card:hover h2,
    .section-card:hover p{
        color: hsl(0, 0%, 0%);
    }
    @media(max-width:991px){
        .section-cards{
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media(max-width:575px){
        .section-cards{
            grid-template-columns: repeat(1, 1fr);
        }
    }

</style>
<body>
  <section class="section">
      <div class="container">
          <div class="section-cards">
              <div class="section-card">
                  <span>H</span>
                  <h2></h2>
                  <p>Hardware Design and Development: We lead the industry in designing and engineering cutting-edge hardware solutions, meticulously crafted to capture and process data from diverse sensors and devices. Our expertise spans the entire hardware development lifecycle, from conceptualization to prototyping and final production, ensuring optimal performance and reliability..</p>
                  <a href="#"></a>
              </div>
              <div class="section-card">
                  <span>S</span>
                  <h2></h2>
                  <p>Software Product Development: Our skilled team of software engineers and developers specializes in creating robust and scalable software solutions that complement our hardware offerings. From intricate data processing algorithms to intuitive user interfaces, we leverage the latest technologies to deliver software products that empower businesses to streamline operations and drive efficiency.</p>
                  <a href="#"></a>
              </div>
              <div class="section-card">
                  <span>C</span>
                  <h2></h2>
                  <p>Cloud Services: Recognizing the pivotal role of cloud technology in modern data management, we provide comprehensive cloud services tailored to meet the evolving needs of our clients. Our cloud infrastructure facilitates secure data storage, real-time analytics, and the creation of customized dashboards, enabling businesses to leverage actionable insights for informed decision-making.</p>
                  <a href="#"></a>
              </div>
              <div class="section-card">
                  <span>D</span>
                  <h2></h2>
                  <p>Customized Dashboards: We are dedicated to transforming raw data into actionable intelligence through the creation of bespoke dashboards. Our team leverages advanced data visualization techniques and user-centric design principles to develop intuitive dashboards that empower clients to monitor key performance metrics, track trends, and make data-driven decisions with confidence.</p>
                  <a href="#"></a>
              </div>
          </div>
      </div>
  </section>

</body>
</html>
""",unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center; color: Black;'>Our Team</h1>", unsafe_allow_html=True)
  st.markdown(f"""
<style>
body {{
  font-family: tahoma;
  height: 100vh;
  background-image: url(https://picsum.photos/g/3000/2000);
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
}}

.our-team {{
  padding: 30px 0 40px;
  margin-bottom: 30px;
  background-color: #f7f5ec;
  text-align: center;
  margin-top: 5px;
  overflow: hidden;
  position: relative;
}}

.our-team .picture {{
  display: inline-block;
  height: 130px;
  width: 130px;
  margin-bottom: 50px;
  z-index: 1;
  position: relative;
}}

.our-team .picture::before {{
  content: "";
  width: 100%;
  height: 0;
  border-radius: 50%;
  background-color: #FF4B4B;
  position: absolute;
  bottom: 135%;
  right: 0;
  left: 0;
  opacity: 0.9;
  transform: scale(3);
  transition: all 0.3s linear 0s;
}}

.our-team:hover .picture::before {{
  height: 100%;
}}

.our-team .picture::after {{
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #FF4B4B;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}}

.our-team .picture img {{
  width: 100%;
  height: auto;
  border-radius: 50%;
  transform: scale(1);
  transition: all 0.9s ease 0s;
}}

.our-team:hover .picture img {{
  box-shadow: 0 0 0 14px #f7f5ec;
  transform: scale(0.7);
}}

.our-team .title {{
  display: block;
  font-size: 15px;
  color: #4e5052;
  text-transform: capitalize;
}}

.our-team .social {{
  width: 100%;
  padding: 0;
  margin: 0;
  background-color: #FF4B4B;
  position: absolute;
  bottom: -100px;
  left: 0;
  transition: all 0.5s ease 0s;
}}

.our-team:hover .social {{
  bottom: 0;
}}

.our-team .social li {{
  display: inline-block;
}}

.our-team .social li a {{
  display: block;
  padding: 10px;
  font-size: 17px;
  color: white;
  transition: all 0.3s ease 0s;
  text-decoration: none;
}}

.our-team .social li a:hover {{
  color: #FF4B4B;
  background-color: #f7f5ec;
}}
</style>
<div class="container">
  <div class="row">
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="our-team">
        <div class="picture">
          <img class="img-fluid" src="https://picsum.photos/130/130?image=1027">
        </div>
        <div class="team-content">
          <h3 class="name">Michele Miller</h3>
          <h4 class="title">Founder</h4>
        </div>
        <ul class="social">
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
        </ul>
      </div>
    </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="our-team">
        <div class="picture">
          <img class="img-fluid" src="https://picsum.photos/130/130?image=839">
        </div>
        <div class="team-content">
          <h3 class="name">Patricia Knott</h3>
          <h4 class="title">Developer</h4>
        </div>
        <ul class="social">
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
        </ul>
      </div>
    </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="our-team">
        <div class="picture">
          <img class="img-fluid" src="https://picsum.photos/130/130?image=856">
        </div>
        <div class="team-content">
          <h3 class="name">Justin Ramos</h3>
          <h4 class="title">Manager</h4>
        </div>
        <ul class="social">
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
        </ul>
      </div>
    </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="our-team">
        <div class="picture">
          <img class="img-fluid" src="https://picsum.photos/130/130?image=836">
        </div>
        <div class="team-content">
          <h3 class="name">Mary Huntley</h3>
          <h4 class="title">Designer</h4>
        </div>
        <ul class="social">
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
          <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
              """,unsafe_allow_html=True)
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