#from os import environ
import cgi, cgitb
cgitb.enable()
form=cgi.FieldStorage()
aid=form.getvalue('name')
import sqlite3 as s
conn=s.connect('articles.db')
d=conn.execute('''select content from articles where aid=?''',(aid,))
data1=d.fetchall()
l=len(data1)
if(l==1):
    print("Content-type:text/html")
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
<title>Modern Login Form Responsive Widget Template :: w3layouts</title>
<!-- Meta tag Keywords -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/png" href="/favicon.png" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
			<h1>Editnow..</h1>
		</div>
		<!--//header-->
		<!--main-->
		<div class="head-but">
		<a href="editarticle.py" class="button1">Back</a> </div><br>
		<div class="main-content-agiless">
		
			<div class="sub-main-w3lm">	
				<h2>Content</h2><br>
			<form action="updatearticle.py" method="post">
			<input type="hidden" value="''',aid,'''" name="name"/>
				
                  <textarea name="cont" rows="20" cols="80">''',data1[0][0])
          
    print(''' </textarea><br><br><br>
		     <input type="submit" value="Update" class="button"><br><br>
                     <input type="reset" value="Reset" class="button"><br><br> 
                   
            </form>
                       <br><br><br>

					<div class="social-icons"> 
							<ul>
								<li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="#"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>  
						</div>
					<br><br><br>
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
conn.commit()
conn.close()

    
