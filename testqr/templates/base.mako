<!DOCTYPE html>
<%def name="additional_content()">
</%def>

<%def name="head_content()">
</%def>

<html>
    <head>
        <title>${title or u"Sample Page"} – Test QR</title>
        <link rel="stylesheet" href="/static/styles/jquery.mobile-1.0a3.css">
        <script type="text/javascript" charset="utf-8" src="/static/scripts/jquery-1.5.js"> </script>
        <script type="text/javascript" charset="utf-8" src="/static/scripts/jquery.mobile-1.0a3.js"> </script>
        ${self.head_content()}
    </head>
    <body>
        <div data-role="page" id="main">
        	<div data-role="header">
        		<h1>Page Title</h1>
        	</div><!-- /header -->

        	<div data-role="content">
                ${self.body()}
        	</div><!-- /content -->
        	
        	<div data-role="footer">
        		<h4>Page Footer</h4>
        	</div><!-- /footer -->
        </div><!-- /page -->
        
        ${self.additional_content()}
    	
    </body>
</html>