# Don't Forget Me
## Category : Forensics
## Points : 500(dynammic)
My boss's name is Bind. He wants everyone to believe that he has no knowledge about hacking. Thus, if someone were to steal his image, they might assume he doesn't know how to hide messages.

However, I am aware that the boss doesn't do anything straightforward. So, when I found it easy to hide, I thought this wasn't the end. Following that, the boss privately called me and said, 'Don't forget me. I am still alive,' ending the conversation there.

This has left me in a state of confusion. What could the hint 'Don't forget me' mean? Can you decode the hint?

Attachments:

![img](/CTFs/CyberCrawler_2023/Forensics/Dont%20Forget%20me/download-image-png.png)


First half of this challenge was solved by team-mate [3m09](https://github.com/3m09) upto input1.rtf.From there I decoded rest of the flag.

1. Run on the image
```cmd
zsteg -a download-image-png.png
```
2. A github [link](https://github.com/pedrooaugusto/steganography-png) will be obtained .

3. The following [website](https://pedrooaugusto.github.io/steganography-png/) link is present in the repo.

4. Giving the original image in the website and via `find secret`,this [link](https://drive.google.com/file/d/16VMjIxU29O_HnyJShhvV8X_TLP5xL-K_/edit) is found.

5. We get yet another image.
<div align="center">
    <img src="DU1.jpg" alt="img" >
</div>


6. Using binwalk we see that a zip file is present in the image.So we extracted it and got `input1.rtf`

7. I opened this file in _word_.
![img](/CTFs/CyberCrawler_2023/Forensics/Dont%20Forget%20me/first.png)

8. This resembled windings.But a flag cannot contain spaces as seen.Actually, there are symbols in these spaces but they __look__ invisible.So I opened the file again in drive .Finally those darn hidden symbols appeared ;).

![img](/CTFs/CyberCrawler_2023/Forensics/Dont%20Forget%20me/second.png)


9. Simply copied and pasted the windings in the following website [lingogram](https://lingojam.com/WingdingsTranslator) and got the flag.

Flag: 
```
C3{My_Br0Th3R_0xt43q}
```


