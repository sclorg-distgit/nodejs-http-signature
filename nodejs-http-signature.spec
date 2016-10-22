%{?scl:%scl_package nodejs-http-signature}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global commit 8881c4a806604deabe958f37e51672a65ef150fe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-http-signature
Version:        0.10.0
Release:        6.1%{?dist}
Summary:        Reference implementation of Joyent's HTTP Signature Scheme
BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/joyent/node-http-signature
Source0:        http://registry.npmjs.org/http-signature/-/http-signature-%{version}.tgz
#grab the tests from github
Source1:        https://github.com/joyent/node-http-signature/archive/%{commit}/%{pkg_name}-%{version}-%{shortcommit}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

#for tests
#BuildRequires:  %{?scl_prefix}npm(tap)
#BuildRequires:  %{?scl_prefix}npm(node-uuid)
#BuildRequires:  %{?scl_prefix}npm(assert-plus)
#BuildRequires:  %{?scl_prefix}npm(asn1)
#BuildRequires:  %{?scl_prefix}npm(ctype)

%description
nodejs-http-signature is a node.js library that has client and server components 
for Joyent's HTTP Signature Scheme.

%prep
%setup -q -n package -a1

%nodejs_fixdep assert-plus '~0.1.2'
%nodejs_fixdep ctype '~0.5.3'
%nodejs_fixdep asn1 '~0.1.11'

#move tests into regular directory
#mv node-http-signature-%{commit}/test .
#rm -rf node-http-signature-%{commit}

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/http-signature
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/http-signature

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%tap test/*.js

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/http-signature
%doc LICENSE README.md http_signing.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.0-6.1
- rebuilt

* Wed Jan 08 2014 Tomas Hrcka <thrcka@redhat.com> - 0.10.0-5.1
- fix dependencies resolution

* Fri Nov 08 2013 Tomas Hrcka <thrcka@redhat.com> - 0.10.0-5
- Software collection support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-2
- grab tests from GitHub
- relax dependency on npm(asn1)

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-1
- initial package
