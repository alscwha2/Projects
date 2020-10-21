Aaron Schwartz-Messing
Mordechai Schmutter

Compilation: javac fat32_reader.java
To Run: java fat32_reader <fat32.img file>

There was an issue that /DIR/.. did not reference back to the root. Had to deal with this case independantly.
If you call /DIR/] ls ..  It won't print anything because for whatever reason the .. entry of DIR does not point back to the root.
When considering . and .. for ls and cd, we implemented those commands as being valid only if . and/or .. are defined for that directory. So calling cd . or cd .. on the root prints an error.

Is stat supposed to work for CHUCKLES? What is it supposed to work for?
Same with size.
What's the deal with .. in DIR?
What is the procedure if there are too many arguments?
Can we leave implemented functions there that were not part of the assignment?
Proper format for hex numbers, specifically if there shuold be leading zeroes?
What's the deal with this "unopened file" business?
"Because you are not writing any data, you can treat the FAT32 free list superficially." <- What does that mean?