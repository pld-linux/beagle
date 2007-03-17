#
# TODO:
#       - kill bashisms in crawl stuff
#	- mozilla extension?
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
%bcond_without	epiphany	# don't build epiphany extension
%bcond_with	sqlite3		# use sqlite3 instead of sqlite2
%bcond_with	thunderbird	# use Thunderbird backend
#
%if !%{with gui}
%undefine	with_evolution
%endif
#
Summary:	Beagle - An indexing subsystem
Summary(pl.UTF-8):	Beagle - podsystem indeksujący
Name:		beagle
Version:	0.2.16.3
Release:	1
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/beagle/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	03b14e6df4afa22cfce8c498f8e43dec
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-crawl.patch
Patch2:		%{name}-kill_exec_a.patch
Patch3:		%{name}-configure.patch
Patch4:		%{name}-epiphany-2.18.patch
URL:		http://beagle-project.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	chmlib-devel
%{?with_evolution:BuildRequires:	dotnet-evolution-sharp-devel >= 0.11.1}
%{?with_galago:BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0}
BuildRequires:	dotnet-gmime-sharp-devel >= 2.2.3
%{?with_gsf:BuildRequires:	dotnet-gsf-sharp-devel >= 0.8.1}
#BuildRequires:	dotnet-gst-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.0
%if %{with epiphany}
BuildRequires:	epiphany-devel >= 2.18.0
%endif
BuildRequires:	gtk+2-devel >= 2:2.10.10
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	mono-csharp >= 1.1.13.5
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	python-devel
%{?with_python:BuildRequires:	python-pygtk-devel >= 2:2.10.4}
%if %{with sqlite3}
BuildRequires:	sqlite3-devel >= 3.3.4
%else
BuildRequires:	sqlite-devel
%endif
BuildRequires:	wv-devel >= 1.2.4
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	zip
# GUI BRs
%if %{with gui}
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	gnome-vfs2-devel >= 2.18.0.1
%endif
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dotnet-gmime-sharp >= 2.2.3
%if %{with sqlite3}
Requires:	sqlite3
%else
Requires:	sqlite
%endif
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net.

%description -l pl.UTF-8
Beagle jest podsystemem indeksującym i wyszukującym zbudowanym na
bazie Lucene.Net.

%package libs
Summary:	Beagle libraries
Summary(pl.UTF-8):	Bibiloteki Beagle
Group:		Libraries

%description libs
Beagle libraries.

%description libs -l pl.UTF-8
Bibiloteki Beagle.

%package devel
Summary:	Beagle development files
Summary(pl.UTF-8):	Pliki programistyczne Beagle
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Beagle development files.

%description devel -l pl.UTF-8
Pliki programistyczne Beagle.

%package static
Summary:	Beagle static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Beagle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Beagle static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Beagle.

%package apidocs
Summary:	libbeagle API documentation
Summary(pl.UTF-8):	Dokumentacja API libbeagle
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libbeagle API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libbeagle.

%package crawl-system
Summary:	Beagle crawl system
Summary(pl.UTF-8):	System przeszukujący beagle-crawl
Group:		Applications/System
Requires:	crondaemon
Provides:	group(beagleindex)
Provides:	user(beagleindex)

%description crawl-system
Beagle crawl system.

%description crawl-system -l pl.UTF-8
System przeszukujący beagle-crawl.

%package evolution
Summary:	Beagle Evolution backend
Summary(pl.UTF-8):	Backend Beagle dla Evolution
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-evolution-sharp >= 0.11.1
Requires:	evolution >= 2.10.0

%description evolution
Beagle Evolution backend.

%description evolution -l pl.UTF-8
Backend Beagle dla Evolution.

%package thunderbird
Summary:	Beagle Mozilla Thunderbird backend
Summary(pl.UTF-8):	Backend Beagle dla Mozilli Thunderbird
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description thunderbird
Beagle Mozilla Thunderbird backend.

%description thunderbird -l pl.UTF-8
Backend Beagle dla Mozilli Thunderbird.

