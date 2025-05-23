# Web Design for a Manufacturing Company
## AIM: 
To design a static website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel="icon" href="{% static 'img/logo.jpg' %}" type="image/x-icon">
</head>

<body>
    <div class="container">
        <div class="banner">
            Silicon Private Limited.
        </div>
        <div class="menu">
            <div class="menuitem"><a href="/home">Home</a></div>
            <div class="menuitem"><a href="/products">Products</a></div>
            <div class="menuitem"><a href="/people">People</a></div>
            <div class="menuitem"><a href="/contact">Contact Us</a></div>
        </div>
        <div class="content">
            {% block content %}
            {% endblock  %}
        </div>
        <div class="footer">
            Copyright © 2020 Silicon Private Limited, Developed by Vincent isaac jeyaraj.
        </div>
    </div>
    
</body>

</html>
```

### home.html
```
{% extends "website/base.html" %}

{% block content %}
<div class="homecontent">
    <h1>About Us</h1>
    <img src="/static/img/company.jpg" alt="Building">
    <div class="contenttext">
        Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the
        data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications
        for its products include: data center networking, home connectivity, broadband access, telecommunications
        equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and
        alternative energy systems, displays, and mainframe operations and management, and application software
        development. Some of Silicon's core technologies and products include:
        <ul>
            <li>Memory Chips</li>
            <li>SATA HDD</li>
            <li>SATA SSD </li>
            <li>Broadband Modems</li>
            <li>Wifi Devices</li>
            <li>Switching Devices</li>
            <li>Optical Sensors</li>
        </ul>
    </div>
</div>
{% endblock  %}
```
### products.html
```
{% extends "website/base.html" %}

{% block content %}
<div class="productcontent">
    <h1 style="text-align:center;"><u>Our Premium Products</u></h1>
    <div class="productitems">
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/HyperX-3200MHz-Desktop-Memory-HX432C16FB3/dp/B07WJJ9CNG/">
                    <img src="/static/img/8gbram.jpg" alt="product image">
                </a>
            </div>
            <div class="itemname">HyperX Fury 8GB 3200MHz DDR4 CL16 DIMM 1Rx8 Black XMP Desktop Memory</div>
            <div class="itemprice">Price:₹ 3,290.00 </div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Corsair-Vengeance-1x16GB-PC4-25600-Optimized/dp/B08D6H22Y3/">
                    <img src="/static/img/16gbram.jpg" alt="product image">
                </a>
            </div>
            <div class="itemname">Corsair Vengeance RGB Pro 16GB (1x16GB) DDR4 3200 (PC4-25600) C16 Optimized for
                AMD Ryzen – Black</div>
            <div class="itemprice">Price:₹ 7,295.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Seagate-FireCuda-Internal-Solid-State/dp/B088GDXKP3/">
                    <img src='/static/img/1tb-sata-ssd.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Seagate FireCuda 120 SSD 1TB Internal Solid State Drive – SATA 6Gb/s 3D TLC for
                Gaming PC Laptop (ZA1000GM10001)</div>
            <div class="itemprice">Price:₹ 17,499.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Seagate-Barracuda-Internal-Solid-State/dp/B07ZPRJFV1/">
                    <img src='/static/img/1tb-ssd.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Seagate Barracuda 120 SSD 1TB Internal Solid State Drive – 2.5 Inch SATA 6Gb/s for
                Computer Desktop PC Laptop (ZA1000CM1A003)</div>
            <div class="itemprice">Price:₹ 11,499.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Seagate-BarraCuda-ST1000DM010-Desktop-Latest/dp/B01LNJBA2I/">
                    <img src='/static/img/1tb-hhd.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Seagate BarraCuda 1 TB Internal Hard Drive HDD – 3.5 Inch SATA 6 Gb/s 7200 RPM 64
                MB Cache for Computer Desktop PC (ST1000DM010)</div>
            <div class="itemprice">Price: ₹ 3,407.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Western-Digital-WD10EZEX-Internal-Desktop/dp/B0088PUEPK/">
                    <img src='/static/img/1tb-sata-hhd.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Western Digital WD10EZEX 1TB Internal Hard Drive for Desktop (Blue)</div>
            <div class="itemprice">Price: ₹ 3,200.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/TP-LINK-TD-W8961N-300Mbps-Antenna-Wireless/dp/B00RK5VU5M/">
                    <img src='/static/img/modem.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">TP-LINK TD-W8961N Wireless N300 ADSL2+ Wi-Fi Modem Router, 2x 5dBi Omni
                directional Fixed antennas, Input ISPs supported- BSNL, MTNL, Tata Indicom (RJ-11 Port)</div>
            <div class="itemprice">Price:₹ 1,279.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href=https://www.amazon.in/TP-Link-Archer-C1200-Gigabit-Wireless/dp/B01IUDUJE0/ref>
                    <img src='/static/img/modems.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">TP-Link Archer C1200 Dual Band Gigabit Wireless Cable Router, Wi-Fi Speed Up to
                867 Mbps/5 GHz + 300 Mbps/2.4 GHz, 4 Gigabit LAN Ports, 1 USB Port, Broadcom Chipset</div>
            <div class="itemprice">Price:₹ 2,549.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/Netgear-Orbi-RBK50-System-White/dp/B01K4CZOBS/">
                    <img src='/static/img/wifi-divice.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Netgear Orbi RBK50 Tri Band Mesh WiFi System (White)</div>
            <div class="itemprice">Price:₹ 24,775.00</div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                <a href="https://www.amazon.in/D-Link-DWA-131-Wireless-Adapter-Black/dp/B002PD61Y4/">
                    <img src='/static/img/wifi.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">D-Link DWA-131 Wireless N Nano USB Adapter (Black)</div>
            <div class="itemprice">Price:₹ 589.00 </div>
        </div>
        <div class="productitem">
            <div class="itemimage"><a
                    href="https://www.amazon.in/Ambrane-WiFi-Smart-Plug-10A/dp/B0819RVZ12/">
                    <img src='/static/img/switch.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">Ambrane WiFi Smart Plug 10A - Control Your Devices from Anywhere, No Hub Required,
                Compatible with Alexa and Google Assistant (ASP-10, White)</div>
            <div class="itemprice">Price:₹ 899.00 </div>
        </div>
        <div class="productitem">
            <div class="itemimage">
                   <a href="https://www.amazon.in/ENTERPRISE%C2%AE-Version-Switch-Splitter-Pigtail/dp/B083GZHWKC/">
                    <img src='/static/img/switchs.jpg' alt="produtct image" width="150" height="200">
                </a>
            </div>
            <div class="itemname">A N ENTERPRISE® 3 Port HDMI 4 K 1.4V Version Switch Splitter with Pigtail Cable
                for Fire Stick, Xbox One, PS3, 4, TV (Black) </div>
            <div class="itemprice">Price: ₹ 549.00</div>
        </div>
    </div>
