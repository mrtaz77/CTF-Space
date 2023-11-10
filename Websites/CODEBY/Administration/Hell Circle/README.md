# Hell Circle
## Category : Administration(Misc + Cryptography)
## Points : 200
## Difficulty : Easy
Archives have random names. The password for each archive is a string that is displayed when you try to unarchive it. It is encoded in ROT13→Base64. Decode it and use it as a password.

[Link](https://codeby.games/game_api/files/download?folder=parts_4ed82185-29dc-4508-a863-eb1d81da9fb3_data&name=task&type=zip)

I started opening the `task.zip` in winrar and soon I saw one zip file after another.After the first file , every zip file was password protected.

But I also saw a comment.

From the description, I first base64 decoded the comment and rot13. Turns out it was the `password`!!!

But I saw another zip file and understood there were a lot of zip files.

*__So, its scripting time !__*
I first made a copy of the original zip file `task copy.zip`

Basically just ran a loop.
For each zip file, took its comment and decoded the password from it.
Used that password to open the zip file and stored the extracted zip file in `output` folder.
Deleted the original zip file and repeated this process.

However, my initial script gave an error right at the end.I got a win.zip.
![img](/Websites/CODEBY/Administration/Hell%20Circle/win.png)

As you can see, the last zip file has an empty `flag.txt` which is useless.But its comment is the flag.

So I modified my script and returned the flag when the comment ended with `}`.

I stored all of my output in a file `log.txt` and its last line will contain the flag.

```
CODEBY{1t_w4s_r34lly_easy!!!}
```
