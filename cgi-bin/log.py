import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
email=form.getvalue('email')
pwd=form.getvalue('pwd')
ad={'email':'admin@gmail.com','pwd':'admin'}
import sqlite3 as s
conn=s.connect('articles.db')
d=conn.execute('''select * from registration where email=? and pwd=?''',(email,pwd))
data=d.fetchall()
if(email==ad['email'] and pwd==ad['pwd']):
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
<title>welcome ADMIN</title>
<!-- Meta tag Keywords -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="icon" type="image/png" href="/favicon.png" />
<meta http-equiv="refresh" content="5;url=/login.html">
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
			<h1>WELCOME Admin</h1>
		</div>
		<div class="head-but">
		<a href="out.py" class="button1">logout</a> </div>
		
		<!--//header-->
		<!--main-->
		<div class="main-content-agile">
			<div class="w3ls-pro">
				
			</div>
			<div class="sub-main-w3ls">	
				<form action="#" method="post">
                                     
                                  <a href="adminselectedarticles.py" class="button">SelectedArticles</a> <br><br>
                                   <a href="adminrejectedarticles.py" class="button">Rejected Articles</a> <br><br>
                                    <a href="adminreadarticle.py" class="button">All Articles</a><br><br>
                                    <a href="users.py" class="button">Users</a><br><br>
									
                               <br><br><br>


					<div class="social-icons"> 
														<ul>
								<li><a href="https://www.facebook.com/E-articles-1988839161361891/"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="https://twitter.com/E_Articles_v1"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="https://plus.google.com/u/0/116741618579126612165"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>  
						</div>
				    
				</form>
			</div>
		</div>
		<!--//main-->
		<!--footer-->
		<div class="footer">
<p>&copy;  All rights reserved | Design by <a href="https://www.facebook.com/Sandeep.kolli">Sandeep Kolli</a></p>
		</div><br><br><br><br><br><br><br><br>
		<!--//footer-->
	</div>
</div>
</body>
</html>
''')
elif len(data)==1 :
    print('Set-Cookie:Email=',email)
    print ('Set-Cookie:Password=',pwd)
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
<title>WELCOME''',email,'''</title>
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
			<h1>WELCOME''',email,'''</h1>
		</div>
		<div class="head-but">
		<a href="out.py" class="button1">logout</a> </div>
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


					<div class="social-icons"> 
							<ul>
								<li><a href="https://www.facebook.com/E-articles-1988839161361891/"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="https://twitter.com/E_Articles_v1"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="https://plus.google.com/u/0/116741618579126612165"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>  
						</div>
					<br>
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
</body>
</html>
''')

else:
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
<title>Modern Login Form Responsive Widget Template :: w3layouts</title>
<!-- Meta tag Keywords -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="icon" type="image/png" href="/favicon.png" /><meta name="keywords" content="Modern Login Form Responsive Widget,Login form widgets, Sign up Web forms , Login signup Responsive web form,Flat Pricing table,Flat Drop downs,Registration Forms,News letter Forms,Elements" />
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
			
		</div>
		<!--//header-->
		<!--main-->
		<div class="main-content-agile">
			<div class="w3ls-pro">
				<h2>Login Failed</h2>
			</div>
			<div class="sub-main-w3lf">	
				<form action="cgi-bin\log.py" method="post">
					<input placeholder="Enter your E-mail" name="email" type="email" required="">
					
					<input  placeholder="Enter your Password" name="pwd" type="password" required=""><br><br><br>
					 <h3 class="w3ls-pro">Login Failed</h3><br>
				    <a href="/login.html" class="button">Retry</a> <br><br>
					<div class="checkbox-w3">
						<span class="check-w3"><input type="checkbox" />Remember Me</span>
						<a href="#">Forgot Password?</a>
						<div class="clear"></div>
					</div>
					0<div class="social-icons"> 
														<ul>
								<li><a href="https://www.facebook.com/E-articles-1988839161361891/"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
								<li><a href="https://twitter.com/E_Articles_v1"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
								<li><a href="https://plus.google.com/u/0/116741618579126612165"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li> 
							</ul>  
						</div>

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
</body>
</html>''')
conn.commit()
conn.close()
             
