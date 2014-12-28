#
# TODO:
#       - kill bashisms in crawl stuff
#	- add qyoto based settings (requires new packages)
#
# Conditional build:
%bcond_without	apidocs		# don't build API documentation
%bcond_with	avahi		# enable Avahi support
%bcond_without	evolution	# don't include evolution support
%bcond_without	galago		# build without galago support
%bcond_without	gsf		# build without libgsf support
%bcond_without	gui		# don't build GNOME based GUI
# required epiphany with python support (2009.06.06 removed permanently from epiphany)
%bcond_with	epiphany	# don't build epiphany extension
%bcond_without	thunderbird	# use Thunderbird backend
#
%if !%{with gui}
%undefine	with_evolution
%endif

%include	/usr/lib/rpm/macros.mono
Summary:	Beagle - An indexing subsystem
Summary(pl.UTF-8):	Beagle - podsystem indeksujący
Name:		beagle
Version:	0.3.9
Release:	7
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/beagle/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	b73c12423d2d67133dbb05933f4c8fe1
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-crawl.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-use-xdg-open.patch
Patch4:		%{name}-epiphany.patch
Patch5:		%{name}-gmime-2.4.patch
Patch6:		%{name}-sqlite.patch
Patch7:		%{name}-mono28.patch
URL:		http://beagle-project.org/Main_Page
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	chmlib-devel
%{?with_avahi:BuildRequires:	dotnet-avahi-devel >= 0.6.10}
%{?with_evolution:BuildRequires:	dotnet-evolution-sharp-devel >= 0.13.3}
%{?with_galago:BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0}
BuildRequires:	dotnet-gmime-sharp-devel >= 2.3.5
%{?with_gsf:BuildRequires:	dotnet-gsf-sharp-devel >= 0.8.1}
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.0
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel >= 0.3.0
BuildRequires:	dotnet-ndesk-dbus-sharp-devel >= 0.6.0
%{?with_epiphany:BuildRequires:	epiphany-devel >= 2.22.0}
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.2.4
BuildRequires:	mono-devel >= 1.2.4
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.3.9
BuildRequires:	taglib-sharp-devel
BuildRequires:	wv-devel >= 1.2.4
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	zip
# GUI BRs
%if %{with gui}
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	rpm-pythonprov
%endif
Requires:	dotnet-gmime-sharp >= 2.3.5
Requires:	dotnet-gsf-sharp
Requires:	shared-mime-info
Requires:	sqlite3
Requires:	xdg-utils
Obsoletes:	beagle-libs
Obsoletes:	beagle-static
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net.

%description -l pl.UTF-8
Beagle jest podsystemem indeksującym i wyszukującym zbudowanym na
bazie Lucene.Net.

%package debug
Summary:	Debug files for the Mono part of Beagle
Summary(pl.UTF-8):	Pliki debugujące dla części Mono Beagle'a
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description debug
Debug files for the Mono part of Beagle.

%description debug -l pl.UTF-8
Pliki debugujące dla części Mono Beagle'a.

%package devel
Summary:	Beagle development files
Summary(pl.UTF-8):	Pliki programistyczne Beagle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Beagle development files.

%description devel -l pl.UTF-8
Pliki programistyczne Beagle.

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

%package webinterface
Summary:	A web interface for Beagle
Summary(pl.UTF-8):	Interfejs sieciowy dla Beagle
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description webinterface
An AJAX interface that allows users to search for data through their
web browser.

%description webinterface -l pl.UTF-8
AJAX-owy interfejs pozwalający użytkownikom wyszukiwać dane za pomocą
przeglądarki internetowej.

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

%package icedove
Summary:	Beagle Icedove backend
Summary(pl.UTF-8):	Backend Beagle dla Icedove
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	icedove
Provides:	beagle-thunderbird
Obsoletes:	beagle-thunderbird

%description icedove
Beagle Icedove backend.

%description icedove -l pl.UTF-8
Backend Beagle dla Icedove.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl.UTF-8):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany-extensions >= 2.22.0

%description -n epiphany-extension-beagle
Epiphany extension that allows Beagle to index every page the user
views.

%description -n epiphany-extension-beagle -l pl.UTF-8
Rozszerzenie dla Epiphany sprawiające, że Beagle indeksuje każdą
odwiedzaną stronę.

%package -n iceweasel-extension-beagle
Summary:	Iceweasel extension - beagle
Summary(pl.UTF-8):	Rozszerzenie dla przeglądarki Iceweasel - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	iceweasel
Provides:	mozilla-firefox-extension-beagle
Obsoletes:	mozilla-firefox-extension-beagle

%description -n iceweasel-extension-beagle
Iceweasel extension that allows Beagle to index every page the user
views.

%description -n iceweasel-extension-beagle -l pl.UTF-8
Rozszerzenie dla przeglądarki Iceweasel sprawiające, że Beagle
indeksuje każdą odwiedzaną stronę.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--%{!?with_epiphany:dis}%{?with_epiphany:en}able-epiphany-extension \
	--%{!?with_evolution:dis}%{?with_evolution:en}able-evolution \
	--%{!?with_gui:dis}%{?with_gui:en}able-gui \
	--%{!?with_thunderbird:dis}%{?with_thunderbird:en}able-thunderbird \
	--%{!?with_avahi:dis}%{?with_avahi:en}able-avahi

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/cache/beagle/indexes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*glue.la

