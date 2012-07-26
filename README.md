Launch GMail using chromium as the browser desktop wide.

This tool is similiar to desktop-webmail, found in the Ubuntu repositories,
with three key differences:

  1. It will always use chromium as the browser.
  2. It only supports GMail.
  3. (most important): It uses the chromium **app mode**.

To use, simply open up *System* -> *Preferences* -> *Preferred Applications*
and use this script as your email program.

Installing on GNOME 3 without root permissions
==============================================
To install this to the little bar on the left side of the screen, some more
steps need to be taken:

  1. Copy the script to somewhere in your path. You can verify this by opening
     a terminal and running `xdg-gmail.py -nv`.
  2. Copy the `xdg-gmail.desktop` file to `~/.local/share/applications/`.
  3. Copy the icon `gmail.png` to `~/.local/share/icons`.
  4. (optional) To make mailto: links open with this script, add the following
     line to `~/.local/share/applications/mimeapps.list`

     `x-scheme-handler/mailto=xdg-gmail.desktop`

     If there's a previous entry for `x-scheme-handler`, remove it.

After these steps, the application should show up in the list of applications
(you can use the search field to find it). Drag it onto the bar to make it
stick there.

License
=======
Copyright (c) 2011 Marc Brinkmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

gmail.svg, gmail.png
====================
The file "gmail.svg" is not covered under the license above and has been taken
from http://gnome-look.org/content/show.php/CheckGmail+svg+icon?content=72704

It is GPL licensed.
