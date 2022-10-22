%define release_name Thirty Six
%define dist_version 36
%define bug_version %{dist_version}
%define releasever %{dist_version}
%define doc_version f%{dist_version}

%bcond_without  basic
%bcond_without  cloud
%bcond_without  container

%bcond_without  iot
%bcond_without  server
%bcond_without  workstation


Summary:        Factory release files
Name:           factory-release
Version:        36
Release:        300%{?dist}
License:        MIT
URL:            https://factorylinux.com/

Source1:        LICENSE

Source10:       85-display-manager.preset
Source11:       90-default.preset
Source12:       90-default-user.preset
Source13:       99-default-disable.preset
Source14:       80-server.preset
Source15:       80-workstation.preset
Source16:       org.gnome.shell.gschema.override
Source17:       80-iot.preset
Source18:       80-iot-user.preset
Source19:       81-desktop.preset
Source20:       factory-workstation.conf

BuildArch:      noarch

Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}

Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}

Recommends:     factory-release-identity-basic
Obsoletes:	fedora-release-identity-basic < %{version}

BuildRequires:  redhat-rpm-config > 121-1
BuildRequires:  systemd-rpm-macros


%description
Factory release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.


%package common
Summary: 	Factory release files

Requires:   	factory-release-variant = %{version}-%{release}
Suggests:   	factory-release

Requires:   	factory-repos(%{version})
Requires:   	factory-release-identity = %{version}-%{release}

Conflicts:  	fedora-release

Obsoletes:  	fedora-release-ostree-counting < %{version}
Obsoletes:	fedora-release-common < %{version}


%description common
Release files common to all Editions and Spins of Factory


%if %{with basic}
%package identity-basic
Summary:        Package providing the basic Factory identity

RemovePathPostfixes: .basic
Provides:       factory-release-identity = %{version}-%{release}

Recommends:     factory-release-identity
Obsoletes:	fedora-release-identity < %{version}


%description identity-basic
Provides the necessary files for a Factory installation that is not identifying
itself as a particular Edition or Spin.
%endif


%if %{with cloud}
%package cloud
Summary:        Base package for Factory Cloud specific default configurations

RemovePathPostfixes: .cloud
Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}

Recommends:     factory-release-identity-cloud
Obsoletes:	fedora-release-identity-cloud < %{version}


%description cloud
Provides a base package for Factory Cloud specific configuration files to
depend on.


%package identity-cloud
Summary:        Package providing the identity for Factory Cloud Edition

RemovePathPostfixes: .cloud
Provides:       factory-release-identity = %{version}-%{release}
Conflicts:      factory-release-identity


%description identity-cloud
Provides the necessary files for a Factory installation that is identifying
itself as Factory Cloud Edition.
%endif


%if %{with container}
%package container
Summary:        Base package for Factory Container specific default configurations

RemovePathPostfixes: .container
Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}

Recommends:     factory-release-identity-container
Obsoletes:	fedora-release-identity-container < %{version}


%description container
Provides a base package for Factory Container specific configuration files to
depend on as well as container system defaults.


%package identity-container
Summary:        Package providing the identity for Factory Container Base Image

RemovePathPostfixes: .container
Provides:       factory-release-identity = %{version}-%{release}
Conflicts:      factory-release-identity


%description identity-container
Provides the necessary files for a Factory installation that is identifying
itself as the Factory Container Base Image.
%endif


%if %{with iot}
%package iot
Summary:        Base package for Factory IoT specific default configurations

RemovePathPostfixes: .iot
Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}

Recommends:     factory-release-identity-iot
Obsoletes:	fedora-release-identity-iot < %{version}


%description iot
Provides a base package for Factory IoT specific configuration files to
depend on as well as IoT system defaults.


%package identity-iot
Summary:        Package providing the identity for Factory IoT Edition

RemovePathPostfixes: .iot
Provides:       factory-release-identity = %{version}-%{release}
Conflicts:      factory-release-identity


%description identity-iot
Provides the necessary files for a Factory installation that is identifying
itself as Factory IoT Edition.
%endif


%if %{with server}
%package server
Summary:        Base package for Factory Server specific default configurations

RemovePathPostfixes: .server
Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}

Recommends:     factory-release-identity-server
Obsoletes:	fedora-release-identity-server < %{version}


%description server
Provides a base package for Factory Server specific configuration files to
depend on.


%package identity-server
Summary:        Package providing the identity for Factory Server Edition

RemovePathPostfixes: .server
Provides:       factory-release-identity = %{version}-%{release}
Conflicts:      factory-release-identity


%description identity-server
Provides the necessary files for a Factory installation that is identifying
itself as Factory Server Edition.
%endif


%if %{with workstation}
%package workstation
Summary:        Base package for Factory Workstation specific default configurations

RemovePathPostfixes: .workstation
Provides:       factory-release = %{version}-%{release}
Provides:       factory-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       factory-release-common = %{version}-%{release}
Provides:       system-release-product

Recommends:     factory-release-identity-workstation
Obsoletes:	fedora-release-identity-workstation < %{version}


%description workstation
Provides a base package for Factory Workstation specific configuration files to
depend on.


%package identity-workstation
Summary:        Package providing the identity for Factory Workstation Edition

RemovePathPostfixes: .workstation
Provides:       factory-release-identity = %{version}-%{release}
Conflicts:      factory-release-identity


