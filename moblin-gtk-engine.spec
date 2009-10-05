Name: moblin-gtk-engine
Summary: Gtk engine for Moblin
Group: Graphical desktop/GNOME 
Version: 1.0.2
License: LGPL v2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: gtk2-devel
Requires: gnome-settings-daemon

%description
Gtk engine for Moblin

%package devel
Summary: Development files for Moblin's Gtk engine
Group: Graphical desktop/GNOME

%description devel
Development files for Moblin's Gtk engine

%prep
%setup -q 
perl -pi -e 's,^./configure.*,,' ./autogen.sh

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc NEWS README COPYING.LIB AUTHORS ChangeLog
%{_libdir}/gtk-2.0/2.10.0/engines/libmoblin-netbook-engine.so
%{_datadir}/themes/Moblin-Netbook/gtk-2.0/gtkrc
%{_datadir}/themes/Moblin-Netbook/index.theme
%{_datadir}/themes/Moblin-Netbook/metacity-1/metacity-theme-1.xml

%files devel
%{_libdir}/gtk-2.0/2.10.0/engines/libmoblin-netbook-engine.la
