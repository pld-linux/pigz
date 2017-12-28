Summary:	A parallel implementation of gzip
Summary(pl.UTF-8):	Zrównoleglona implementacja gzipa
Name:		pigz
Version:	2.4
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.zlib.net/pigz/%{name}-%{version}.tar.gz
# Source0-md5:	def2f6e19d9d8231445adc1349d346df
URL:		http://www.zlib.net/pigz/
BuildRequires:	sed >= 4.0
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

%{__sed} -i -e '/pigz/ s/-lm/-lm -lz/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-Wall -Wextra %{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p pigz unpigz $RPM_BUILD_ROOT%{_bindir}
cp -p pigz.1 $RPM_BUILD_ROOT%{_mandir}/man1
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