dest=$RPM_BUILD_ROOT%{_datadir}/iceweasel/extensions/\{fda00e13-8c62-4f63-9d19-d168115b11ca\}
install -d $dest $dest/chrome
install firefox-extension/{chrome.manifest,install.rdf} $dest
cp -r firefox-extension/chrome/* $dest/chrome

%if %{with thunderbird}
tdest=$RPM_BUILD_ROOT%{_libdir}/icedove/extensions/\{b656ef18-fd76-45e6-95cc-8043f26361e7\}
install -d $tdest
install thunderbird-extension/{chrome.manifest,install.rdf} $tdest
cp -r thunderbird-extension/{chrome,components,defaults} $tdest
%endif

%if %{with gui}
[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}
%else
touch %{name}.lang
%endif

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/beagle-config
%{?with_gsf:%attr(755,root,root) %{_bindir}/beagle-doc-extractor}
%attr(755,root,root) %{_bindir}/beagle-extract-content
%attr(755,root,root) %{_bindir}/beagle-index-info
%attr(755,root,root) %{_bindir}/beagle-info
%attr(755,root,root) %{_bindir}/beagle-ping
%attr(755,root,root) %{_bindir}/beagle-query
%attr(755,root,root) %{_bindir}/beagle-shutdown
%attr(755,root,root) %{_bindir}/beagle-static-query
%attr(755,root,root) %{_bindir}/beagle-status
%attr(755,root,root) %{_bindir}/beagled
%attr(755,root,root) %{_bindir}/blocate
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%attr(755,root,root) %{_libdir}/%{name}/libbeagleglue.so*
%dir %{_sysconfdir}/beagle
%dir %{_sysconfdir}/beagle/config-files
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/blocate.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/query-mapping.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/config-files/BeagleSearch.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/config-files/Daemon.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/config-files/FilesQueryable.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/config-files/GoogleBackends.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/config-files/Networking.xml
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/Backends
%dir %{_libdir}/%{name}/Filters
%{_libdir}/%{name}/*.dll
%{_libdir}/%{name}/*.dll.config
%{_libdir}/%{name}/Backends/GoogleBackends*.dll
%{_libdir}/%{name}/Filters/*.dll
%attr(755,root,root) %{_libdir}/%{name}/beagled-index-helper
%{_mandir}/man1/beagle-config.1*
%{_mandir}/man1/beagle-info.1*
%{_mandir}/man1/beagle-ping.1*
%{_mandir}/man1/beagle-query.1*
%{_mandir}/man1/beagle-shutdown.1*
%{_mandir}/man1/beagle-status.1*
%{_mandir}/man1/beagled.1*
%{_mandir}/man8/beagle-doc-extractor.8*
%{_mandir}/man8/beagle-index-info.8*

%files debug
%defattr(644,root,root,755)
%{_libdir}/%{name}/Backends/*.mdb
%{_libdir}/%{name}/Filters/*.mdb
%{_libdir}/%{name}/*.mdb

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/beagle-0.0.pc
%{?with_gui:%{_pkgconfigdir}/beagle-ui-0.0.pc}
%{_pkgconfigdir}/beagle-daemon.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/sources/*
%endif

%files crawl-system
%defattr(644,root,root,755)
%dir %{_sysconfdir}/beagle/crawl-rules
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-applications
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-documentation
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-executables
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-manpages
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-monodoc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/crawl-rules/crawl-windows
# XXX: samples not here
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/beagle/external-filters.xml.sample
%attr(750,root,crontab) %config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/beagle-crawl-system
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle
%dir %attr(755,beagleindex,beagleindex) %{_var}/cache/beagle/indexes
%attr(755,root,root) %{_sbindir}/beagle-build-index
%attr(755,root,root) %{_sbindir}/beagle-dump-index
%attr(755,root,root) %{_sbindir}/beagle-manage-index
%attr(755,root,root) %{_sbindir}/beagle-master-delete-button
%attr(755,root,root) %{_sbindir}/beagle-removable-index
%{_mandir}/man8/beagle-dump-index.8*
%{_mandir}/man8/beagle-build-index.8*
%{_mandir}/man8/beagle-extract-content.8*
%{_mandir}/man8/beagle-manage-index.8*

%if %{with gui}
%files search-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beagle-imlogviewer
%attr(755,root,root) %{_bindir}/beagle-search
%attr(755,root,root) %{_bindir}/beagle-settings
%attr(755,root,root) %{_libdir}/%{name}/libbeagleuiglue.so*
%attr(755,root,root) %{_libdir}/%{name}/keygrabber.py
%{_mandir}/man1/beagle-search.1*
%{_mandir}/man1/beagle-settings.1*
%{_mandir}/man8/beagle-imlogviewer.8*
%{_desktopdir}/*.desktop
%endif

%files startup
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/beagled-autostart.desktop
%{?with_gui:%{_sysconfdir}/xdg/autostart/beagle-search-autostart.desktop}

%files webinterface
%defattr(644,root,root,755)
%{_datadir}/%{name}

%if %{with evolution}
%files evolution
%defattr(644,root,root,755)
%{_libdir}/%{name}/Backends/Evolution*.dll
%endif

%if %{with thunderbird}
%files icedove
%defattr(644,root,root,755)
%{_libdir}/%{name}/Backends/Thunderbird*.dll
%{_libdir}/icedove/extensions/{b656ef18-fd76-45e6-95cc-8043f26361e7}
%endif

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/epiphany/2.26/extensions/beagle.py
%{_libdir}/epiphany/2.26/extensions/*.ephy-extension
%endif

%files -n iceweasel-extension-beagle
%defattr(644,root,root,755)
%{_datadir}/iceweasel/extensions/{fda00e13-8c62-4f63-9d19-d168115b11ca}
