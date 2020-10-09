from os import environ
import cgi, cgitb
if 'HTTP_COOKIE' in environ:
    cookies = environ['HTTP_COOKIE']
    cookies = cookies.split(';')
    for cookie in cookies:
      (key, value ) = cookie.split('=')
      if key == "Email":
         em = value

import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
name=form.getvalue('name')
catagery=form.getvalue('cars')
content=form.getvalue('content')
import sqlite3 as s
conn=s.connect('articles.db')
conn.execute('''insert into articles(name,category,content) values(?,?,?)''',(name,catagery,content))
conn.commit()
conn.close()
conn1=s.connect('articles.db')
d=conn1.execute('''select aid from articles where aid=(select max(aid) from articles)''')
data=d.fetchall()
conn1.commit()
conn1.close()
conn2=s.connect('articles.db')
conn2.execute('''insert into uart values(?,?)''',(data[0][0],em))
print('Content-type:text/html')
print()
print('''
<!--Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html lang="en">
<head>
<title>Modern Login Form Responsive Widget Template :: w3layouts</title>
<!-- Meta tag Keywords -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/png" href="/favicon.png" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Modern Login Form Responsive Widget,Login form widgets, Sign up Web forms , Login signup Responsive web form,Flat Pricing table,Flat Drop downs,Registration Forms,News letter Forms,Elements" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Meta tag Keywords -->
<!-- css files -->
<link rel="stylesheet" href="/css/style.css" type="text/css" media="all" /> <!-- Style-CSS --> 
<link rel="stylesheet" href="/css/font-awesome.css"> <!-- Font-Awesome-Icons-CSS -->
<!-- //css files -->
<!-- web-fonts -->
<link href="//fonts.googleapis.com/css?family=Snippet" rel="stylesheet"><!--online fonts-->
<!-- //web-fonts -->
</head>
<body style="background-image:url(/888.jpg)">
	<div class="main-container">
		<!--header-->
		<div class="header-w3l">
			<h1>WELCOME''',em,'''</h1>
		</div>
		
		<!--//header-->
		<!--main-->
		<div class="main-content-agile">
			<div class="w3ls-pro">
				
			</div>
			<div class="sub-main-w3ls">	
				<form action="#" method="post">
                                     
                                 <a href="updateprofile.py" class="button">   Your Profile  </a> <br><br><br>
                                   <a href="writepage.py" class="button">    Write Articles    </a> <br><br><br>
                                    <a href="readarticle.py" class="button">    Read Articles   </a> <br><br><br> 
                                      <a href="editarticle.py" class="button">    Edit Articles    </a> <br><br><br>
                                      <a href="out.py" class="button">    Logout   </a> <br><br><br>
                                      

					<div class="social-icons"> 
							<ul>
								<li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="#"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>  
						</div>
					<input type="submit" value="">
				</form>
			</div>
		</div>
		<!--//main-->
		<!--footer-->
		<div class="footer">
			<p>&copy; 2017 modern Login Form. All rights reserved | Design by <a href="http://w3layouts.com">W3layouts</a></p>
		</div>
		<!--//footer-->
	</div>
</div>
<!-- js -->
<script type="text/javascript" src="js/jquery-2.1.4.min.js"></script><!--common-js-->
<script src="js/jquery.vide.min.js"></script><!--video-js-->
<!-- //js -->
</body>
</html>
''')
conn2.commit()
conn2.close()


