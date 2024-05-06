from turtle import width
import streamlit as st
def app():
    st.markdown(f"""
<style>
              @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
* {{
  margin: 0;
  padding: 0;
  font-family: "Poppins", sans-serif;
}}

html,
body {{
  height: 100%;
  width: 100%;
}}
body {{
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.container {{
  width: 100%;
  height: 100%;
  max-width: 1200px; /* Added max-width for better readability on larger screens */
  background: #fff;
  padding: 20px 60px 30px 40px;
  
}}

.container .content {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}}

.container .content .left-side {{
  width: 25%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 15px;
  position: relative;
}}

.content .left-side::before {{
  content: '';
  position: absolute;
  height: 70%;
  width: 2px;
  right: -15px;
  top: 50%;
  transform: translateY(-50%);
  background: #afafb6;
}}

.content .left-side .details {{
  margin: 14px;
  text-align: center;
}}

.content .left-side .details i {{
  font-size: 30px;
  color: #ff4b4b;
  margin-bottom: 10px;
}}

.content .left-side .details .topic {{
  font-size: 18px;
  font-weight: 500;
}}

.content .left-side .details .text-one,
.content .left-side .details .text-two {{
  font-size: 14px;
  color: #afafb6;
}}

.container .content .right-side {{
  width: 75%;
  margin-left: 75px;
}}

.content .right-side .topic-text {{
  font-size: 23px;
  font-weight: 600;
  color: #ff4b4b;
}}

.right-side .input-box {{
  height: 50px;
  width: 100%;
  margin: 12px 0;
}}

.right-side .input-box input,
.right-side .input-box textarea {{
  height: 100%;
  width: 100%;
  border: none;
  outline: none;
  font-size: 16px;
  background: #f0f1f8;
  padding: 5px;
  resize: none;
}}

.right-side .message-box {{
  min-height: 110px;
}}

.right-side .input-box textarea {{
  padding-top: 6px;
}}

.right-side .button {{
  display: inline-block;
  margin-top: 12px;
}}

.right-side .button input[type="button"] {{
  color: #fff;
  font-size: 18px;
  outline: none;
  border: none;
  padding: 8px 16px;
  background: #3e2093;
  cursor: pointer;
  transition: all 0.3s ease;
}}

.button input[type="button"]:hover {{
  background: #5029bc;
}}

@media (max-width: 950px)
  .container {{
    width: 100%;
    padding: 30px 40px 40px 35px;
  }}

  .container .content .right-side {{
    width: 100%;
    margin-left: 55px;
  }}

@media (max-width: 820px) {{
  .container {{
    margin: 40px 0;
    height: auto;
  }}

  .container .content {{
    flex-direction: column-reverse;
  }}

  .container .content .left-side {{
    width: 100%;
    flex-direction: row;
    margin-top: 80px;
    justify-content: center;
  }}

  .container .content .left-side::before {{
    display: none;
  }}

  .container .content .right-side {{
    width: 100%;
    margin-left: 0;
  }}
}}

               </style>
<!-- Created By CodingLab - www.codinglabweb.com -->
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8">
    <title> Contact Us Form  | CodingLab </title>
    <link rel="stylesheet" href="style.css">
    <!-- Fontawesome CDN Link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"/>
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
   </head>
<body>
  <div class="container">
    <div class="content">
      <div class="left-side">
        <div class="address details">
          <i class="fas fa-map-marker-alt"></i>
          <div class="topic">Address</div>
          <div class="text-one"> Flat-No-502 Mathru Chaya Complex, 16-11-767</div>
          <div class="text-two">East Prasanth Nagar, Moosarambagh</div>
          <div class="text-two"> Hyderabad, Telangana 500036</div>
        </div>
        <div class="phone details">
          <i class="fas fa-phone-alt"></i>
          <div class="topic">Phone</div>
          <div class="text-one">+91 8790207755</div>
        </div>
        <div class="email details">
          <i class="fas fa-envelope"></i>
          <div class="topic">Email</div>
          <div class="text-one">office@atya.co.in</div>
        </div>
      </div>
      <div class="right-side">
        <div class="topic-text">Send us a message</div>
        <p>If you have any work from me or any types of quries related to my tutorial, you can send me message from here. It's my pleasure to help you.</p>
      <form action="#">
        <div class="input-box">
          <input type="text" placeholder="Enter your name">
        </div>
        <div class="input-box">
          <input type="text" placeholder="Enter your email">
        </div>
        <div class="input-box">
          <input type="text" placeholder="Mobile number">
        </div>
        <div class="input-box message-box">
          <input type="text_area" placeholder="Enter your Message here"
        </div>
  </div>
</body>
</html>
""", unsafe_allow_html=True)
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