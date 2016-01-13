#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
  
$session = CGI::Session->load();
$input = new CGI;
 



if($session->is_expired or $session->is_empty)
{
    print $input->header(-cache_control=>"no-cache, no-store, must-revalidate");

print <<ENDHTML;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Error Sign In</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Error Login page - Associazione calcistica dilettantistica Camponogarese" />
	  <meta name="description" content="Pagina error login A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,login" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
	</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
  <div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="../html/index.html">Home</a></span>&gt Error Login</p></div>
  <div id="fail"> <img src="../immagini/failLog.jpg" ></img></div>
	<div id="section">
	<h1>La sessione e' scaduta o non hai effettuato l'accesso!</h1>
	<p>Effettuare nuovamente il login.</p>
		<form action="../cgi-bin/accesso1.cgi" method="post">
			<fieldset>
				<legend>Login amministratore</legend>
				<label for="username">Username</label>
				<input class="casella_input" name="username" id="user" value="user" maxlength="20" />
				<label for="password">Password</label>
				<input class="casella_input" type="password" name="pwd" id="password" value="pwd" maxlength="20" />
				<input type="submit" value="Accedi"></input>
			</fieldset>
		</form>
</div>
</body>
</html>

ENDHTML
}
else{
    print $input->header(-cache_control=>"no-cache, no-store, must-revalidate");
   
print <<ENDHTML;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Pannello di controllo</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Pannello di controllo amministratore - A.C.D. Camponogarese" />
	  <meta name="description" content="Pagina principale del sito A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,login" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
	</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
  <div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="../html/index.html">Home</a></span>&gt <span xml:lang="en">
  Control Panel</span></p></div>
 	<div id="menu">
	<ul>
			<!--<li id="CurrentLink"><span xml:lang="en">Control Panel</span></li> -->
			<li><a href="../html/amministratore.html">Gestione personale</a></li>
			<li><a href="">Gestione calendario</a></li>
			<li><a href='logout.cgi'>Logout</a></li>
		</ul>
	</div>
	<div id="section">
	<h2>Benvenuto</h2> 
<img src="../immagini/wellcome.jpg" ></img>

	<form action="../cgi-bin/aggiungiPersonale.cgi" method="post">
		<fieldset>
			<legend>Aggiungi organizzazione</legend>
			<input type="submit" value="aggiungi" name="aggiungi"></input>
		</fieldset>
	</form>
</div>
</body>
</html>

ENDHTML
    
    
}



