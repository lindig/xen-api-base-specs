%global debug_package %{nil}

Name:           ocaml-re
Version:        1.2.2
Release:        2%{?dist}
Summary:        A regular expression library for OCaml
License:        LGPL
URL:            https://github.com/ocaml/ocaml-re
Source0:        https://github.com/ocaml/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc

%description
A regular expression library for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc CHANGES
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/re
%exclude %{_libdir}/ocaml/re/*.a
%exclude %{_libdir}/ocaml/re/*.cmxa
%exclude %{_libdir}/ocaml/re/*.cmx
%exclude %{_libdir}/ocaml/re/*.mli
%exclude %{_libdir}/ocaml/re/*.annot
%exclude %{_libdir}/ocaml/re/*.cmt
%exclude %{_libdir}/ocaml/re/*.cmti

%files devel
%doc re-api.docdir/*
%exclude /usr/local/share/doc/re/
%{_libdir}/ocaml/re/*.a
%{_libdir}/ocaml/re/*.cmx
%{_libdir}/ocaml/re/*.cmxa
%{_libdir}/ocaml/re/*.mli

%changelog
* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 1.2.2-2
- Remove *.cmt, *.cmti and *.annot

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 1.2.2-1
- Update to 1.2.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.2.1-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

