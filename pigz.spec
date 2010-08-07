Summary:	A parallel implementation of gzip
Name:		pigz
Version:	2.1.6
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.zlib.net/pigz/%{name}-%{version}.tar.gz
# Source0-md5:	cbe9030c4be3d0ef2438ee5f8b169ca4
URL:		http://www.zlib.net/pigz/
BuildRequires:	rpmbuild(macros)
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A parallel implementation of gzip for modern multi-processor,
multi-core machines

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install {pigz,unpigz} $RPM_BUILD_ROOT/%{_bindir}
install pigz.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pigz
%attr(755,root,root) %{_bindir}/unpigz
%{_mandir}/man1/pigz.1*
