from os import environ
import cgi, cgitb
if 'HTTP_COOKIE' in environ:
    cookies = environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
      (key, value ) = cookie.split('=')
      if key == "Email":
         email = value
      if key == "Password":
         pwd = value
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
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="icon" type="image/png" href="/favicon.png" />
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
<style>
.fixed-bg {
	background-image: url("/888.jpg");
   
}
</style>
</head>
<body>
<div class="fixed-bg">
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
						<p>&copy;  All rights reserved | Design by <a href="https://www.facebook.com/Sandeep.kolli">Sandeep Kolli</a></p>
		</div>
		<!--//footer-->
	</div>
</div></div>
</body>
</html>
''')
