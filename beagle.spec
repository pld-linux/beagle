#
# TODO:
# - package 'crawl' files
# - check .desktop files
# - separate libs (future proof)
#
%include	/usr/lib/rpm/macros.mono
#
# Conditional build:
%bcond_without	epiphany	# don't build epiphany extension
%bcond_with	evolution	# don't include evolution support
#
Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.1.1
Release:	0.1
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/beagle/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	e788ed11077e576797a0793631f2fe8b
URL:		http://beaglewiki.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_evolution:BuildRequires:	dotnet-evolution-sharp-devel >= 0.6}
BuildRequires:	dotnet-gecko-sharp2-devel = 0.11
BuildRequires:	dotnet-gmime-sharp-devel >= 2.1.16-2
#BuildRequires:	dotnet-gsf-sharp-devel >= 0.2
#BuildRequires:	dotnet-gst-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-gnome-devel
%{?with_epiphany:BuildRequires:	epiphany-devel >= 1.8}
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtk-doc
BuildRequires:	libexif-devel >= 0.5.0
BuildRequires:	libgnome-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	mono-csharp >= 1.0.6
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel
BuildRequires:	wv-devel >= 1.0.0
BuildRequires:	zip
Requires:	dotnet-gmime-sharp >= 2.1.16-2
%{?with_epiphany:Requires:	epiphany-extensions}
Requires:	gtk+2 >= 2:2.4.0
Requires:	sqlite
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--%{!?with_epiphany:dis}%{?with_epiphany:en}able-epiphany-extension \
	--%{!?with_evoultion:dis}%{?with_evolution:en}able-evolution-sharp
	

%{__make} \
	MOZILLA_HOME=%{_libdir}/mozilla

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/1.8/extensions/*.la \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
	
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/Filters
%{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll*

# to be separtated
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/beagled-index-helper

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libbeagle
%{_libdir}/*.la
%{_libdir}/*.so
%{_gtkdocdir}/beagle
%{_pkgconfigdir}/*

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/1.8/extensions/libbeagleextension.so*
%{_libdir}/epiphany/1.8/extensions/*.xml
%endif
