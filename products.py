import streamlit as st
from streamlit_option_menu import option_menu
def app():
  st.markdown("<h1 style='text-align: center; color: Black;'>Our Products</h1>", unsafe_allow_html=True)
  st.write("At EmbedView Solutions, our commitment lies in pioneering innovation and providing clients with unparalleled value through comprehensive hardware and software development solutions. Leveraging expertise, creativity, and state-of-the-art technology, we empower businesses to seize new prospects, optimize operations, and foster sustainable growth in an ever-evolving digital landscape.")
  st.markdown(f"""
              <style>
              @import url("https://fonts.googleapis.com/css?family=Cardo:400i|Rubik:400,700&display=swap");
:root {{
  --d: 700ms;
  --e: cubic-bezier(0.19, 1, 0.22, 1);
  --font-sans: "Rubik", sans-serif;
  --font-serif: "Cardo", serif;
}}
* {{
  box-sizing: border-box;
}}
html,
body {{
  height: 100%;
}}
body {{
  display: grid;
  place-items: center;
  background-color: black;
}}
.page-content {{
  display: grid;
  grid-gap: 1rem;
  padding: 1rem;
  max-width: 1024px;
  margin: 0 auto;
  font-family: var(--font-sans);
}}
@media (min-width: 600px) {{
  .page-content {{
    grid-template-columns: repeat(2, 1fr);
  }}
}}
@media (min-width: 800px) {{
  .page-content {{
    grid-template-columns: repeat(4, 1fr);
  }}
}}
.card {{
  position: relative;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
  padding: 1rem;
  width: 100%;
  text-align: center;
  color: whitesmoke;
  background-color: whitesmoke;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1), 0 2px 2px rgba(0, 0, 0, 0.1),
    0 4px 4px rgba(0, 0, 0, 0.1), 0 8px 8px rgba(0, 0, 0, 0.1),
    0 16px 16px rgba(0, 0, 0, 0.1);
}}
@media (min-width: 600px) {{
  .card {{
    height: 350px;
  }}
}}
.card:before {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 110%;
  background-size: cover;
  background-position: 0 0;
  transition: transform calc(var(--d) * 1.5) var(--e);
  pointer-events: none;
}}
.card:after {{
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 200%;
  pointer-events: none;
  background-image: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.009) 11.7%,
    rgba(0, 0, 0, 0.034) 22.1%,
    rgba(0, 0, 0, 0.072) 31.2%,
    rgba(0, 0, 0, 0.123) 39.4%,
    rgba(0, 0, 0, 0.182) 46.6%,
    rgba(0, 0, 0, 0.249) 53.1%,
    rgba(0, 0, 0, 0.32) 58.9%,
    rgba(0, 0, 0, 0.394) 64.3%,
    rgba(0, 0, 0, 0.468) 69.3%,
    rgba(0, 0, 0, 0.54) 74.1%,
    rgba(0, 0, 0, 0.607) 78.8%,
    rgba(0, 0, 0, 0.668) 83.6%,
    rgba(0, 0, 0, 0.721) 88.7%,
    rgba(0, 0, 0, 0.762) 94.1%,
    rgba(0, 0, 0, 0.79) 100%
  );
  transform: translateY(-50%);
  transition: transform calc(var(--d) * 2) var(--e);
}}
.card:nth-child(1):before {{
  background-image: url(https://i.imgur.com/8XVyWeY.jpeg);
}}
.card:nth-child(2):before {{
  background-image: url(https://i.imgur.com/5rUlT3c.jpeg);
}}
.card:nth-child(3):before {{
  background-image: url(https://i.imgur.com/aVm4INe.jpeg);
}}
.card:nth-child(4):before {{
  background-image: url(https://i.imgur.com/5huz1p3.jpeg)}}
.content {{
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 1rem;
  transition: transform var(--d) var(--e);
  z-index: 1;
}}
.content > * + * {{
  margin-top: 1rem;
}}
.title {{
  font-size: 1.3rem;
  font-weight: bold;
  line-height: 1.2;
}}
.copy {{
  font-family: var(--font-serif);
  font-size: 1.125rem;
  font-style: italic;
  line-height: 1.35;
}}
.btn {{
  cursor: pointer;
  margin-top: 1.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.65rem;
  font-weight: bold;
  letter-spacing: 0.025rem;
  text-transform: uppercase;
  color: white;
  background-color: black;
  border: none;
}}
.btn:hover {{
  background-color: #0d0d0d;
}}
.btn:focus {{
  outline: 1px dashed yellow;
  outline-offset: 3px;
}}
@media (hover: hover) and (min-width: 600px) {{
  .card:after {{
    transform: translateY(0);
  }}
  .content {{
    transform: translateY(calc(100% - 4.5rem));
  }}
  .content > *:not(.title) {{
    opacity: 0;
    transform: translateY(1rem);
    transition: transform var(--d) var(--e), opacity var(--d) var(--e);
  }}
  .card:hover,
  .card:focus-within {{
    align-items: center;
  }}
  .card:hover:before,
  .card:focus-within:before {{
    transform: translateY(-4%);
  }}
  .card:hover:after,
  .card:focus-within:after {{
    transform: translateY(-50%);
  }}
  .card:hover .content,
  .card:focus-within .content {{
    transform: translateY(0);
  }}
  .card:hover .content > *:not(.title),
  .card:focus-within .content > *:not(.title) {{
    opacity: 1;
    transform: translateY(0);
    transition-delay: calc(var(--d) / 8);
  }}
  .card:focus-within:before,
  .card:focus-within:after,
  .card:focus-within .content,
  .card:focus-within .content > *:not(.title) {{
    transition-duration: 0s;
  }}
    .title{{
              color:white;
    }}
}}
</style>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <main class="page-content">
      <div class="card">
        <div class="content">
          <h2 class="title">Humidity Sensors</h2>
          <p class="copy">
           Humidity sensors are utilized across 
           various fields to monitor moisture levels, including agriculture, meteorology, and industrial processes.
          </p>
        </div>
      </div>
      <div class="card">
        <div class="content">
          <h2 class="title">Temperature Sensors</h2>
          <p class="copy">
            Temperature sensors are employed in diverse sectors for monitoring heat levels, including climate control,
            manufacturing, and automotive systems.
          </p>
        </div>
      </div>
      <div class="card">
        <div class="content">
          <h2 class="title">Pressure Sensors</h2>
          <p class="copy">Pressure sensors are utilized across numerous applications to measure force exerted on a surface, such as in aerospaceautomotive
          and medical devices.</p>
        </div>
      </div>
      <div class="card">
        <div class="content">
          <h2 class="title">Force Sensors</h2>
          <p class="copy">
            Force sensors measure applied force in various applications like robotics.
          </p>
        </div>
      </div>
    </main>
  </body>
</html>
                 """,unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center; color: Black;'>How do Sensor's Work</h1>", unsafe_allow_html=True)
  st.markdown("""
<h1>Humidity sensor</h1>
<p>It is a device that measures the amount of moisture in the air. It's like a tiny weather station inside your home or device. It helps you know if the air is dry or humid. This information is useful for many things. For example, if the air is too dry, it can help you decide to use a humidifier to add moisture. If it's too humid, you might want to turn on a dehumidifier to remove some moisture. Humidity sensors are also used in weather forecasts and to control things like air conditioning and heating systems for comfort and health.</p>
<h1>Temperature sensor</h1>
<p>It is a device that measures the warmth or coldness of its surroundings. It's like a thermometer that can be used in various gadgets. It helps you understand if the environment is hot, cold, or just right. This information is crucial for many purposes. For example, it helps control heating and cooling systems in homes and buildings to maintain a comfortable temperature. Temperature sensors are also used in weather forecasting, monitoring industrial processes, and ensuring the safe operation of electronic devices by preventing overheating</p>
<h1>Pressure sensor</h1>
<p>It is a device that measures the force exerted by gases or liquids on its surface. It's like a barometer that can be used in various applications. It helps determine if the pressure is high or low in a particular environment. This information is essential for many purposes. For example, pressure sensors are used in weather forecasting to predict changes in atmospheric pressure. They're also crucial in monitoring tire pressure in vehicles for safety and efficiency. In industrial settings, pressure sensors help regulate processes and ensure equipment operates within safe limits.</p>
<h1>Force sensor</h1>
<p>It is a device that measures the amount of force applied to it. It's like a scale that can detect how hard something is pushing or pulling. Force sensors are used in various applications to determine the level of pressure or tension in objects or systems. For instance, they're crucial in industrial machinery to ensure proper functioning and safety by monitoring the force exerted on mechanical parts. In robotics, force sensors help robots interact with their environment delicately, enabling tasks such as object manipulation and assembly.</p>          
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