Summary: SME server Audittools manager
%define name smeserver-audittoolsmanager
Name: %{name}
%define version 0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: SWT
Group: Administration
Source: %{name}-%{version}.tar.gz
Packager: Stephane de Labrusse <stephdl@de-labrusse.fr>
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-release >= 8.0
AutoReqProv: no

%changelog
* Fri Apr 4 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1
- First release

%description
Display Audittools in server-manager

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post
#echo "Rebuilding Server Manager Panel."
#/etc/e-smith/events/actions/navigation-conf >/dev/null 2>&1
#echo "Done."

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
