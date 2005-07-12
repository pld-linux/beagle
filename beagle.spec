#	TODO:
#	- bcond is broken, it must be checked
#
# Conditional build:
%bcond_with	epiphany	# build epiphany extension
				# (just a hack)
Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.0.12
Release:	0.1
License:	Various
Group:		Libraries
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Source0:	http://ftp.gnome.org/pub/gnome/sources/beagle/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	27bfdc64982a471a7d9c2a86c620752d
Patch0:		%{name}-Filters-dir.patch
Patch1:		%{name}-pc.patch
Patch2:		%{name}-bash.patch
URL:		http://beaglewiki.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	dotnet-dbus-sharp-devel >= 0.23.4
BuildRequires:	dotnet-evolution-sharp-devel >= 0.6
BuildRequires:	dotnet-gecko-sharp-devel = 0.6
BuildRequires:	dotnet-gmime-sharp-devel
#BuildRequires:	dotnet-gsf-sharp-devel >= 0.2
#BuildRequires:	dotnet-gst-sharp-devel
BuildRequires:	dotnet-gtk-sharp-gnome-devel
BuildRequires:	dotnet-gtk-sharp-devel
%{?with_epiphany:BuildRequires:	epiphany-devel >= 1.6}
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libexif-devel >= 0.5.0
BuildRequires:	libgnome-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	mono-csharp >= 1.0.6
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	wv-devel >= 1.0.0
BuildRequires:	zip
Requires:	dotnet-dbus-sharp >= 0.23.4
Requires:	dotnet-evolution-sharp = 0.6
#Requires:	dotnet-gsf-sharp >= 0.2
#Requires:	dotnet-gst-sharp
Requires:	dotnet-gtk-sharp
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net.

%description -l pl
Beagle jest podsystemem indeksuj±cym i wyszukuj±cym zbudowanym na
bazie Lucene.Net.

%package devel
Summary:	Beagle development files
Summary(pl):	Pliki programistyczne Beagle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Beagle development files.

%description devel -l pl
Pliki programistyczne Beagle.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany >= 1.2.1
Requires:	epiphany < 1.3.0

%description -n epiphany-extension-beagle
Epiphany extension that allows Beagle to index every page the user
views.

%description -n epiphany-extension-beagle -l pl
Rozszerzenie dla Epiphany sprawiaj±ce, ¿e Beagle indeksuje ka¿d±
odwiedzan± stronê.

%prep
%setup -q
#%patch0 -p0
#%patch1 -p0
#%patch2 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
%if %{with epiphany}
	--enable-epiphany-extension
%else
	--disable-epiphany-extension
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/extensions/*.la \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/filesystems/*.la \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root)%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/Filters
%{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll*
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/beagled-index-helper
%attr(755,root,root) %{_libdir}/gtk-2.0/2.4.0/filesystems/libbeaglechooserhack.so*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libbeagle
%{_pkgconfigdir}/*

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/extensions/libbeagleextension.so*
%endif
