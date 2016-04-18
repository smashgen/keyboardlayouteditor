# Introduction #

In this page we document any prior art regarding keyboard layout editors.

# Somewhat sorted list #

  * [xkeyboard-config project](http://www.freedesktop.org/wiki/Software/XKeyboardConfig), with links to documentation, developer website.
    * [keyboard layout files](http://webcvs.freedesktop.org/xkeyboard-config/xkeyboard-config/symbols/)
  * [Comparing Keyman Developer and Microsoft Keyboard Layout Creator](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=KeymanVsMSKLC)
  * [Creating layouts with Keyman, walkthrough to Keyman layout format](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=KeymanIPATutorial)
  * [Convert/create layouts through web tool(OSX specific?)](http://wordherd.com/keyboards/)
  * [Keyboard view utility in OS/X](http://benleivian.wordpress.com/2006/04/24/keyboard-viewer/)
  * [Michael Kaplan's blog (around MS Layout Creator)](http://blogs.msdn.com/michkap/archive/tags/Keyboards/default.aspx)
    * [one codepoint per SGCAPS](http://blogs.msdn.com/michkap/archive/2006/01/16/513088.aspx)
  * [Keyman sample layouts from sil.org](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=SILKeyboards)
  * [Perl script, from simple format creates OS/X .keylayout XML layout files](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=keylayoutmaker)
  * [http://www.open-std.org/jtc1/sc35/wg1/docs/projects#24757
ISO/IEC 24757 Information technology Keyboard interaction model, machine-readable description and interaction of keyboard keys]
  * [An unreliable guide to XKB, by Doug Palmer, 2004](http://www.charvolant.org/~doug/xkb/)
  * [Enhancing XKB, by Kamil Toman, Ivan Pascal](http://www.xfree86.org/current/XKB-Enhancing.html)

  * Different layout formats
    1. [XKB](http://www.xfree86.org/current/XKBproto.pdf)
    1. SCIM
    1. [Keyman Developer PDF documentation (build 6.0.164.0)](http://www.tavultesoft.com/account/home/download/index.php?DownloadCategoryID=9)
    1. OS/X XML format. [link/dtd](http://developer.apple.com/technotes/tn2002/tn2056.html)
    1. Windows binary format. link?, spec?

  * Existing programs that create keyboard layouts
    1. [Keyman Developer](http://www.tavultesoft.com/keymandev/)
    1. [Microsoft Keyboard Layout Creator](http://www.microsoft.com/globaldev/tools/msklc.mspx), not available to use with Wine, etc.
    1. [Ukelele](http://scripts.sil.org/ukelele), by Sil.org, OS/X program for OS/X layouts
    1. [KLC](http://www.mail-archive.com/gnome-devel-list@gnome.org/msg00509.html), Keyboard Layout Creator by Ankit, written in GTK+, for SCIM and IIIMF, [source](http://indianoss.cvs.sourceforge.net/indianoss/KLC/src/).