<html>
<head>
    <title>INDEX</title>
</head>
<h1>Hello {{name}}!</h1>
<ul>
%for item in things:
<li>{{item}}</li>
%end
</ul>

<form action="/fav_fruit" method="POST">
Fav fruit:
<input type="text" name="fruit" size="50">
<input type="submit" value="Submit">
</form>

</html>