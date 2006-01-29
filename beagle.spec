#
# TODO:
#	- finish crawl system
#       - separtate CLI utilities
#
%include	/usr/lib/rpm/macros.mono
#
# Conditional build:
%bcond_with	epiphany	# build epiphany extension
%bcond_with	gsf		# build with libgsf support
%bcond_without	evolution	# don't include evolution support
#
Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.2.0
Release:	1
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/beagle/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	faa236b812db1a8ee72c58d2cb810010
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-crawl.patch
URL:		http://beaglewiki.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_evolution:BuildRequires:	dotnet-evolution-sharp-devel >= 0.10.2}
BuildRequires:	dotnet-gmime-sharp-devel >= 2.1.19
%{?with_gsf:BuildRequires:	dotnet-gsf-sharp-devel >= 0.7}
#BuildRequires:	dotnet-gst-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-gnome-devel >= 2.3.90
%{?with_epiphany:BuildRequires:	epiphany-devel >= 1.8}
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gtk-doc
BuildRequires:	libexif-devel >= 0.5.0
BuildRequires:	libgnome-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.19
BuildRequires:	mono-csharp >= 1.1.10
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	sqlite-devel
BuildRequires:	wv-devel >= 1.0.0
BuildRequires:	zip
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dotnet-gmime-sharp >= 2.1.19
%{?with_epiphany:Requires:	epiphany-extensions}
Requires:	gtk+2 >= 2:2.6.0
Requires:	sqlite
ExcludeArch:	alpha i386 sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net.

%description -l pl
Beagle jest podsystemem indeksuj±cym i wyszukuj±cym zbudowanym na
bazie Lucene.Net.

%package libs
Summary:	Beagle libraries
Summary(pl):	Bibiloteki Beagle
Group:		Libraries

%description libs
Beagle libraries.

%description libs -l pl
Bibiloteki Beagle.

%package devel
Summary:	Beagle development files
Summary(pl):	Pliki programistyczne Beagle
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Beagle development files.

%description devel -l pl
Pliki programistyczne Beagle.

%package static
Summary:	Beagle static libraries
Summary(pl):	Statyczne biblioteki Beagle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Beagle static libraries.

%description static -l pl
Statyczne biblioteki Beagle.

%package crawl-system
Summary:	Beagle crawl system
Summary(pl):	System przeszukuj±cy beagle-crawl
Group:		Applications/System
Requires:	crondaemon
Provides:       group(avahi)
Provides:       user(avahi)

%description crawl-system
Beagle crawl system.

%description crawl-system -l pl
System przeszukuj±cy beagle-crawl.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany >= 1.2.1

%description -n epiphany-extension-beagle
Epiphany extension that allows Beagle to index every page the user
views.

%description -n epiphany-extension-beagle -l pl
Rozszerzenie dla Epiphany sprawiaj±ce, ¿e Beagle indeksuje ka¿d±
odwiedzan± stronê.

%package -n python-%{name}
Summary:	Beagle Python bindings
Summary(pl):	Wi±zania jêzyka Python dla Beagle
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq  python-libs

%description -n python-%{name}
Beagle Python bindings.

%description -n python-%{name} -l pl
Wi±zania jêzyka Python dla Beagle.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--%{!?with_epiphany:dis}%{?with_epiphany:en}able-epiphany-extension \
	--%{!?with_evolution:dis}%{?with_evolution:en}able-evolution-sharp

%{__make} \
	MOZILLA_HOME=%{_libdir}/mozilla \
	pythondir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/cache/beagle/index

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/1.8/extensions/*.la \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre crawl-system
%groupadd -g 166 -r -f beagleindex
%useradd -u 166 -r -d /var/cache/beagle -s /bin/false -c "Beagle indexing" -g beagleindex beagleindex

%postun crawl-system
if [ "$1" = "0" ]; then
        %userremove beagleindex
        %groupremove beagleindex
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/Backends
%{_libdir}/%{name}/Filters
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll*

%attr(755,root,root) %{_libdir}/%{name}/beagled-index-helper

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/libbeagle
%{_libdir}/*.la
%{_gtkdocdir}/beagle
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files crawl-system
%defattr(644,root,root,755)
%attr(750,root,crontab) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/*.crontab
%attr(750,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/*
%dir %attr(750,beagleindex,beagleindex) %{_var}/cache/beagle
%dir %attr(750,beagleindex,beagleindex) %{_var}/cache/beagle/index
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/beagle-crawl-system

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/1.8/extensions/libbeagleextension.so*
%{_libdir}/epiphany/1.8/extensions/*.xml
%endif

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
