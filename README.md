Chrome/Chromium as your mail program
====================================

This tool is similiar to desktop-webmail, found in the Ubuntu repositories,
with three key differences:

  1. It will always use Chrome/Chromium as the browser.
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

     If there's a previous entry for `x-scheme-handler/mailto`, remove it.

After these steps, the application should show up in the list of applications
(you can use the search field to find it). Drag it onto the bar to make it
stick there.
