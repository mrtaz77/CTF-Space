# Don't Hide Me
## Category : Forensics
## Points : 500(dynammic)
I have a super-secret message for my friend, who isn't very tech-savvy and lacks expertise in IT. As the message is highly confidential, I need to conceal it within eight categorized images, each numbered, to guide him through the process. However, despite this assistance, he still struggles to understand the process. Could you please help him uncover the super-secret message?

Note:I use numbers such as 1, 2, 3, etc., to facilitate understanding which image comes next

Attachments:
[Link 1](https://drive.google.com/drive/folders/104C8Fx7W9HWxiuK0vDMCwYWrRhsnGGp0?usp=sharing)

The __folder__ 7 images followed by a final `HereIam`.
![img](/CTFs/CyberCrawler_2023/Forensics/Dont%20Hide%20me/hideMe.png)

From the note, I noticed an order among the first 7 images.Taking the letters which followed the numbering of the images , I got `DREAMDU`.

I thought this is the password.

I went to this [website](https://futureboy.us/stegano/decinput.html), pasted the image and gave the pwd and got the flag.

Flag:
```
C3{Ev3Ry_Th1nG_H4s_It'S_OWN_CluE}
```