# Sanity Check In Space WEB


## Problem

Man, web exploitation sure is fun. Sometimes you just need to go back to the basics, you know what I mean? Everything you need to get started on your journey to becoming a web master is here.

p.s: You can make anything space themed if you try hard enough.

http://scis.hackers.best:31337/

## Solution

Single Page Website

![WebSite](./src/s1.png)

as usual checks the inspect panel and robots.txt

![s2](./src/s2.png)

it shows human.txt

![s3](./src/s3.png)
and
![s4](./src/s4.png)

taking the hint to check verify as human and the cookie in picture.I changed the cookie human value from false to true

![s5](./src/s5.png)
visiting arrakis as per the hint

![s6](./src/s7.png)
asks to enter the password 
password is in the view-source 
![s7](./src/s6.png)

Next is input tab to ping a website.

![s8](./src/s8.png)


The playload is
```bash
;cat flag.txt
```
![s9](./src/s9.png)

```bash
Flag: shctf{exp01ting_w3bs1tes_1N_SP@C3}
```





