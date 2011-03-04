<%inherit file="base.mako"/>

<h1>Welcome to QRCard. Submit your form</h1>
<form action="/cards/${uuid}" method="post">
    <label for="name">Name</label> <input type="text" name="name"/><br/>
    <label for="company">Company</label>  <input type="text" name="company"/><br/>
    <label for="phone.work">Work</label>  <input type="tel" name="phone.work"/><br/>
    <label for="phone.mobile">Mobile</label>  <input type="tel" name="phone.mobile"/><br/>
    <label for="phone.home">Home</label>  <input type="tel" name="phone.home"/><br/>
    <label for="email">Email</label> <input type="text" name="email"/><br/>
    <button type="submit">Submit</button>
</form>
