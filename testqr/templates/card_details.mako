<%inherit file="base.mako"/>

<h1>${card.name}</h1>
<h2>Company: ${card.company}</h2>

<img src="http://chart.apis.google.com/chart?chs=200x200&cht=qr&chl=${url}" width="200" height="200" alt="" />

<ul data-role="listview" data-inset="true" data-theme="d">
    <li data-role="list-divider">Contact Information</li>
    <li>Mobile: <a href="tel:${card.phone_mobile}">${card.phone_mobile}</a></li>
    <li>Home: <a href="tel:${card.phone_home}">${card.phone_home}</a></li>
    <li>Work: <a href="tel:${card.phone_work}">${card.phone_work}</a></li>
    <li class="human-placeholder">Email: 
        <a href="#human_popup" data-rel="dialog"
        data-transition="slidedown">hidden for security</a></li>
    <li class="human-proved">Email: <a href="mailto:${card.email}">${card.email}</a></li>
    <li><a href="${url}/downloads/vcard.vcf">Download vCard</a></li>
</ul>

<%def name="additional_content()">
<div data-role="page" id="human_popup">
    <div data-role="content">
        <h1>Are you a human?</h1>
        <a href="#" data-rel="back" data-role="button" class="yes">Yes I am</a>
    </div>
</div>
</%def>


<%def name="head_content()">
<style type="text/css" media="screen">
    .human-proved {
        display: none;
    }
</style>
<script type="text/javascript" charset="utf-8">
    
    $(function() {
        var human = false;

        $('#main').live('pageshow',function(event){
          if(human) {
              $('.human-placeholder').hide();
              $('.human-proved').show();
          }
        });
        
        $('#human_popup a.yes').click(function() {
            human = true;
        });
    });
</script>
</%def>