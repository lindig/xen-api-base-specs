%define debug_package %{nil}

Name:           ocaml-shared-block-ring
Version:        2.2.0
Release:        2%{?dist}
Summary:        OCaml implementation of shared block rings
License:        ISC
URL:            https://github.com/mirage/shared-block-ring/
Source0:        https://github.com/mirage/shared-block-ring/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-sexplib-devel

%description
The shared memory ring protocols are used for: xenstore, console, disk and network devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-mirage-block-unix-devel%{?_isa}
Requires:       ocaml-mirage-clock-unix-devel%{?_isa}
Requires:       ocaml-io-page-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n shared-block-ring-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p ${OCAMLFIND_DESTDIR}
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
make install

%files
%doc CHANGES
%doc README.md
%{_libdir}/ocaml/shared-block-ring
%exclude %{_libdir}/ocaml/shared-block-ring/*.a
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmxa
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmx
%exclude %{_libdir}/ocaml/shared-block-ring/*.mli
%exclude %{_libdir}/ocaml/shared-block-ring/*.annot
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmt
%exclude %{_libdir}/ocaml/shared-block-ring/*.cmti

%files devel
%{_libdir}/ocaml/shared-block-ring/*.a
%{_libdir}/ocaml/shared-block-ring/*.cmx
%{_libdir}/ocaml/shared-block-ring/*.cmxa
%{_libdir}/ocaml/shared-block-ring/*.mli

%changelog
* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 2.2.0-2
- Remove *.cmt, *.cmti and *.annot

* Mon Apr 25 2016 Euan Harris <euan.harris@citrix.com> - 2.2.0-1
- Update to 2.2.0

* Fri Apr 15 2016 Euan Harris <euan.harris@citrix.com> - 2.1.0-1
- Update to 2.1.0

* Thu Apr 30 2015 David Scott <dave.scott@citrix.com> - 2.0.0-1
- Update to 2.0.0

* Sun Apr 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.1.1-1
- Initial package

