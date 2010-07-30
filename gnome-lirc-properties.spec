%define		lirc_version 0.8.3

Name:		gnome-lirc-properties
Version:	0.5.1
Release:	%mkrel 1
Summary:	Infrared Remote Controls setup tool

Group:		System/Configuration/Hardware
License:	GPLv2+
URL:		http://svn.gnome.org/svn/gnome-lirc-properties/trunk
Source:		http://ftp.gnome.org/pub/GNOME/sources/gnome-lirc-properties/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	python 
Requires:	polkit
Requires:	pygtk2.0
Requires:	lirc >= %{lirc_version} lirc-remotes >= %{lirc_version}

BuildRequires:	python-devel
BuildRequires:	polkit-1-devel >= %{polkit_version} gtk2-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	lirc >= %{lirc_version} lirc-remotes >= %{lirc_version}
BuildRequires:	desktop-file-utils
BuildRequires:	intltool

BuildArch:	noarch

%description
gnome-lirc-properties helps users set up infrared remote controls for use with
the LIRC framework.

%prep
%setup -q

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
%{_datadir}/polkit-1/actions/org.gnome.lirc-properties.mechanism.policy
%{_datadir}/dbus-1/system-services/org.gnome.LircProperties.Mechanism.service
%{_datadir}/hal/fdi/policy/10osvendor/20-x11-remotes.fdi
%{_datadir}/applications/gnome-lirc-properties.desktop
%{_datadir}/gnome/help/gnome-lirc-properties/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_datadir}/omf/gnome-lirc-properties/
%{_bindir}/gnome-lirc-properties
%{python_sitelib}/gnome_lirc_properties
%{_datadir}/%{name}/