%package -n mozilla-firefox-extension-beagle
Summary:	Mozilla Firefox extension - beagle
Summary(pl.UTF-8):	Rozszerzenie dla Mozilla Firefox - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	mozilla-firefox >= 2.0.0.1-2

%description -n mozilla-firefox-extension-beagle
Mozilla Firefox extension that allows Beagle to index every page the
user views.

%description -n mozilla-firefox-extension-beagle -l pl.UTF-8
Rozszerzenie dla Mozilla Firefox sprawiające, że Beagle indeksuje
każdą odwiedzaną stronę.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl.UTF-8):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany-extensions >= 2.18.0

%description -n epiphany-extension-beagle
Epiphany extension that allows Beagle to index every page the user
views.

%description -n epiphany-extension-beagle -l pl.UTF-8
Rozszerzenie dla Epiphany sprawiające, że Beagle indeksuje każdą
odwiedzaną stronę.

%package -n python-%{name}
Summary:	Beagle Python bindings
Summary(pl.UTF-8):	Wiązania języka Python dla Beagle
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq  python-libs

%description -n python-%{name}
Beagle Python bindings.

%description -n python-%{name} -l pl.UTF-8
Wiązania języka Python dla Beagle.

%package search-gui
Summary:	GNOME based Beagle GUI
Summary(pl.UTF-8):	Oparty na GNOME graficzny interfejs dla Beagle
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.10.10

%description search-gui
GNOME based Beagle GUI.

%description search-gui -l pl.UTF-8
Oparty na GNOME graficzny interfejs dla Beagle.

%package startup
Summary:	Automatic startup integration for Beagle
Summary(pl.UTF-8):	Integracja funkcji automatycznego startu Beagle
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	beagle-gnome

%description startup
Automatic session startup integration for Beagle.

%description startup -l pl.UTF-8
Integracja funkcji automatycznego startu Beagle.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
	--%{!?with_thunderbird:dis}%{?with_thunderbird:en}able-thunderbird

%{__make} \
	MOZILLA_HOME=%{_libdir}/mozilla \
	pythondir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/cache/beagle/indexes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

dest=$RPM_BUILD_ROOT%{_datadir}/mozilla-firefox/extensions/\{fda00e13-8c62-4f63-9d19-d168115b11ca\}
install -d $dest $dest/chrome
install mozilla-extension/{chrome.manifest,install.rdf} $dest
install mozilla-extension/chrome/beagle.jar $dest/chrome

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/2.18/extensions/*.{la,a} \
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
%attr(755,root,root) %{_bindir}/beagle-doc-extractor
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
%dir %{_libdir}/%{name}/Filters
%{_libdir}/%{name}/*.dll
%{_libdir}/%{name}/*.dll.config
%{_libdir}/%{name}/Filters/*.dll
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
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/beagle
%endif

%files crawl-system
%defattr(644,root,root,755)
%attr(750,root,crontab) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/*
%dir %{_sysconfdir}/beagle
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/*
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle/indexes
%attr(755,root,root) %{_sbindir}/*

%if %{with evolution}
%files evolution
%defattr(644,root,root,755)
%{_libdir}/%{name}/Backends/Evolution*.dll
%endif

%if %{with thunderbird}
%files thunderbird
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beagle-contactviewer
%{_libdir}/%{name}/Backends/Thunderbird*.dll
%endif

%files -n mozilla-firefox-extension-beagle
%defattr(644,root,root,755)
%{_datadir}/mozilla-firefox/extensions/{fda00e13-8c62-4f63-9d19-d168115b11ca}

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/2.18/extensions/libbeagleextension.so*
%{_libdir}/epiphany/2.18/extensions/*.xml
%endif

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%endif

%if %{with gui}
%files search-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beagle-imlogviewer
%attr(755,root,root) %{_bindir}/beagle-search
%attr(755,root,root) %{_bindir}/beagle-settings
%attr(755,root,root) %{_libdir}/%{name}/libbeagleuiglue.so*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%endif

%files startup
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/beagled-autostart.desktop
%{_sysconfdir}/xdg/autostart/beagle-search-autostart.desktop
