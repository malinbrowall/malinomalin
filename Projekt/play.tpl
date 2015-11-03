<!DOCTYPE html>
<html>
  <head>
    <title>Radio</title>
    <link rel="stylesheet" href="/static/css.css" type="text/css">
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
  </head>
    <body>
      <h1>Diggypy.</h1> 
      <div id="box" >
        <p>{{text}}</p>
        <p>{{sr_song}}</p>
        % if spoty != None:
          <p><a href="{{spoty}}">Länk till Spotify</a></p>
       
      </div>
   

</body>
</html>