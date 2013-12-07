Summary:	Frontend for GIO/GVFS
Name:		gigolo
Version:	0.4.1
Release:	11
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.uvena.de/gigolo/
Source0:	http://files.uvena.de/gigolo/%{name}-%{version}.tar.bz2

BuildRequires:	intltool
BuildRequires:	waf
BuildRequires:	pkgconfig(gtk+-2.0)
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

