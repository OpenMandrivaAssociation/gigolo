%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Frontend for GIO/GVFS
Name:		gigolo
Version:	0.4.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/gigolo/%{url_ver}/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	waf
BuildRequires:	intltool
BuildRequires:	gtk+2-devel
Obsoletes:	sion < 0.2.0
Provides:	sion
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Gigolo is a frontend to easily manage connections to remote filesystems 
using GIO/GVFS. It allows you to quickly connect/mount a remote filesystem 
and manage bookmarks of such.

%prep
%setup -q

%build
%configure_waf

%waf

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%waf_install

rm -rf %{_docdir}/%{name}

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