%description identity-workstation
Provides the necessary files for a Factory installation that is identifying
itself as Factory Workstation Edition.
%endif


%prep


%build


%install
install -d %{buildroot}%{_prefix}/lib
echo "Factory release %{version} (%{release_name})" > %{buildroot}%{_prefix}/lib/factory-release
echo "cpe:/o:factorylinux:factory:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/factory-release %{buildroot}%{_sysconfdir}/factory-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s factory-release %{buildroot}%{_sysconfdir}/system-release

# Create the common os-release file
%{lua:
  function starts_with(str, start)
   return str:sub(1, #start) == start
  end
}
%define starts_with(str,prefix) (%{expand:%%{lua:print(starts_with(%1, %2) and "1" or "0")}})
%if %{starts_with "a%{release}" "a0"}
  %global prerelease \ Prerelease
%endif

cat > os-release << EOF
NAME="Factory"
VERSION="%{dist_version} (%{release_name}%{?prerelease})"
ID=factory
ID_LIKE=fedora
VERSION_ID=%{dist_version}
VERSION_CODENAME=""
PLATFORM_ID="platform:f%{dist_version}"
PRETTY_NAME="Factory %{dist_version} (%{release_name}%{?prerelease})"
ANSI_COLOR="0;34"
LOGO=factory-logo-icon
CPE_NAME="cpe:/o:factorylinux:factory:%{dist_version}"
HOME_URL="https://factorylinux.com/"
DOCUMENTATION_URL="https://docs.factorylinux.com/"
EOF

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

# Create os-release files for the different editions

%if %{with basic}
# Basic
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.basic
%endif

%if %{with cloud}
# Cloud
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.cloud
echo "VARIANT=\"Cloud Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.cloud
echo "VARIANT_ID=cloud" >> %{buildroot}%{_prefix}/lib/os-release.cloud
sed -i -e "s|(%{release_name}%{?prerelease})|(Cloud Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.cloud
%endif

%if %{with container}
# Container
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.container
echo "VARIANT=\"Container Image\"" >> %{buildroot}%{_prefix}/lib/os-release.container
echo "VARIANT_ID=container" >> %{buildroot}%{_prefix}/lib/os-release.container
sed -i -e "s|(%{release_name}%{?prerelease})|(Container Image%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.container
%endif

%if %{with iot}
# IoT
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.iot
echo "VARIANT=\"IoT Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.iot
echo "VARIANT_ID=iot" >> %{buildroot}%{_prefix}/lib/os-release.iot
sed -i -e "s|(%{release_name}%{?prerelease})|(IoT Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.iot
install -Dm0644 %{SOURCE17} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE18} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
%endif

%if %{with server}
# Server
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.server
echo "VARIANT=\"Server Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.server
echo "VARIANT_ID=server" >> %{buildroot}%{_prefix}/lib/os-release.server
sed -i -e "s|(%{release_name}%{?prerelease})|(Server Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.server
install -Dm0644 %{SOURCE14} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
%endif

%if %{with workstation}
# Workstation
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT=\"Workstation Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT_ID=workstation" >> %{buildroot}%{_prefix}/lib/os-release.workstation
sed -i -e "s|(%{release_name}%{?prerelease})|(Workstation Edition%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.workstation
install -Dm0644 %{SOURCE20} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with workstation}
# Workstation
install -Dm0644 %{SOURCE15} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE19} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# Override the list of enabled gnome-shell extensions for Workstation
install -Dm0644 %{SOURCE16} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
%endif

ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF

%%__bootstrap         ~bootstrap
%%factory              %{dist_version}
%%fc%{dist_version}                 1
%%dist                 %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}.fc%%{factory}%%{?with_bootstrap:%{__bootstrap}}
EOF

mkdir -p licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE

install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/


%files common
%license licenses/LICENSE
%{_prefix}/lib/factory-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/factory-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_prefix}/lib/systemd/user-preset/
%{_prefix}/lib/systemd/user-preset/90-default-user.preset
%{_prefix}/lib/systemd/user-preset/99-default-disable.preset
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset


%if %{with basic}
%files
%files identity-basic
%{_prefix}/lib/os-release.basic
%endif


%if %{with cloud}
%files cloud
%files identity-cloud
%{_prefix}/lib/os-release.cloud
%endif


%if %{with container}
%files container
%files identity-container
%{_prefix}/lib/os-release.container
%endif


%if %{with iot}
%files iot
%files identity-iot
%{_prefix}/lib/os-release.iot
%{_prefix}/lib/systemd/system-preset/80-iot.preset
%{_prefix}/lib/systemd/user-preset/80-iot-user.preset
%endif


%if %{with server}
%files server
%files identity-server
%{_prefix}/lib/os-release.server
%{_prefix}/lib/systemd/system-preset/80-server.preset
%endif


%if %{with workstation}
%files workstation
%files identity-workstation
%{_prefix}/lib/os-release.workstation
%{_sysconfdir}/dnf/protected.d/factory-workstation.conf
# Keep this in sync with silverblue above
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%{_prefix}/lib/systemd/system-preset/80-workstation.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%endif


%changelog
* Sat Oct 22 2022 Factory Linux Developers <info@factorylinux.com> 
- Built For The Factory Linux!
