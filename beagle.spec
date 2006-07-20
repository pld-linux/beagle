#
# TODO:
#       - kill bashisms in crawl stuff
#
%include	/usr/lib/rpm/macros.mono
#
# Conditional build:
%bcond_without	apidocs		# don't build API documentation
%bcond_without	evolution	# don't include evolution support
%bcond_without	galago		# build without galago support
%bcond_without	gsf		# build without libgsf support
%bcond_without	gui		# don't build GNOME based GUI
%bcond_without	python		# don't build python libraries
%bcond_with	epiphany	# build epiphany extension
%bcond_with	sqlite3		# use sqlite3 instead of sqlite2
#
%if %{without gui}
%undefine	with_evolution
%endif
#
Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.2.7
Release:	2
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/beagle/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	d4c8e93db23c9b7d06104ce97a182502
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-crawl.patch
Patch2:		%{name}-kill_exec_a.patch
Patch3:		%{name}-configure.patch
URL:		http://beaglewiki.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_evolution:BuildRequires:	dotnet-evolution-sharp-devel >= 0.11.1}
%{?with_galago:BuildRequires:	dotnet-galago-sharp-devel >= 0.3.2}
BuildRequires:	dotnet-gmime-sharp-devel >= 2.1.19
%{?with_gsf:BuildRequires:	dotnet-gsf-sharp-devel >= 0.7}
#BuildRequires:	dotnet-gst-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.8.2
%{?with_epiphany:BuildRequires:	epiphany-devel >= 2.15.3}
BuildRequires:	gtk+2-devel >= 2:2.9.4
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	librsvg-devel >= 1:2.15.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	mono-csharp >= 1.1.13.8
# not used atm
#BuildRequires:	mozilla-devel
%{?with_python:BuildRequires:	python-pygtk-devel >= 2.9.2}
BuildRequires:	pkgconfig
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel
%if %{with sqlite3}
BuildRequires:	sqlite3-devel >= 3.3.4
%else
BuildRequires:	sqlite-devel
%endif
BuildRequires:	wv-devel >= 1.2.1
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	zip
# GUI BRs
%if %{with gui}
BuildRequires:	dotnet-gtk-sharp2-gnome-devel >= 2.8.2
BuildRequires:	gnome-vfs2-devel >= 2.15.2
%endif
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dotnet-gmime-sharp >= 2.1.19
%if %{with sqlite3}
Requires:	sqlite3
%else
Requires:	sqlite
%endif
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
Requires:	%{name} = %{version}-%{release}

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
Provides:	group(beagleindex)
Provides:	user(beagleindex)

%description crawl-system
Beagle crawl system.

%description crawl-system -l pl
System przeszukuj±cy beagle-crawl.

%package evolution
Summary:	Beagle Evolution backend
Summary(pl):	Backend Beagle dla Evolution
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-evolution-sharp >= 0.11.1
Requires:	evolution >= 2.7.3

%description
Beagle Evolution backend.

%description evolution -l pl
Backend Beagle dla Evolution.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany-extensions >= 2.15.1

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

%package search-gui
Summary:	GNOME based Beagle GUI
Summary(pl):	Bazowane na GNOME GUI dla Beagle
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.9.4

%description search-gui
GNOME based Beagle GUI.

%description search-gui -l pl
Bazowane na GNOME GUI dla Beagle.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--%{!?with_epiphany:dis}%{?with_epiphany:en}able-epiphany-extension \
	--%{!?with_evolution:dis}%{?with_evolution:en}able-evolution-sharp \
	--%{!?with_gui:dis}%{?with_gui:en}able-gui \

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
%attr(755,root,root) %{_bindir}/beagle-config
%attr(755,root,root) %{_bindir}/beagled
%attr(755,root,root) %{_bindir}/beagle-exercise-file-system
%attr(755,root,root) %{_bindir}/beagle-extract-content
%attr(755,root,root) %{_bindir}/beagle-index-info
%attr(755,root,root) %{_bindir}/beagle-index-url
%attr(755,root,root) %{_bindir}/beagle-info
%attr(755,root,root) %{_bindir}/beagle-ping
%attr(755,root,root) %{_bindir}/beagle-query
%attr(755,root,root) %{_bindir}/beagle-shutdown
%attr(755,root,root) %{_bindir}/beagle-status
%attr(755,root,root) %{_libdir}/%{name}/libbeagleglue.so*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/Backends
%{_libdir}/%{name}/Filters
%{_libdir}/%{name}/*.dll*
%attr(755,root,root) %{_libdir}/%{name}/beagled-index-helper
%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/libbeagle
%{_libdir}/*.la
%{?with_apidocs:%{_gtkdocdir}/beagle}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files crawl-system
%defattr(644,root,root,755)
%attr(640,root,crontab) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/*
%dir %{_sysconfdir}/beagle
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/*
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle/index
%attr(755,root,root) %{_sbindir}/*

%if %{with evolution}
%files evolution
%defattr(644,root,root,755)
%{_libdir}/%{name}/Backends/Evolution*
%endif

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/1.8/extensions/libbeagleextension.so*
%{_libdir}/epiphany/1.8/extensions/*.xml
%endif

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%endif

%if %{with gui}
%files search-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beagle-search
%attr(755,root,root) %{_bindir}/beagle-imlogviewer
%attr(755,root,root) %{_bindir}/beagle-settings
%attr(755,root,root) %{_libdir}/%{name}/libbeagleuiglue.so*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%endif
