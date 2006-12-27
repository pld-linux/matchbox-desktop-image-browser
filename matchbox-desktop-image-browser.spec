Summary:	Image browser for Matchbox desktop
Summary(pl):	Przegl±darka obrazków dla ¶rodowiska Matchbox
Name:		matchbox-desktop-image-browser
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/mb-desktop-image-browser/%{version}/mb-desktop-image-browser-%{version}.tar.bz2
# Source0-md5:	c54ca1c24a5b9b062c6fc38b006eceb5
Patch0:		%{name}-ac.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libmatchbox-devel >= 1.1
BuildRequires:	libtool
BuildRequires:	matchbox-desktop-devel
BuildRequires:	pkgconfig
Requires:	libmatchbox >= 1.1
Requires:	matchbox-desktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image browser for Matchbox desktop.

%description -l pl
Przegl±darka obrazków dla ¶rodowiska Matchbox.

%prep
%setup -q -n mb-desktop-image-browser-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make} \
	libdir=%{_libdir}/matchbox/desktop

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}/matchbox/desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/matchbox/desktop/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/matchbox/desktop/imgbrowser.so
%{_pixmapsdir}/mbpicturefolder.png
