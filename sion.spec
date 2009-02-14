Summary:	Frontend for GIO/GVFS
Name:		sion
Version:	0.1.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/sion
Source0:	http://goodies.xfce.org/releases/sion/sion-0.1.0.tar.bz2
BuildRequires:	waf
BuildRequires:	intltool
BuildRequires:	gtk+2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Sion is a frontend to easily manage connections to remote filesystems 
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