</div>
{% endblock  %}
```
### people.html
```
{% extends "website/base.html" %}

{% block content %}
    <h1 id="Ex">Executives</h1>
    <div class="row">
        <div class="column">
            <h2>Bill gates</h2>
            <img src="/static/img/bill.jpg" alt="executive image" width="250" height="300">
            <P>Founder</P>
        </div>
        <div class="column">
            <h2>Nadella</h2>
            <div class="img">
            <img src="/static/img/Nadella-Satya.jpg" alt="executive image" width="250" height="300">
            </div>
            <p>Chief Executive Officer (CEO)</p>
        </div>
        <div class="column">
            <h2>Amy Hood</h2>
            <img src="/static/img/Amy-Hood.jpg" alt="executivet image" width="250" height="300">
            <p>Chief Financial Officer (CFO)</p>
        </div>
        <div class="column">
            <h2>Rajiv Sodhi</h2>
            <img src="/static/img/Rajiv-Sodhi-profile.jpg" alt="executive image" width="250" height="300">
            <p>Chief Operating Office (COO)</p>
        </div>
        <div class="column">
            <h2>Jim DuBois</h2>
            <img src="/static/img/jimdubois.jpg" alt="executive image" width="250" height="300">
            <p>Chief Information Officer (CIO)</p>
        </div>
        <div class="column">
            <h2>Chris Capossela</h2>
            <img src="/static/img/Chris-Capossela.jpg" alt="executive image" width="250" height="300">
            <P>Chief Marketing Officer (CMO)</P>
        </div>
    </div>

{% endblock  %}
```
### contact.html
```
{% extends "website/base.html" %}

{% block content %}
<p class="free">

</p>
<div class="contain">
    <div class="image">
        <img src="/static/img/dail.png" alt="contact" width="50" height="50">
    </div>
    <div class="text">
        <h1>+044 40405667/50504667</h1>
    </div>
</div>
<div class="contain">
    <div class="image">
        <img src="/static/img/mail.png" alt="contact" width="50" height="50">
    </div>
    <div class="text">
        <h1>siliconpvt.ltd@gmail.com</h1>
    </div>
</div>
<div class="contain">
    <div class="image">
        <img src="/static/img/address.png" alt="contact" width="50" height="50">
    </div>
    <div class="text">
        <h1>New york City, 145,Redmond,Washington, United States</h1>
    </div>
</div>

{% endblock  %}
```
## OUTPUT:
![output](./static/img/Image-5.png)

![output](./static/img/Image-6.png)

![output](./static/img/Image-7.png)

![output](./static/img/Image-8.png)

![output](./static/img/Image-9.png)

![output](./static/img/Image-10.png)

## CODE VALIDATION REPORT:
![output](./static/img/Image-1.png)

![output](./static/img/Image-2.png)

![output](./static/img/Image-3.png)

![output](./static/img/Image-4.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://vincent.student.saveetha.in:8000/. HTML code is validated.