Summary:	Frontend for GIO/GVFS
Name:		gigolo
Version:	0.4.1
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.uvena.de/gigolo/
Source0:	http://files.uvena.de/gigolo/%{name}-%{version}.tar.bz2
BuildRequires:	waf
BuildRequires:	intltool
BuildRequires:	gtk+2-devel
Obsoletes:	sion < 0.2.0
Provides:	sion

%description
Gigolo is a frontend to easily manage connections to remote filesystems 
using GIO/GVFS. It allows you to quickly connect/mount a remote filesystem 
and manage bookmarks of such.

%prep
%setup -q

%build
%define __waf ./waf
%configure_waf
%waf

%install
%waf_install

rm -rf %{_docdir}/%{name}

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*


%changelog
* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-5
+ Revision: 789868
- rebuild
- drop old stuff from spec file

* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-4
+ Revision: 653538
- rebuild

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-3
+ Revision: 633054
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2011.0
+ Revision: 579665
- rebuild for new xfce 4.7.0

* Mon Aug 02 2010 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 565050
- New version 0.4.1

* Thu Dec 31 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 484472
- update to new version 0.4.0

* Fri May 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2010.0
+ Revision: 369236
- update to new version 0.3.2

* Mon Apr 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 364422
- update to new version 0.3.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-2mdv2009.1
+ Revision: 349143
- rebuild whole xfce

* Mon Feb 23 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 344142
- update to new version 0.2.1

* Sat Feb 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 340221
- upstream has changed name to gigolo ;)
- new version 0.2.0
- upstream has changed name

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-1mdv2009.1
+ Revision: 324335
- add missing buildrequires
- add source and spec files
- Created package structure for sion.

