%define		polkit_version 0.8
%define		lirc_version 0.8.3

Name:		gnome-lirc-properties
Version:	0.2.8
Release:	%mkrel 1
Summary:	Infrared Remote Controls setup tool

Group:		System/Configuration/Hardware
License:	GPLv2+
URL:		http://svn.gnome.org/svn/gnome-lirc-properties/trunk
Source:		http://ftp.gnome.org/pub/GNOME/sources/gnome-lirc-properties/%{name}-%{version}.tar.bz2
# http://bugzilla.gnome.org/show_bug.cgi?id=530359
# http://bugzilla.gnome.org/show_bug.cgi?id=540897
# based on fedora support patch
Patch0:		glp-mdv-support.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	python 
Requires:	policykit >= %{polkit_version}
Requires:	pygtk2.0
Requires:	lirc >= %{lirc_version} lirc-remotes >= %{lirc_version}

BuildRequires:	python-devel
BuildRequires:	policykit-gnome-devel >= %{polkit_version} gtk2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	lirc >= %{lirc_version} lirc-remotes >= %{lirc_version}
BuildRequires:	desktop-file-utils

# For the Fedora patch
BuildRequires:	autoconf automake intltool

BuildArch:	noarch

%description
gnome-lirc-properties helps users set up infrared remote controls for use with
the LIRC framework.

%prep
%setup -q
%patch0 -p0 -b .mandriva

#needed by patch0
autoreconf

%build
PATH=$PATH:/usr/sbin %configure2_5x --with-lirc-confdir=%{_sysconfdir} --with-remotes-database=%{_datadir}/lirc-remotes/

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

# Validate the desktop file
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/gnome-lirc-properties.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING README AUTHORS
%{_sysconfdir}/dbus-1/system.d/org.gnome.LircProperties.Mechanism.conf
%{_datadir}/PolicyKit/policy/gnome-lirc-properties-mechanism.policy
%{_datadir}/dbus-1/system-services/org.gnome.LircProperties.Mechanism.service
%{_datadir}/applications/gnome-lirc-properties.desktop
%{_datadir}/gnome/help/gnome-lirc-properties/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_datadir}/omf/gnome-lirc-properties/
%{_bindir}/gnome-lirc-properties
%{python_sitelib}/gnome_lirc_properties
%{_datadir}/%{name}/

