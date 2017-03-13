%{?scl:%scl_package nodejs-http-signature}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

#%global commit 8881c4a806604deabe958f37e51672a65ef150fe
#%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-http-signature
Version:    1.1.1
Release:    1%{?dist}
Summary:        Reference implementation of Joyent's HTTP Signature Scheme
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

License:        MIT
URL:            https://github.com/joyent/node-http-signature
Source0:        http://registry.npmjs.org/http-signature/-/http-signature-%{version}.tgz
#grab the tests from github
# this is oudated, but we're not running tests anyway, so not updating tests
#Source1:        https://github.com/joyent/node-http-signature/archive/%{commit}/%{pkg_name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
nodejs-http-signature is a node.js library that has client and server components 
for Joyent's HTTP Signature Scheme.

%prep
%setup -q -n package
#%setup -q -n package -a1

%nodejs_fixdep assert-plus

#move tests into regular directory
#mv node-http-signature-%{commit}/test .
#rm -rf node-http-signature-%{commit}

%build
#nothing to do

%install

mkdir -p %{buildroot}%{nodejs_sitelib}/http-signature
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/http-signature

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%tap test/*.js


%files
%{nodejs_sitelib}/http-signature
%doc LICENSE README.md http_signing.md

%changelog
* Fri Sep 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-1
- Updated with script

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
