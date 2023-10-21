%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	Frontend for GIO/GVFS
Name:		gigolo
Version:	0.5.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/gigolo/%{url_ver}/gigolo-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  xfce-dev-tools
Recommends:	gvfs-obexftp
Recommends:	gvfs-smb

Provides:	sion

%description
Gigolo is a frontend to easily manage connections to remote filesystems 
using GIO/GVFS. It allows you to quickly connect/mount a remote filesystem 
and manage bookmarks of such.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

rm -rf %{_docdir}/%{name}

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*x*/apps/org.xfce.gigolo.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.gigolo.svg
