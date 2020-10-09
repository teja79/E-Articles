import cgi,cgitb
cgitb.enable()
import sqlite3 as s
conn=s.connect('articles.db')
d=conn.execute('''select a.name,a.aid from articles a,status s where a.aid=s.aid and status=0''')
data=d.fetchall()
l=len(data)

print('Content-type:text/html')
print()
print('''<!--
Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html lang="en">
<head>
<title>REJECTED ARTICLES</title>
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
			<h1>List Of Articles...</h1>
		</div>
		<div class="btn-group">
		<a href="adminfirst.py" class="button1">Back</a>
		<a href="/contact1.html" class="button1">contact</a>
		<a href="/about1.html" class="button1">about</a></div>
		<!--//header-->
		<!--main--><br>
		<div class="main-content-agile">
		
			<div class="sub-main-w3lm">	
							 <center><table align="center">
			    <th><h2><u>Titles</u></h2></th><br><br><br>''')
for i in range(0,l):
        print('''
         <form action="adminshowdecidearticles.py" method="post">
         <input type="hidden" value="''',data[i][1],'''" name="name"/>


''')
        print('''<tr><td><input type="submit" value="''',data[i][0],'''"   class="button"><br><br>
</form>''')

print('''</table></center>
           
    
                       <br><br><br>

					<div class="social-icons"> 
														<ul>
								<li><a href="https://www.facebook.com/E-articles-1988839161361891/"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="https://twitter.com/E_Articles_v1"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="https://plus.google.com/u/0/116741618579126612165"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>
						</div></div>
					<br><br><br></div>
			
		
		<!--//main-->
		<!--footer-->
		<div class="footer">
			<p>&copy;  All rights reserved | Design by <a href="https://www.facebook.com/Sandeep.kolli">Sandeep Kolli</a></p>
		
		<!--//footer-->
	</div><br><br><br><br><br><br><br><br><br><br><br></div>
</div>
<!-- js -->
<script type="text/javascript" src="js/jquery-2.1.4.min.js"></script><!--common-js-->
<script src="js/jquery.vide.min.js"></script><!--video-js-->
<!-- //js -->
</body>
</html>
''')
conn.commit()
conn.close()
