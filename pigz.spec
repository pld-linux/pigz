Summary:	A parallel implementation of gzip
Summary(pl.UTF-8):	Zrównoleglona implementacja gzipa
Name:		pigz
Version:	2.3.1
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.zlib.net/pigz/%{name}-%{version}.tar.gz
# Source0-md5:	e803f8bc0770c7a5e96dccb1d2dd2aab
URL:		http://www.zlib.net/pigz/
BuildRequires:	rpmbuild(macros)
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A parallel implementation of gzip for modern multi-processor,
multi-core machines.

%description -l pl.UTF-8
Zrównoleglona implementacja gzipa dla nowoczesnych maszyn -
wieloprocesorowych i wielordzeniowych.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install pigz unpigz $RPM_BUILD_ROOT%{_bindir}
install pigz.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo '.so pigz.1' >$RPM_BUILD_ROOT%{_mandir}/man1/unpigz.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pigz
%attr(755,root,root) %{_bindir}/unpigz
%{_mandir}/man1/pigz.1*
%{_mandir}/man1/unpigz.1*
