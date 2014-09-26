%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Frontend for GIO/GVFS
Name:		gigolo
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/gigolo/%{url_ver}/gigolo-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-2.0)
Provides:	sion

%description
Gigolo is a frontend to easily manage connections to remote filesystems 
using GIO/GVFS. It allows you to quickly connect/mount a remote filesystem 
and manage bookmarks of such.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

rm -rf %{_docdir}/%{name}

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*

