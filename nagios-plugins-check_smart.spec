# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


Name:    nagios-plugins-check_smart

# renovate: datasource=github-releases depName=Napsty/check_smart versioning=loose
Version: 6.14.1
Release: 2.ndias%{?dist}

Summary: Plugin to monitor the health and values of SMART
License: GPLv3

URL:     https://www.claudiokuenzler.com/monitoring-plugins/check_smart.php
Source0: https://github.com/Napsty/check_smart/archive/refs/tags/%{version}.tar.gz#/check_smart-%{version}.tar.gz

BuildArch: noarch
Requires: smartmontools

%description
This is a plugin to monitor the health and values of SMART attributes of hard
(HDD), solid state (SSD) and NVMe drives. The plugin is a fork of check_smart
released in 2009 by Kurt Yoder. Since then the plugin has undergone a lot of
changes. It allows to monitor drives behind hardware controllers and added a
lot of parameters to fine tune the checks and set thresholds (on a per
attribute setting).

%prep
%setup -q -n check_smart-%{version}


%build


%install
install -p -m 755 -D check_smart.pl %{buildroot}%{_libdir}/nagios/plugins/check_smart.pl


%files
%doc README.md SSD-TBW-Warranty.md 
%license COPYING.md

%{_libdir}/nagios/plugins/check_smart.pl

%changelog
* Tue Oct 3 2023 Nuno Dias <Nuno.Dias@gmail.com> - 6.14.1-2.ndias
- Update requires

* Thu Sep 28 2023 Nuno Dias <Nuno.Dias@gmail.com> - 6.14.1-1.ndias
- Version 6.14.1
