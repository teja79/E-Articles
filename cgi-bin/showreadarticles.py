import cgi, cgitb
cgitb.enable()
form=cgi.FieldStorage()
name=form.getvalue('aid')
import sqlite3 as s
conn=s.connect('articles.db')
d=conn.execute('''select content,category,name from articles where aid=?''',(name,))
data1=d.fetchall()
d1=conn.execute('''select status from status where aid=?''',(name,))
data2=d1.fetchall()
l=len(data1)
l1=len(data2)
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
			<h1>Read.....</h1>
		</div>
		<!--//header-->
		<!--main-->
		<div class="head-but">
		<a href="/cgi-bin/readarticle.py" class="button1">Back</a> </div><br>
		<div class="main-content-agiless">
		
			<div class="sub-main-w3lm">	
				<h2>TITLE</h2><br><br>
			<form action="#" method="post">
			<input type="text" value="''',data1[0][2],'''"><br><br><br>
                         <h2>CATAGERY</h2><br><br>

			<input type="text" value="''',data1[0][1],'''"><br><br><br>
			
			<h2>CONTENT</h2><br><br>	
                  <textarea name="content" rows="20" cols="80">''',data1[0][0],'''
          
</textarea><br><br><br>
              <h2>Status of the Article</h2><br><br>
             <input type="text"

''')
if(data2==[]):
    stat='UnderProcessing'
else:
    if(data2[0][0]==1):
        stat='Accepted'
    if(data2[0][0]==0):
        stat='Rejected'
    
print('''value="''',stat,'''"/><br><br><br>
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

    
