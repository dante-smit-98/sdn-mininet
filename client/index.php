<?php
	header('Access-Control-Allow-Origin: *');
	header('Access-Control-Allow-Headers: Range');
 ?>

 <!DOCTYPE html>
 <html>
 	<head>
		<script src="dashplayer.js"></script>
	</head>
	<style>
    video {
       width: 640px;
       height: 360px;
    }
</style>
   <body>
     <h1>Adaptive Streaming with HTML5</h1>
       <video data-dashjs-player autoplay src="http://10.0.0.1/webD/Videos/bunny_cartoon/manifest.mpd" controls></video>
   </body>
 </html>
